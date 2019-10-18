import io
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer

###########
# APIVIEW #
###########


# class snippet_list(APIView):
#     """
#     View to list all snippets in the system, and also add a new snippet
#     """
#     def get(self, request, format=None):
#         """
#         Method to list all snippets, or create a new snippet
#         """
#         queryset = Snippet.objects.all()
#         serializer = SnippetSerializer(queryset, many=True)
#         res = Response(serializer.data)
#         return res
    
#     def post(self, request, format=None):
#         """
#         Method to add a new snippet
#         """
#         serializer = SnippetSerializer(data=request.data)
#         serializer.is_valid()
#         serializer.save()
#         res = Response(serializer.data, status=status.HTTP_201_CREATED)
#         return res

# class snippet_detail(APIView):
#     """
#     View to retrieve, update or delete a snippet
#     """
#     def get_object(self, pk):
#         """
#         Get the snippet instance
#         """
#         try:
#             snippet = Snippet.objects.get(pk=pk)
#             return snippet
#         except:
#             raise Http404

#     def get(self, request, pk, format=None):
#         """
#         Show the snippet
#         """
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         res = Response(serializer.data)
#         return res

#     def put(self, request, pk, format=None):
#         """
#         Update a snippet
#         """
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             res = Response(serializer.data, status=status.HTTP_200_OK)
#             return res
#         else:
#             res = Response(status = status.HTTP_400_BAD_REQUEST)
#             return res

#     def delete(self, request, pk, format=None):
#         """
#         Delete a snippet
#         """
#         snippet = self.get_object(pk)
#         snippet.delete()
#         res = Response(status=status.HTTP_204_NO_CONTENT)
#         return res

###########
# GENERIC #
###########


# class snippet_list(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     """
#     View to list all snippets in the system, and also add a new snippet
#     """
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request):
#         """
#         Method to list all snippets, or create a new snippet
#         """
#         res = self.list(request)
#         return res

#     def post(self, request):
#         """
#         Method to add a new snippet
#         """
#         res = self.create(request)
#         return res


# class snippet_detail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     """
#     View to retrieve, update or delete a snippet
#     """
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         """
#         Show a snippet
#         """
#         res = self.retrieve(request, *args, **kwargs)
#         return res

#     def put(self, request, pk, *args, **kwargs):
#         """
#         Update a snippet
#         """
#         res = self.update(request, *args, **kwargs)
#         return res

#     def delete(self, request, *args, **kwargs):
#         """
#         Delete a snippet
#         """
#         res = self.destroy(request, *args, **kwargs)
#         return res

###########
# MIXEDIN #
###########


class snippet_list(generics.ListCreateAPIView):
    """
    View to list all snippets in the system, and also add a new snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class snippet_detail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete a snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


############
# FUNCTION #
############


# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
#     """
#     GET returns a list off all snippets, POST adds a new snippet to db
#     """

#     if request.method == "GET":
#         queryset = Snippet.objects.all()
#         serializer = SnippetSerializer(queryset, many=True)
#         res = Response(serializer.data, status=status.HTTP_200_OK)
#         return res

#     if request.method == "POST":
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             res = Response(serializer.data, status=status.HTTP_201_CREATED)
#             return res
#         else:
#             res = Response(status=status.HTTP_400_BAD_REQUEST)
#             return res


# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
#     """
#     GET returns requested snippet, PUT updates snippet, DEL deletes snippet
#     """
    
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except:
#         res = Response(status=status.HTTP_404_NOT_FOUND)
#         return res

#     if request.method == "GET":
#         serializer = SnippetSerializer(snippet)
#         res = Response(serializer.data, status=status.HTTP_200_OK)
#         return res
    
#     if request.method == "PUT":
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             res = Response(serializer.data, status = status.HTTP_202_ACCEPTED)
#             return res
#         else:
#             res = Response(status=status.HTTP_400_BAD_REQUEST)
#             return res

#     if request.method == "DELETE":
#         snippet.delete()
#         res = Response(status=status.HTTP_204_NO_CONTENT)
#         return res