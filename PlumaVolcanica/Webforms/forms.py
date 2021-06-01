#Django 
from django import forms

#automation process libraries
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from requests_html import HTMLSession
 
url = "https://www.ready.noaa.gov/hyreg-bin/dispsrc.pl?category=Volcanic_ash"

#forms
class PlumaForm(forms.Form):
    """Pluma form"""

    metdata="HRRR"
    SOURCELOC="decdegree"
    Lat=forms.DecimalField(required=True)
    Latns=forms.BooleanField(required=True)
    Lon=forms.DecimalField(required=True)
    Lonew=forms.BooleanField(required=True)

    Latd=forms.DecimalField(disabled=True)
    Latm=forms.DecimalField(disabled=True)
    Lats=forms.DecimalField(disabled=True)
    Latdns=forms.BooleanField(required=True)
    Lond=forms.DecimalField(disabled=True)
    Lonm=forms.DecimalField(disabled=True)
    Lons=forms.DecimalField(disabled=True)

    Londew=forms.BooleanField(required=False, disabled=True)
    VOLCNAME=forms.CharField(required=False, disabled=True)


