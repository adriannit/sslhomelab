from django.http import HttpResponse
from django.template import loader
from lab.dnsmasq import Dnsmasq


def index(request):
    template = loader.get_template("lab/index.html")
    return HttpResponse(template.render({'nbar': 'Home'}))


def proxyhosts(request):
    template = loader.get_template("lab/index.html")
    return HttpResponse(template.render({'nbar': 'Proxy Hosts'}))


def dns(request):
    dns = Dnsmasq("/etc/dnsmasq.conf")
    A_values = dns.print_dnsA()
    CNAME_values = dns.print_dnsCNAME()
    template = loader.get_template("lab/index.html")
    return HttpResponse(template.render({'nbar': 'DNS Server', 'A_values': A_values, 'CNAME_values': CNAME_values}))


def dhcp(request):
    template = loader.get_template("lab/index.html")
    return HttpResponse(template.render({'nbar': 'DHCP Server'}))


def ssl(request):
    template = loader.get_template("lab/index.html")
    return HttpResponse(template.render({'nbar': 'SSL Certificates'}))


def logs(request):
    template = loader.get_template("lab/index.html")
    return HttpResponse(template.render({'nbar': 'Logs'}))
