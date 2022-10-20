from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db
import db2
import re
hostname = '9938aec0-8105-433e-8bf9-0fbb7e483086.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud'
uid = 'cjn94379'
pwd = 'Ep20Vfe3GyURJPRU'
driver = "{IBM DB2 ODBC DRIVER}"
db_name = 'Bludb'
port = '32459'
protocol = 'TCPIP'
dsn = (
"DATABASE ={0};"
"HOSTNAME ={1};"
"PORT ={2};"
"UID ={3};"
"SECURITY=SSL;"
"PROTOCOL={4};"
"PWD ={5};"
).format(db_name, hostname, port, uid, protocol, pwd)
print(dsn)
try:
	print("Connecting to db2.....")
	db2 = ibm_db.connect(dsn, "", "")
	print()
	print("Connected to database")
	print("Connection Successful!!!")
except Exception as exception:
	print("unable to connect ", exception)