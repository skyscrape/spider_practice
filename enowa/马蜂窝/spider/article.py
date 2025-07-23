import base64
import re
import time
from io import BytesIO
from PIL import Image
import requests
from DrissionPage import ChromiumPage, ChromiumOptions


def image_to_base64(img: Image.Image, encoding='utf-8') -> str:
    """将 PIL 图片对象转为 base64 编码字符串"""
    img_format = img.format or 'JPEG'
    if img.mode == 'P':
        img = img.convert("RGB")
    if img.mode == 'RGBA':
        img_format = 'PNG'

    output_buffer = BytesIO()
    img.save(output_buffer, quality=100, format=img_format)
    byte_data = output_buffer.getvalue()
    base64_str = f'data:image/{img_format.lower()};base64,' + base64.b64encode(byte_data).decode(encoding)
    return base64_str


def download_and_resize_image(image_url, save_path):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
    }
    # 发送请求获取图片内容
    response = requests.get(image_url, headers=headers)
    response.raise_for_status()
    # 读取图片数据到内存
    image_data = BytesIO(response.content)
    # 打开图片
    img = Image.open(image_data)
    # 调整图片大小
    resized_img = img.resize((340, 200), Image.Resampling.LANCZOS)
    # 保存调整大小后的图片
    resized_img.save(save_path)


def get_slide_distance(image_path: str, api_key: str) -> int:
    """调用滑块验证码识别接口，返回需要滑动的距离"""
    url = 'http://bq1gpmr8.xiaomy.net/openapi/verify_code_identify/'
    headers = {"Content-Type": "application/json"}
    img_base64 = image_to_base64(Image.open(image_path))
    data = {
        "key": api_key,
        "verify_idf_id": "6",
        "img_base64": img_base64
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    distance = response.json().get('data', {}).get('distance', 0)
    print('没有去掉边距的=>',distance)
    distance = distance - 30
    return distance


def simulate_slide_action(frame, distance: int, steps=10, delay=0.02):
    """模拟滑块拖动行为，分多步慢慢拖动"""
    slider_xpath = "x://div[@class='tc-fg-item tc-slider-normal']"
    frame.actions.hold(slider_xpath)

    step_distance = distance / steps  # 每步移动距离
    for _ in range(steps):
        frame.actions.right(step_distance)
        time.sleep(delay)  # 每步后暂停，单位秒
    time.sleep(0.1)
    frame.actions.release()



def main():
    # 初始化 - 使用无痕模式
    co = ChromiumOptions()
    # co.set_argument('--incognito')  # 无痕模式   #不太建议使用无痕，每次都滑，次数太多了也不给过了
    # co.set_argument('--headless=new')
    page = ChromiumPage(co)         # 启动 ChromiumPage

    target_url = 'https://www.mafengwo.cn/wenda/detail-11199436.html'
    api_key = "W65eeDqISmY61Uv5fTzF"
    image_save_path = 'bg.jpg'

    try:
        page.get(target_url)
        time.sleep(3)
        # 进入 iframe
        frame = page.get_frame('t:iframe')
        # 获取验证码背景图 URL
        style_attr = frame.ele('x://div[@class="tc-bg-img unselectable"]').attr('style')
        match = re.search(r'background-image:\s*url\("([^"]+)"\)', style_attr)
        image_url = match.group(1)
        print("提取到的图片URL：", image_url)
        # 下载图片
        download_and_resize_image(image_url, image_save_path)
        # 获取滑动距离
        slide_distance = get_slide_distance(image_save_path, api_key)
        print(f"滑动距离为: {slide_distance}px")
        # 模拟滑块滑动
        simulate_slide_action(frame, slide_distance)

        # 获取当前页面数据
        time.sleep(3) #等滑块页面跳走，刷出数据页面
        print('当前页面数据=>', page.html)
        input() #防止页面直接关闭

    except Exception as e:
        print("执行过程中发生错误:", e)
        # 如果报错说明就不需要过滑块，直接获取页面数据
        time.sleep(1)
        print('当前页面数据=>',page.html)
        # input()#防止页面直接关闭

if __name__ == '__main__':
    main()