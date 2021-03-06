import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

from handlers import main

define('port',default='8000',help='Listening port',type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            ('/',main.IndexHandler),
            ('/explore',main.ExploreHandler),
            ('/post/(?P<post_id>[0-9]+)',main.PostHandler),
            ('/upload',main.UploadHandler)
        ]
        settings = dict(
            debug = True,
            template_path = 'templates',
            static_path = 'static', #设置static目录
            # static_url_prefix = '/pics/'  #设置目录修饰
        )
        super().__init__(handlers, **settings)

application = Application()

if __name__ == '__main__':
    tornado.options.parse_command_line()
    application.listen(options.port)
    print('Server start on port{}'.format(str(options.port)))
    tornado.ioloop.IOLoop.current().start()