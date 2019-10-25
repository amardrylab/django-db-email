"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from home.views import CustomerView, CustomerList, CustomerDetail, CustomerUpdate, CustomerDelete, sendemailto
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer', CustomerView.as_view(), name='customer_create'),
    path('success', TemplateView.as_view(template_name='success.html')),
    path('list', CustomerList.as_view(), name='customer_list'),
    path('detail/<int:pk>', CustomerDetail.as_view(), name='customer_detail'),
    path('update/<int:pk>', CustomerUpdate.as_view(), name='customer_update'),
    path('delete/<int:pk>', CustomerDelete.as_view(), name='customer_delete'),
    path('mailto/<int:customerid>', sendemailto, name='mail_to_customer'),
    path('success_mail', TemplateView.as_view(template_name='success_mail.html')),

]
