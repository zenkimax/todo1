import tornado.web
from util.photo import get_images,make_thumb

class IndexHandler(tornado.web.RequestHandler):
    '''
    Homepage for users,photo feeds of follow
    '''
    def get(self, *args, **kwargs):
        imgs = get_images('uploads')
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
        imgs = get_images('uploads/thumbs')
        self.render('explore.html',imgs=imgs)

class UploadHandler(tornado.web.RequestHandler):
    '''
    图片上传处理
    '''
    def get(self, *args, **kwargs):
        self.render('upload.html')

    def post(self, *args, **kwargs):
        '''
        获取用户上传图片
        '''
        img_list = self.request.files.get('newimg',None)
        for img in img_list:
            save_to = 'static/uploads/{}'.format(img['filename'])
            with open(save_to,'wb') as f:
                f.write(img['body'])
            make_thumb(save_to)

        self.write('upload done')
