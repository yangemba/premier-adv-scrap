import logging
from tornado import web
import tornado.ioloop
import time
import asyncio

def setup_logging():
    logger = logging
    return logger


class FileManagerHandler(web.RequestHandler):

    async def get(self):
        logging.warning('req')
        # await asyncio.sleep(1)
        return self.finish()


if __name__ == "__main__":
    application = tornado.web.Application(logging=setup_logging(),
                                          handlers=[(r"/",
                                                     FileManagerHandler)],
                                          )
    application.listen(8888)
    file_list_holder = []
    tornado.ioloop.IOLoop.current().start()




