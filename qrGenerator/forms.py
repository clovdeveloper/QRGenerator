from django import forms


class QRCodeForm(forms.Form):
    url = forms.URLField(label="URL", max_length=200, required=True)
    box_size = forms.IntegerField(label="Box Size", min_value=1, initial=10, required=True)
    border_size = forms.IntegerField(label="Border Size", min_value=1, initial=4, required=True)

