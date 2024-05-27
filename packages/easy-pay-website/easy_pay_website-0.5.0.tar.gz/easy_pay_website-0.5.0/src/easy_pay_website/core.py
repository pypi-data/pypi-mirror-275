import httpx
import re
import os
import time
from bs4 import BeautifulSoup
import ddddocr
from odin_functions import check
from typing import Union

async def login(url: str, username: str, password: str, query_key: Union[str, int], query_value: Union[str, int]) -> dict:
    """
    Login to the specified URL using the provided username and password, along with additional query parameters.
    """
    async with httpx.AsyncClient() as client:
        timestamp = int(time.time())

        try:
            response = await client.get(url=f"{url}/manage.php?{query_key}={query_value}", timeout=5)
            if check.type_name(response) == 'NoneType':
                return {"result": False, "message": "failed", "data": []}
        except Exception as e:
            return {"result": False, "message": f"failed error: {e}", "data": []}

        cookiesPHPSESSID = response.cookies.get("PHPSESSID", None)
        if not cookiesPHPSESSID:
            return {"result": False, "message": "failed", "data": []}

        cookiesLogin = {'QINGZHIFU_PATH': 'qingzhifu', 'PHPSESSID': cookiesPHPSESSID}

        try:
            response = await client.get(url=f"{url}/manage.php?{query_key}={query_value}", cookies=cookiesLogin, timeout=5)
            if check.type_name(response) == 'NoneType':
                return {"result": False, "message": "failed", "data": []}
        except Exception as e:
            return {"result": False, "message": f"failed, error: {e}", "data": []}

        soup = BeautifulSoup(response.text, 'html.parser')
        form = soup.find('form', {'method': 'post'})
        action_value = form['action'] if form else None
        match = re.search(r'/(\d+)\.html$', action_value) if action_value else None
        number = match.group(1) if match else None

        if not number:
            return {"result": False, "message": "failed", "data": []}

        urlVerify = f"{url}/Manage/Index/verify.html"

        try:
            response = await client.get(url=urlVerify, cookies=cookiesLogin, timeout=5)
            if check.type_name(response) == 'NoneType':
                return {"result": False, "message": "failed", "data": []}
        except Exception as e:
            return {"result": False, "message": f"failed , error : {e}", "data": []}

        with open(f"captcha_{timestamp}.png", "wb") as file:
            file.write(response.content)

        ocr = ddddocr.DdddOcr()
        with open(f"captcha_{timestamp}.png", 'rb') as f:
            image = f.read()

        if os.path.exists(f"captcha_{timestamp}.png"):
            os.remove(f"captcha_{timestamp}.png")

        code = ocr.classification(image)
        if len(code) != 4:
            return {"result": False, "message": "failed", "data": []}

        data = {"username": username, "password": password, "yzm": code}
        urlLogin = f"{url}/Manage/Index/login/{number}.html"

        try:
            responseLogin = await client.post(url=urlLogin, data=data, cookies=cookiesLogin, timeout=5)
            if check.type_name(responseLogin) == 'NoneType':
                return {"result": False, "message": "failed", "data": []}
        except Exception as e:
            return {"result": False, "message": f"failed, error: {e}", "data": []}

        if responseLogin.cookies:
            cookiesR = responseLogin.cookies
            fx_admin_user_CODE = cookiesR.get("fx_admin_user_CODE", "")
            with open('fx_admin_user_CODE.txt', 'w') as file:
                file.write(fx_admin_user_CODE)
            with open('PHPSESSID.txt', 'w') as file:
                file.write(cookiesPHPSESSID)

            return {
                "result": True,
                "message": "success",
                "data": [{"fx_admin_user_CODE": fx_admin_user_CODE, "PHPSESSID": cookiesPHPSESSID}]
            }

        return {"result": False, "message": "failed", "data": []}


