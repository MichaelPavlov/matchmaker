"""matchmaker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from matches.views import position_match_view, employer_match_view, location_match_view
from profiles.views import profile_view, jobs_add, jobs_edit

urlpatterns = [
	url(r'^poition/(?P<slug>[\w-]+)/$', position_match_view, name='position_match_view_url'),
	url(r'^employer/(?P<slug>[\w-]+)/$', employer_match_view, name='employer_match_view_url'),
	url(r'^poition/(?P<slug>[\w-]+)/$', location_match_view, name='location_match_view_url'),

]
