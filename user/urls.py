from django.urls import path, include
from rest_framework import routers
from .views import UserViews, UserProfileViews,PostViews, LikeViews,PokeViews,CommentsViews,MessageViews,CustomAuthToken,PlogPostcommetsViews,PlogPostViews

router = routers.DefaultRouter()
router.register(r"users",UserViews)
router.register(r"profile",UserProfileViews)
router.register(r"posts",PostViews)
router.register(r"like",LikeViews)
router.register(r"poke",PokeViews)
router.register(r"comments",CommentsViews)
router.register(r"message",MessageViews)
router.register(r"plogPost",PlogPostViews)
router.register(r"plogPostComment",PlogPostcommetsViews)








urlpatterns = [
    path('', include(router.urls)),
    path('auth', CustomAuthToken.as_view()),
]
