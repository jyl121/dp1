from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# 주소 요청 하나당 함수를 하나 호출하는 방식!!
# 호출되는 함수는 반드시 입력값으로 request 객체를 가져야 함.
# request 객체는 클라이언트가 입력한 데이터를 서버에서 받아주는 역할의 부품.
def start(request):
    print('shop01 주소로 요청했을 때, start함수가 호출됨.')
    return HttpResponse("start 함수 호출!!!")

def index(request):
    return HttpResponse("<body bgcolor=yellow>장고 첫 페이지입니다!!!</body><br>" +
                        "<a href=http://www.naver.com>네이버로 이동</a><br>" +
                        "<a href=http://www.daum.net>다음으로 이동</a><br>" +
                        "<a href=admin>관리자모드로 이동</a><br>" +
                        "<a href=shop01>shop01시작 페이지로</a><br>" +
                        "<a href=shop01/index1>shop01/index1페이지로</a><br>" +
                        "<a href=shop01/index2>shop01/index2페이지로</a><br>" +
                        "<a href=shop01/index0>shop01/index0페이지로</a><br>" +
                        "<a href=shop01/index3>shop01/index3페이지로</a><br>" +
                        "<a href=shop01/index4>shop01/index4페이지로</a><br>"
                        )

def index1(request):
    return HttpResponse("<body bgcolor=pink>장고 index1 페이지입니다!!!</body>")

def index2(request):
    return HttpResponse("<font color=red>장고</font> index2 페이지입니다!!!")

def index0(request):
    return render(request, 'shop01/index.html')

def index3(request):
    return render(request, 'shop01/index3.html')

def index4(request):
    return render(request, 'shop01/index4.html')