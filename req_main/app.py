import logging
import time
import socket
import random
import sys
from main import logger
import requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from threading import current_thread




def get_request(url: str):
    """
    :param url: "https://google.com"
    :return:
    """
    flag = True
    res_get_status = 0
    while flag:
        count_error = 0
        count_success = 0
        for i in range(1000):
            try:
                res_get = requests.get(url, timeout=10)
                res_get_status = res_get.status_code
                # print(f"{url} :  {res_get_status}")
                logger.info(f'Site {url} has GET status {res_get_status} {current_thread().getName()} count {count_success}')

                count_success += 1
            except:
                count_error += 1
                logger.error(f'Site {url} has some problem with GET connection thread {current_thread().getName()} count {count_error}')
                # print(f'Site {url} has some problem with GET connection thread {current_thread().getName()} count {count_error}')
            try:
                requests.post(url)
            except:
                logger.error(f'Site {url} has some problem with POST connection')
                # print(f'Site {url} has some problem with POST connection')

        if not flag and count_error > 300:
            break
        logger.debug(f"Success connection {url} are {count_success}")
        # print(f"Success connection {url} are {count_success}")
        logger.error(f"Error connection {url} are {count_error}")
        # print(f"Error connection {url} are {count_error}")
        logger.debug(f'Site {url} was made GET with status {res_get_status}')
        # print(f'Site {url} was made GET with status {res_get_status}')


def do_threads(max_workers, list_url):
    """

    :return:
    """
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for ul in list_url:
            executor.submit(get_request, ul)
    return


if __name__ == "__main__":
    logger.info('START PROGRAMMING')
    sys.argv.pop(0)
    if (url := sys.argv):
        url = url
    else:
        # url = ["https://gosuslugi1.ru/", "https://gosuslugi.ru/", "https://sber.ru", "https://lenta.ru/", "https://riafan.ru/", "https://savelife.pw/"]
        #        # "https://profile.sber.ru", "https://developers.sber.ru/portal/tools/api-sber"]
        url = ["https://esia.gosuslugi.ru", "https://lukoil.com", "https://www.gazprom.ru", "https://nlmk.com", "https://tektorg.ru",
            "https://ruspolitnews.ru/"
            # "https://Acron.ru"
            ]

    # get_request(url)
    do_threads(12, url)
