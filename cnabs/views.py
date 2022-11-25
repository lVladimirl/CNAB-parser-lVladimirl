from rest_framework import views 
from rest_framework import generics

from .forms import UploadFileForm
from .serializers import CnabSerializer, CnabViewSerializer
from .models import Cnab
from users.models import User
from shops.models import Shop
from utils.file_handler import file_handler

from django.shortcuts import render

class CnabTemplateView(views.APIView):
    def get(self, request: views.Request )-> views.Response:
        form = UploadFileForm()
        return render(request, 'cnabs/upload_cnab.html', {'form':form})

class CnabView(generics.ListAPIView):
    queryset = Cnab.objects.all()
    serializer_class = CnabSerializer

    def post(self,request: views.Request)-> views.Response:    
        array =[]
        file = request.FILES['file']
        raw_array = file.read().decode('windows-1252').splitlines()
        treat_array = file_handler(raw_array)

        for object in treat_array:
            owner, q = User.objects.get_or_create(username=object['owner'], cpf=object['cpf'])
            shop, q = Shop.objects.get_or_create(name=object['shop'],owner=owner)
            data = {
                "type":object['type'],
                "date":object['date'],
                "value":object['value'],
                "card":object['card'],
                "hour":object['hour'],
            }
            serializer = CnabSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save(owner=owner, shop=shop)
            array.append(serializer.data)
        return_array = Cnab.objects.all()
        serializer = CnabViewSerializer(return_array, many=True)
        return views.Response(serializer.data, status=views.status.HTTP_201_CREATED)

    
