from django.shortcuts import render
from urllib import request
import simplejson as json
from django.http import (HttpResponse,HttpResponseRedirect)
from django.contrib.auth.decorators import login_required
import MySQLdb
import random
from django.core.files.storage import FileSystemStorage
from django.views.decorators.cache import cache_control
import smtplib 
import urllib.request
import webbrowser
from django.contrib import messages
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from tkinter import *
from tkinter import messagebox
import os
import pyodbc

# con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Program Files (x86)\\BioEnable\\BioDesk\\fppayroll.mdb;')
# cursor = conn.cursor()

# import pyodbc
# import adodbapi
# database = "fppayroll.mdb"
# constr = 'Provider=Microsoft.Jet.OLEDB.4.0; Data Source=fppayroll.mdb'
# conn11 = adodbapi.connect(constr)
# database_path='fppayroll'
# connectionString = (
    # f'Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={database_path};'
# )
# connection = pyodbc.connect(connectionString, autocommit = True)

# conn1 = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Program Files (x86)\\BioEnable\\BioDesk\\fppayroll.mdb;')
# cursor = conn1.cursor()
# cursor.execute('select * from table name')
   
# for row in cursor.fetchall():
#     print (row)


# def sendmail(toadd,msg):

#     #create smtp session
#     s = smtplib.SMTP('smtp.gmail.com',587)

#     #start TLS for security
#     s.starttls()

#     #Authentication
#     s.login("gmedifile@gmail.com","gmedifile123")

#     #Message you need to be send
    
#     #Sending the mail
#     s.sendmail("gmedifile@gmail.com",toadd,msg)

#     #terminating the session
#     s.quit()
    
# def sendsms(ph,msg):

#     sendToPhoneNumber= "+91"+ph
#     userid = "2000022557"
#     passwd = "54321@lcc"
#     url = "http://enterprise.smsgupshup.com/GatewayAPI/rest?method=sendMessage&send_to=" + sendToPhoneNumber + "&msg=" + msg + "&userid=" + userid + "&password=" + passwd + "&v=1.1&msg_type=TEXT&auth_scheme=PLAIN"
#     # contents = urllib.request.urlopen(url)
#     webbrowser.open(url)



# Create your views here.
conn = MySQLdb.connect("localhost","root","","medifile")
c = conn.cursor()


def user_homeview(request):
    # print(date.today())
    # print(time.now())
    print(datetime.now().time())

    print(date.today())
    return render(request,"user_home.html")

def user_tempview(request):
    return render(request,"user_temp.html")

def user_contactview(request):
    msg=""
    if(request.POST):
        name =  request.POST.get("name")
        g_id = request.POST.get("g_id")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        designation = "guest"
        s = "insert into pt_contact values('"+str(name)+"','"+str(g_id)+"','"+str(email)+"','"+str(phone)+"','"+str(subject)+"','"+str(message)+"','"+str(designation)+"')"
        c.execute(s)
        conn.commit()
        msg="MESSAGE SEND SUCCESSFULLY"
    return render(request,"user_contact.html",{"msg":msg})

def user_loginview(request):
    
    alert =""
    try:
        if(request.POST):
            g_id = request.POST.get("g_id")
            password = request.POST.get("password")
            # s = "select * from login where g_id='"+g_id+"' AND password='"+password+"' and status='Approved'"
            s = "select * from login where g_id='"+g_id+"' AND password='"+password+"' "
            c.execute(s)
            print(s)
            data = c.fetchone()
            print("#################################")
            print(data[4])
            print("#################################")
            if (g_id == "admin" and password == "admin123"):
                return HttpResponseRedirect("/dashview")
            elif (data[4] == "hospital"):
                request.session["uname"] = data[2]
                request.session["ug_id"] = g_id
                return HttpResponseRedirect("/hos_homeview")
            elif (data[4] =="patient"):
                request.session["uname"] = data[2]
                request.session["ug_id"] = g_id
                return HttpResponseRedirect("/pt_homeview")
            elif (data[4] == "doctor"):
                request.session["uname"] = data[2]
                request.session["ug_id"] = g_id 
                request.session["uhos_id"] = data[5]
                return HttpResponseRedirect("/dr_homeview")
            elif (data[4] == "staff" or data[4] == "nurse"):
                request.session["desig"] = data[4]
                request.session["uname"] = data[2]
                request.session["ug_id"] = g_id
                request.session["uhos_id"] = data[5]
                return HttpResponseRedirect("/st_homeview")
            # else:
            #     alert="Invalid User Name or Password"
    except:
        alert="Invalid USER NAME or PASSWORD"
    return render(request,"user_login.html",{"alert":alert})

def user_registerview(request):
    g_id = random.randrange(100000, 1000000, 3)
    designation = "hospital"
    null =  "NULL"
    gid=""
    if(request.POST):
        name =  request.POST.get("name")
        hos_id = request.POST.get("hos_id")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        site = request.POST.get("site")
        password = request.POST.get("password")
        cnf_password = request.POST.get("cnf_password")
        s = "insert into register(name,hos_id,address,phone,site,password,cnf_password,g_id,designation) values('"+str(name)+"','"+str(hos_id)+"','"+str(address)+"','"+str(phone)+"','"+str(site)+"','"+str(password)+"','"+str(cnf_password)+"','"+str(g_id)+"','"+str(designation)+"')"
        c.execute(s)
        conn.commit()
        log = "insert into login(g_id,name,password,designation,hos_id,status) values('"+str(g_id)+"','"+str(name)+"','"+str(password)+"','"+str(designation)+"','"+str(null)+"','Registred')"
        c.execute(log)
        conn.commit()
        c.execute("select g_id from login where id in (select max(id) from login)")
        dataa=c.fetchone()
        gid=dataa[0]
        print("*****************************///////////////////////////********************")
        print(gid)
        msg="Welcome to Global Medifile\nRegistration Successfull\n Your Details : \n Username: "+name+"\n Password : "+password+"\n Global ID : "+str(dataa[0])
        # sendsms(phone,msg)
        # sendmail(site,msg)

        # return HttpResponseRedirect("/user_loginview", {"g_id":gid})
        # return render(request,"user_login.html",{"g_id":g_id})
    # os.startfile("C:\Program Files (x86)\BioEnable\BioDesk\BioDesk.exe")
    return render(request,"user_register.html",{"g_id":gid})
    # return render_to_response("user_register.html",context_instance=RequestContext(request))

def forgotpassword(request):
    if(request.POST):
        name =  request.POST.get("name")
        g_id = request.POST.get("g_id")
        password = request.POST.get("password")
        cnf_password = request.POST.get("cnf_password")
        q="select name from login where g_id='"+str(g_id)+"'"
        c.execute(q)
        d=c.fetchone()
        namme=d[0]
        print(namme)
        if namme==name:
            s = "update login set password='"+str(password)+"' where g_id='"+str(g_id)+"'"
            c.execute(s)
            conn.commit()
            return HttpResponseRedirect("/user_loginview")
    return render(request,"forgotpassword.html")
    

