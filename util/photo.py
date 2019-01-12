from glob import glob
import os
from PIL import Image




def get_images(dirname):
    os.chdir('static')
    img_paths = glob('{}/*.jpg'.format(dirname))
    os.chdir('..')
    return img_paths


def make_thumb(path):
    """
    在thumbs目录生成小图
    """
    im = Image.open(path)
    size = (200, 200)
    im.thumbnail(size)
    filename = os.path.basename(path)
    name, ext = os.path.splitext(filename)
    im.save('static/uploads/thumbs/{}_{}x{}{}'.format(name, size[0], size[1], ext), 'JPEG')
