# Snowpark_Hands-on_Lab
Detailed instructions for setting up and running Snowpark hands-on lab.

**What You'll Need**
You will need the following things before beginning:

- A Snowflake Account
- A Snowflake user created with ACCOUNTADMIN permissions. This user will be used to get things setup in Snowflake.
- Anaconda Terms & Conditions accepted. See Getting Started section in Third-Party Packages. https://docs.snowflake.com/en/developer-guide/udf/python/udf-python-packages.html#getting-started
- A Python Environment and Python IDE or Code Editor. We recommend Visual Studio Code. https://code.visualstudio.com/
- Access to Git to fork the Snowpark_Hands-on_Lab clone locally


**Step 1 - Snowflake Environment Setup**

Log into Snowflake as AccountAdmin to run the Snowpark_Hands-on_Lab_SF_setup code. https://github.com/sfc-gh-DShaw98/Snowpark_Hands-on_Lab/blob/main/Snowpark_Hands-on_Lab_SF_setup

This code is required to create all the required Snowflake Database Roles, Database, Schema, Warehouse and to grant required permissions.

Step through and run each line to ensure all code runs without error.
![image](https://user-images.githubusercontent.com/120119246/226479301-26ed74a1-6d12-4e82-afef-081622a0fc50.png)

**Step 2 - Python Environment Setup**

We suggest Visual Studio Code (https://code.visualstudio.com/Suggest) be installed on your computer. Check out the Visual Studio Code homepage for a link to the download page. Ensure the Python extension is installed. Search for and install the "Python" extension (from Microsoft) in the Extensions pane in VS Code. Also ensure Snowflake extension installed. Search for and install the "Snowflake" extension (from Snowflake) in the Extensions pane in VS Code.

Log into Visual Studio Code as follows:
 - ROLE: snowpark_workshop_role
 - DATABASE: snowpark_workshop
 - SCHEMA: campaign_demo
 - WAREHOUSE: snowparkws_wh
