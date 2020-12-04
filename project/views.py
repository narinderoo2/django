from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.filters import OrderingFilter
from project.models import Pizza
from project.serializers import PizzaSerializer
from rest_framework import generics, permissions, status, authentication, mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class TotalPizzaAPIView(APIView):

    def get(self,request):
        article = Pizza.objects.all()
        serializer = PizzaSerializer(article,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = PizzaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class PizzaDetail(APIView):

    def get_object(self, id):
        try:
            return Pizza.objects.get(id = id)
        except Pizza.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request, id):
        article = self.get_object(id)
        serializer = PizzaSerializer(article)
        return Response(serializer.data)

    def put(self,request,id):
        article = self.get_object(id)
        serializer = PizzaSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,mixins.CreateModelMixin, mixins.UpdateModelMixin
    , mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()

class SearchListView(generics.ListAPIView):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()
    filter_backends = [SearchFilter,OrderingFilter]
    ordering_fields = ['Type_of_pizza','Size_of_pizza']
    search_fields = ['Type_of_pizza','Size_of_pizza']
