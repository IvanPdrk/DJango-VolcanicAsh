from django.shortcuts import render, redirect
import requests
# Models

# Forms
from Webforms.forms import PlumaForm

#AUTOMATION CODE



payload = {
    "metdata":"GFS",
    "SOURCELOC":"decdegree",
    "Lat":"19.02",
    "Latns":"N",
    "Lon":"98.62",
    "Lonew":"W",
    "Latd":"",
    "Latm":"",
    "Lats":"",
    "Latdns":"N",
    "Lond":"",
    "Lonm":"",
    "Lons":"",
    "Londew":"E",
    "VOLCNAME":""
}
#r = s.get("https://www.ready.noaa.gov/hyreg-bin/dispsrc.pl?category=Volcanic_ash")
#r1 = s.post("https://www.ready.noaa.gov/hyreg-bin/disptype.pl", data=payload, cookies=r.cookies, timeout=10)   
#print(r1.text)

# Create your views here.
def index(request):
    return render(request, 'feed.html')

def formulario(request):
    #missing line using model <<here>>

    if request.method == 'POST':
        form = PlumaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        s = requests.Session()
        s.auth = ('jjimeneze@ipn.mx', 'Alexandro04')
        r = s.get("https://www.ready.noaa.gov/hyreg-bin/dispsrc.pl?category=Volcanic_ash")
        form = PlumaForm()
    return render(request, 'Pluma/pluma_form.html')
