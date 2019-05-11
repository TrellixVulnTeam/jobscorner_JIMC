from builtins import super

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms
from pagedown.widgets import PagedownWidget

from .models import Location


class LocationForm(forms.ModelForm):
    name = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Location Name'}))
    description = forms.CharField(label='', required=False, max_length=1024,
                                  widget=PagedownWidget(attrs={'placeholder': 'Description'}))

    class Meta:
        model = Location
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='mt-10 form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'description',
            Submit('submit', 'Submit'),
        )
