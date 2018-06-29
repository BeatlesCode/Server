from django import forms
from .models import UploadModel

# class UploadFileForm(forms.Form):
#     fileName = forms.CharField(label='fileName');
#     uploadfile = forms.FileField(label='uploadfile')

class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadModel
        fields = "__all__"