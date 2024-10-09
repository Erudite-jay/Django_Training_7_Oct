from django import forms
from .models import FileUpload

# class FileUploadFormClass(forms.Form):
#     name = forms.CharField(max_length=100)
#     file = forms.FileField()


class FileUploadFormClass(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['name', 'file']