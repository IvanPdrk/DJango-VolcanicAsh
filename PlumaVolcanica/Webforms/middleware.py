"""Middleware"""
from django.shortcuts import render, redirect
import requests
import urllib


s = requests.Session()
s.auth = ('jjimeneze@ipn.mx', 'Alexandro04')


class Middleware:
    def __init__(self,get_response):
        self.response = get_response
        
        
    def __call__(self,request):
        """Code excetuded to each request before the view is called"""
        #import pdb; pdb.set_trace()
        self.response(request)
        return self.response(request)
        pass