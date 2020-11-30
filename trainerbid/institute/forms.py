from django import forms
from django.forms import ModelForm
from institute.models import Skills
from django.contrib.auth.forms import UserCreationForm
from institute.models import Requirements
from django.contrib.auth.models import User
from trainer.models import Application


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


class AddSkillForm(ModelForm):
    class Meta:
        model = Skills
        fields = "__all__"
        widgets = {
            "skill": forms.TextInput(attrs={'class': "form-control"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        skill = cleaned_data.get("skill")
        skill_name = Skills.objects.filter(skill=skill)
        if (skill_name):
            msg = "Skill already exists"
            self.add_error('skill', msg)


class AddRequirementForm(ModelForm):
    class Meta:
        model = Requirements
        fields = "__all__"
        widgets = {
            "skill_needed": forms.Select(attrs={'class': "form-control"}),

        }

    def clean(self):
        cleaned_data = super().clean()

        rate = cleaned_data.get('rate_per_hour')
        yop = cleaned_data.get('years_of_experience')
        skill = cleaned_data.get('skill_needed')
        vacancy = cleaned_data.get('vacancies')

        job = Requirements.objects.filter(years_of_experience=yop, skill_needed=skill)

        if rate < 500:
            msg = "Enter rate greater than 500"
            self.add_error('rate_per_hour', msg)
        if job:
            msg = "Already created requirement for this job"
            self.add_error('years_of_experience', msg)
            self.add_error('skill_needed', msg)
        if yop < 0 or yop > 25:
            msg = "Enter a valid value for experience"
            self.add_error('years_of_experience', msg)
        if vacancy <= 0:
            msg = "Enter a valid value for vacancies"
            self.add_error('vacancy', msg)


class EditRequirementsForm(ModelForm):
    class Meta:
        model = Requirements
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        rate = cleaned_data.get('rate_per_hour')
        if rate < 500:
            msg = "Enter rate greater than 500"
            self.add_error('rate_per_hour', msg)


class FilterForm(ModelForm):
    class Meta:
        model = Requirements
        fields = ['skill_needed']
        widgets = {
            "skill_needed": forms.Select(attrs={'class': 'select'}),
        }


class ApplicationProcessingForm(ModelForm):
    class Meta:
        model = Application
        fields = "__all__"
        widgets = {

        "jobid":forms.HiddenInput(attrs={'class': "form-control"}),
        "job_title":forms.HiddenInput(attrs={'class': "form-control"}),
        "user":forms.HiddenInput(attrs={'class': "form-control"}),
        "skill":forms.HiddenInput(attrs={'class': "form-control"}),
        "location":forms.HiddenInput(attrs={'class': "form-control"}),
        "name": forms.TextInput(attrs={'class': "form-control", 'readonly': True}),
        "years_of_experience": forms.TextInput(attrs={'class': "form-control", 'readonly': True}),
        "qualification": forms.TextInput(attrs={'class': "form-control", 'readonly': True}),
        "cgpa": forms.TextInput(attrs={'class': "form-control", 'readonly': True}),
        "email": forms.TextInput(attrs={'class': "form-control", 'readonly': True}),
        "phone": forms.TextInput(attrs={'class': "form-control", 'readonly': True}),
        "status": forms.Select()

        }

class SearchByIDForm(ModelForm):
    class Meta:
        model=Application
        fields=["jobid"]

