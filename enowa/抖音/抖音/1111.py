import requests
import execjs

js = execjs.compile(open('1111.js', encoding='utf-8').read())


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.douyin.com/user/MS4wLjABAAAAompXkPoYOGsA152dqYoytKycjIZ_aCCxHwGmLX5IsDM?from_tab_name=main",
    "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    'cookie':'__ac_nonce=067e50b730048202039fb; __ac_signature=_02B4Z6wo00f01MwANOQAAIDA-yTwuHIzhVzMIDBAAFTq9d; ttwid=1%7C29mihvz1kxX5-wUXM29s4wcwiiYMlKJ8y_pJD18pK24%7C1743063923%7C8ede36c02cf435da7ae54293e1bfe7f61138208506adbd072d72c539a02c65fe; UIFID_TEMP=2eb4f745f9fe6544447c1d68cb43a44931f67e23b1951fd9ca8b76ce94a622367d0cf02cb7c8543e90c1695f54cf9540f65b69f067bd7f144cf1dfb874b18c2e5cae8da978f6cd99f9364b891d0d1f45; x-web-secsdk-uid=b1f236ff-1882-48f6-a9a3-7ddd294e0e3f; s_v_web_id=verify_m8r398vx_DkJsaZsw_qJot_4xeO_AQTm_zZMXohfzUvf2; hevc_supported=true; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22; dy_swidth=1536; dy_sheight=864; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22',
    "uifid": "2eb4f745f9fe6544447c1d68cb43a44931f67e23b1951fd9ca8b76ce94a62236d5645c11e681d53746aa0d2edadaf80264646774559cf6f983437a000cbb223275b4be0410c823254ffbff67225e2b5e089c589ae4f37c40213418dae5d3209115b565aabb84880064e3cd49f570e66f1408e40b0c729eeb17417ade490f85e19c3f1a3a235633d0b743f5e218cda4773ff5da7fd80f9ccfd79a08763e31d7b5",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}

url = "https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAompXkPoYOGsA152dqYoytKycjIZ_aCCxHwGmLX5IsDM&max_cursor=0&locate_query=false&show_live_replay_strategy=1&need_time_list=1&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&from_user_page=1&update_version_code=170400&pc_client_type=1&pc_libra_divert=Windows&support_h265=1&support_dash=0&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=134.0.0.0&browser_online=true&engine_name=Blink&engine_version=134.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7486402491123959332&uifid=2eb4f745f9fe6544447c1d68cb43a44931f67e23b1951fd9ca8b76ce94a622367d0cf02cb7c8543e90c1695f54cf9540f65b69f067bd7f144cf1dfb874b18c2e5cae8da978f6cd99f9364b891d0d1f45&verifyFp=verify_m8r398vx_DkJsaZsw_qJot_4xeO_AQTm_zZMXohfzUvf2&fp=verify_m8r398vx_DkJsaZsw_qJot_4xeO_AQTm_zZMXohfzUvf2"
ab = js.call('get_a_b', url)
print( ab)
url += '&a_bogus=' + ab


response = requests.get(url, headers=headers)

print(response.text)
print(response)