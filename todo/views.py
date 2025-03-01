from django.shortcuts import render

from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer


# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# @api_view(['GET', 'POST'])
# def todo_list(request):
#     if request.method == 'GET':
#         todos = Todo.objects.all().order_by('-created_at')
#         serializer = TodoSerializer(todos, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
