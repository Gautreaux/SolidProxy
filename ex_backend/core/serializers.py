

from rest_framework import serializers
from .models import SWModel

class SWModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SWModel
        fields = (
            'title',
            'filetype',
            'bodycount',
            'facecount',
        )
    