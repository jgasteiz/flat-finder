from django.conf import settings
from django.shortcuts import render
from django.views.generic import FormView

import requests

from core.forms import SearchForm

ZOOPLA_API_URL = 'http://api.zoopla.co.uk/api/v1/'
ZOOPLA_LISTINGS = 'property_listings.json'


class Home(FormView):
    form_class = SearchForm
    template_name = 'home.html'

    def form_valid(self, form):
        payload = dict(
            api_key=settings.ZOOPLA_API_KEY,
            area=form.cleaned_data.get('area'),
            listing_status=form.cleaned_data.get('listing_status')
        )
        listings_url = '{0}{1}'.format(ZOOPLA_API_URL, ZOOPLA_LISTINGS)

        response = requests.get(listings_url, params=payload)

        return render(self.request, self.template_name, dict(
            form=form,
            results=response.json()
        ))

home = Home.as_view()