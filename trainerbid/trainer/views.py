from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from trainer.forms import RegistrationForm, PersonProfileForm, ApplicationForm, FilterApplicationForm
from django.contrib import messages
from institute.models import Requirements
from trainer.models import Application
from django.contrib.auth.decorators import login_required
from django.forms import forms

# Create your views here.
from trainer.models import PersonProfile


def trainerRegistration(request):
    form = RegistrationForm()
    context = {}
    context["form"] = form
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            context["form"] = form
            return render(request, "trainer/registration.html", context)

    return render(request, "trainer/registration.html", context)


def trainerLogin(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        user = authenticate(request, username=uname, password=pwd)
        if user is not None:
            login(request, user)
            return redirect("trainerhome")
        else:
            messages.info(request, 'invalid credentials!')
            return render(request, "trainer/login.html")
    return render(request, "trainer/login.html")


@login_required(login_url='login')
def trainerHome(request):
    return render(request, 'trainer/trainerhome.html')





@login_required(login_url='login')
def trainerLogout(request):
    logout(request)
    return redirect("login")


@login_required(login_url='login')
def trainerProfile(request):
    context = {}
    user = User.objects.get(username=request.user)
    fname = user.first_name
    lname = user.last_name
    fullname = fname + " " + lname
    email = user.email
    form = PersonProfileForm(initial={'user': request.user, 'name': fullname, 'email': email})
    context["form"] = form
    if request.method == 'POST':
        form = PersonProfileForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("viewprofile")
        else:
            context["form"] = form
            return render(request, "trainer/createprofile.html", context)

    return render(request, "trainer/createprofile.html", context)


@login_required(login_url='login')
def viewProfile(request):
    profile = PersonProfile.objects.get(user=request.user)
    context = {}
    context["profile"] = profile
    return render(request, "trainer/viewprofile.html", context)


@login_required(login_url='login')
def updateProfile(request):
    profile = PersonProfile.objects.get(user=request.user)
    form = PersonProfileForm(instance=profile)
    context = {}
    context["form"] = form
    if request.method == 'POST':
        form = PersonProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewprofile")
        else:
            context["form"] = form
            return render(request, "trainer/updateprofile.html", context)
    return render(request, "trainer/updateprofile.html", context)


@login_required(login_url='login')
def matchingJobs(request):
    context = {}
    profile = PersonProfile.objects.get(user=request.user)

    skill = profile.skill
    requirements = Requirements.objects.filter(skill_needed=skill)
    context["requirements"] = requirements
    return render(request, "trainer/listjobs.html", context)


@login_required(login_url='login')
def applyJob(request, pk):
    context = {}
    profile = PersonProfile.objects.get(user=request.user)
    job = Requirements.objects.get(id=pk)
    form = ApplicationForm(
        initial={'jobid': job.jobid, 'job_title': job.job_title, 'location': job.location, 'user': request.user,
                 'name': profile.name,
                 'skill': profile.skill, 'years_of_experience': profile.years_of_experience,
                 'qualification': profile.qualification, 'cgpa': profile.cgpa, 'email': profile.email,
                 'phone': profile.phone})
    context["form"] = form
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()

            return render(request, "trainer/msgapplied.html")
        else:
            context["form"] = form
            return render(request, "trainer/applyjob.html", context)

    return render(request, "trainer/applyjob.html", context)


@login_required(login_url='login')
def viewApplications(request):
    context = {}
    form = FilterApplicationForm()
    context["form"] = form
    queryset = Application.objects.filter(user=request.user)
    count = queryset.count()
    context["count"] = count
    context["applications"] = queryset
    return render(request, "trainer/viewapplications.html", context)


@login_required(login_url='login')
def filterApplications(request):
    context = {}
    form = FilterApplicationForm()
    context["form"] = form
    if request.method == 'POST':
        form = FilterApplicationForm(request.POST)
        if form.is_valid():
            status = form.cleaned_data['status']
            queryset = Application.objects.filter(status=status, user=request.user)
            count = queryset.count()
            context["applications"] = queryset
            context["count"] = count
            return render(request, "trainer/viewapplications.html", context)
        else:
            context["form"] = form
            return render(request, "trainer/viewapplications.html", context)

    return render(request, "trainer/viewapplications.html", context)
