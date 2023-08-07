# XGames_Snowpark_SiS
Streamlit in Snowflake app to track Snowpark Workshops vs Snowpark Consumption vs all Snowflake consumption

Here is the code to create an XGames tracking application that feeds off Snowhouse data from the finance.customer.snowflake_account_revenue table and sales.sales_engineering.partner_credit_usage tracking tool=Snowpark usage table. A third table is tracking Snowpark workshop information located in dshaw.SNOWPARK_WORKSHOPS table.
![image](https://github.com/sfc-gh-DShaw98/XGames_Snowpark_SiS/assets/120119246/2cc47b05-23bb-45e5-963f-3ccf6a56f62b)

SiS users are currently limited to Sales Engineering only since they have grant usage access to the three tables noted above.

SiS users should first select the DM, then the AE, then their aligned account. You can modify the start / end dates in the left nav.

If you'd like to add or edit Snowpark workshops aligned to the selected account, ensure you enter the exact name listed in the left nav. A primary key is created to match the account name and date. Do not enter two workshops with the same account name and date, else the merge code to update the dshaw.SNOWPARK_WORKSHOPS table will fail.
