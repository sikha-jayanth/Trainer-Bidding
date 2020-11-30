from django import forms
from django.forms import ModelForm
from institute.models import Skills
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from trainer.models import PersonProfile,Application
import re





class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password1", "password2"]
        wiggets = {
            "first_name": forms.TextInput(attrs={'class': "form-control"}),
            "last_name": forms.TextInput(attrs={'class': "form-control"}),
            "email": forms.EmailInput(attrs={'class': "form-control"}),
            "username": forms.TextInput(attrs={'class': "form-control"}),
            "password1": forms.PasswordInput(attrs={'class': "form-control"}),
            "password2": forms.PasswordInput(attrs={'class': "form-control"}),
        }






class PersonProfileForm(ModelForm):
    class Meta:
        model=PersonProfile
        fields="__all__"
        widgets={
            "user":forms.HiddenInput(attrs={'class':"form-control"}),
            "skill":forms.Select(attrs={'class':"form-control"}),
            "email":forms.EmailInput(attrs={'class':"form-control"}),
            "cgpa":forms.NumberInput(attrs={'class':"form-control"}),
            "address":forms.Textarea(attrs={'class':"form-control"}),

        }
    def clean(self):
        cleaned_data = super().clean()
        yop = cleaned_data.get('years_of_experience')
        cgpa = cleaned_data.get('cgpa')
        phno = cleaned_data.get('phone')
        pattern = '(0/91)?[7-9][0-9]{9}'
        matcher = re.fullmatch(pattern, phno)
        if yop < 0 or yop > 25:
            msg = "enter a valid value for experience"
            self.add_error('years_of_experience', msg)
        if cgpa < 0 or cgpa > 10:
            msg = "enter a valid value for cgpa"
            self.add_error('cgpa', msg)
        if matcher is None:
            msg = "enter a valid phone number"
            self.add_error('phone', msg)


class ApplicationForm(ModelForm):
    class Meta:
        model=Application
        fields="__all__"
        widgets={
            "jobid": forms.HiddenInput(attrs={'class': "form-control"}),
            "job_title": forms.TextInput(attrs={'class': "form-control",'readonly':True}),
            "location": forms.TextInput(attrs={'class': "form-control", 'readonly': True}),
            "skill": forms.TextInput(attrs={'class': "form-control", 'readonly': True}),
            "user":forms.HiddenInput(attrs={'class':"form-control"}),
            "name":forms.TextInput(attrs={'class':"form-control"}),

            "email":forms.EmailInput(attrs={'class':"form-control"}),
            "cgpa":forms.NumberInput(attrs={'class':"form-control"}),
            "status": forms.HiddenInput(),


        }
    def clean(self):
        cleaned_data = super().clean()
        yop = cleaned_data.get('years_of_experience')
        cgpa = cleaned_data.get('cgpa')
        phno = cleaned_data.get('phone')
        pattern = '(0/91)?[7-9][0-9]{9}'
        jobid=cleaned_data.get('jobid')
        user=cleaned_data.get('user')
        application=Application.objects.filter(jobid=jobid,user=user)

        matcher = re.fullmatch(pattern, phno)




        if yop < 0 or yop > 25:
            msg = "enter a valid value for experience"
            self.add_error('years_of_experience', msg)
        if application:
            msg = "ALREADY APPLIED FOR THIS JOB"
            self.add_error('job_title', msg)

        if cgpa < 0 or cgpa > 10:
            msg = "enter a valid value for cgpa"
            self.add_error('cgpa', msg)
        if matcher is None:
            msg = "enter a valid phone number"
            self.add_error('phone', msg)


class FilterApplicationForm(ModelForm):
    class Meta:
        model=Application
        fields=['status']
        widgets={
            "status":forms.Select(attrs={'class':'select'}),
        }


