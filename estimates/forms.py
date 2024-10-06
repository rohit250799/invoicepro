from django import forms
from estimates.models import Estimates, EstimateItems
from items.models import Item

class EstimateForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Estimates
        fields = '__all__'