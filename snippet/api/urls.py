from django.conf.urls import url, include
from .views import SnippetsViewSet, TagsViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("snippet", SnippetsViewSet, basename="snippet")
router.register("tag", TagsViewSet, basename="tag")


urlpatterns = [
    url('', include(router.urls))
]
