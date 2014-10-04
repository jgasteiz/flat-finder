from core.models import Search
from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Div, Layout
from django.forms import ModelForm


class SearchForm(ModelForm):
    class Meta:
        fields = ('area', 'postcode', 'country',
                  'radius', 'latitude', 'longitude', 'order_by', 'ordering',
                  'listing_status', 'minimum_price', 'maximum_price',
                  'minimum_beds', 'maximum_beds', 'furnished',)
        model = Search

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        helper = FormHelper()
        helper.form_class = 'form'
        helper.attrs['name'] = 'form'
        helper.attrs['novalidate'] = ''
        self.helper = helper
        self.helper.layout = Layout(
            Div(
                'area',
                'postcode',
                'country',
                'radius',
                'latitude',
                'longitude',
                'order_by',
                'ordering',
                'listing_status',
                'minimum_price',
                'maximum_price',
                'minimum_beds',
                'maximum_beds',
                'furnished',
            ),
            FormActions(
                Submit('Search', 'Search'),
            )
        )
