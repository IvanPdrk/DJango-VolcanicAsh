#Django 
from django import forms
#automation process libraries
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from requests_html import HTMLSession


url = "https://www.ready.noaa.gov/hyreg-bin/dispsrc.pl?category=Volcanic_ash"

#AUTOMATION CODE


class PlumaForm(forms.Form):
    """Pluma form"""
    DecDeg = forms.BooleanField()
    DMS = forms.BooleanField()

    DecDegLat = forms.DecimalField(required=True)
    DecDegLon = forms.DecimalField(required=True)
    
    latNS = forms.BooleanField(required=True)
    lonEW = forms.BooleanField(required=True)

    latdNS = forms.BooleanField(required=True)
    londEW = forms.BooleanField(required=True)

    latd = forms.CharField(required=True)
    latm = forms.CharField(required=True)

    lats = forms.CharField(required=True)
    lond = forms.CharField(required=True)

    lonm = forms.CharField(required=True)
    lons = forms.CharField(required=True)


    location = forms.CharField(required=True)
