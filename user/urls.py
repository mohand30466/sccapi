from django.urls import path, include
from rest_framework import routers
from .views import  BussinessStaffViews,ToDoListViews, BussinessUsViews, HoursViews, InvoicesViews, ShiftViews, UserViews, UserProfileViews,PostViews, LikeViews,PokeViews,CommentsViews,MessageViews,CustomAuthToken,PlogPostcommetsViews,PlogPostViews,ContactUsViews,PaysleeveViews

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
router.register(r"contactus",ContactUsViews)
router.register(r"bussines",BussinessUsViews)
router.register(r"staff",BussinessStaffViews)
router.register(r"shift",ShiftViews)
router.register(r"card",HoursViews)
router.register(r"invoice",InvoicesViews)
router.register(r"paysleeve",PaysleeveViews)
router.register(r"todolist",ToDoListViews)








urlpatterns = [
    path('', include(router.urls)),
    path('auth', CustomAuthToken.as_view()),
]
