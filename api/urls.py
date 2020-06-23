from api.views import PostViewSet
from rest_framework.routers import DefaultRouter
from django.conf.urls import include, url

router = DefaultRouter()

router.register(r'Post', PostViewSet)

urlpatterns = [
    url(r'',include(router.urls))
]
