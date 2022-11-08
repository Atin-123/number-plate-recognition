from django import forms
from app.models import Anpr

class Anprform(forms.ModelForm):

    class Meta:
        model = Anpr
        fields = ['image']

    def __init__(self,*args, **kwargs):
        super().__init__(*args,*kwargs)
        self.fields['image'].widget.attrs.update({'class': 'form-control'})