import requests


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "x-secsdk-csrf-token": "000100000001d2078505b14dd89f7a7e9d46729db4622f4376397da4f9295a9ef16617e546b5184e15679852dc9a"
}
cookies = {
    "UIFID_TEMP": "9f119777b70db29e092f16dc2972b95ccc9df01a979ae01132052c40ee3e10baa79bb8cdb15e42fc5397db9a3f55379bd0f8246d0cd838a5a77b03cb8d6042b660855f31307a643e625c33c50b51715b",
    "hevc_supported": "true",
    "bd_ticket_guard_client_web_domain": "2",
    "UIFID": "9f119777b70db29e092f16dc2972b95ccc9df01a979ae01132052c40ee3e10baa79bb8cdb15e42fc5397db9a3f55379b1ba2403098e9f62f88881fe4265475d9197999bc05ee8863bc9097a63b5b83f99cb6f12c60f388bde77a56c52a183f9cf33e254670aa499f042bc06fb936e60fe3515442da50a30cbf4db78687f71baa3b7e78540b23491ee8049382d408a26554af88c99dad1fcc93ba0c8e5b298a0b",
    "SEARCH_RESULT_LIST_TYPE": "%22single%22",
    "__security_mc_1_s_sdk_sign_data_key_sso": "d3bd24d5-4cf4-a8ee",
    "passport_mfa_token": "Cjdtz0%2BYLYRy1O5fi%2Bi53jstdrxSCTJVSBotPD5DH1EYfiVMsS5TagHFRaTB3DMvSIPjgocFyJvwGkoKPAAAAAAAAAAAAABPD5JV1q0%2B4r6AL%2Bjf6D8zOoZ31Lc2%2B0o64TX3Bu32erqllZy5zQAqszh7DjgP8hXOIRDX7%2FINGPax0WwgAiIBA7AhzTU%3D",
    "d_ticket": "54c35e1abb4bfe8b99ba1d353ae4227065334",
    "locale": "zh-cn",
    "kura_cloud_uid": "e4f1bedf73245df9f09ff2758600e0d1",
    "n_mh_douhot": "9-mIeuD4wZnlYrrOvfzG3MuT6aQmCUtmr8FxV8Kl8xY",
    "is_staff_user_douhot": "false",
    "ttcid": "3826d178920d4a6b9ab8efdcd1cf02eb33",
    "x_dpss_uuid": "15b779eb-3bb2-4d8a-9567-305e0c684bba",
    "x_dpss_uuid.sig": "h9QdsZLoVbAZGWgKuZELmD82xA4pGQGvNvuir2bejNo",
    "csrf_session_id": "36bbfe80ba21b2a2d594295a655548a9",
    "passport_csrf_token": "8dee6803cfeedf52992c06db6f3a56f4",
    "passport_csrf_token_default": "8dee6803cfeedf52992c06db6f3a56f4",
    "bd_ticket_guard_client_data": "eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSzBuc0tLY0VDc0YwMHZ3K3VtQmVxZzhQd0l5Qk9PKzRFZ0xiWldnNXBwQ0pjcXJGQUxGZy9ORHdkSHplMTZGOVY0Q1ZNUC9CdmxCZzVCVVcwbmVmT009IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D",
    "ttwid": "1%7CWW5yZsW6c1qKS-isqVMX2G9JsKofQc9afudia0GDOaY%7C1751348617%7C00ee1cdf7e0e2738049b3ed01703bdd4e14aeb7bec90b555262ea6e85dfa8198",
    "odin_tt": "d8a904148ad3669725e9e7c0d9bc1fb4f719c1c61a1c21d7ae4b0e10931cf0bbc214f024f0cb1b88ec92f0349d4e903e896c7271ca13e5d88e4cbdbcbd773c24",
    "sid_guard_douhot": "3ae42b5e628fc3dd7d1847e0ff8894cc%7C1751348662%7C5184000%7CSat%2C+30-Aug-2025+05%3A44%3A22+GMT",
    "uid_tt_douhot": "d32d643148d2ddef01ef8bb67549c969",
    "uid_tt_ss_douhot": "d32d643148d2ddef01ef8bb67549c969",
    "sid_tt_douhot": "3ae42b5e628fc3dd7d1847e0ff8894cc",
    "sessionid_douhot": "3ae42b5e628fc3dd7d1847e0ff8894cc",
    "sessionid_ss_douhot": "3ae42b5e628fc3dd7d1847e0ff8894cc",
    "sid_ucp_v1_douhot": "1.0.0-KGVkYTYxYzIyZGY5MjllNGMyZjI4ZTI3MDA2ZDUzOGM5MWQzNTVkYzQKHQjnq8DQqqxUELbrjcMGGO0xIAwwxcOqwQY4CEAmGgJobCIgM2FlNDJiNWU2MjhmYzNkZDdkMTg0N2UwZmY4ODk0Y2M",
    "ssid_ucp_v1_douhot": "1.0.0-KGVkYTYxYzIyZGY5MjllNGMyZjI4ZTI3MDA2ZDUzOGM5MWQzNTVkYzQKHQjnq8DQqqxUELbrjcMGGO0xIAwwxcOqwQY4CEAmGgJobCIgM2FlNDJiNWU2MjhmYzNkZDdkMTg0N2UwZmY4ODk0Y2M",
    "tt_scid": "9E4b4HBaejkOU.9M7v.G.soY-Ie1IC3Ts56-5iPrBwG8jSugC0-b4JouOAiyTs8j99aa"
}
url = "https://douhot.douyin.com/douhot/v1/item_analysis/7520560264119373083/item_info"
params = {
    "msToken": "",
    "X-Bogus": "DFSzswVOQDGANVWsCtUiQslUrn0o",
    "_signature": "_02B4Z6wo00001TGlGegAAIDAGKGHlseWvC0xpR1AACQNaoMfVkWV3ptwAIP6EcP1WwKBPEcHFwH-fPx1TNacbpJjjOkWkVTpgLzpCHNGm7LBr0E1atFUa4CIFx432y1RqJzLiy8isMa-b8s-bd"
}
response = requests.get(url, headers=headers, cookies=cookies)

print(response.text)
print(response)