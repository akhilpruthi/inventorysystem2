from django import forms
from .models import *

class userDataform(forms.ModelForm):
    class Meta:
        model = userdata
        fields = "__all__"