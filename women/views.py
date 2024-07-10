from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women, Category
from .serializers import WomenSerializer


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

    # для возвращения определённх записей необходимо переопределить метод get_queryset
    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Women.objects.all()[:3]
        return Women.objects.filter(pk=pk)

    # для добавления собственных маршрутов во ViewSet например для вывода списка категорий
    # detail=True для возвращения одной записи, False - для списка
    @action(methods=['get'], detail=False)
    # имя функции подставляется в адрес марщрута api/v1/women/category/
    # для возвращения отдельной записи необходимо дописать параметр pk
    def category(self, request):
        cats = Category.objects.all()
        return Response({'cats': [c.name for c in cats]})

# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# class WomenAPIView(APIView):
#     def get(self, request):
#         w = Women.objects.all()
#         # так как сериализатор будет обрабатывать не одну а список записей указываем many=True,
#         # и обращаемся к колекции data который будет представлять собой словарь преобразованных данных из таблицы Women
#         return Response({'posts': WomenSerializer(w, many=True).data})
#
#     def post(self, request):
#         # создаём сериализатор на основе донных поступивших с пост запросом
#         serializer = WomenSerializer(data=request.data)
#         # проверяем коректность переданных данных
#         serializer.is_valid(raise_exception=True)
#         # вызывает метод create() сериализатора
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         # из переданных данных берём pk
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         instance.delete()
#
#
#         return Response({"post": f'Delete post - {pk}'})


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer