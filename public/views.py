import json
from core.models import Search
from django.conf import settings
from django.shortcuts import render
from django.views.generic import FormView

import requests

from core.forms import SearchForm

ZOOPLA_API_URL = 'http://api.zoopla.co.uk/api/v1/'
ZOOPLA_LISTINGS = 'property_listings.json'
PAGE_SIZE = 100


class Home(FormView):
    form_class = SearchForm
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super(Home, self).get_context_data(**kwargs)
        ctx.update(dict(
            saved_searches=Search.objects.all()
        ))
        return ctx

    def form_valid(self, form):

        monthly_rent = form.cleaned_data.get('maximum_price', None)
        weekly_rent = None
        if monthly_rent:
            weekly_rent = monthly_rent / (365 / 7 / 12)

        payload = dict(
            api_key=settings.ZOOPLA_API_KEY,
            page_size=PAGE_SIZE,
            area=form.cleaned_data.get('area'),
            listing_status=form.cleaned_data.get('listing_status'),
            order_by=form.cleaned_data.get('order_by'),
            ordering=form.cleaned_data.get('ordering'),
            maximum_price=weekly_rent,
        )
        listings_url = '{0}{1}'.format(ZOOPLA_API_URL, ZOOPLA_LISTINGS)

        if form.cleaned_data.get('save_search'):
            form.save()

        response = requests.get(listings_url, params=payload)

        ctx = self.get_context_data()
        ctx.update(dict(
            # results=response.json(),
            results_json=json.dumps(response.json()),
            form=form
        ))
        return render(self.request, self.template_name, ctx)

home = Home.as_view()
