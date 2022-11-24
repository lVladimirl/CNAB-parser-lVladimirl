from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import FormTemplateView, CnabView
urlpatterns = [
    path("form/", FormTemplateView.as_view()),
    path("parser/", CnabView.as_view(), name='parser'),
]