def user_register_ptview(request):
    g_id = random.randrange(100000, 1000000, 3)
    designation = "patient"
    null =  "NULL"
    gid=""
    if 'reg' in request.POST:
        img = request.POST.get("img")
        myfile = request.FILES["img"]
        fs = FileSystemStorage()        
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        name = request.POST.get("name")
        mail = request.POST.get("email")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        dob = request.POST.get("dob")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        votersid = request.POST.get("votersid")
        adharno = request.POST.get("adharno")
        licno = request.POST.get("licno")
        blood =  request.POST.get("blood")
        password = request.POST.get("password")
        cnf_password = request.POST.get("cnf_password")
        # check = "select count(*) from login where name='"+name+"'"
        # c.execute(check)
        # data = c.fetchall()
        # if(data[0][0]==0):
        relative1 = request.POST.get("relative1")
        relation1 = request.POST.get("relation1")
        address1 = request.POST.get("address1")
        phone1 = request.POST.get("phone1")
        relative2 = request.POST.get("relative2")
        relation2 = request.POST.get("relation2")
        address2 = request.POST.get("address2")
        phone2 = request.POST.get("phone2")
        s = "insert into addpat(img,name,email,age,gender,dob,phone,address,votersid,adharno,licno,blood,password,cnf_password,g_id,designation) values('"+str(filename)+"', '"+str(name)+"', '"+str(mail)+"', '"+str(age)+"','"+str(gender)+"', '"+str(dob)+"','"+str(phone)+"','"+str(address)+"','"+str(votersid)+"','"+str(adharno)+"','"+str(licno)+"','"+str(blood)+"','"+str(password)+"','"+str(cnf_password)+"','"+str(g_id)+"','"+str(designation)+"')"
        c.execute(s)
        conn.commit()
        log = "insert into login(g_id,name,password,designation,hos_id) values('"+str(g_id)+"','"+str(name)+"','"+str(password)+"','"+str(designation)+"','"+str(null)+"')"
        c.execute(log)
        conn.commit()
        msg="Welcome to Global Medifile\nRegistration Successfull\n Your Details : \n Username: "+name+"\n Password : "+password+"\n Global ID : "+str(g_id)
        # sendsms(phone,msg)
        # sendmail(mail,msg)
        a = "insert into relative(`g_id`,`patient_name`,`relative1`,`relation1`,`address1`,`phone1`,`relative2`,`relation2`,`address2`,`phone2`) values('"+str(g_id)+"','"+str(name)+"','"+str(relative1)+"','"+str(relation1)+"','"+str(address1)+"','"+str(phone1)+"','"+str(relative2)+"','"+str(relation2)+"','"+str(address2)+"','"+str(phone2)+"')"
        c.execute(a)
        conn.commit()
        c.execute("select g_id from login where id in (select max(id) from login)")
        dataa=c.fetchone()
        gid=dataa[0]
        # os.startfile("C:\Program Files (x86)\BioEnable\BioDesk\BioDesk.exe")
        

        # return HttpResponseRedirect("/user_loginview")
    # if 'finger' in request.POST:
    #     os.startfile("C:\Program Files (x86)\BioEnable\BioDesk\BioDesk.exe")
       
    #     os.startfile("E:\\medifile\\userapp\\static\\bin\\Debug\\ConsoleApplication1.exe")
    #     file1 = open("C:\\t.txt","r+")  
    #     data=file1.read()
    #     ss="select * from addpat where g_id='"+data+"'"   
    #     print(ss)  
    #     c.execute(ss)
    #     d=c.fetchall()
    #     print(d)
    #     return render(request,"user_register_pt.html",{"data":d})
    return render(request,"user_register_pt.html",{"g_id":gid})

# def patient_relativesview(request):
#     print("hiiiiiiiiiiiiiiiii")
#     if 'view_detail' in request.POST:
#         os.startfile("C:\Program Files (x86)\BioEnable\BioDesk\BioDesk.exe")
#         os.startfile("E:\\medifile\\userapp\\static\\bin\\Debug\\ConsoleApplication1.exe")
#         file1 = open("C:\\t.txt","r+")  
#         data=file1.read()
#         ss="select * from relative where g_id='"+data+"'"   
#         print(ss)  
#         c.execute(ss)
#         d=c.fetchall()
#         print(d)
#         return render(request,"patient_relatives.html",{"data":d}) 
#     return render(request,"patient_relatives.html")

def user_aboutview(request):
    return render(request,"user_about.html")

# hospital Section

def hos_tempview(request):
    return render(request,"hos_temp.html")

@cache_control(no_cache=True, must_revalidate=True)
def hos_homeview(request):
    uname = request.session["uname"]
    ug_id = request.session["ug_id"]
    return render(request,"hos_home.html",{"ug_id":ug_id,"uname":uname})

def hos_dptview(request):
    uname = request.session["uname"]
    ug_id = request.session["ug_id"]
    return render(request,"hos_dpt.html",{"ug_id":ug_id,"uname":uname})

def hos_cardiologyview(request):
    uname = request.session["uname"]
    ug_id = request.session["ug_id"]
    return render(request,"hos_cardiology.html",{"ug_id":ug_id,"uname":uname})

def hos_suggestview(request):
    uname = request.session["uname"]
    ug_id = request.session["ug_id"]
    return render(request,"hos_suggest.html",{"ug_id":ug_id,"uname":uname})

def hos_adddptview(request):
    data2=""
    hos_id = request.session["ug_id"]
    name = request.session["uname"]
    dpt_id = random.randrange(1000,9999,3)
    dptname = request.POST.get("dptname")
    gid=0
    if 'search' in request.POST:
       
        s = "select name from adddoc where department='"+str(dptname)+"'"
        c.execute(s)
        data2 = c.fetchall()
        print("**************************************************************")
        print(data2)
        # return HttpResponseRedirect("/hos_adddptviews")
        return render(request,"hos_adddpt.html",{"data2":data2})

    if 'add' in request.POST:
        dpthead = request.POST.get("dpthead")
        phone = request.POST.get("phone")
        drlist = request.POST.get("drlist")
        details = request.POST.get("details")
        s = "insert into adddpt(dptname,dptid,dpthead,phone,drlist,details,hos_id,hos_name) values('"+str(dptname)+"','"+str(dpt_id)+"','"+str(dpthead)+"','"+str(phone)+"','"+str(drlist)+"','"+str(details)+"','"+str(hos_id)+"','"+str(name)+"')"
        c.execute(s)
        conn.commit()
        
    return render(request,"hos_adddpt.html",{"dpt_id":dpt_id,"ug_id":hos_id,"uname":name,"data2":data2})

