#Author : tannt@abivin.com
#Date   : 20180822
#Version: 1.0
#Status : New

#libraries
import pandas as pd
import xlsxwriter
import os

from pymongo import MongoClient
from tabulate import tabulate
from datetime import datetime, date, timedelta
from io import BytesIO
from urllib.request import urlopen
from pprint import pprint

#in-project files
#from server.config import Config

#modules

#Main Class:
class Drivers_And_Orders:

    #Connect to LearningNoSQL
    # client = MongoClient('localhost',27017)

    # db = client.LearningNoSQL
    
    MONGODB_LOC  = "mongodb://root:006c31acbeeee2031a9dd17c59e59a6d8c731db6@"+ \
                   "cotest1.abivin.vn/vApp?authSource=admin";
    
    DB_LOC = "vApp";

    client = MongoClient(MONGODB_LOC)

    db = client[DB_LOC]

    #get Admin username
    adminUsername = 'kospa'

    #get list of organization and roles by 
    admin = list(db.users.find(
        {
            "username" : adminUsername,
            "isDeleted" : False
        },
        {
            "organizationIds"
        }
    ));

    parent_orgs = admin[0]["organizationIds"]

    print(admin)
    print(type(admin))
    print("\n")
    df_admin = pd.DataFrame(admin)
    print(df_admin)
    print("\n")

    print(parent_orgs)
    print(type(parent_orgs))
    print("\n")
    
    #get list of all child and subsequent orgs
    all_orgs = []
    queue    = parent_orgs
    while len(queue) > 0:
        child_orgs = []
        child_doc  = db.organizations.find (
            {
                "$or": [
                    # to remove parentId is null
                    {"parentId": {"$in": queue}},
                    {"_id": {"$in": queue}}
                ],
                "isDeleted": False
            }, {
                "_id"
            })
        for item in child_doc:
            child_orgs.append(item["_id"])
        #end for
        all_orgs = queue
        queue    = child_orgs
        if len(all_orgs) == len(queue):
            break
        #end if
    #end while    

    all_orgs = list(set(all_orgs))

    print(all_orgs)
    print("\n")

    #get roles by orgs and 'DELIVERER' status
    role_doc = list(db.roles.find ({
            "organizationId": {"$in": all_orgs},
            "isDeleted": False
        }, {
            "_id"
        }));

    roleIds = []

    for item in role_doc:
        roleIds.append(item["_id"])
    #end for

    print(roleIds)
    print("\n")

    print("Number of roles found: " + str(len(roleIds))) 

    #get all drivers belong to orgs
    user_doc = list(db.users.find (
        {
            "roleIds": {"$in":roleIds},
            "isDeleted": False
        }, {
            "_id"
        }));

    usernames = []

    for i in range(0,len(user_doc)):
        if user_doc[i]["_id"] not in usernames:
            usernames.append(user_doc[i]["_id"])
        #end if
    #end for

    #bdate and edate
    begin_date = '2018-08-20'
    end_date   = '2018-08-20'
    
    bdate = datetime.strptime(begin_date+"T00:00:00.000Z", "%Y-%m-%dT%H:%M:%S.000Z") - timedelta(hours=7)
    edate = datetime.strptime(end_date+"T23:59:59.999Z", "%Y-%m-%dT%H:%M:%S.999Z") - timedelta(hours=7)


    #get tasks that are valid
    # lấy ra tất cả các 
    mg_tasks = list(db.tasks.aggregate([
            {
                "$match": {
                    "isDeleted": False,
                    "$nor":[
                        {"orderList": {"$size":0}},
                        {"createdAt": {"$lt":bdate}},
                        {"dueDate": {"$gt":edate}}
                    ],
                    "assignedTo": {"$in":usernames}
                    
                }
            }, {
                "$unwind": {
                    "path": "$orderList"
                }
            }, {
                "$lookup": {
                    "from": "saleOrders",
                    "localField": "orderList",
                    "foreignField": "_id",
                    "as": "order"
                }
            }, {
                "$unwind": {
                    "path": "$order"
                }
            }, {

                # đặt tên cho order.totalWeight là totalWeight và tương tự, lấy ra Id, OrderList, assignedToInfo, fullfillmentStatus
                "$project": {
                    "_id": False,
                #orderList này join như nào, lấy ra a sao
                #tại sao dùng được assignedToInfo. lieu co phai nhung column nao ma refer sang cac id o bang khac thi co the extend

                    "orderList": 1,
                    "assignedToInfo": 1,
                    
                    "totalWeight": "$order.totalWeight",            
                    "totalVolume": "$order.totalVolume",
                    
                    "fulfillmentStatus": "$order.fulfillmentStatus"
                }
            }
        ]))

    #assign dataframe
    df_tasks = pd.DataFrame(mg_tasks)
        
    print(df_tasks)






