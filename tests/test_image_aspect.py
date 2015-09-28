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
import unittest
import tempfile
from sxtools import ImageAspect
PROJECT_APPLICATION_PATH = os.path.dirname(os.path.abspath(__file__))
CACHE_PATH = PROJECT_APPLICATION_PATH


class TestImageAspect(unittest.TestCase):

    def test_image_aspect_1(self):
        filename_or_obj = os.path.join(CACHE_PATH, 'imgs/wallpaper.jpg')
        ai = ImageAspect(filename_or_obj)
        ai.aspect(aspect='distortion', width=200, height=100)
        self.assertIn(
            'data:image/jpeg;base64,',
            ai.base64()
        )

    def test_image_aspect_2(self):
        filename_or_obj = os.path.join(CACHE_PATH, 'imgs/wallpaper.jpg')
        ai = ImageAspect(filename_or_obj)
        ai.aspect(aspect='distortion', width=200, height=100)
        ai.save(os.path.join(tempfile.gettempdir(), 'filename_new.jpg'))
