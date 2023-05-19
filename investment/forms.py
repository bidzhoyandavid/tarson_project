from django import forms
from .models import Company


class Portfolio(forms.Form):
    symbols = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=[])
    search_query = forms.CharField(required=False)

    def __init__(self):
        super(Portfolio, self).__init__()
        self.fields["symbols"].choices = self.get_choices()

    def get_choices(self):
        choices = Company.objects.values_list("symbol", "name")

        search_query = self.cleaned_data["symbol"]
        if search_query:
            choices = choices.filter(symbol__startswith=search_query)

        return choices
