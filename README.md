# Snowpark_Hands-on_Lab
Detailed instructions for setting up and running Snowpark hands-on lab.

****What You'll Need****
You will need the following things before beginning:

- A Snowflake Account
- A Snowflake user created with ACCOUNTADMIN permissions. This user will be used to get things setup in Snowflake.
- Anaconda Terms & Conditions accepted. See Getting Started section in Third-Party Packages. https://docs.snowflake.com/en/developer-guide/udf/python/udf-python-packages.html#getting-started
- A Python Environment and Python IDE or Code Editor. We recommend Visual Studio Code. https://code.visualstudio.com/
- Access to Git to fork the Snowpark_Hands-on_Lab clone locally

Prerequisites




**Pre-Workshop Instructions**

**Snowflake Environment Setup**

- Log into your Snowflake account and switch to ACCOUNTADMIN role
- Click on Admin and then Billing & Terms on the left side panel
- On the Terms and Billing tab, read and accept terms to continue with the workshop
- Create a new worksheet and run the Snowpark_Hands-on_Lab_SF_setup code. https://github.com/sfc-gh-DShaw98/Snowpark_Hands-on_Lab/blob/main/Snowpark_Hands-on_Lab_SF_setup. This code is required to create all the required Snowflake Database Roles, Database, Schema, Warehouse and to grant required permissions. Step through and run each line to ensure all code runs without error.
![image](https://user-images.githubusercontent.com/120119246/226479301-26ed74a1-6d12-4e82-afef-081622a0fc50.png)


**Python Environment Setup**

- Create and Activate Conda Environment (OR, use any other Python environment with Python 3.8). 
- conda create --name snowpark -c https://repo.anaconda.com/pkgs/snowflake python=3.8
- conda activate snowpark
- Install Snowpark for Python, Streamlit and other libraries in Conda environment
- conda install -c https://repo.anaconda.com/pkgs/snowflake snowflake-snowpark-python pandas notebook scikit-learn cachetools
- Update connection.json with your Snowflake account details and credentials

TIP: We suggest installing Visual Studio Code (https://code.visualstudio.com/Suggest) on your computer. Check out the Visual Studio Code homepage for a link to the download page. Ensure the Python extension is installed. Search for and install the "Python" extension (from Microsoft) in the Extensions pane in VS Code. Also ensure Snowflake extension installed. Search for and install the "Snowflake" extension (from Snowflake) in the Extensions pane in VS Code. We also recommend installing GitHub Desktop on your computer (https://desktop.github.com/). 

Log into Visual Studio Code as follows:
 - ROLE: snowpark_workshop_role
 - DATABASE: snowpark_workshop
 - SCHEMA: campaign_demo
 - WAREHOUSE: snowparkws_wh
 
 ![image](https://user-images.githubusercontent.com/120119246/226482767-21dccaba-158e-4523-add8-42a9092a2eab.png)




**Workshop Instructions**

**Step 1 - Walk through Snowpark Overview Deck**

**Step 2 - Ensure participants can access hands-on lab instructions, Snowflake, and Visual Studio Code (or other Python IDE)** 

**Step 3 - Walk through an run Snowpark_For_Python notebook**
- Navigate to the GitHub repo for this lab: https://github.com/sfc-gh-DShaw98/Snowpark_Hands-on_Lab/blob/main/Snowpark_For_Python.ipynb
- Click on the Green button to get the files in GitHub Desktop
- Select the Open in Visual Studio Code button
![image](https://user-images.githubusercontent.com/120119246/227010729-5e46c1d4-5ccd-47d1-936b-fa36e6e868ac.png)
![image](https://user-images.githubusercontent.com/120119246/227010286-4db464d3-03f7-460c-942a-1b8d3498a813.png)

- Go to the connection.json file and update as follows:
  - account: _update with your Snowflake account_
  - user: _update with your user_
  - password: _update with your password_
  - role: snowpark_workshop_role
  - warehouse: snowparkws_wh
  - database: snowpark_workshop
  - schema: campaign_demo
![image](https://user-images.githubusercontent.com/120119246/227032958-a69b85a5-8546-4446-8103-02763436c7b8.png)

Trying to determine your Snowflake account name? Log into Snowflake. Click your account on the bottom left corner. Select the account to expose the details. Click to _copy account identifier_.
![image](https://user-images.githubusercontent.com/120119246/227042133-77525131-d482-46e4-b666-4ab82dfe9232.png)


- Go to the Snowpark_For_Python.ipynb file
- Ensure you have selected snowpark (Python 3.8.13) as your Python kernel
- ![image](https://user-images.githubusercontent.com/120119246/227042426-9748ad79-6941-4508-873d-18b1f9fb1398.png)

- Read through the Objective and Instructions
- Execute the code to import required Snowpark, json, pandas and logging libraries
- ![image](https://user-images.githubusercontent.com/120119246/227033232-3cc2a43e-53cb-4469-8413-6a2658048481.png)

- Execute the code to user your connection.json file 


