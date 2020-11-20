import logging
from paste.translogger import TransLogger
from waitress import serve
from redirect_website.wsgi import application
import socket

class RunServer:
    def run_waitress_server(self):
        logger = logging.getLogger(type(self).__name__)

        PORT = 8080
        LISTEN = f"127.0.0.1:{PORT} [::1]:{PORT} {socket.gethostbyname(socket.gethostname())}:{PORT}"

        logger.info(f"Start Waitress Server: DEBUG=True, LOGGING_OUTPUT=True, LISTEN={LISTEN}")
        logger.info("Press CTRL+c to exit.")
        logger.propagate = True

        serve(
            TransLogger(
                application=application, logger=logger, setup_console_handler=True
            )
            , listen=LISTEN
        )


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime)s] | %(levelname)s | %(name)s | %(funcName)s | %(lineno)d | %(message)s'
    )
    RunServer().run_waitress_server()
