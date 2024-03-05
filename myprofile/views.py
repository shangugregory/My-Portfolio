from django.shortcuts import render
from .models import Institution, Education, Projects, AboutMe, Skills, UpcommingProjects

# Create your views here.
def Home(request):
    education = Education.objects.filter()
    projects = Projects.objects.filter()
    skills = Skills.objects.filter()
    upcomingprojects=UpcommingProjects.objects.filter()
    newprojects = Projects.objects.get(project_name="Arlio Enterprice")
    aboutme = AboutMe.objects.get()
    context={
        'education':education,
        'projects':projects,
        'newprojects':newprojects,
        'aboutme':aboutme,
        'skills':skills,
        'upcomingprojects':upcomingprojects
    }
    return render(request, 'myprofile/index.html', context)