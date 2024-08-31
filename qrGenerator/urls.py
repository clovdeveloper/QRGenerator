
from django.urls import path

from qrGenerator import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('', views.QRCodeView.as_view(), name='qrcode')

]
