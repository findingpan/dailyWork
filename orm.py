#coding=utf-8
from sqlalchemy import Table, MetaData, Column, Integer, String, DateTime 
from datetime import datetime 
from sqlalchemy.engine import create_engine 
 
engine = create_engine('oracle://ihis:ihis@127.0.0.1:1521/tjncich')  

metadata = MetaData()  