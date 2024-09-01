from django.shortcuts import render
from django.views import View
from django import forms
import os
import qrcode
from django.conf import settings

from qrGenerator.forms import QRCodeForm


class QRCodeView(View):
    form_class = QRCodeForm
    template_name = 'qr/qr_code.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'qr_code_url': None})

    def post(self, request):
        form = self.form_class(request.POST)
        qr_code_url = None

        if form.is_valid():
            url = form.cleaned_data['url']
            box_size = form.cleaned_data['box_size']
            border_size = form.cleaned_data['border_size']

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=box_size,
                border=border_size,
            )
            qr.add_data(url)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads", "qr")
            media_folder = os.path.join(settings.MEDIA_ROOT, "qr")
            os.makedirs(downloads_folder, exist_ok=True)
            os.makedirs(media_folder, exist_ok=True)
            file_name = "generated_qr_code.png"
            download_path = os.path.join(downloads_folder, file_name)
            media_path = os.path.join(media_folder, file_name)
            img.save(download_path)
            img.save(media_path)
            qr_code_url = os.path.join("qr", file_name)

        return render(request, self.template_name, {'form': form, 'qr_code_url': qr_code_url})


def index(request):
    return render(request, 'qr/index.html')
