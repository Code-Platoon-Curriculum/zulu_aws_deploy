from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from user_app.views import TokenReq
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

from .serialiers import TaskSerializer
# Create your views here.
class All_tasks(TokenReq):
    def get(self, request, list_id):
        # grab user from request find its lists and query by list id to get one list and grab all tasks belonging to said list
        tasks = TaskSerializer(request.user.lists.get(id=list_id).tasks, many=True)
        return Response(tasks.data, status= HTTP_200_OK)

    def post(self, request, list_id):
        data = request.data.copy()
        get_object_or_404(request.user.lists, id = list_id)
        data['parent_list'] = list_id
        new_task = TaskSerializer(data = data)
        if new_task.is_valid():
            new_task.save()
            return Response(new_task.data, status=HTTP_201_CREATED)
        else:
            return Response(new_task.errors, status=HTTP_400_BAD_REQUEST)