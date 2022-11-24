from rest_framework import views 
from rest_framework import generics

from .forms import UploadFileForm
from .serializers import CnabSerializer
from .models import Cnab
from utils.file_handler import file_handler

from django.shortcuts import render

import  ipdb
# def cnab_upload(request):
#     if request.method == "POST":
#         form = UploadFileForm(request.POST, request.FILES)
#         file = request.FILES['file']
#         array = file.read().decode('windows-1252').splitlines()
#         macacos = file_handler(array)
#         serializer = CnabSerializer(macacos, many=True)
#         print(serializer.data)
#         # return HttpResponse("the name of the file " + str(file))
#     else:
#         form = UploadFileForm()
#     return render(request, 'cnab/upload_cnab.html', {'form':form})

class FormTemplateView(views.APIView):
    def get(self, request: views.Request )-> views.Response:
        form = UploadFileForm()
        return render(request, 'cnab/upload_cnab.html', {'form':form})

class CnabView(generics.ListAPIView):
    queryset = Cnab.objects.all()
    serializer_class = CnabSerializer

    def post(self,request: views.Request)-> views.Response:    
        # form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES['file']
        raw_array = file.read().decode('windows-1252').splitlines()
        treat_array = file_handler(raw_array)
        for object in treat_array:
            serializer = CnabSerializer(data=object)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return views.Response(serializer.data, status=views.status.HTTP_201_CREATED)

            serializer = CnabSerializer(data=object)
            serializer.is_valid(raise_exception=True)
            cnab_register = Cnab.objects.create(**serializer.validated_data)
            cnab_register.save()

        # list_cnab = Cnab.objects.all()    
        
        # serializer_output = CnabSerializer(data=list_cnab, many=True)
        # if serializer_output.is_valid():
        #     return views.Response(serializer_output.data, status=views.status.HTTP_201_CREATED)
        # else:
        #     return views.Response(serializer_output.errors, status=views.status.HTTP_403_FORBIDDEN)

