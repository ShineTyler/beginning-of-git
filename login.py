from django.hTTP import HttpResponse
from django.shortcuts import redirect

def index(request):
	return httpResponse('index')
def login(request):
    return redirect('/index')
