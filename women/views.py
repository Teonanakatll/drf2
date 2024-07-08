from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer


class WomenAPIView(APIView):
    def get(self, request):
        w = Women.objects.all()
        # так как сериализатор будет обрабатывать не одну а список записей указываем many=True,
        # и обращаемся к колекции data который будет представлять собой словарь преобразованных данных из таблицы Women
        return Response({'posts': WomenSerializer(w, many=True).data})

    def post(self, request):
        # создаём сериализатор на основе донных поступивших с пост запросом
        serializer = WomenSerializer(data=request.data)
        # проверяем коректность переданных данных
        serializer.is_valid(raise_exception=True)

        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': WomenSerializer(post_new).data})


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer