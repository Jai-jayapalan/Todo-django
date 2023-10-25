from django.shortcuts import render, redirect
from .models import Datas

# Create your views here.
def home(req):
    myData = Datas.objects.all()
    if(myData!=''):
        return render(req,'curd.html',{'datas':myData})
    else:
        return render(req, "curd.html")
def addData(req):
    if req.method=='POST':
        name = req.POST['u_name']
        age = req.POST['u_age']
        address = req.POST['u_add']
        contact = req.POST['u_phone']
        mail = req.POST['u_mail']

        obj = Datas()
        obj.Name = name
        obj.Age=age
        obj.Address=address
        obj.Contact=contact
        obj.Mail=mail
        obj.save()
        #retrive data
        mydata = Datas.objects.all()
        return redirect('home')
    return render(req,"curd.html")

def updateData(req, id):
    uniqueId = Datas.objects.get(id=id)
    if req.method=='POST':
        name = req.POST['u_name']
        age = req.POST['u_age']
        address = req.POST['u_add']
        contact = req.POST['u_phone']
        mail = req.POST['u_mail']

        uniqueId.Name = name
        uniqueId.Age = age
        uniqueId.Address =address
        uniqueId.Contact = contact
        uniqueId.Mail = mail
        uniqueId.save()
        return redirect('home')
    return render(req,"update.html",{'data':uniqueId})

def deleteData(req,id):
    deleData = Datas.objects.get(id=id)
    deleData.delete()
    return redirect('home')