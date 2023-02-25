from django.shortcuts import render
from .models import Activity, ActivityTracker
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ActivitySerializer, ActivityTrackerSerializer, ActivityDataSerializer

#################################################
###  view for activity table
################################################# 
class ActivityViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Activity.objects.all()
    # The serializer class for serializing output
    serializer_class = ActivitySerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Could be [permissions.IsAuthenticated]
    
#################################################
###  view for activity tracker table
################################################# 
class ActivityTrackerViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = ActivityTracker.objects.all()
    # The serializer class for serializing output
    serializer_class = ActivityTrackerSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Could be [permissions.IsAuthenticated]
    
#################################################
###  view for activity table along with the 
###     activity_tracker data 
###  note:  the activity_tracker Data is read only
################################################# 
class ActivityDataViewset(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivityDataSerializer
    permission_classes = [permissions.AllowAny] #Could be [permissions.IsAuthenticated]
    