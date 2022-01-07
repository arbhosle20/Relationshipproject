from django import forms
from .models import Dept

class DeptModelForm(forms.ModelForm):
    class Meta:
        model = Dept
        fields = "__all__"
