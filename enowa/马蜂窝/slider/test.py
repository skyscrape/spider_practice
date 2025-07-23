import asyncio
import random
import cv2
import numpy as np
import pandas as pd
import math
import os
from playwright.async_api import async_playwright

# ==== 滑块识别函数 ====
def get_dx_median(dx, x, y, w, h):
    return np.median(dx[y:(y + h), x])

def pre_process(img_path):
    img = cv2.imread(img_path, 1)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    cnt_infos = {}
    dx = cv2.Sobel(img, -1, 1, 0, ksize=5)

    for i, cnt in enumerate(contours):
        area = cv2.contourArea(cnt)
        if area < 5000 or area > 25000:
            continue
        x, y, w, h = cv2.boundingRect(cnt)
        cnt_infos[i] = {
            'rect_area': w * h,
            'rect_arclength': 2 * (w + h),
            'cnt_area': area,
            'cnt_arclength': cv2.arcLength(cnt, True),
            'cnt': cnt,
            'w': w, 'h': h, 'x': x, 'y': y,
            'mean': np.mean(np.min(img[y:(y + h), x:(x + w)], axis=2)),
        }
    return img, dx, cnt_infos

def qq_mark_pos(img_path):
    if not os.path.exists(img_path):
        raise FileNotFoundError("背景图未找到")
    img, dx, cnt_infos = pre_process(img_path)
    df = pd.DataFrame(cnt_infos).T
    df['dx_mean'] = df.apply(lambda x: get_dx_median(dx, x['x'], x['y'], x['w'], x['h']), axis=1)
    df['rect_ratio'] = df.apply(lambda v: v['rect_arclength'] / 4 / math.sqrt(v['rect_area'] + 1), axis=1)
    df['area_ratio'] = df.apply(lambda v: v['rect_area'] / v['cnt_area'], axis=1)
    df['score'] = df.apply(lambda x: abs(x['rect_ratio'] - 1), axis=1)
    result = df.query('x>0').query('area_ratio<2').query('rect_area>5000').query('rect_area<20000') \
        .sort_values(['mean', 'score', 'dx_mean']).head(1)
    return result.x.values[0]

# ==== 拖动轨迹生成函数 ====
def get_track_list(distance):
    v = 0
    t = 0.2
    tracks = []
    current = 0
    mid = distance * 7 / 8
    distance += 10
    while current < distance:
        a = random.randint(2, 4) if current < mid else -random.randint(3, 5)
        v0 = v
        s = v0 * t + 0.5 * a * (t ** 2)
        current += s
        tracks.append(round(s))
        v = v0 + a * t
    for _ in range(4): tracks.append(-random.randint(2, 3))
    for _ in range(4): tracks.append(-random.randint(1, 3))
    return tracks

# ==== 拖动操作 ====
async def drag_slider(frame, x_offset):
    slider = await frame.query_selector(".tc-slider-normal")
    box = await slider.bounding_box()
    start_x = box["x"] + box["width"] / 2
    start_y = box["y"] + box["height"] / 2

    track = get_track_list(x_offset)
    await frame.page.mouse.move(start_x, start_y)
    await frame.page.mouse.down()
    current = 0
    for dx in track:
        current += dx
        await frame.page.mouse.move(start_x + current, start_y)
        await asyncio.sleep(random.uniform(0.01, 0.03))
    await asyncio.sleep(0.1)
    await frame.page.mouse.up()
    print("✅ 拖动完成")

# ==== 主函数 ====
async def main():
    bg_path = "./bg.jpg"
    slider_init_x = 22.7679  # 页面中滑块的初始横坐标

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=100)
        context = await browser.new_context()
        page = await context.new_page()

        async def on_bg_image_response(response):
            if "cap_union_new_getcapbysig" in response.url and "img_index=1" in response.url:
                buffer = await response.body()
                with open(bg_path, "wb") as f:
                    f.write(buffer)

        page.on("response", on_bg_image_response)

        await page.goto("https://www.mafengwo.cn/wenda/detail-18342660.html", timeout=60000, wait_until="load")
        await asyncio.sleep(3)

        slider_frame = None
        for frame in page.frames:
            if "captcha" in frame.url:
                slider_frame = frame
                break

        await slider_frame.wait_for_selector(".tc-slider-normal", timeout=10000)
        await asyncio.sleep(1.5)

        # 识别缺口位置
        gap_x_image = qq_mark_pos(bg_path)

        # 获取图像像素宽 + 页面实际渲染宽
        bg_element = await slider_frame.query_selector(".tc-bg-img")
        bg_box = await bg_element.bounding_box()
        bg_dom_width = bg_box['width']
        bg_img = cv2.imread(bg_path)
        bg_img_width = bg_img.shape[1]

        # 图像坐标 → 页面坐标 → 拖动距离
        gap_x_page = (gap_x_image / bg_img_width) * bg_dom_width
        x_offset = gap_x_page - slider_init_x
        print(f"🎯 拖动距离: {x_offset:.2f}px")

        await drag_slider(slider_frame, x_offset)
        await asyncio.sleep(3)
        await browser.close()

# ==== 运行入口 ====
asyncio.run(main())