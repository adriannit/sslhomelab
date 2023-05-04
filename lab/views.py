from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("lab/index.html")
    return HttpResponse(template.render({'nbar': 'Home'}))

def proxyhosts(request):
    template = loader.get_template("lab/index.html")
    return HttpResponse(template.render({'nbar': 'Proxy Hosts'}))

def dns(request):
    template = loader.get_template("lab/index.html")
    return HttpResponse(template.render({'nbar': 'DNS Server'}))

def dhcp(request):
    template = loader.get_template("lab/index.html")
    return HttpResponse(template.render({'nbar': 'DHCP Server'}))

def ssl(request):
    template = loader.get_template("lab/index.html")
    return HttpResponse(template.render({'nbar': 'SSL Certificates'}))

def logs(request):
    template = loader.get_template("lab/index.html")
    return HttpResponse(template.render({'nbar': 'Logs'}))