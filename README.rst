======
image_aspect
======

.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/sxslex/image_aspect
   :target: https://gitter.im/sxslex/image_aspect?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. image:: https://travis-ci.org/sxslex/image_aspect.svg?branch=master
    :target: https://travis-ci.org/sxslex/image_aspect

The "image_aspect" library will allowing to adjust the images to different aspects according to the need.

Each aspect is a way to work an image to allow it to adjust to the desired size

Installing
--------

For install image_aspect, run on terminal: ::

    $ [sudo] cd image_aspect
    $ [sudo] python setup.py install

Using image_aspect
--------

.. code-block:: python


    from image_aspect import ImageAspect
    ia = ImageAspect('/tmp/wallpaper.jpg')
    ia.aspect(aspect='thumbnail', width=200, height=100)
    ia.save('/tmp/wallpaper_200_100.jpg')
    print(ia.base64())


Development
--------

* Source hosted at `GitHub <https://github.com/sxslex/image_aspect>`_

Pull requests are very welcomed! Make sure your patches are well tested.

Running the tests
--------

All you need is: ::

    $ nosetests -dsv --with-yanc --with-coverage --cover-package image_aspect tests/test_*.py



