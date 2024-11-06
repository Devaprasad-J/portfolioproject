from django.contrib import admin
from .models import Profile, Project, Experience, Education, Certification

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Certification)

