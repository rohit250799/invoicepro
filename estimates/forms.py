from django import forms
from estimates.models import Estimates

class EstimateForm(forms.ModelForm):
    class Meta:
        model = Estimates
        fields = '__all__'