from django.db import models
from django.forms import ValidationError

from SolidProxy.swconst.swDocumentTypes_e import swDocumentTypes_e

# Create your models here.

def _validFileType(i:int) -> bool:
    try:
        _ = swDocumentTypes_e(i)
        return True
    except ValueError:
        raise ValidationError


class SWModel(models.Model):
    title = models.CharField(max_length=60)
    filetype = models.IntegerField(
        validators=[_validFileType],
        default=swDocumentTypes_e.swDocNONE.value,      
    )
    bodycount = models.IntegerField(
        default=-1,
    )
    facecount = models.IntegerField(
        default=-1,
    )

    def __str__(self) -> str:
        return self.title

    def my_hash(self) -> int:
        return hash((self.title, self.filetype, self.bodycount, self.facecount))
    