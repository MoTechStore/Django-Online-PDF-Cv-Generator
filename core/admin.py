from django.contrib import admin
from .models import Referee, User,Skill,Experience,Academic,Certification,Strength,Weakness,Language,Hobby,Publication,Cv,Profile


models_list = [User,Skill,Experience,Academic,Certification,Referee,Strength,Weakness,Language,Hobby,Publication,Cv,Profile] 
admin.site.register(models_list)

