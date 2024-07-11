"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import djoser
from django.contrib import admin
from django.urls import path, include, re_path

from women.views import WomenAPIList, \
    WomenAPIDestroy, WomenAPIUpdate  # WomenViewSet, WomenAPIList, WomenAPIUpdate, WomenAPIDetailView, WomenAPIView

from rest_framework import routers


# router = routers.SimpleRouter()
router = routers.DefaultRouter()

# при использовании DefaultRouter можно обращаться к корню маршрутов (api/v1/) чтобы получить запись, и автоматически
# появляются имена у маршрутов по имени моделей

# если во вьюсете не указан queryset в роутере необходимо указать параметп basename='имя' которае будет использоваться
# в имени вместо имени модели в названии маршрута

# регистрируем вьюсет в роутере, придумываем префикс и укаываем вьюсет
# router.register(r'women', WomenViewSet)
# print(router.urls)

urlpatterns = [

    path('admin/', admin.site.urls),  # http://127.0.0.1:8000/api/v1/women/
    # path('api/v1/', include(router.urls)),

    # маршрут авторизации на основе сессии и cookies, префикс придумываем сами
    path('api/v1/drf-auth/', include('rest_framework.urls')),

    # авторизация на основе токенов, пакет djoser
    path('api/v1/auth/', include('djoser.urls')),
    # ендпоинты токена (login, logout)
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),


    # во вьюсетах можно указывать метод обработки запроса и
    # метод который будет вызываться в самом вьюсете
    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),

    # path('api/v1/womenlist/', WomenAPIList.as_view()),
    # path('api/v1/womenlist/<int:pk>/', WomenAPIUpdate.as_view()),
    # path('api/v1/womendetail/<int:pk>/', WomenAPIDetailView.as_view()),
]
