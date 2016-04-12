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
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from dashboard.views import newsletter_home
from likes.views import like_user
from matchmaker.views import about
from newsletter.views import newsletter_contact
from profiles.views import jobs_add, jobs_edit, profile_user, profile_view, profile_edit
from questions.views import question_single, question_home

urlpatterns = [
	url(r'^admin/', admin.site.urls),

	url(r'^$', newsletter_home, name='home'),
	url(r'^contact/$', newsletter_contact, name='contact'),
	url(r'^question/(?P<id>\d+)$', question_single, name='question_single'),
	url(r'^question/$', question_home, name='question_home'),
	url(r'^about/$', about, name='about'),
	url(r'^like/(?P<id>\d+)$', like_user, name='like_user'),
	url(r'^profile/$', profile_user, name='profile_user'),
	url(r'^profile/edit/$', profile_edit, name='profile_edit'),
	url(r'^profile/jobs/add/$', jobs_add, name='jobs_add'),
	url(r'^profile/jobs/edit/$', jobs_edit, name='jobs_edit'),
	url(r'^profile/(?P<username>[\w.@+-]+)/$', profile_view, name='profile'),

	url(r'^accounts/', include('registration.backends.default.urls')),
	url(r'^matches/', include('matches.urls')),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
