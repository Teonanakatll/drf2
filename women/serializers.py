import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from women.models import Women


class WomenSerializer(serializers.ModelSerializer):
    # для автомотическаго заполнения поля юзер данными текущего пользавателя
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Women
        fields = '__all__'


# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     # read_only=True - только чтение при добавлении в бд
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Women.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         # выбранной записи устанавливаем значение из словаря validated_data или оставляем старое значение
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.time_update = validated_data.get("time_update", instance.time_update)
#         instance.is_published = validated_data.get("is_published", instance.is_published)
#         instance.cat_id = validated_data.get("cat_id", instance.cat_id)
#         instance.save()
#         return instance

    # def delete(self, instance):
    #     instance.delete()
    #     return instance.title

# def encode():
#     model = WomenModel('Angelina Jolie', 'content: Angelina Jolie')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='/n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"Cntent: Angelina Jolie"}')
#     data = JSONParser().parse(stream)
#     # чтобы сериализатор декодировал джсон строку в абьекты пайтон необходимо передать в
#     # параметр data распарсеные json данные
#     serializer = WomenSerializer(data=data)
#     # проверяес коректность переданных данных
#     serializer.is_valid()
#     print(serializer.validated_data)