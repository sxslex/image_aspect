# -*- coding: utf-8 -*-
#
# Copyright 2015 Alexandre Villela (SleX) <https://github.com/sxslex/sxtools/>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    by sx.slex@gmail.com

import os
# import pprint
import unittest
# import tempfile
import ImageAspect
PROJECT_APPLICATION_PATH = os.path.dirname(os.path.abspath(__file__))
CACHE_PATH = PROJECT_APPLICATION_PATH


class TestImageAspect(unittest.TestCase):

    def test_01_image_aspect_contents(self):
        filename_or_obj = os.path.join(CACHE_PATH, 'imgs/wallpaper.jpg')
        ai = ImageAspect.ImageAspect(filename_or_obj)
        ai.aspect(width=200, height=100, aspect='distortion')
        self.assertTrue(len(ai.contents()) > 2000)

    def test_02_image_aspect_base64(self):
        filename_or_obj = os.path.join(CACHE_PATH, 'imgs/wallpaper.jpg')
        ai = ImageAspect.ImageAspect(filename_or_obj)
        ai.aspect(width=200, height=100, aspect='distortion')
        self.assertIn('data:image/JPEG;base64', ai.base64())

    def test_03_image_aspect_save(self):
        filename_or_obj = os.path.join(CACHE_PATH, 'imgs/wallpaper.jpg')
        new_filename = os.path.join(CACHE_PATH, 'imgs/wallpaper_new.jpg')

        ai = ImageAspect.ImageAspect(filename_or_obj)
        ai.aspect(width=200, height=100, aspect='distortion')
        ai.save(new_filename)