def hos_addstaffview(request):
    g_id = random.randrange(100000, 1000000, 3)
    hos_id = request.session["ug_id"]
    uname = request.session["uname"]
    dpt = "select distinct dptname, hos_id from adddpt where hos_id='"+hos_id+"'"
    c.execute(dpt)
    conn.commit()
    data = c.fetchall()
    gid=""
    if(request.POST.get("submit")=="Add"):
        img_files = request.POST.get("img_files")
        myfile = request.FILES["img_files"]
        fs = FileSystemStorage()        
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        name = request.POST.get("name")
        mail = request.POST.get("email")
        age = request.POST.get("age")
        phone = request.POST.get("phone")
        department = request.POST.get("department")
        date = request.POST.get("date")
        designation = request.POST.get("designation")
        salary = request.POST.get("salary")
        files = request.POST.get("files")
        password = request.POST.get("password")
        cnf_password = request.POST.get("cnf_password")
        s = "insert into addstaff(img_files,name,email,age,phone,department,date,designation,salary,files,password,cnf_password,g_id,hos_id,hos_name) values('"+str(filename)+"','"+str(name)+"','"+str(mail)+"','"+str(age)+"','"+str(phone)+"','"+str(department)+"','"+str(date)+"','"+str(designation)+"','"+str(salary)+"','"+str(files)+"','"+str(password)+"','"+str(cnf_password)+"','"+str(g_id)+"','"+str(hos_id)+"','"+str(uname)+"')"
        c.execute(s)
        conn.commit()   
        log = "insert into login(g_id,name,password,designation,hos_id) values('"+str(g_id)+"','"+str(name)+"','"+str(password)+"','"+str(designation)+"','"+str(hos_id)+"')"
        c.execute(log)
        conn.commit()
        c.execute("select g_id from login where id in (select max(id) from login)")
        dataa=c.fetchone()
        gid=dataa[0]
        msg="Welcome to Global Medifile,\n Your Staff Registration details: \n username: "+name+"\n Password : "+password+"\n Global ID : "+str(g_id)
        # sendsms(phone,msg)
        # sendmail(mail,msg)
    return render(request,"hos_addstaff.html",{"data":data,"ug_id":hos_id,"uname":uname,"g_id":gid})

def hos_adddocview(request):
    g_id = random.randrange(100000, 1000000, 3)
    designation = "doctor"
    hos_id = request.session["ug_id"]
    uname = request.session["uname"]
    dpt = "select distinct dptname, hos_id from adddpt where hos_id='"+hos_id+"'"
    print(dpt)
    c.execute(dpt)
    conn.commit()
    data = c.fetchall()
    gid=""
    if(request.POST):
        img_files = request.POST.get("img_files")
        myfile = request.FILES["img_files"]
        fs = FileSystemStorage()        
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        name = request.POST.get("name")
        mail = request.POST.get("email")
        age =  request.POST.get("age")
        phone = request.POST.get("phone")
        qualification = request.POST.get("qualification")
        department = request.POST.get("department")
        # fnoon = request.POST.get("fnoon")
        # ftoken = request.POST.get("ftoken")
        # anoon = request.POST.get("anoon")
        # atoken = request.POST.get("atoken")
        specialization = request.POST.get("specialization")
        date = request.POST.get("date")
        salary = request.POST.get("salary")
        files = request.POST.get("files")
        password = request.POST.get("password")
        cnf_password = request.POST.get("cnf_password")
        # ,`forenoon`,`fore_token`,`afternoon`,`after_token`       ,'"+str(fnoon)+"','"+str(ftoken)+"','"+str(anoon)+"','"+str(atoken)+"'
        s = "insert into adddoc(img_files,name,email,age,phone,qualification,department,spacialization,date,salary,designation,files,password,cnf_password,g_id,hos_id,hos_name) values('"+str(filename)+"','"+str(name)+"','"+str(mail)+"','"+str(age)+"','"+str(phone)+"','"+str(qualification)+"','"+str(department)+"','"+str(specialization)+"','"+str(date)+"','"+str(salary)+"','"+str(designation)+"','"+str(files)+"','"+str(password)+"','"+str(cnf_password)+"','"+str(g_id)+"','"+str(hos_id)+"','"+str(uname)+"')"
        c.execute(s)
        conn.commit()       
        log = "insert into login(g_id,name,password,designation,hos_id) values('"+str(g_id)+"','"+str(name)+"','"+str(password)+"','"+str(designation)+"','"+str(hos_id)+"')"
        c.execute(log)
        conn.commit()
        msg="Welcome to Global Medifile,\n Your Doctor Registration details: \n username: "+name+"\n Password : "+password+"\n Global ID : "+str(g_id)
        # sendsms(phone,msg)
        # sendmail(mail,msg)
        c.execute("select g_id from login where id in (select max(id) from login)")
        dataa=c.fetchone()
        gid=dataa[0]
    return render(request,"hos_adddoc.html",{"data":data,"ug_id":hos_id,"uname":uname,"dr_id":gid})

def hos_addpatview(request):
    g_id = random.randrange(100000, 1000000, 3)
    designation = "patient"
    hos_id = "null"
    ug_id = request.session["ug_id"]
    uname = request.session["uname"]
    gid=""
    if(request.POST):
        img = request.POST.get("img")
        myfile = request.FILES["img"]
        fs = FileSystemStorage()        
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        name = request.POST.get("name")
        mail = request.POST.get("email")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        dob = request.POST.get("dob")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        votersid = request.POST.get("votersid")
        adharno = request.POST.get("adharno")
        licno = request.POST.get("licno")
        blood =  request.POST.get("blood")
        password = request.POST.get("password")
        cnf_password = request.POST.get("cnf_password")
        s = "insert into addpat(img,name,email,age,gender,dob,phone,address,votersid,adharno,licno,blood,password,cnf_password,g_id,designation) values('"+str(filename)+"','"+str(name)+"', '"+str(mail)+"', '"+str(age)+"','"+str(gender)+"', '"+str(dob)+"','"+str(phone)+"','"+str(address)+"','"+str(votersid)+"','"+str(adharno)+"','"+str(licno)+"','"+str(blood)+"','"+str(password)+"','"+str(cnf_password)+"','"+str(g_id)+"','"+str(designation)+"')"
        c.execute(s)
        conn.commit()
        log = "insert into login(g_id,name,password,designation,hos_id) values('"+str(g_id)+"','"+str(name)+"','"+str(password)+"','"+str(designation)+"','"+str(hos_id)+"')"
        c.execute(log)
        conn.commit()
        msg="Welcome to Global Medifile.\n Your REgistration Details: \n username: "+name+"\n Password : "+password+"\n Global ID : "+str(g_id)
        # sendsms(phone,msg)
        # sendmail(mail,msg)
        c.execute("select g_id from login where id in (select max(id) from login)")
        dataa=c.fetchone()
        gid=dataa[0]
    return render(request,"hos_addpat.html",{"ug_id":gid,"uname":uname,"g_id":gid})

def hos_contactview(request):
    ug_id = request.session["ug_id"]
    uname = request.session["uname"]
    if(request.POST):
        name =  request.POST.get("name")
        g_id =  request.POST.get("g_id")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        designation = "hospital"
        s = "insert into pt_contact values('"+str(name)+"','"+str(g_id)+"','"+str(email)+"','"+str(phone)+"','"+str(subject)+"','"+str(message)+"','"+str(designation)+"')"
        c.execute(s)
        conn.commit()
    return render(request,"hos_contact.html",{"ug_id":ug_id,"uname":uname})
    

