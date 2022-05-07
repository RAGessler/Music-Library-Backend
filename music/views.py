from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import MusicSerializer
from .models import Music
from music import serializer
# Create your views here.

@api_view(['GET','POST'])
def music_library(request):
    if request.method == 'GET':
        music = Music.objects.all()
        serializer = MusicSerializer(music, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
   
    elif request.method == 'POST':
        serializer = MusicSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def music_detail(request, pk):
    music = get_object_or_404(Music, pk=pk)
    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = MusicSerializer(music, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        serializer = MusicSerializer(music)
        music.delete()
        return_value = serializer.data
        return_value['id'] = pk
        return Response(return_value, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = MusicSerializer(music, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)