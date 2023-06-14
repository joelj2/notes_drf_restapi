from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from note.models import Note,Register,Login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from note.serializers import noteserializers
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.

@api_view(['GET'])
def getlist(request):
    list=Note.objects.all()
    serializer=noteserializers(list, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postlist(request):
    serializer=noteserializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
@api_view(['GET'])
def single_list(request,pk):
    list=Note.objects.get(pk=pk)
    serializer=noteserializers(list, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def updatelist(request,pk):
    list=Note.objects.get(pk=pk)
    serializer=noteserializers(instance=list, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deletelist(request,pk):
    list=Note.objects.get(pk=pk)
    list.delete()
    return Response('Item successfully deleted')
   

def createnote(request):
    if request.method=='POST':
        no=Note()
        no.title=request.POST.get('title')
        no.content=request.POST.get('content')
        no.save()
    return render(request,'note/create.html')

def viewnote(request):
    uid=request.session['u_id']
    ob=Note.objects.filter(pk=uid)
    context={
        'x':ob
    }
    return render(request,'note/view.html',context)

def editnote(request,id):
    ob=Note.objects.get(pk=id)
    context={
        'x':ob
    }
    if request.method=='POST':
        ob=Note.objects.get(pk=id)
        ob.title=request.POST.get('title')
        ob.content=request.POST.get('content')
        ob.save()
        return viewnote(request)
    return render(request,'note/edit.html',context)

def delete(request,id):
    obj=Note.objects.get(pk=id)
    obj.delete()
    return viewnote(request)


def register(request):
    if request.method=="POST":
        obj=Register()
        obj.name=request.POST.get('name')
        obj.email=request.POST.get('email')
        obj.mobile=request.POST.get('mobile')
        obj.password=request.POST.get('password')
        obj.save()
        messages.success(request,("Account created successfully"))

        ob=Login()
        ob.name=obj.name
        ob.password=obj.password
        ob.u_id=obj.register_id
        ob.type='user'
        ob.save()
    return render(request,'note/register.html')


def login(request):
    if request.method=="POST":
        name=request.POST.get('name')
        password=request.POST.get('password')
        ob=Login.objects.filter(username=name,password=password)
        tp=''
        for obj in ob:
            tp=obj.type
            uid=obj.u_id
            if tp == 'user':
                request.session["u_id"] = uid
                return redirect('create')
            
        else:
            messages.error(request,("The Username or Password was not found"))
            return redirect('login')
    else:
        return render(request,'note/login.html')
    