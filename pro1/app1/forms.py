from django import forms
from .models import Manangesystem


class ManageForm(forms.ModelForm):
    class Meta:
        model = Manangesystem
        fields = '__all__'


