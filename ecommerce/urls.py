"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from .views import SignUpView
from .views import CatAttributeList
from .views import CatCategoryList
from .views import CatPayTypeList
from .views import CatSkillList
from .views import CatStatusOrderList
from .views import CatTypeUserList

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('attributes/', CatAttributeList.as_view()),
    path('categories/', CatCategoryList.as_view()),
    path('paytypes/', CatPayTypeList.as_view()),
    path('skills/', CatSkillList.as_view()),
    path('orderstatus/',CatStatusOrderList.as_view()),
    path('typeusers/', CatTypeUserList.as_view()),
]
