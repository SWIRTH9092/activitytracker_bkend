### Project4 Python Backend for Activity Tracker

##### Links
- GitHub: https://github.com/SWIRTH9092/activitytracker_backend
- Render: https://sw-activitytracker-bkend.onrender.com/activity/

##### Dependencies
- Django
    - dj-database-url 
    - psycopg2-binary
    - rest-framework
- Postgres

##### Activity Tracker Tables
-   Postgres database name:  
    - projects
-   table names:
    - activity (parent table)
    - activity tracker (child table)
- Features:
    -  referential integrity between the tables
        - activity.activity_id = activity_tracker.act_main_id
    -  cascading deletes if activity row is deleted (data is also deleted from the activitytracker table as well)

<img src="https://i.imgur.com/Ie0D0Jf.jpg" alt="sql database drawing" title="SQL database drawing" width="90%"/> 

#### Routes 

| Table |Routes | Method | EndPoints | Expected Result |
|------|-------|--------|-----------|-----------------|
| activity | Index | GET | /activity | Gets all entries |
| activity | Create | POST | /activity | Creates a new entry |
| activity | Show | GET | /activity:id | Gets 1 entry
| activity | Update | PUT | /activity:id | Updates Existing Entry |
| activity | Delete | DELETE | /activity:id | Removes entry from database
| activitytracker| Index | GET | /activitytracker | Gets all entries |
| activitytracker| Create | POST | /activitytracker | Creates a new entry |
| activitytracker| Show | GET | /activitytracker:id | Shows all entries for an activity
| activitytracker| Update | PUT | /activitytracker:id | Updates Existing Entry |
| activitytracker| Delete | DELETE | /activitytracker:id | Removes entry from database
| activitydata| Show | GET | /activitydata:id | Gets 1 entry for an activity and all of the activitytracker detail|

##### SQL to define tables to Postgres

- SQL to create activity table (parent)
    CREATE TABLE activity (     
        activity_id serial PRIMARY KEY,     
        activity VARCHAR(30) NOT NULL,     
        category VARCHAR(30) NOT NULL DEFAULT 'Other',     
        description VARCHAR(50)     
    );

- SQL to create activity_tracker table (child)     
    CREATE TABLE activity_tracker (     
        tracker_id serial PRIMARY KEY,     
        act_main_id INTEGER,     
        activity_date DATE DEFAULT CURRENT_DATE,     
        activity_count INTEGER DEFAULT 0,     
        CONSTRAINT fk_activity_id     
            FOREIGN KEY(act_main_id)     
                REFERENCES activity(activity_id)    
                On DELETE CASCADE     
    );    