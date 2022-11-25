from django.urls import path
from .views import RegisterShopView,ListDetailUSerView
urlpatterns = [
    path("", RegisterShopView.as_view()),
    path("<str:id>/", ListDetailUSerView.as_view()),
]