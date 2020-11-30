from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from institute.forms import AddSkillForm,AddRequirementForm,EditRequirementsForm,FilterForm,RegistrationForm,ApplicationProcessingForm,SearchByIDForm
from institute.models import Skills,Requirements
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from trainer.models import Application



def instituteRegistration(request):
    form=RegistrationForm()
    context={}
    context["form"]=form
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("institutelogin")
        else:
            context["form"]=form
            return render(request, "institute/registration.html", context)

    return render(request,"institute/registration.html",context)


def instituteLogin(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        user = authenticate(request, username=uname, password=pwd)
        if user is not None:
            login(request, user)
            return redirect("institutehome")
        else:
            messages.info(request, 'invalid credentials!')
            return render(request, "institute/login.html")


    return render(request, "institute/login.html")


@login_required(login_url='institutelogin')
def instituteLogout(request):
    logout(request)
    return redirect("institutelogin")

@login_required(login_url='institutelogin')
def instituteHome(request):
    context={}
    jobs=Requirements.objects.all().count()
    applications=Application.objects.all().count()
    context["jobs"]=jobs
    context["applications"] = applications

    return render(request,"institute/institutehome.html",context)


@login_required(login_url='institutelogin')
def createSkill(request):
    form=AddSkillForm()
    context={}
    context["form"]=form
    queryset = Skills.objects.all()
    context["skills"] = queryset
    if request.method=='POST':
        form=AddSkillForm(request.POST)
        if form.is_valid():
            form.save()

            return render(request, "institute/createskills.html", context)
        else:
            context["form"]=form
            return render(request, "institute/createskills.html", context)


    return render(request, "institute/createskills.html", context)


@login_required(login_url='institutelogin')
def deleteSkill(request,pk):

    Skills.objects.get(id=pk).delete()
    return redirect("createskill")

@login_required(login_url='institutelogin')
def updateSkill(request,pk):
    skill=Skills.objects.get(id=pk)
    form=AddSkillForm(instance=skill)
    context={}
    context["form"]=form
    if request.method=='POST':
        form=AddSkillForm(instance=skill,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("createskill")
    return render(request,"institute/updateskills.html",context)

@login_required(login_url='institutelogin')
def createRequirement(request):


    form=AddRequirementForm()
    context={}
    context["form"]=form

    if request.method=='POST':
        form=AddRequirementForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("viewrequirements")
        else:
            context["form"]=form
            return render(request, "institute/createrequirement.html", context)


    return render(request, "institute/createrequirement.html", context)


@login_required(login_url='institutelogin')
def viewRequirements(request):

    context = {}
    form = FilterForm()
    context["form"] = form
    count = Requirements.objects.all().count()
    context["count"] = count

    queryset = Requirements.objects.all()
    context["requirements"] = queryset
    return render(request, "institute/viewrequirements.html", context)

@login_required(login_url='institutelogin')
def updateRequirements(request,pk):
    requirement = Requirements.objects.get(id=pk)
    form = EditRequirementsForm(instance=requirement)
    context = {}
    context["form"] = form
    if request.method == 'POST':
        form = EditRequirementsForm(instance=requirement, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewrequirements")
        else:
            context["form"] = form
            return render(request, "institute/updaterequirement.html", context)
    return render(request, "institute/updaterequirement.html", context)


@login_required(login_url='institutelogin')
def deleteRequirement(request,pk):

    Requirements.objects.get(id=pk).delete()
    return redirect("viewrequirements")






@login_required(login_url='institutelogin')
def filterRequirements(request):
    context = {}
    form = FilterForm()
    context["form"] = form
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            skill = form.cleaned_data['skill_needed']
            queryset = Requirements.objects.filter(skill_needed=skill)
            count = Requirements.objects.filter(skill_needed=skill).count()
            context["requirements"] = queryset
            context["count"] = count
            return render(request, "institute/viewrequirements.html", context)
        else:
            context["form"]=form
            return render(request, "institute/viewrequirements.html", context)

    return render(request, "institute/viewrequirements.html", context)


@login_required(login_url='institutelogin')
def viewApplications(request):
    context={}
    form=SearchByIDForm()
    context["form"]=form


    queryset=Application.objects.all()
    count=queryset.count()
    context["count"]=count
    context["applications"]=queryset
    return render(request,"institute/viewallapplications.html",context)

@login_required(login_url='institutelogin')
def applicationDetails(request,pk):
    applicant = Application.objects.get(id=pk)
    form = ApplicationProcessingForm(instance=applicant)
    context = {}
    context["form"] = form
    if request.method == 'POST':
        form = ApplicationProcessingForm(instance=applicant, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewallapplications")
        else:
            context["form"] = form
            return render(request, "institute/applicantdetails.html", context)
    return render(request, "institute/applicantdetails.html", context)


@login_required(login_url='institutelogin')
def deleteApplication(request,pk):
    Application.objects.get(id=pk).delete()
    return redirect("viewallapplications")


@login_required(login_url='institutelogin')
def searchById(request):
    context = {}
    form = SearchByIDForm()
    context["form"] = form
    if request.method == 'POST':
        form = SearchByIDForm(request.POST)
        if form.is_valid():
            jobid = form.cleaned_data['jobid']
            queryset = Application.objects.filter(jobid=jobid)
            count = Application.objects.filter(jobid=jobid).count()
            context["applications"] = queryset
            context["count"] = count
            return render(request, "institute/viewallapplications.html", context)
        else:
            context["form"] = form
            return render(request, "institute/viewallapplications.html", context)

    return render(request, "institute/viewallapplications.html", context)


