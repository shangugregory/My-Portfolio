from django.contrib import admin
from . models import Institution, Education, Projects, UpcommingProjects, Work,AboutMe, Skills
# Register your models here.
admin.site.register(Institution)
admin.site.register(Education)
admin.site.register(Projects)
admin.site.register(UpcommingProjects)
admin.site.register(Work)
admin.site.register(AboutMe)
admin.site.register(Skills)