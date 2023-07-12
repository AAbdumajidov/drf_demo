from django.http import JsonResponse
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer, PostCreateSerializer
from rest_framework import status, generics


@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def post_detail(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise NotFound("404")
    serializer = PostSerializer(post)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def post_create(request):
    data = request.data
    serializer = PostCreateSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def post_update(request, pk):
    try:
        instance = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise NotFound("404")

    data = request.data
    serializer = PostCreateSerializer(instance, data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PATCH'])
def post_partial_update(request, pk, **kwargs):
    try:
        instance = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise NotFound("404")
    data = request.data
    partial = kwargs['partial'] = True
    serializer = PostCreateSerializer(instance, data=data, partial=partial)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def post_list_create(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    data = request.data
    serializer = PostCreateSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def post_delete(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise NotFound("404")
    post.delete()
    return Response({"detail":"successfully deleted"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE', 'PUT', 'PATCH', 'GET'])
def post_rud(request, pk, **kwargs):
    try:
        instance = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise NotFound("404")
    data = request.data

    if request.method == 'DELETE':
        instance.delete()
        return Response({"detail":"successfully deleted"}, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PATCH':
        partial = kwargs['partial'] = True
        serializer = PostCreateSerializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = PostCreateSerializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'GET':
        serializer = PostSerializer(instance)

    return Response(serializer.data, status=status.HTTP_200_OK)

