import os
import sys
import daemon
from loguru import logger
from app import main


if __name__ == "__main__":
    sys.argv.pop(0)
    if data := sys.argv:
        host = data[0]
        port = data[1]
        type_conn = data[2]
    else:
        host = 'my.bank-hlynov.ru'
        port = 443
        type_conn = 'tcp'

    with daemon.DaemonContext(working_directory=os.getcwd()):
        logger.add(f"log_{host}.log", rotation="1 min", retention="2 min")
        pid = os.getpid()
        os.system(f"echo {pid} > pid_{host}.py")
        main(host, port, type_conn, logger)
        logger.info('end')


