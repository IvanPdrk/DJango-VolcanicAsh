"""Post URLs"""
from django.urls import path

from Webforms import views


urlpatterns = [
    #Managment
    path(
        route = 'index/',
        view = views.index,
        name="pluma"
    ),
    
    path(
        route = 'pluma/login/',
        view = views.login_view,
        name='login'
        ),

    path(
        route = 'pluma/logout/',
        view = views.logout_view,
        name='logout'
        ),

    path(
        route = 'pluma/signup/',
        view = views.signup_view,
        name = 'signup'
        ),
    
    path(
        route = 'form/',
        view = views.formulario,
        name="form"
        ),

    path(
        route = 'form2/',
        view = views.formulario2,
        name="form2"
        ),
    
    path(
        route = 'form3/',
        view = views.formulario3,
        name="form3"
        )
]