async def check_login_status(url: str, admin_name: str, admin_id: str) -> dict:
    """
    Check the login status by sending a GET request to the specified URL.
    """
    if os.path.exists('fx_admin_user_CODE.txt'):
        with open('fx_admin_user_CODE.txt', 'r') as file:
            fx_admin_user_CODE = file.read()
    else:
        return {"result": False, "message": "fx_admin_user_CODE.txt not found", "data": []}

    if os.path.exists('PHPSESSID.txt'):
        with open('PHPSESSID.txt', 'r') as file:
            cookiesPHPSESSID = file.read()
    else:
        return {"result": False, "message": "PHPSESSID.txt not found", "data": []}

    cookies = {
        "JSESSIONID": cookiesPHPSESSID,
        'QINGZHIFU_PATH': 'qingzhifu',
        'fx_admin_user_UNAME': admin_name,
        'menudd': '0',
        'fx_admin_user_UID': admin_id,
        'fx_admin_user_CODE': fx_admin_user_CODE
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url=f"{url}/manage/main/index.html", cookies=cookies, timeout=5)
            if check.type_name(response) == 'NoneType':
                return {"result": False, "message": "check.type_name(response) == 'NoneType'", "data": []}
        except Exception as e:
            return {"result": False, "message": f"error: {e}", "data": []}

        if "Cache-Control" in response.headers and response.headers["Cache-Control"] == "private":
            return {
                "result": True,
                "message": "success",
                "data": [{"fx_admin_user_CODE": fx_admin_user_CODE, "PHPSESSID": cookiesPHPSESSID}]
            }

        return {"result": False, "message": "login failed , please check your username and password", "data": []}


async def main(url: str, path: str, query: dict, admin_name: str, admin_id: str) -> dict:
    """
    Executes a main function that performs a series of operations.
    """
    result = await check_login_status(url, admin_name, admin_id)
    if check.type_name(result) == 'NoneType':
        return {"result": False, "message": "check_login_status() result is NoneType", "data": []}

    if not result["result"]:
        return {"result": False, "message": "login failed", "data": []}

    fx_admin_user_CODE = result["data"][0]["fx_admin_user_CODE"]
    cookiesPHPSESSID = result["data"][0]["PHPSESSID"]

    cookies = {
        "JSESSIONID": cookiesPHPSESSID,
        'QINGZHIFU_PATH': 'qingzhifu',
        'fx_admin_user_UNAME': admin_name,
        'menudd': '0',
        'fx_admin_user_UID': admin_id,
        'fx_admin_user_CODE': fx_admin_user_CODE
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url=f"{url}{path}", params=query, cookies=cookies, timeout=5)
            if check.type_name(response) == 'NoneType':
                return {"result": False, "message": "failed", "data": []}
        except Exception as e:
            return {"result": False, "message": f"error : {e}", "data": []}

        soup = BeautifulSoup(response.text, 'html.parser')
        form = soup.find('form', {'method': 'post'})
        table = form.find('table', {'class': 'table table-hover'}) if form else None
        tbody = table.find('tbody') if table else None

        trs = tbody.find_all('tr') if tbody else []
        data = [[td.text for td in tr.find_all('td')] for tr in trs if tr.find_all('td')]

        try:
            tagtopdiv = soup.find('div', class_='row tagtopdiv')
            data_top = []
            if tagtopdiv:
                divs = tagtopdiv.find_all('div', class_='panel')
                for div in divs:
                    panel_body = div.find('div', class_='panel-body')
                    h4_elements = panel_body.find_all('h4', class_='pull-left text-danger')
                    data_top.append([h4.text.strip() for h4 in h4_elements])
        except Exception as e:
            data_top = []

        try:
            page_info = soup.find('div', id='wypage')
            data_page = {}
            if page_info:
                page_info_text = page_info.find('a', class_='number').text.strip()
                record_count, page_number, total_pages = map(int, re.search(r'(\d+) 条记录 (\d+)/(\d+) 页', page_info_text).groups())
                data_page = {"record_count": record_count, "page_number": page_number, "total_pages": total_pages}
        except Exception as e:
            data_page = {}

        return {
            "result": True,
            "message": "success",
            "data": data,
            "data_top": data_top,
            "data_page": data_page
        }
