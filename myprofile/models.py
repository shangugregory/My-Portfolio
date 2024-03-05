from django.db import models

# Create your models here.
class Institution(models.Model):
    institution_name = models.CharField(max_length = 300)

    def __str__(self):
        return self.institution_name
class Education(models.Model):
    institution = models.ForeignKey(Institution, on_delete = models.CASCADE)
    study_level = models.CharField(max_length = 130)
    qualification = models.CharField(max_length = 130)
    start_date = models.CharField(max_length = 130, null = True)
    end_date = models.CharField(max_length = 130, null = True)
    
    def __str__(self):
        return self.study_level

class Projects(models.Model):
    project_name = models.CharField(max_length = 130)
    project_image = models.ImageField(max_length = 130)
    project_description = models.TextField(max_length = 1500)
    github_link = models.CharField(max_length = 230)

    def __str__(self):
        return self.project_name
    
class UpcommingProjects(models.Model):
    project_name = models.CharField(max_length = 130)
    project_image = models.ImageField(null=True, blank = True)
    project_description = models.TextField(max_length = 500)
    github_link = models.CharField(max_length = 230)

    def __str__(self):
        return self.project_name
    

class Work(models.Model):
    company_name = models.CharField(max_length = 130)
    Job_title = models.CharField(max_length = 130)
    work_description = models.TextField(max_length = 500)
    
    def __str__(self):
        return self.company_name


class AboutMe(models.Model):
    paragraph1 = models.TextField(max_length = 1030)
    paragraph2 = models.TextField(max_length = 1030)
    paragraph3 = models.TextField(max_length = 1030)
    
class Skills(models.Model):
    programing_language = models.CharField(max_length = 1030)
    learning_progress = models.IntegerField()
    
    