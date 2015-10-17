try:
    from PIL import Image
except ImportError:
    import Image


def thumbnail_convert(img, width, height):
    return img.thumbnail((width, height), Image.ANTIALIAS)
