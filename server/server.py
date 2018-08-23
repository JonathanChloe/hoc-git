#Config Database here
#Author : tannt@abivin.com
#Date   : 20180817
#Version: 1.0
#Status : New

#libraries
import sys;
import json;
import os;
import socket;

from pymongo        import MongoClient;
from datetime       import datetime, timedelta;
from io             import BytesIO;

#in-project files
from config import Config;

#modules
from standard_reports.drivers.drivers_and_routes import Drivers_And_Routes;

#class Server
class Server:

    #connect to MongoDB
    client = MongoClient('localhost',27017);

    db = client.LearningNoSQL;

    #get list of Employees
    def get_list_of_employee:

