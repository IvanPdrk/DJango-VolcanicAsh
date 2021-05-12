from django.shortcuts import render
# Models

# Forms
from pluma.form import PlumaForm

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
        form = PlumaForm()
    return render(request, 'pluma_form.html')
