from django.shortcuts import render
from .models import Institution, Education, Projects

# Create your views here.
def Home(request):
    education = Education.objects.filter()
    projects = Projects.objects.filter()
    context={
        'education':education,
        'projects':projects
    }
    return render(request, 'myprofile/index.html', context)