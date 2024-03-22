from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList

class UploadFileForm(forms.Form):
    url=forms.CharField(max_length=900)
    file=forms.FileField()
    def __init__(self, *args,**kwargs):
        super(UploadFileForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
            self.fields[field].widget.attrs['id']='fields'