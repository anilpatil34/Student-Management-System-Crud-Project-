"""
URL configuration for studentproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from studentapp import views
# from studentapp.views1 import *  


urlpatterns = [
    # path("admin/", admin.site.urls),
    # path("home/", StudentHomeView.as_view(), name='index'),  # Class-based view
    # path("display-all/", StudentDisplayAllView.as_view(), name='display_all'),  # Class-based view
    # path("insert-student/", StudentInsertView.as_view(), name='insert_student'),  # Class-based view
    # path("update-student/<int:roll>/", StudentUpdateView.as_view(), name='update_student'),  # Class-based view
    path("student/", include("studentapp.urls")),
]