def hos_leaveview(request):
    hos_id = request.session["ug_id"]
    uname = request.session["uname"]
    print(hos_id)
    d = "select * from dr_leave where hos_id='"+hos_id+"'"
    c.execute(d)
    data = c.fetchall()
    a = "nurse"
    n = "select * from st_leave where hos_id='"+hos_id+"' and designation='nurse ' and status='applied'"
    c.execute(n)
    data1 = c.fetchall()
    b = "staff"
    s = "select * from st_leave where hos_id='"+hos_id+"' and designation='"+b+"'"
    c.execute(s)
    data2 = c.fetchall()
    return render(request,"hos_leave.html",{"data":data,"data1":data1,"data2":data2,"ug_id":hos_id,"uname":uname})

def statusview(request):
    status = request.GET.get("status")
    dr_id = request.GET.get("dr_id")
    if (status == "Approved"):
        a = "update dr_leave set status='"+status+"' where dr_id='"+dr_id+"'"
        c.execute(a)
        conn.commit()
        # return HttpResponseRedirect("/dr_leaveview")

    if (status == "Rejected"):
        b = "update dr_leave set status='"+status+"' where dr_id='"+dr_id+"'"
        c.execute(b)
        conn.commit()
        # return HttpResponseRedirect("/dr_leaveview")
    return HttpResponseRedirect("/hos_leaveview")

def nu_statusview(request):
    status = request.GET.get("status")
    nu_id = request.GET.get("nu_id")
    print(nu_id)
    print(status)
    if(status == "Approved"):
        a = "update st_leave set status='approved' where st_id='"+nu_id+"'"
        c.execute(a)
        conn.commit()
    if(status == "Rejected"):
        a = "update st_leave set status='"+status+"' where st_id='"+nu_id+"'"
        c.execute(a)
        conn.commit()
    return HttpResponseRedirect("/hos_leaveview")

def st_statusview(request):
    status = request.GET.get("status")
    st_id = request.GET.get("nu_id")
    if(status == "Approved"):
        a = "update st_leave set status='"+status+"' where st_id='"+st_id+"'"
        c.execute(a)
        conn.commit()
    elif(status == "Rejected"):
        a = "update st_leave set status='"+status+"' where st_id='"+st_id+"'"
        c.execute(a)
        conn.commit()
    return HttpResponseRedirect("/hos_leaveview")

def hos_editview(request):
    print("1000000000")
    hos_id = request.session["ug_id"]
    uname = request.session["uname"]
    dict_1 = {"hos_id":hos_id,"uname":uname}
    if 'change_name' in request.POST:
        new_name = request.POST.get("new_name")
        s = "update "
    return render(request,"hos_edit.html",dict_1)

# Doctor page Section
# ===================
def dr_tempview(request):
    return render(request,"dr_temp.html")

def dr_homeview(request):
    uname = request.session["uname"]
    ug_id = request.session["ug_id"] 
    uhos_id = request.session["uhos_id"]
    s = "select img_files from adddoc where g_id='"+ug_id+"'"
    c.execute(s)
    data1 =  c.fetchall()
    return render(request,"dr_home.html",{"data1":data1,"uname":uname,"ug_id":ug_id,"uhos_id":uhos_id})

def dr_dptview(request):
    uname = request.session["uname"]
    ug_id = request.session["ug_id"] 
    return render(request,"dr_dpt.html",{"uname":uname,"ug_id":ug_id})

def dr_cardiologyview(request):
    uname = request.session["uname"]
    ug_id = request.session["ug_id"] 
    uhos_id = request.session["uhos_id"]
    return render(request,"dr_cardiology.html",{"uname":uname,"ug_id":ug_id,"uhos_id":uhos_id})

def testtab(request):
    value = request.GET.get("value")
    print("hello")
    print(value)
    # ss = "select * from pt_book where date like '%"+str(value)+"%' or name like '%"+str(value)+"%' or patient_id like '%"+str(value)+"%'"
    if value == "":
        data3=""        
        return HttpResponse(json.dumps(data3),content_type="application/json")
    
    ss = "select `name`,`g_id` from addpat where name like '%"+str(value)+"%' or g_id like '%"+str(value)+"%' "
    c.execute(ss)
    print("hiiii")
    print(ss)
    print("hiiii")
    data3 =  c.fetchall()
    # data3="hello"
    print(data3)
    return HttpResponse(json.dumps(data3),content_type="application/json")

def dr_bookview(request):   
    dt=date.today()
    name = request.session["uname"]
    dr_id = request.session["ug_id"]
    hos_id = request.session["uhos_id"]
    s = "select img_files from adddoc where g_id='"+str(dr_id)+"'"
    c.execute(s)
    data1 =  c.fetchall()
    

    # if 'search_btn' in request.POST:
    value = request.GET.get("value")
    print("hello")
    print(value)
    # if value != "None":
    #     ss = "select * from pt_book where date like '%"+str(value)+"%' or name like '%"+str(value)+"%' or patient_id like '%"+str(value)+"%'"
    #     c.execute(ss)
    #     print("hiiii")
    #     print(ss)
    #     print("hiiii")
    #     data3 =  c.fetchall()
    #     print("hiiii")
    #     return HttpResponse(json.dumps(data3),content_type="application/json")
    #     #return HttpResponse(json.dumps(data3),content_type="application/json")
    #     # return HttpResponseRedirect("/dr_bookview",{"data3":data3})


    if 'delete_book' in request.POST:
        x = "delete from pt_book where date='"+str(dt)+"'"
        c.execute(x)
        conn.commit()

    
    t = "select * from pt_book where doctor_id='"+str(dr_id)+"' and date='"+str(dt)+"' and hospital_id='"+str(hos_id)+"' order by token"
    c.execute(t)
    data = c.fetchall()
    
    
    x = "select * from pt_book where doctor_id='"+str(dr_id)+"' and hospital_id='"+str(hos_id)+"' order by date "
    c.execute(x)
    data2 = c.fetchall()
    # print(data2)
    
    return render(request,"dr_book.html",{"uname":name,"ug_id":dr_id,"uhos_id":hos_id,"dt":str(dt),"data":data,"data1":data1,"data2":data2})

    

def dr_leaveview(request):
    msg=""
    dt = date.today()
    name = request.session["uname"]
    dr_id = request.session["ug_id"]
    hos_id = request.session["uhos_id"]
    s = "select img_files from adddoc where g_id='"+dr_id+"'"
    c.execute(s)
    data1 =  c.fetchall()
    l = "select * from dr_leave where dr_id = '"+dr_id+"'"
    c.execute(l)
    data = c.fetchall()
    if(request.POST):
        leave = request.POST.get("leave")
        # days = request.POST.get("days")
        date_from =  request.POST.get("date_from")
        date_to = request.POST.get("date_to")
        subject = request.POST.get("subject")
        reason = request.POST.get("reason")

        # s = "select sum(days) from dr_leave where dr_id='"+str(dr_id)+"'"
        # c.execute(s)
        # data = c.fetchone()
        # if(int(data[0])<=12):
        s = "insert into dr_leave(name,dr_id,`leave`,date_from,date_to,subject,reason,hos_id,status) values('"+str(name)+"','"+str(dr_id)+"','"+str(leave)+"','"+str(date_from)+"','"+str(date_to)+"','"+str(subject)+"','"+str(reason)+"','"+str(hos_id)+"','applied')"
        c.execute(s)
        conn.commit()
        

       
    return render(request,"dr_leave.html",{"uname":name,"ug_id":dr_id,"hos_id":hos_id,"data":data,"data1":data1,"dt":str(dt),"msg":msg})

