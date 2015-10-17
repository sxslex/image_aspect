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
# Lets you create a generic image to use in development servers
#    by sx.slex@gmail.com

import base64
try:
    from PIL import Image
except ImportError:
    import Image
from StringIO import StringIO

import aspects


class ImageAspect(object):

    def __init__(
        self,
        filename_or_obj=None
    ):
        self.new_img = None
        self.image_obj = Image.open(filename_or_obj)
        self._aspects = {}
        self._get_exif()
        self._adjustment_orientation()

    def _load_aspect(self, aspect):
        if self._aspects.get('aspect'):
            return self._aspects.get('aspect')
        try:
            self._aspects['aspect'] = getattr(aspects, '%s_convert' % aspect)
        except AttributeError:
            raise ValueError('Aspects (import) "%s" not found' % aspect)
        return self._aspects['aspect']

    def _adjustment_orientation(self):
        self.orientation = 1
        try:
            self.orientation = int(str(self.info_exif.get('Orientation', 1)))
        except:
            pass
        # rotaciona a imagem caso ela nao esteja correta
        if hasattr(self.image_obj, 'transpose'):
            if self.orientation == 2:
                # Vertical Mirror
                self.image_obj = self.image_obj.transpose(
                    Image.FLIP_LEFT_RIGHT
                )
            elif self.orientation == 3:
                # Rotation 180°
                self.image_obj = self.image_obj.transpose(Image.ROTATE_180)
            elif self.orientation == 4:
                # Horizontal Mirror
                self.image_obj = self.image_obj.transpose(
                    Image.FLIP_TOP_BOTTOM
                )
            elif self.orientation == 5:
                # Horizontal Mirror + Rotation 90° CCW
                self.image_obj = self.image_obj.transpose(
                    Image.FLIP_TOP_BOTTOM
                ).transpose(Image.ROTATE_90)
            elif self.orientation == 6:
                # Rotation 270°
                self.image_obj = self.image_obj.transpose(Image.ROTATE_270)
            elif self.orientation == 7:
                # Horizontal Mirror + Rotation 270°
                self.image_obj = self.image_obj.transpose(
                    Image.FLIP_TOP_BOTTOM
                ).transpose(Image.ROTATE_270)
            elif self.orientation == 8:
                # Rotation 90°
                self.image_obj = self.image_obj.transpose(Image.ROTATE_90)

    def _get_exif(self):
        self.info_exif = {}
        try:
            from PIL.ExifTags import TAGS
            if not hasattr(self.image_obj, '_getexif'):
                return {}
            info = self.image_obj._getexif()
            if info:
                for tag, value in info.items():
                    decoded = TAGS.get(tag, tag)
                    self.info_exif[decoded] = value
        except:
            pass
        return self.info_exif

    def contents(self, ):
        if not self.new_img:
            raise Exception('run aspect')
        r = StringIO()
        self.new_img.convert('RGB').save(r, 'JPEG')
        r.seek(0)
        content = r.read()
        r.close()
        return content

    def aspect(self, width, height, aspect='thumbnail'):
        func_aspect = self._load_aspect(aspect)
        self.new_img = self.image_obj.copy()
        return func_aspect(img=self.new_img, width=width, height=height)

    def save(self, filename_or_fobj):
        icontents = self.contents()
        if not icontents:
            raise Exception('run aspect')
        if getattr(filename_or_fobj, 'read', None) is not None:
            fobj = filename_or_fobj
        else:
            fobj = open(filename_or_fobj, mode='wb')
        fobj.write(icontents)
        fobj.close()
        return True

    def base64(self):
        icontents = self.contents()
        if not icontents:
            raise Exception('run aspect')
        return 'data:image/JPEG;base64,' + \
            base64.b64encode(icontents)
