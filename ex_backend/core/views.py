from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import NoteSerializer, SWModelSerializer
from .models import Notes, SWModel

# Create your views here.

def front(request):
    context = { }
    return render(request, "index.html", context)


@api_view(['GET', 'POST'])
def note(request):

    if request.method == 'GET':
        note = Notes.objects.all()
        serializer = NoteSerializer(note, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def note_detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_all_models(request):

    m = SWModel.objects.all()
    serializer = SWModelSerializer(m, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_models_hash(request):
    """Get the model hash to determine if open models have changed"""
    m = SWModel.objects.values_list('title', flat=True)
    h = hash(tuple(m))
    print(f'\thash: {h}')
    return Response(data={'h': h})