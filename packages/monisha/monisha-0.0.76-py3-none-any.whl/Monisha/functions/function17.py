import os
import random
from ..scripts import Scripted
from urllib.parse import unquote
from urllib.parse import urlparse
#=========================================================================


class SMessages:
    def __init__(self, **kwargs):
        self.errors = kwargs.get("errors", None)
        self.result = kwargs.get("result", None)
        self.filename = kwargs.get("filename", None)
        self.extension = kwargs.get("extension", None)

#=========================================================================

class Filename:

    async def get01(extension=None):
        mainos = str(random.randint(10000, 100000000000000))
        moonus = mainos + extension if extension else mainos
        return moonus

#=========================================================================

    async def get02(filename):
        nameas = str(filename)
        finame = os.path.splitext(nameas)[0]
        exexon = os.path.splitext(nameas)[1]
        exoexo = exexon if exexon else Scripted.DATA06
        moonus = finame if finame else Scripted.DATA13
        return SMessages(filename=moonus, extension=exoexo)

#=========================================================================

    async def get03(filelink):
        try:
            findne = urlparse(filelink)
            fnameo = os.path.basename(findne.path)
            moonus = unquote(fnameo)
            return SMessages(filename=moonus, errors=None)
        except Exception as errors:
            return SMessages(filename=Scripted.DATA14, errors=errors)

#=========================================================================

    async def get04(location):
        try:
            moonus = str(os.path.basename(location))
            return SMessages(filename=moonus, errors=None)
        except Exception as errors:
            return SMessages(filename=Scripted.DATA14, errors=errors)

#=========================================================================