def dr_suggestview(request):
    uname = request.session["uname"]
    ug_id = request.session["ug_id"] 
    uhos_id = request.session["uhos_id"]
    s = "select img_files from adddoc where g_id='"+ug_id+"'"
    c.execute(s)
    data1 =  c.fetchall()
    if(request.POST):
        name = request.POST.get("name")
        dr_id = request.POST.get("dr_id")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        s = "insert into dr_suggest values('"+str(name)+"','"+str(dr_id)+"','"+str(phone)+"','"+str(email)+"','"+str(subject)+"','"+str(message)+"')"
        c.execute(s)
        conn.commit()
    return render(request,"dr_suggest.html",{"uname":uname,"ug_id":ug_id,"uhos_id":uhos_id,"data1":data1})

def pt_suggestview(request):
    pt_id=""
    uname = request.session["uname"]
    g_id = request.session["ug_id"] 
    # uhos_id = request.session["uhos_id"]
    s = "select img from addpat where g_id='"+g_id+"'"
    c.execute(s)
    data1 =  c.fetchall()
    if(request.POST):
        name = request.POST.get("name")
        pt_id = request.POST.get("dr_id")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        s = "insert into pt_suggest(`name`,`pt_id`,`phone`,`email`,`subject`,`message`) values('"+str(name)+"','"+str(pt_id)+"','"+str(phone)+"','"+str(email)+"','"+str(subject)+"','"+str(message)+"')"
        c.execute(s)
        conn.commit()
    return render(request,"pt_suggest.html",{"uname":uname,"ug_id":pt_id,"data1":data1})

def dr_chatview(request):
    uname = request.session["uname"]
    ug_id = request.session["ug_id"] 
    uhos_id = request.session["uhos_id"]
    return render(request,"dr_chat.html",{"uname":uname,"ug_id":ug_id,"uhos_id":uhos_id})

def dr_prescribeview(request):

    # uname = request.session["uname"]
    ug_id = request.session["ug_id"] 
    uhos_id = request.session["uhos_id"]

    name=request.GET.get("name")
    pt_id = request.GET.get("pt_id")
    dt= request.GET.get("dt")

    request.session["name"] = name
    request.session["pt_id"] = pt_id 
    request.session["dt"] = dt

    a = "SELECT AUTO_INCREMENT FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'medifile' AND TABLE_NAME = 'dr_prescribe'"
    c.execute(a)
    p_id = c.fetchone()
    request.session["p_id"] = p_id[0]
    print(p_id)

    q = "select max(presc_id) from medicine"
    c.execute(q)
    last_medid = c.fetchone()
    print(last_medid[0])

    r = "select max(presc_id) from test"
    c.execute(r)
    last_testid = c.fetchone()
    print(last_testid[0])

    

    med =""
    test1 = ""
    d = "select disease,presc_id,date_from,status from dr_prescribe where pt_id='"+str(pt_id)+"'"
    # d = "select distinct * from medicine m join dr_prescribe p on (m.presc_id = p.presc_id) where p.pt_id='"+str(pt_id)+"' order by date_from desc"
    print(d)
    # d = "select * from dr_prescribe where pt_id='"+str(pt_id)+"' and dr_id='"+ug_id+"' and hos_id='"+uhos_id+"'"
    c.execute(d)
    data = c.fetchall()
    presc_id = request.GET.get("presc_id")
    print(data)
    d = "select * from medicine where presc_id='"+str(presc_id)+"'"
     
    
    if 'presc_add' in request.POST:

        if(str(p_id[0])==str(last_testid[0]) or str(p_id[0])==str(last_medid[0])):
            dr_id = request.POST.get("dr_id")
            date_from = request.POST.get("date_from")
            disease = request.POST.get("disease")
            status = request.POST.get("status")
            # med1 = request.POST.get("med1")
            # day1 = request.POST.get("day1")
            # test = request.POST.get("test")
            if disease != "":
                s = "insert into dr_prescribe(`name`,`pt_id`,`date_from`,`disease`,`status`,`dr_id`,`hos_id`) values('"+str(name)+"','"+str(pt_id)+"','"+str(date_from)+"','"+str(disease)+"','"+str(status)+"','"+str(ug_id)+"','"+str(uhos_id)+"')"
                c.execute(s)
                conn.commit()
                print(s)
            return render(request,"dr_prescribe.html",{"name":name,"ug_id":ug_id,"uhos_id":uhos_id,"pt_id":pt_id,"dt":dt,"data":data,"med":med,"test1":test1})
        else: 
            b = "insert into medicine(`presc_id`,`name`,`forenoon`,`afternoon`,`timing`,`review`) values('"+str(p_id[0])+"','No Medicine','none','none','none','none')"
            c.execute(b)
            conn.commit()
            t = "insert into test(`presc_id`,`test`,`results`) values('"+str(p_id[0])+"','No Test','None')"
            c.execute(t)
            conn.commit()
            dr_id = request.POST.get("dr_id")
            date_from = request.POST.get("date_from")
            disease = request.POST.get("disease")
            status = request.POST.get("status")
            # med1 = request.POST.get("med1")
            # day1 = request.POST.get("day1")
            # test = request.POST.get("test")
            if disease != "":
                s = "insert into dr_prescribe(`name`,`pt_id`,`date_from`,`disease`,`status`,`dr_id`,`hos_id`) values('"+str(name)+"','"+str(pt_id)+"','"+str(date_from)+"','"+str(disease)+"','"+str(status)+"','"+str(ug_id)+"','"+str(uhos_id)+"')"
                c.execute(s)
                conn.commit()
                print(s)
            return render(request,"dr_prescribe.html",{"name":name,"ug_id":ug_id,"uhos_id":uhos_id,"pt_id":pt_id,"dt":dt,"data":data,"med":med,"test1":test1})
    else:
        # if str(p_id[0])==str(last_medid[0]):
        print("megha")
        del1 = "delete from medicine where presc_id='"+str(p_id[0])+"'"
        c.execute(del1)
        conn.commit()

        # if (str(p_id[0])==str(last_testid[0])):
        del2 = "delete from test where presc_id='"+str(p_id[0])+"'"
        c.execute(del2)
        conn.commit()
    
        
    
    return render(request,"dr_prescribe.html",{"name":name,"ug_id":ug_id,"uhos_id":uhos_id,"pt_id":pt_id,"dt":dt,"data":data,"med":med,"test1":test1})
