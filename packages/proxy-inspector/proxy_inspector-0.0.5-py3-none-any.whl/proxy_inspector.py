import random
from urllib.parse import urlparse

import grequests

from useragents import ua


def exception_handler(request, exception):
    pass


class ProxyInspector:
    """
    a simple tool for verify proxy
    """

    def __init__(self, timeout=5):
        self.__timeout = timeout

    def validate(self, target_url: str, proxy_urls):
        """
        An Simple Tool for Validate Proxy \n
        :param target_url: Target URL, like "https://www.bing.com/robots.txt"
        :param proxy_urls: Proxy URL list, like ["http://127.0.0.1:7777"]
        :return: Return True if the condition is met

        """
        proxies = []

        # ----------------------------------------
        # Check Schema
        # ----------------------------------------
        proxies_obj_pending = []
        proxies_pending = []
        for proxy in proxy_urls:

            proxy_url_obj = urlparse(proxy)
            proxy_scheme = proxy_url_obj.scheme
            proxy_netloc = proxy_url_obj.netloc

            target_url_obj = urlparse(target_url)
            target_scheme = target_url_obj.scheme
            target_netloc = target_url_obj.netloc

            if proxy_scheme == target_scheme:
                proxies_obj_pending.append({proxy_scheme: proxy_netloc})
                proxies_pending.append(proxy)

        if len(proxies_obj_pending) == 0:
            return proxies

        # ----------------------------------------
        # Request Network
        # ----------------------------------------

        user_agent = random.choice(ua)
        headers = {
            'Referer': 'https://www.google.com/',
            'user-agent': user_agent,
        }
        rs = (grequests.get(target_url, proxies=proxy, headers=headers, timeout=self.__timeout) for proxy in
              proxies_obj_pending)
        res_list = grequests.map(rs, exception_handler=exception_handler)

        for k in range(0, len(res_list)):
            res = res_list[k]
            if res and res.status_code == 200:
                proxies.append(proxies_pending[k])

        return proxies
