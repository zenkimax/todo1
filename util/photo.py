def get_images():
    img_paths = []
    for i in range(1,5):
        img_paths.append('imgs/{}.jpg'.format(i))
    return img_paths