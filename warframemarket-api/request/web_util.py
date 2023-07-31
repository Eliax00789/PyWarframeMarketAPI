import json
import time

import requests


class WebUtil:
    def __init__(self, api_url: str, login_url: str, rate_limit: int = 0.75):
        self._session = requests.Session()
        self._api_url = api_url
        self._login_url = login_url
        self._auth_cookie = None
        self._last_request = time.time()
        self._rate_limit = rate_limit

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._session.close()

    def signin(self, data: dict) -> dict:
        csrf_token = self._get_csrf_token()

        response = self._session.post(
            self._api_url + '/auth/signin',
            data=json.dumps(data),
            headers={
                'content-type': 'application/json',
                'x-csrftoken': csrf_token,
            }
        )

        response_json = response.json()
        if 'payload' in response_json:
            self._auth_cookie = response.headers['set-cookie']
        return response_json

    def _get_csrf_token(self) -> str:
        response = self._session.get(self._login_url)
        login_page_html = response.text
        login_page_html = login_page_html.split('<meta name="csrf-token" content="', 1)[1].split('">', 1)
        return login_page_html[0]

    def request(self, target_method: str, url: str, data: dict | None):
        time_since_last_request = time.time() - self._last_request
        if time_since_last_request < self._rate_limit:
            time.sleep(self._rate_limit - time_since_last_request)
        self._last_request = time.time()
        method = getattr(self._session, target_method)
        headers = {}
        if data is not None:
            data = json.dumps(data)
            headers['Content-Type'] = 'application/json'
        response = method(
            self._api_url + url,
            data=data,
            headers=headers
        )
        if response.status_code == 503:
            return {'error': 'Rate limit exceeded'}
        try:
            return response.json()
        except requests.JSONDecodeError:
            raise RuntimeError(response.text)
