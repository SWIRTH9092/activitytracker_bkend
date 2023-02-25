"""activityproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework import routers
from activityapp.views import ActivityTrackerViewSet, ActivityViewSet, ActivityDataViewset

# Create a Router
router = routers.DefaultRouter()
# Register viewset with the router

##  router to get the activity_tracker table data only
router.register(r'activitytracker', ActivityTrackerViewSet,basename="activitytracker")

## router to get the activity table data only
router.register(r'activity', ActivityViewSet, basename="activity")

## router to get the activity data along with the associated activity_tracker data
router.register(r'activitydata', ActivityDataViewset, basename="activitydata")

urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
]