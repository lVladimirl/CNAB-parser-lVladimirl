from django.urls import path
from .views import CnabTemplateView, CnabView
urlpatterns = [
    # path("list/", cnab_upload, name='list'),
    path("form/", CnabTemplateView.as_view()),
    path("parser/", CnabView.as_view(), name='parser')
]