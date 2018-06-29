from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
from .forms import UploadForm
from django.views.decorators.http import require_POST
from shutil import copyfile
import os

from pygame import mixer

from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

@require_POST
@csrf_exempt
def index_upload(request):
    if request.method == 'POST':
        print("post")
        form = UploadForm(request.POST, request.FILES) #넘겨 받는다
        # file1 = request.FILES['myFile']
        print(form);
        # print(file1);
        if form.is_valid(): # 데이터가 있는지 확인
            print("파일 있음")
            fileName = form.data['fileName']
            print(fileName)
            file = request.FILES['uploadfile']
            # file = form.data['uploadfile']
            print(file)
            form.save()
            # print(os.getcwd())  # 현재 디렉토리의
            print(os.path.realpath(fileName))  # 파일
            # print(os.path.dirname(os.path.realpath(file)))  # 파일이 위치한 디렉토리

            # save_music(fileName)

            return render(request, 'index.html')
        else :
            print("파일 없음")
            print(form.errors)
            return HttpResponse("실패")


def save_music(src):
    copyfile("D:\\" + src, os.getcwd()+"\\media\\music")
    print(os.getcwd()+"\\media\\music")