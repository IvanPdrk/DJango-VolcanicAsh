# 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import requests
import urllib


# Models
from django.contrib.auth.models import User
#from Webforms.models import Profile

# Forms
from Webforms.forms import SignupForm

#AUTOMATION CODE
s = requests.Session()
s.auth = ('jjimeneze@ipn.mx', 'Alexandro04')

# Create your views here.
def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('Webforms:pluma')
        else:
            print("HOLA PPASOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
            return render(request, 'login.html', {'error': 'Invalid username and password'})

    return render(request, 'login.html')


def signup_view(request):
    """Sign up view."""
    #import pdb; pdb.set_trace()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Webforms:login')
    else:
        print("123456789")
        form = SignupForm()

    return render(
        request=request,
        template_name='signup.html',
        context={'form': form}  
    )

@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('Webforms:login') 
    
@login_required
def index(request):
    return render(request, 'feed.html')

def formulario(request):
    #missing line using model <<here>>
    #import pdb; pdb.set_trace()
    if request.method == 'POST':
        #form = PlumaForm(request.POST)
        #if form.is_valid():
        return redirect(request, 'Pluma/pluma_form2.html')
    else:
        
        r = s.get("https://www.ready.noaa.gov/hyreg-bin/dispsrc.pl?category=Volcanic_ash",auth=('jjimeneze@ipn.mx', 'Alexandro04'))
        return render(request, 'Pluma/pluma_form.html')

def formulario2(request):
    import pdb; pdb.set_trace()
    if request.method == 'POST':
        #r=s.post("https://www.ready.noaa.gov/hyreg-bin/disptype.pl",auth=('jjimeneze@ipn.mx', 'Alexandro04'))
        return render(request, 'Pluma/pluma_form2.html')
    else:
        return render(request, 'Pluma/pluma_form2.html')

def formulario3(request):
    #import pdb; pdb.set_trace()
    if request.method == 'POST':
        #print(request) 
        return render(request, 'Pluma/pluma_form3.html')
    else:
        return render(request, 'Pluma/pluma_form3.html')
