from gevent import monkey
monkey.patch_all()

from gevent.pywsgi import WSGIServer
from flask import Flask
from flask_restplus import Api
from netstatd_engine.api.system_resources import api as system_resources
from netstatd_engine.common.logging_utils import get_logger, set_logger_level, DEBUG


app = Flask(__name__)
api = Api(app=app, title='NetstatD Engine API', version='0.1')
api.add_namespace(system_resources)


def main():
    logger = get_logger('netstatd-engine-server')
    set_logger_level(logger, DEBUG)
    host, port = "0.0.0.0", 9001
    server_addr = (host, port)
    wsgi = WSGIServer(server_addr, app, log=get_logger('pywsgi'))
    logger.info('start server on %s:%s' % server_addr)
    wsgi.serve_forever()


if __name__ == '__main__':
    main()
