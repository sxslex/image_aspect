======
ImageAspect
======

The ``ImageAspect`` library will allowing to adjust the images to different aspects according to the need.

Each aspect is a way to work an image to allow it to adjust to the desired size


Installing
--------

For install ImageAspect, run on terminal: ::

    $ [sudo] cd ImageAspect
    $ [sudo] python setup.py install

Using ImageAspect
--------

.. code-block:: python

    from ImageAspect import ImageAspect
    ia = ImageAspect('/tmp/wallpaper.jpg')
    ia.aspect(aspect='distortion', width=200, height=100)
    ia.save('/tmp/wallpaper_200_100.jpg')
    print(ia.base64())

development
--------

* Source hosted at `GitHub <https://github.com/sxslex/ImageAspect>`_

Pull requests are very welcomed! Make sure your patches are well tested.

Running the tests
--------

