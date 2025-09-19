from .views import CategoryView, TagView, PostView
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("post", PostView, basename="post")
router.register("category", CategoryView, basename="category")
router.register("tag", TagView, basename="tag")
urlpatterns = [path("", include(router.urls))]
