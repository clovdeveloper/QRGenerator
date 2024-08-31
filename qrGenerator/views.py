from django.shortcuts import render
from django.views import View
import os
import qrcode

from qrGenerator.forms import QRCodeForm


class QRCodeView(View):
    form_class = QRCodeForm
    template_name = 'qr/qr_code.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'qr_code': None})

    def post(self, request):
        form = self.form_class(request.POST)
        qr_code = None

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

            downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
            file_name = "generated_qr_code.png"
            file_path = os.path.join(downloads_folder, file_name)
            img.save(file_path)

            qr_code = file_name

        return render(request, self.template_name, {'form': form, 'qr_code': qr_code})


def index(request):
    return render(request, 'qr/index.html')
