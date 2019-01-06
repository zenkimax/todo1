import tornado.web
from util.photo import get_images

class IndexHandler(tornado.web.RequestHandler):
    '''
    Homepage for users,photo feeds of follow
    '''
    def get(self, *args, **kwargs):
        imgs = get_images()
        self.render('index.html',imgs=imgs)


class PostHandler(tornado.web.RequestHandler):
    def get(self, post_id):
        img_path = "imgs/{}.jpg".format(post_id)
        self.render('post.html', img_path=img_path)


class ExploreHandler(tornado.web.RequestHandler):
    '''
    Explorepage,photo for other users.
    '''
    def get(self, *args, **kwargs):
        imgs = get_images()
        self.render('explore.html',imgs=imgs)