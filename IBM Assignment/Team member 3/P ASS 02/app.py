from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db
import db2
import re
hostname = '125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud'
uid = 'tvd12891'
pwd = 'izfrMX9ZvAGAoLSE'
driver = "{IBM DB2 ODBC DRIVER}"
db_name = 'Bludb'
port = '30426'
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