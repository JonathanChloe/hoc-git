#Config Database here
#Author : tannt@abivin.com
#Date   : 20180817
#Version: 1.0
#Status : New

#libraries
import socket;
import pymongo;
from pymongo import MongoClient;

#configuration class
class Config:

    #Connect to MongoDB

    MONGODB_LOC  = "mongodb://root:006c31acbeeee2031a9dd17c59e59a6d8c731db6@"+ \
                   "cotest1.abivin.vn/vApp?authSource=admin";
    
    DB_LOC = "vApp";

    print("\nDatabase URL: ",MONGODB_LOC);

    print("Database Name: ", DB_LOC)
#end Class

#end of file
