from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SWModelSerializer
from .models import SWModel

# Create your views here.

def front(request):
    context = { }
    return render(request, "index.html", context)


@api_view(['GET', 'DELETE'])
def get_all_models(request):

    if request.method == "GET":
        m = SWModel.objects.all()
        serializer = SWModelSerializer(m, many=True)
        return Response(serializer.data)
    elif request.method == "DELETE":
        SWModel.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_models_hash(request):
    """Get the model hash to determine if open models have changed"""
    m = map(lambda x: x.my_hash(), SWModel.objects.all())
    h = hash(tuple(m))
    print(f'\thash: {h}')
    return Response(data={'h': h})