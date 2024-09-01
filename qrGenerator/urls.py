from django.conf.urls.static import static
from django.urls import path

from QRGenerator import settings
from qrGenerator import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('', views.QRCodeView.as_view(), name='qrcode')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)