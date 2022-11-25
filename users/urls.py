from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateUserView, ListDetailUserView
urlpatterns = [
    path("admin/login/", obtain_auth_token),
    path("", CreateUserView.as_view()),
    path("<str:id>/", ListDetailUserView.as_view()),
]