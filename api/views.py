from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import PostSerializer
from api.models import Post
from rest_framework.decorators import action
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
    @action(detail=False)
    def boast(self, request):
        boast = Post.objects.filter(boast_or_roast=True).order_by('-date')
        page = self.paginate_queryset(boast)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.boast)
        serializer = self.get_serializer(boast, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roast(self, request):
        roast = Post.objects.filter(boast_or_roast=False).order_by('-date')
        page = self.paginate_queryset(roast)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.roast)
        serializer = self.get_serializer(roast, many=True)
        return Response(serializer.data)
