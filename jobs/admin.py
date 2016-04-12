from django.contrib import admin

from jobs.models import Employer, Location, Job
from profiles.models import UserJob

admin.site.register(Employer)
admin.site.register(Job)
admin.site.register(Location)

