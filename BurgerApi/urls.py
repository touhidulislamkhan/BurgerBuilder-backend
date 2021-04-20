from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewset

router = DefaultRouter()
router.register(r'user', UserProfileViewset)

urlpatterns = [

] + router.urls
