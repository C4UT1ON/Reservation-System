from django.shortcuts import render
from .models import Item
from django.http import Http404
from rest_framework.response import Response
from .serializers import ItemSerializer
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
# Create your views here.


class ItemList(APIView):
    @csrf_exempt
    def get(self, request):
        items = Item.objects.all()
        return Response(ItemSerializer(items, many=True).data, status=status.HTTP_200_OK)

    @csrf_exempt
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemObject(APIView):
    @csrf_exempt
    def get_item(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, pk):
        item = self.get_item(pk)
        return Response(ItemSerializer(item).data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        serializer = ItemSerializer(self.get_item(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        self.get_item(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




