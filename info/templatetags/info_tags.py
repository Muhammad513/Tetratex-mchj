from datetime import date
from info.views import tabel
from django import template
from info.models import*


register=template.Library()

#@register.simple_tag()
#def get_menu():
 #   return Menu.objects.all()

@register.inclusion_tag('nav.html')
def show_menu():
    submenu=Submenu.objects.all()
    return {'submenu':submenu}

@register.inclusion_tag('sidebar.html')
def show_sidebar():
    sidebar=Sidebar.objects.all()
    return {'sidebar':sidebar}

@register.simple_tag(name='filtertable')
def show_menu(filter=None):
    if not filter:    
        tabel=Tabel.objects.all()
    else:
        tabel=Tabel.objects.filter(date=filter)    
    return {'tabel':tabel}    