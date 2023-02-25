from .models import Activity, ActivityTracker
###### from django.contrib.auth.models import User, Group
from rest_framework import serializers

#######################################################
### serializer to process only the Activity Table
#######################################################

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Activity
        # the fields that should be included in the serialized output
        fields = ['activity_id', 'name', 'category', 'description']


#######################################################
### serializer to process only the Activity Tracker Table
#######################################################
        
class ActivityTrackerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = ActivityTracker
        # the fields that should be included in the serialized output
        fields = ['tracker_id', 'act_main', 'activity_date', 'activity_count']
     
     
class ActivityDataSerializer(serializers.HyperlinkedModelSerializer):
    #######################################################
    ###  the "activitydata" field name below comes from the model 
    ###    definition for ActivityTracker.  In the act_main
    ###    field that defines the foreign key to the parent table:
    ###    activity, the related_name='activitydata'.  this is what
    ###    needs to be coded here...
    #######################################################
    activitydata = ActivityTrackerSerializer(read_only=True, many=True)
    
    class Meta:
        model = Activity
        fields = ['activity_id', 'name', 'category', 'description', 'activitydata']        