def st_emergencyview(request):

    if 'find' in request.POST:
        id=request.POST["id"]
        c.execute(" select * from addpat join relative on(relative.g_id=addpat.g_id) where addpat.g_id='"+str(id)+"'")
        d1=c.fetchall()
        
        return render(request,"st_emergency.html",{"data":d1}) 

    # os.startfile("C:\\Program Files (x86)\\BioEnable\\BioDesk\\BioDesk.exe")
    

    return render(request,"st_emergency.html")
   
def addmedicineview(request):
    p_id = request.session["p_id"]
    name = request.session["name"]
    pt_id = request.session["pt_id"]
    dt =  request.session["dt"]
    
    med_id = request.GET.get("med_id")
    print("med_id")
    #print(p)
    # p1=p.split(',')
    # p_id=p1[1]
    # med_id=p1[0]
    d = "delete from medicine where presc_id='"+p_id+"' and med_id='"+med_id+"'"
    print(d)
    c.execute(d)
    conn.commit()
    dd = "select name,timing,review,med_id from medicine where presc_id='"+str(p_id)+"'"
    c.execute(dd)
    data = c.fetchall()
    print(data)

    t = request.GET.get("t_id")
    print(t)
    # p1=t.split(',')
    # tp_id=p1[1]
    # test_id=p1[0]
    # print(test_id)
    # t = "delete from test where presc_id='"+tp_id+"' and test_id='"+test_id+"'"
    # print(t)
    # c.execute(t)
    # conn.commit()

    r = "select * from test where presc_id='"+str(p_id)+"'"
    c.execute(r)
    test1 = c.fetchall()
    print(test1)
        

    # if 'med_add' in request.POST:
    #     medicine = request.POST.get("medicine")
    #     fnoon = request.POST.get("fnoon")
    #     anoon = request.POST.get("anoon")
    #     timing = request.POST.get("timing")
    #     review = request.POST.get("review")
    #     b = "insert into medicine(`presc_id`,`name`,`forenoon`,`afternoon`,`timing`,`review`) values('"+str(p_id+1)+"','"+str(medicine)+"','"+str(fnoon)+"','"+str(anoon)+"','"+str(timing)+"','"+str(review)+"')"
    #     c.execute(b)
    #     print(b)
    #     conn.commit()
    #     return HttpResponseRedirect("/dr_prescribeview?name="+name+"&pt_id="+pt_id+"&dt="+dt)
    # return render(request,"dr_prescribe.html")   
    return HttpResponse(json.dumps(data),content_type="application/json")
        

def med_addview(request):
    p_id = request.session["p_id"]
    print(p_id)

    med_name = request.GET.get("med_name")
    fnoon = request.GET.get("fnoon")
    anoon = request.GET.get("anoon")
    med_timing = request.GET.get("med_timing")
    med_review = request.GET.get("med_review")
    b = "insert into medicine(`presc_id`,`name`,`forenoon`,`afternoon`,`timing`,`review`) values('"+str(p_id)+"','"+str(med_name)+"','"+str(fnoon)+"','"+str(anoon)+"','"+str(med_timing)+"','"+str(med_review)+"')"
    c.execute(b)
    conn.commit()
    aa = "select name,timing,review,med_id from medicine where presc_id='"+str(p_id)+"'"
    c.execute(aa)
    med_data = c.fetchall()
    print(med_data)
    # return HttpResponseRedirect("/dr_prescribeview?name="+name+"&pt_id="+pt_id+"&dt="+dt)   
    return HttpResponse(json.dumps(med_data),content_type="application/json")

def test_addview(request):
    p_id = request.session["p_id"]
    test_add = request.GET.get("test_name")
    results = ""
    t = "insert into test(`presc_id`,`test`,`results`) values('"+str(p_id)+"','"+str(test_add)+"','"+str(results)+"')"
    c.execute(t)
    conn.commit()
    r = "select * from test where presc_id='"+str(p_id)+"'"
    c.execute(r)
    test1 = c.fetchall()
    print(test1)
    return HttpResponse(json.dumps(test1),content_type="application/json")

def result_addview(request):
    p_id = request.session["presc_id"]
    test_id = request.GET.get("data_id")
    print(test_id)
    result_name = request.GET.get("data")
    print('image path',result_name)
    myfile = request.FILES["test_add"]
    fs = FileSystemStorage()        
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)
    t = "update test set results='"+str(filename)+"' where test_id='"+str(test_id)+"'"
    c.execute(t)
    conn.commit()
    r = "select test,results from test where presc_id='"+str(p_id)+"'"
    c.execute(r)
    test1 = c.fetchall()
    print(test1)
    return HttpResponse(json.dumps(test1),content_type="application/json")

