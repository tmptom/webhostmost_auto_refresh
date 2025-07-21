import requests
import re
import urllib
import os

URL_LOGIN = "https://client.webhostmost.com/login"
HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}

HTML_FILE1 = "login1.html"
HTML_FILE2 = "login2.html"

def login(username, password, idx):
    client = requests.session()
    response = client.get(URL_LOGIN)
    response.raise_for_status()

    with open(f"{HTML_FILE1}_{idx}", "wb") as file:
        file.write(response.content)

    tokens = re.findall(r'name="token" value="(.*?)"', response.text)
    print(f"[{idx}] tokens: {tokens}")

    if not tokens:
        print(f"[{idx}] No CSRF token found, skipping.")
        return

    params = 'token={}&username={}&password={}'.format(tokens[0], urllib.parse.quote(username), password)
    print(f'[{idx}] params: {params}')

    response2 = client.post(URL_LOGIN, data=params, headers=HEADERS)
    response2.raise_for_status()

    with open(f"{HTML_FILE2}_{idx}", "wb") as file:
        file.write(response2.content)

    timeUntil = re.findall(r'Time until suspension:', response2.text)
    print(f"[{idx}] timeUntil: {timeUntil}")
    if len(timeUntil) > 0:
        print(f'[{idx}] success')
    else:
        print(f'[{idx}] failed')

    print(f'[{idx}] StatusCode: {response2.status_code}, StatusDescription: {response2.ok}, Cookie: {response2.cookies}')

if __name__ == "__main__":
    for i in range(1, 6):  # 支持5组账户，可自行调整
        username = os.environ.get(f"MY_USERNAME_{i}")
        password = os.environ.get(f"MY_PASSWORD_{i}")
        if username and password:
            print(f"=== Running for account {i} ===")
            login(username, password, i)
        else:
            print(f"Account {i} not set, skipping.")
