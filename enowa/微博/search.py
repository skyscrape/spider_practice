import re


urls = [
    "https://www.weibo.com/1911451427/PvSNw8bFF",  # 9位(含P) → P后8个
    "https://weibo.com/2400966427/PvWkHaa6"        # 8位(含P) → P后7个
]

pat = re.compile(
    r'https?://(?:www\.)?weibo\.com/(?P<uid>\d+)/P(?P<mid>[a-zA-Z0-9]{7,8})'
)

for url in urls:
    m = pat.search(url)
    if m:
        print("✅", url, "→ uid:", m['uid'], "mid:", m['mid'])
    else:
        print("❌ 不匹配", url)