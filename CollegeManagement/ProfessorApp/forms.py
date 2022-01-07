from django import forms
from .models import Prof

class ProfModelForm(forms.ModelForm):
    class Meta:
        model = Prof
        fields = "__all__"
