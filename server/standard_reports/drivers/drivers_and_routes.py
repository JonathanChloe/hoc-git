#Author : tannt@abivin.com
#Date   : 20180817
#Version: 1.0
#Status : New

#libraries
import pandas as pd;
import pymongo;
from pymongo import MongoClient;
import os;

#in-project files

#modules

#configuration class
class Drivers_And_Routes:

    # Connect to LearningNoSQL
    client = MongoClient('localhost',27017);

    db = client.LearningNoSQL;

    # Get data from DB
    li_emp = list(db.Employee.find());

    # Input into dataframe
    df_emp = pd.DataFrame(li_emp);

    df_emp_short = df_emp[['first_name','last_name','dept_id','title']]

    print(df_emp_short);

    # Write to .xlsx File
    #os.chdir('D:/Learning/hoc-git/export/')

    # writer = pd.ExcelWriter(r'/mnt/d/Learning/hoc-git/export/Employee_Listing.xlsx', engine = 'xlsxwriter')

    # df_emp_short.to_excel(writer, sheet_name ='Employee_Listing')

    # writer.save()


    # Test sales
    admin = list(db.Sales.find (
            {
                "item": 'abc'
            }, 
            {
                "price" , "quantity"
            }
        ));
    
    print(admin)

    













