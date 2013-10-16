from django.http import HttpResponse
from django.template import loader, RequestContext
from main.models import Page

def home(request):
    page = Page.objects.get(alias='mainpage')
    t = loader.get_template('home.html')
    c = RequestContext(request,{'page': page})
    return HttpResponse(t.render(c))

def show(request,alias):
    
    page = Page.objects.get(alias=alias)
    t = loader.get_template('home.html')
    c = RequestContext(request,{'page': page})
    return HttpResponse(t.render(c))