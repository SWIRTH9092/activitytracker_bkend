from django.db import models

########################################################
####   activity table
####      1. contains all the activities
####      2. key - activity id (auto integer field)
####      3. parent of the activity_tracker table
####      4. table was created using sql - see 
####         activity.sql file in repo
####      5. the databases were created from sql so in the
####         class meta:  managed must = true and db_table is 
####         the name of the table 
########################################################
class Activity(models.Model):

    activity_id = models.AutoField(
        primary_key=True,
        )
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'activity'


########################################################
####   activity_tracker table
####      1. contains all the tracking for an activity
####      2. key - tracker id (auto integer field)
####      3. child of the activity table
####      4. key of parent in act_main.  On the postgre 
####         database and in the sql to define the field, 
####         the field was specified as act_main_id but 
####         requires the field name to be specified as:  act_main
####      5. table was created using sql - see 
####         activity.sql file in repo
####      6. the databases were created from sql so in the
####         class meta:  managed must = true and db_table is 
####         the name of the table 
########################################################
class ActivityTracker(models.Model):

    tracker_id = models.AutoField(
         primary_key=True, editable=False
          )
    act_main = models.ForeignKey(
        "activityapp.Activity", on_delete=models.CASCADE, related_name='activitydata')
    # activity_date = models.DateField(default=date.today())
    activity_date = models.DateField(blank=False,null=False)
    activity_count = models.IntegerField(blank=True, null=True)    

    class Meta:
        managed = True
        db_table = 'activity_tracker'
