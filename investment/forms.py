from django import forms
from .models import Company, StockPortfolio
from django.shortcuts import render, redirect


class CheckboxSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)
    options = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)

    def clean_search(self):
        search = self.cleaned_data["search"]
        # Perform validation on the search input
        # if len(search) < 3:
        #     raise forms.ValidationError('Search input must be at least 3 characters long.')
        return search
