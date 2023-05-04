# The Snowpark package is required for Python Worksheets. 
# You can add more packages by selecting them using the Packages control and then importing them.

import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col

def main(session: snowpark.Session): 
    # Your code goes here, inside the "main" handler.

    # Populate the following list with the user account names for all attendees
    # ex. the_userList = ["User1", "User2", "User3", ....]
    the_userList = []

    for theUser in the_userList:
        session.sql("GRANT ROLE snowflake_workshop_role TO {}".format(theUser))

    # Return value will appear in the Results tab.
    return the_userList[0]
