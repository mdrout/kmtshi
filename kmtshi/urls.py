"""kmtshi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from kmtshi import views

urlpatterns = [url(r'^$', views.index, name='index'),
               url(r'^all-fields/candidates/$', views.candidates, name='candidates'),
               url(r'^(?P<field>[A-Z0-9-]+)/candidates/$', views.candidates_field, name='candidates_field'),
               url(r'^all-fields/transients/$', views.transients, name='transients'),
               url(r'^(?P<field>[A-Z0-9-]+)/transients/$', views.transients_field, name='transients_field'),
               url(r'^all-fields/variables/$', views.variables, name='variables'),
               url(r'^(?P<field>[A-Z0-9-]+)/variables/$', views.variables_field, name='variables_field'),
               url(r'^object/(?P<candidate_id>[0-9]+)/$', views.detail,name='detail'),
               url(r'^object/(?P<candidate_id>[0-9]+)/class_edit/$', views.classification_edit,name='classification_edit'),
               url(r'^admin/', admin.site.urls)]

