from django.urls import path
from .views import AuthViews, MemberViews

urlpatterns = [
    path("auth", AuthViews.as_view()),
    path("member", MemberViews.as_view()),
]
