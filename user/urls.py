from django.urls import path, include
from rest_framework import routers
from .views import Userviews

router = routers.DefaultRouter()
router.register(r"users",Userviews)








urlpatterns = [
    path('', include(router.urls)),
]
