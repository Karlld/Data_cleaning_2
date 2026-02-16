import pandas as pd 

df = pd.read_csv('/Users/Karl/Documents/Messy_Employee_dataset.csv')

#remove white space from column names and cast to lowercase
                   
df.columns = df.columns.str.strip().str.lower()

#set the age column to numeric and fill empty records with nulls

df['age'] = pd.to_numeric(df['age'],errors= 'coerce')

#set the join date column to datetime and fill empty records with nulls

df['join_date'] = pd.to_datetime(df['join_date'], errors= 'coerce')

#set the salary column to numeric and fill empty cells with nulls

df['salary'] = pd.to_numeric(df['salary'], errors= 'coerce')

#split the department_region column into two new columns

df[['department','region']] = df['department_region'].str.split('-',expand=True)

df = df.drop(columns=['department_region'])

#set phone numbers to string and remove non-digits 

df["phone"] = df["phone"].astype(str).str.replace(r"\D", "", regex=True)

#set phone numbers shorter than 10 digits to none

df.loc[df["phone"].str.len() < 10, "phone"] = None

#Check emails are valid in the email column

df = df[df["email"].str.contains("@", na=False)]

#Create a new CSV file for the cleaned dataset

df.to_csv('/Users/Karl/Documents/Cleaned_Employee_dataset.csv', index=False)

print(df.head(10))


| employee_id | first_name | last_name | age  | status   | join_date  | salary     | email                         | phone        | performance_score | remote_work | department  | region      |
|------------|------------|------------|------|----------|------------|------------|--------------------------------|--------------|------------------|------------|-------------|-------------|
| EMP1000    | Bob        | Davis      | 25.0 | Active   | 2021-04-02 | 59767.65   | bob.davis@example.com         | 1651623000   | Average          | True       | DevOps      | California  |
| EMP1001    | Bob        | Brown      |      | Active   | 2020-07-10 | 65304.66   | bob.brown@example.com         | 1898471000   | Excellent        | True       | Finance     | Texas       |
| EMP1002    | Alice      | Jones      |      | Pending  | 2023-12-07 | 88145.90   | alice.jones@example.com       | 5596363000   | Good             | True       | Admin       | Nevada      |
| EMP1003    | Eva        | Davis      | 25.0 | Inactive | 2021-11-27 | 69450.99   | eva.davis@example.com         | 3476491000   | Good             | True       | Admin       | Nevada      |
| EMP1004    | Frank      | Williams   | 25.0 | Active   | 2022-01-05 | 109324.61  | frank.williams@example.com    | 1586734000   | Poor             | False      | Cloud Tech  | Florida     |
| EMP1005    | Alice      | Garcia     | 40.0 | Inactive | 2020-06-10 | 88642.84   | alice.garcia@example.com      | 5409003000   | Good             | False      | Sales       | Texas       |
| EMP1006    | Frank      | Jones      |      | Active   | 2020-04-03 | 96288.43   | frank.jones@example.com       | 4518376000   | Good             | False      | Admin       | Nevada      |
| EMP1007    | Bob        | Jones      | 30.0 | Inactive | 2022-07-17 | 94497.91   | bob.jones@example.com         | 4134328000   | Average          | True       | Cloud Tech  | Florida     |
| EMP1008    | Frank      | Davis      | 35.0 | Inactive | 2023-12-08 | 115565.82  | frank.davis@example.com       | 4177656000   | Excellent        | True       | Admin       | Nevada      |
| EMP1009    | Charlie    | Johnson    |      | Active   | 2022-08-04 | 76561.88   | charlie.johnson@example.com   | 8156986000   | Excellent        | True       | DevOps      | New York    |

