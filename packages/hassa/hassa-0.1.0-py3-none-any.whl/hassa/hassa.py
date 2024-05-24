try:
    import requests
    from fake_useragent import UserAgent # type: ignore
except ModuleNotFoundError:
    import os
    os.system("pip install requests")
    os.system("pip install fake_useragent")

class InstagramSession:    
    
    def __init__(self, csrftoken, ds_user_id, rur, sessionid):
        self.csrftoken = csrftoken
        self.ds_user_id = ds_user_id
        self.rur = rur
        self.sessionid = sessionid

def log_in(username, password):
    if not username or not password:
        raise ValueError("يرجى تمرير قيم لاسم المستخدم وكلمة المرور")
    ua = UserAgent()
    agnt = str(ua.getChrome)

    url = 'https://www.instagram.com/accounts/login/ajax/'

    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-length': '275',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'csrftoken=DqBQgbH1p7xEAaettRA0nmApvVJTi1mR; ig_did=C3F0FA00-E82D-41C4-99E9-19345C41EEF2; mid=X8DW0gALAAEmlgpqxmIc4sSTEXE3; ig_nrcb=1',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': agnt,
        'x-csrftoken': 'DqBQgbH1p7xEAaettRA0nmApvVJTi1mR',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': 'bc3d5af829ea',
        'x-requested-with': 'XMLHttpRequest'
    }

    data = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
        'queryParams': '{}',
        'optIntoOneTap': 'false'
    }

    response = requests.post(url, headers=headers, data=data)
    cookies = None
    if response.status_code == 200:
        cookies = response.cookies.get_dict()
        csrftoken = cookies.get("csrftoken")
        ds_user_id = cookies.get("ds_user_id")
        rur = cookies.get("rur")
        sessionid = cookies.get("sessionid")
        return InstagramSession(csrftoken, ds_user_id, rur, sessionid)
    else:
        return None