from django import forms
from app_crud_cvb import models as mo

class FO_candidates(forms.ModelForm):
    class Meta:
        model = mo.MO_candidates
        fields = "__all__"