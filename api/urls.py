from api.views import PostViewSet
from rest_framework.routers import DefaultRouter
from django.conf.urls import include, url
from django.urls import path
from . import views

router = DefaultRouter()

router.register(r'Post', PostViewSet)

urlpatterns = [
    url(r'',include(router.urls)),
    path('addpost/', views.addpost, name = 'addpost')
]
