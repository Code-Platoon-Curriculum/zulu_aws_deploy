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
from .serializers import ListSerializer, List

class Lists_test(APIView):
    def get(self, request):
        return Response("api/lists/test response")

# Create your views here.
class All_lists(TokenReq):
    def get(self, request):
        try:
            all_lists = ListSerializer(request.user.lists.order_by("id"), many=True)
            return Response(all_lists.data, status=HTTP_200_OK)
        except Exception as e:
            return Response(e, status=HTTP_400_BAD_REQUEST)

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id
        ser_list = ListSerializer(data = data)
        if ser_list.is_valid():
            ser_list.save()
            return Response(ser_list.data, status=HTTP_201_CREATED)
        else:
            print(ser_list.errors)
            return Response(ser_list.errors, status=HTTP_400_BAD_REQUEST)
        
class A_list(TokenReq):
    def get_list(self, request, list_id):
        return get_object_or_404(request.user.lists, id=list_id)
    
    def get(self, request, list_id):
        return Response(ListSerializer(self.get_list(request, list_id)).data, status=HTTP_200_OK)
    
    def put(self, request, list_id):
        curr_list = self.get_list(request, list_id)
        ser_list = ListSerializer(curr_list, data= request.data, partial=True)
        if ser_list.is_valid():
            ser_list.save()
            return Response(ser_list.data, status=HTTP_200_OK)
        else:
            return Response(ser_list.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, list_id):
        curr_list = self.get_list(request, list_id)
        curr_list.delete()
        return Response(status=HTTP_204_NO_CONTENT)