def resultdeleteview(request):
    print('hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
    p_id = request.session["presc_id"]
    test_id = request.GET.get("test_id")
    print("hello     ")
    # result_name = request.GET.get("data")
    results=""
   
    t = "update test set results='"+str(results)+"' where presc_id='"+str(p_id)+"' and test_id='"+str(test_id)+"'"
    print(t)
    c.execute(t)
    conn.commit()
    aa = "select name, timing,review from medicine where presc_id = '"+str(p_id)+"'"
    c.execute(aa)
    data3=c.fetchall()
    print(data3)

    bb = "select test,results,test_id from test where presc_id = '"+str(p_id)+"'"
    c.execute(bb)
    data4=c.fetchall()
    print(data4)

    data5 = [data3,data4]
    # print(test1)s
    # return render(request,"dr_prescribe.html")
    return HttpResponse(json.dumps(data5),content_type="application/json")
    

def testdeleteview(request):
    t = request.GET.get("t_id")
    print(t)
    p1=t.split(',')
    tp_id=p1[1]
    test_id=p1[0]
    print(test_id)
    t = "delete from test where presc_id='"+tp_id+"' and test_id='"+test_id+"'"
    print(t)
    c.execute(t)
    conn.commit()
    return render(request,"dr_prescribe.html")

def diseaseview(request):
    # name = request.session["name"]
    # pt_id = request.session["pt_id"]
    presc_id = request.GET.get("data_id")
    request.session["presc_id"]= presc_id
    print(presc_id)
    aa = "select name, timing,review from medicine where presc_id = '"+str(presc_id)+"'"
    c.execute(aa)
    data3=c.fetchall()
    print(data3)

    bb = "select test,results,test_id from test where presc_id = '"+str(presc_id)+"'"
    c.execute(bb)
    data4=c.fetchall()
    print(data4)

    data5 = [data3,data4]
    return HttpResponse(json.dumps(data5),content_type="application/json")


def pt_diseaseview(request):
    # name = request.session["uname"]
    # pt_id = request.session["g_id"]
    presc_id = request.GET.get("data_id")
    print(presc_id)
    aa = "select name, timing,review from medicine where presc_id = '"+str(presc_id)+"'"
    c.execute(aa)
    data3=c.fetchall()
    print(data3)

    bb = "select test,results from test where presc_id = '"+str(presc_id)+"'"
    c.execute(bb)
    data4=c.fetchall()
    print(data4)

    data5 = [data3,data4]
    return HttpResponse(json.dumps(data5),content_type="application/json")

# Patient Page Section
# ====================
def pt_tempview(request):
    return render(request,"pt_temp.html")

def pt_homeview(request):
    g_id = request.session["ug_id"]
    uname = request.session["uname"]
    s = "select img from addpat where g_id='"+g_id+"'"
    c.execute(s)
    data = c.fetchall()
    return render(request,"pt_home.html",{"data":data,"ug_id":g_id,"uname":uname})

def pt_contactview(request):
    ug_id = request.session["ug_id"]
    uname = request.session["uname"]
    s = "select img from addpat where g_id='"+ug_id+"'"
    c.execute(s)
    data = c.fetchall()
    if(request.POST):
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        designation = "patient"
        s = "insert into pt_contact values('"+str(uname)+"','"+str(ug_id)+"','"+str(email)+"','"+str(phone)+"','"+str(subject)+"','"+str(message)+"','"+str(designation)+"')"
        c.execute(s)
        conn.commit()
    return render(request,"pt_contact.html",{"data":data,"ug_id":ug_id,"uname":uname})

def st_contactview(request):
    ug_id = request.session["ug_id"]
    uname = request.session["uname"]
    # s = "select img from addpat where g_id='"+ug_id+"'"
    # c.execute(s)
    # data = c.fetchall()
    if(request.POST):
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        designation = "patient"
        s = "insert into pt_contact values('"+str(uname)+"','"+str(ug_id)+"','"+str(email)+"','"+str(phone)+"','"+str(subject)+"','"+str(message)+"','"+str(designation)+"')"
        c.execute(s)
        conn.commit()
    return render(request,"pt_contact.html",{"ug_id":ug_id,"uname":uname})

def pt_bookview(request):
    ug_id = request.session["ug_id"]
    uname = request.session["uname"]
    alert1 = ""
    dt = date.today()
    
    b = "select d.hos_name,d.name,pb.date,pb.token  from adddoc d join pt_book pb on (pb.doctor_id = d.g_id) join addpat p on (pb.patient_id = p.g_id) where p.g_id= '"+ug_id+"'"
    c.execute(b)
    data1 = c.fetchall()
    

    a = "select img from addpat where g_id='"+ug_id+"'"
    c.execute(a)
    data = c.fetchall()

    s = "select distinct dptname from adddpt"
    c.execute(s)
    dpt = c.fetchall()
    if(request.POST):
        token1 = request.POST.get("token1")
        department = request.POST.get("department")
        doctor = request.POST.get("doctor")
        hospital = request.POST.get("hospital")
        patient = request.POST.get("patient")
        date1 = request.POST.get("date")
        name = request.POST.get("name")
        pt_id = request.POST.get("pt_id")
        phone = request.POST.get("phone")
        cnt = "select count(*),token from pt_book where patient_id='"+ug_id+"' AND doctor_id='"+doctor+"' AND hospital_id='"+hospital+"' AND date='"+date1+"'"
        c.execute(cnt)
        count1 = c.fetchone()
        if(count1[0]==0):
        # if(token1.isdigit()):
            s = "insert into pt_book(`curr_dt`,`department`,`doctor_id`,`hospital_id`,`patient`,`date`,`name`,`patient_id`,`phone`,`token`) values('"+str(dt)+"','"+str(department)+"','"+str(doctor)+"','"+str(hospital)+"','"+str(patient)+"','"+str(date1)+"','"+str(uname)+"','"+str(ug_id)+"','"+str(phone)+"','"+str(token1)+"')"
            c.execute(s)
            conn.commit()
            msg="Booking is successfull.\n Token no :"+token1+"\n Date : "+date1+"."
            # sendsms(phone,msg)
            return render(request,"pt_book.html",{"data1":data1})
        else:
            alert1 = "Already booked on "+date1+" Your token no is :"+count1[1]
    return render(request,"pt_book.html",{"data":data,"dpt":dpt,"ug_id":ug_id,"uname":uname,"alert1":alert1,"data1":data1,"dt":str(dt)})

def subhosview(request):
  sublist=[]
  catid=request.GET.get("dataid")
  c.execute("select hos_id,hos_name from adddpt where dptname='"+ str(catid)+"'")
  data2=c.fetchall()
  
#   for d in data2:
#     sublist.append(d[0])
  return HttpResponse(json.dumps(data2),content_type="application/json")

def subdocview(request):
  sublist=[]
  catid=request.GET.get("dataid")
  dptname=request.GET.get("depid")
#   s = "select g_id from register where g_id='"+str(catid)+"'"
#   c.execute(s)
#   data = c.fetchall()
#   a = data[0][0]
#   print(a)
  d = "select g_id,name from adddoc where hos_id='"+str(catid)+"'  and department='"+dptname+"'"
  print(d)
  c.execute(d)
  data2=c.fetchall()
  
#   for d in data2:
#     sublist.append(d[0])
  return HttpResponse(json.dumps(data2),content_type="application/json")

def token_detail(request):
    doctor=request.GET.get("dataid")
    date=request.GET.get("date")
    ug_id = request.session["ug_id"]
    s = "select count(*) from pt_book where doctor_id='"+doctor+"' and date='"+date+"' AND patient_id<>'"+ug_id+"'"
    print(s)
    c.execute(s)
    data = c.fetchone()
    if(data[0]>=5):
        alert="No Tokens available."
    else:
        alert = str(int(data[0]+1))
    return HttpResponse(json.dumps(alert),content_type="application/json")

def pt_prescribeview(request):
    g_id = request.session["ug_id"]
    uname = request.session["uname"]
    s = "select img from addpat where g_id='"+g_id+"'"
    c.execute(s)
    data = c.fetchall()
    med =""
    test1 = ""
    d = "select disease,presc_id,date_from,status from dr_prescribe where pt_id='"+str(g_id)+"'"
    # d = "select distinct * from medicine m join dr_prescribe p on (m.presc_id = p.presc_id) where p.pt_id='"+str(pt_id)+"' order by date_from desc"
    print(d)
    # d = "select * from dr_prescribe where pt_id='"+str(pt_id)+"' and dr_id='"+ug_id+"' and hos_id='"+uhos_id+"'"
    c.execute(d)
    data1 = c.fetchall()
    # presc_id = request.GET.get("presc_id")
    print(data1)
    return render(request,"pt_prescribe.html",{"data":data,"ug_id":g_id,"uname":uname,"data1":data1})

def pt_detailview(request):
    g_id = request.session["ug_id"]
    uname = request.session["uname"]
    s = "select * from addpat where g_id='"+str(g_id)+"'"
    c.execute(s)
    pic = c.fetchall()
    print(pic)
    detail = (uname,g_id)
    
    return render(request,'pt_detail.html',{"detail":detail,"pic":pic})
# Staff Portion
#==============

def st_tempview(request):
    return render(request,"st_temp.html")

def st_homeview(request):
    ug_id = request.session["ug_id"]
    uname = request.session["uname"]
    s = "select img_files from addstaff where g_id= '"+str(ug_id)+"'"
    c.execute(s)
    data = c.fetchall()
    return render(request,"st_home.html",{"data":data,"ug_id":ug_id,"uname":uname})

def st_leaveview(request):
    msg=""
    ug_id = request.session["ug_id"]
    uname = request.session["uname"]
    designation = request.session["desig"]
    hos_id =  request.session["uhos_id"]
    s = "select img_files from addstaff where g_id='"+str(ug_id)+"' and designation='"+str(designation)+"'"
    c.execute(s)
    data = c.fetchall()
    st = "select * from st_leave where st_id='"+str(ug_id)+"'"
    c.execute(st)
    data1 = c.fetchall()
    if(request.POST):
        leave = request.POST.get("leave")
        days = request.POST.get("days")
        date_from =  request.POST.get("date_from")
        date_to = request.POST.get("date_to")
        subject = request.POST.get("subject")
        reason = request.POST.get("reason")
        s = "select sum(days) from st_leave where st_id='"+str(ug_id)+"'"
        c.execute(s)
        data = c.fetchone()
        # if(int(data[0])<=12):
        d = "insert into st_leave(`name`,`st_id`,`leave`,`days`,`date_from`,`date_to`,`subject`,`reason`,`hos_id`,`designation`,`status`) values('"+str(uname)+"','"+str(ug_id)+"','"+str(leave)+"','"+str(days)+"','"+str(date_from)+"','"+str(date_to)+"','"+str(subject)+"','"+str(reason)+"','"+str(hos_id)+"','"+str(designation)+"','applied')"
        c.execute(d)
        conn.commit()
        # else:
        #     msg="SORRY YOU HAVE ALREADY TAKEN YOUR FULL ANNUAL LEAVE"
    return render(request,"st_leave.html",{"data":data,"data1":data1,"ug_id":ug_id,"uname":uname,"msg":msg})

def st_resultview(request):
    dt = date.today()
    print(dt)
    name = request.GET.get("name")
    pt_id = request.GET.get("pt_id")
    request.session["name"] = name 
    request.session["pt_d"] = pt_id 

    d = "select disease,presc_id,date_from,status from dr_prescribe where pt_id='"+str(pt_id)+"'"
    # d = "select distinct * from medicine m join dr_prescribe p on (m.presc_id = p.presc_id) where p.pt_id='"+str(pt_id)+"' order by date_from desc"
    print(d)
    # d = "select * from dr_prescribe where pt_id='"+str(pt_id)+"' and dr_id='"+ug_id+"' and hos_id='"+uhos_id+"'"
    c.execute(d)
    data = c.fetchall()
    return render(request,"st_result.html",{"data":data,"name":name,"pt_id":pt_id})

def st_prescribeview(request):
    dt = date.today()
    print(dt)

    return render(request,"st_prescribe.html",{"dt":str(dt)})

def st_addview(request):
    test_id = request.GET.get("test_id")
    pt_id = request.GET.get("pt_id")
    name = request.session["name"]

    s= "select * from test where test_id='"+str(test_id)+"'"
    c.execute(s)
    data1 = c.fetchall()
    print(data1)
    msg = ""
    if 'test_submit' in request.POST:
        test_result = request.POST.get("test_result")
        myfile = request.FILES["test_result"]
        fs = FileSystemStorage()        
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        ss = "update test set results='"+str(filename)+"' where test_id='"+str(test_id)+"'"
        c.execute(ss)
        conn.commit()
        msg = "  FILE Uploaded   "
        return HttpResponseRedirect("/st_resultview?name="+str(name)+"&pt_id="+str(pt_id)+"")
    if 'test_delete' in request.POST:
        res=""
        aa = "update test set results='"+str(res)+"' where test_id='"+str(test_id)+"'"       
        c.execute(aa)
        conn.commit()
        return HttpResponseRedirect("/st_resultview?name="+str(name)+"&pt_id="+str(pt_id)+"")
        # return HttpResponseRedirect("/st_addview?=test_id="+str(test_id)+"&pt_id="+str(pt_id)+"&data1.0.2=data1[3]")
    return render(request,"st_add.html",{"pt_id":pt_id,"data1":data1,"msg":msg})


def emergencyview(request):
    # os.startfile("C:\Program Files (x86)\BioEnable\BioDesk\BioDesk.exe")
    if(request.POST):
        os.startfile("C:\Program Files (x86)\BioEnable\BioDesk\BioDesk.exe")
        file1 = open("C:\t.txt","r+")  
        data=file1.read()
        ss="select * from addpat where g_id='"+data+"'"     
        c.execute(ss)
        d=c.fetchall()

    return render(request,"st_home.html",{"data":d})

def st_bookview(request):
    alert1=""
    ug_id = request.session["ug_id"]
    uname = request.session["uname"]
    s = "select distinct dptname from adddpt"
    c.execute(s)
    dpt = c.fetchall()
    dt = date.today()
    
    b = "select d.hos_name,d.name,pb.date,pb.token  from adddoc d join pt_book pb on (pb.doctor_id = d.g_id) join addpat p on (pb.patient_id = p.g_id) where p.g_id= '"+ug_id+"'"
    c.execute(b)
    data1 = c.fetchall()
    
    if(request.POST):
        token1 = request.POST.get("token1")
        department = request.POST.get("department")
        doctor = request.POST.get("doctor")
        hospital = request.POST.get("hospital")
        patient = request.POST.get("patient")
        date1 = request.POST.get("date")
        name = request.POST.get("name")
        pt_id = request.POST.get("pt_id")
        phone = request.POST.get("phone")
        cnt = "select count(*),token from pt_book where patient_id='"+ug_id+"' AND doctor_id='"+doctor+"' AND hospital_id='"+hospital+"' AND date='"+date1+"'"
        c.execute(cnt)
        count1 = c.fetchone()
        if(count1[0]==0):
        # if(token1.isdigit()):
            s = "insert into pt_book(`curr_dt`,`department`,`doctor_id`,`hospital_id`,`patient`,`date`,`name`,`patient_id`,`phone`,`token`) values('"+str(dt)+"','"+str(department)+"','"+str(doctor)+"','"+str(hospital)+"','"+str(patient)+"','"+str(date1)+"','"+str(uname)+"','"+str(ug_id)+"','"+str(phone)+"','"+str(token1)+"')"
            c.execute(s)
            conn.commit()
            msg="Booking is successfull.\n Token no :"+token1+"\n Date : "+date1+"."
            # sendsms(phone,msg)
            return render(request,"pt_book.html",{"data1":data1})
        else:
            alert1 = "Already booked on "+date1+" Your token no is :"+count1[1]
    # return render(request,"pt_book.html",{"data":data,"dpt":dpt,"ug_id":ug_id,"uname":uname,"alert1":alert1,"data1":data1,"dt":str(dt)})
    return render(request,"st_book.html",{"dpt":dpt,"ug_id":ug_id,"uname":uname,"alert1":alert1,"data1":data1})

# Logout Session
# ==============
def logoutview(request):
    for key in list(request.session.keys()):
        del request.session[key]
    return render(request,"user_logout.html")
    