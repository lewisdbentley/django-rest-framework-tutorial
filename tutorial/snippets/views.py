import io
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, mixins, generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.parsers import JSONParser
from rest_framework import renderers
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list-view', request=request, format=format),
        'snippets': reverse('list-view', request=request, format=format)
    })

class snippet_list(generics.ListCreateAPIView):
    """
    View to list all snippets, and also add a new snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class snippet_detail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete a snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.IsAuthenticatedOrReadOnly]

class snippet_highlight(generics.GenericAPIView):
    """
    View to retrieve highlighted code of a snippet
    """
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

class user_list(generics.ListAPIView):
    """
    View to list all users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class user_detail(generics.RetrieveAPIView):
    """
    View to retrieve a snippet
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer