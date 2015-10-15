
image_aspect
============

The *image_aspect* library will allowing to adjust the images to different aspects according to the need.

Each aspect is a way to work an image to allow it to adjust to the desired size


Installing
----------

For install image_aspect, run on terminal: 
```bash

    $ cd image_aspect
    $ [sudo] python setup.py install
```

Using ImageAspect
-----------------

```python

    from image_aspect import ImageAspect
    ia = ImageAspect('/tmp/wallpaper.jpg')
    ia.aspect(aspect='distortion', width=200, height=100)
    ia.save('/tmp/wallpaper_200_100.jpg')
    print(ia.base64())
```

Development
----------

* Source hosted at [GitHub] (https://github.com/sxslex/ImageAspect)

Pull requests are very welcomed! Make sure your patches are well tested.
