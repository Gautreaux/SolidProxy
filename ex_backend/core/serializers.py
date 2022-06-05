

from rest_framework import serializers
from .models import Notes, SWModel

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ('id', 'title', 'content')

class SWModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SWModel
        fields = ('title',)
    