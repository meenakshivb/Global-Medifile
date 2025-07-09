from urllib import request

from django.http import (HttpResponse,HttpResponseRedirect)
from django.shortcuts import render

import MySQLdb


#create db 

conn=MySQLdb.connect("localhost","root","","medifile")
c = conn.cursor()

# Create your views here.

def dashview(request):
    h = "select count(*) from register"
    c.execute(h)
    data1 = c.fetchone()
    hos_count = data1[0]

    p = "select count(*) from addpat"
    c.execute(p)
    data2 = c.fetchone()
    patient_count = data2[0]

    f = "select count(*) from pt_contact"
    c.execute(f)
    data3 = c.fetchone()
    feed_count = data3[0]
    return render(request,"dashioadmin.html",{"data1":hos_count,"data2":patient_count,"data3":feed_count})

def dhomeview(request):
    return render(request,"dhome.html")

def mailview(request):
    return render(request,"mail.html")

def eventsview(request):
    return render(request,"events.html")

def mailcomposeview(request):
    return render(request,"mail_compose.html")

def loginview(request):
    alert = ""
    if(request.POST):
        name = request.POST.get("name")
        password =request.POST.get("password")
        if(name == "admin" and password == "admin123"):
            return HttpResponseRedirect("/dashview")
        else:
            alert ="Inavid User or Password"
    return render(request,"login.html",{"alert":alert})

def hlistview(request):
    if "msg" in request.GET:
        msg=request.GET["msg"]
    else:
        msg=""
    d = "select * from register"
    c.execute(d)
    conn.commit()
    data =  c.fetchall()
    return render(request,"hlist.html",{"data":data,"msg":msg})
def hlistapproved(request):
    if "msg" in request.GET:
        msg=request.GET["msg"]
    else:
        msg=""
    d = "select * from register where g_id in(select g_id from login where status='Approved')"
    c.execute(d)
    conn.commit()
    data =  c.fetchall()
    return render(request,"hlistapproved.html",{"data":data,"msg":msg})
def approve(request):
    g_id=request.GET["g_id"]
    d = "update login set status='Approved' where g_id='"+str(g_id)+"'"
    print(d)
    c.execute(d)
    conn.commit()
    return HttpResponseRedirect("/hlistview?msg='Approved'")
def hremoveview(request):
    g_id = request.GET.get("g_id")
    print(g_id)
    a = "delete from register where g_id='"+g_id+"'"
    c.execute(a)
    
    b = "delete from adddoc where hos_id='"+g_id+"'"
    c.execute(b)

    d = "delete from adddpt where hos_id='"+g_id+"'"
    c.execute(d)

    return HttpResponseRedirect("/hlistview")

def plistview(request):
    s =  "select * from addpat"
    c.execute(s)
    conn.commit()
    data = c.fetchall()
    return render(request,"plist.html",{"data":data})

def drlistview(request):
    s = "select * from adddoc"
    c.execute(s)
    data = c.fetchall()
    return render(request,"drlist.html",{"data":data})

def stlistview(request):
    s = "select * from addstaff"
    c.execute(s)
    data = c.fetchall()
    return render(request,"stlist.html",{"data":data})
    
def dptlistview(request):
    # hos_id = request.session["ug_id"]
    s =  "select * from adddpt"
    c.execute(s)
    data = c.fetchall()
    return render(request,"dptlist.html",{"data":data})

def hrequestview(request):
    return render(request,"hrequest.html")

def prequestview(request):
    return render(request,"prequest.html")

def arequestview(request):
    return render(request,"arequest.html")

def medi_listview(request):
    return render(request,"medi_list.html")

def medi_newview(request):
    return render(request,"medi_new.html")
    
def contactview(request):
    s = "select * from pt_contact"
    c.execute(s)
    conn.commit()
    data = c.fetchall()
    return render(request,"contact.html",{"data":data})

def admin_logoutview(request):
    for key in list(request.session.keys()):
        del request.session[key]
    return render(request,"user_logout.html")