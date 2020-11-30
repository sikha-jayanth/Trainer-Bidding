"""clinic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.shortcuts import render
from institute.views import *

urlpatterns = [
    path("register",instituteRegistration,name="register"),
    path("login",instituteLogin,name="institutelogin"),
    path("istitutelogout",instituteLogout,name="institutelogout"),
    path("institutehome", instituteHome, name="institutehome"),
    path("createskill", createSkill, name="createskill"),
    path("updateskill<int:pk>", updateSkill, name="updateskill"),
    path("deleteskill<int:pk>", deleteSkill, name="deleteskill"),
    path("createrequirement", createRequirement, name="createrequirement"),
    path("viewRequirements", viewRequirements, name="viewrequirements"),
    path("updaterequirements<int:pk>", updateRequirements, name="updaterequirements"),
    path("deleterequirement<int:pk>", deleteRequirement, name="deleterequirement"),
    path("filterrequirements",filterRequirements,name="filterrequirements"),
    path("viewallapplications",viewApplications,name="viewallapplications"),
    path("applicationdetails<int:pk>",applicationDetails,name="applicationdetails"),
    path("deleteApplication<int:pk>",deleteApplication,name="deleteapplication"),
    path("searchbyid",searchById,name="searchbyid")


]
