from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db
import db2
import re
hostname = '98538591-7217-4024-b027-8baa776ffad1.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud'
uid = 'djw31186'
pwd = 'UknSZfcxrWVNlIxT'
driver = "{IBM DB2 ODBC DRIVER}"
db_name = 'Bludb'
port = '30875'
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