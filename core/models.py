from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class User(AbstractUser):
    is_author = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)



class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    s_name = models.CharField(max_length=255)
    s_level = models.CharField(max_length=255, default='')


    def __str__(self):
        return self.s_name


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    e_office = models.CharField(max_length=255)
    e_position = models.CharField(max_length=255)
    e_year = models.CharField(max_length=255)


    def __str__(self):
        return self.e_office




class Academic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    a_name = models.CharField(max_length=255)
    a_year = models.CharField(max_length=255)
    a_award = models.CharField(max_length=255)


    def __str__(self):
        return self.a_name



class Certification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    c_name = models.CharField(max_length=255)
    c_org = models.CharField(max_length=255)


    def __str__(self):
        return self.c_name




class Referee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    r_names = models.CharField(max_length=255)
    r_office = models.CharField(max_length=255)
    r_phone = models.CharField(max_length=255)
    r_email = models.CharField(max_length=255)


    def __str__(self):
        return self.r_names





class Publication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    p_name = models.CharField(max_length=255)


    def __str__(self):
        return self.p_name




class Hobby(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    h_name = models.CharField(max_length=255)

    def __str__(self):
        return self.h_name




class Language(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    l_name = models.CharField(max_length=255)

    def __str__(self):
        return self.l_name



class Strength(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ss_name = models.CharField(max_length=255)

    def __str__(self):
        return self.ss_name



class Weakness(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    w_name = models.CharField(max_length=255)

    def __str__(self):
        return self.w_name



class Cv(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to = '', default = 'profile/avator.png', blank=True)
    fname = models.CharField(max_length=255)
    mname = models.CharField(max_length=255, null=True)
    lname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, default='0000000000')
    bio = models.TextField()
    gender = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(default='None')
    street = models.CharField(max_length=255, default='')
    region = models.CharField(max_length=255, default='')
    country = models.CharField(max_length=255, default='Tanzania')


    def __str__(self):
        return self.fname

