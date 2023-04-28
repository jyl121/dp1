"""
URL configuration for dp1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import shop01.views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', shop01.views.index), #/주소로 클라이언트가 요청하면, 오른쪽의 함수가 호출되어 처리함.
    path('shop01/', shop01.views.start),
    path('shop01/index1', shop01.views.index1),
    path('shop01/index2', shop01.views.index2),
    path('shop01/index0', shop01.views.index0),
    path('shop01/index3', shop01.views.index3),
    path('shop01/index4', shop01.views.index4)
    # 이렇게 ,뒤에 클래스 안쓰고 함수쓰면 내부적으로 어떤일이 일어나는지, 에러도 잡기 쉬움.
    # 완전히 이해 다 하고 익숙해지면 나중에 클래스로 바꾸고. 더 간결.
]
