from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *


def index(request):
    request.session.clear()
    return render(request, "logreg/index.html")

def success(request):
    if ('user' in request.session):
        context = {
            'all_messages': Message.objects.all()
        }
        return render(request, "logreg/success.html", context)
    else:
        return redirect('/')

def register(request):
    if request.method == 'POST':
        if (request.POST['password'] == request.POST['confirm_password']):
            errors = User.objects.basic_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/')
            new_user = User.objects.create(name=request.POST['name'], password=request.POST['password'])
            request.session['user'] = new_user.name
    
            return redirect('/success')
        else:
            return redirect('/')
    else: 
        return HttpResponse("Confirm Password and Password do not match")

def login(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        logged_user = User.objects.filter(name=request.POST['name'])
        print(logged_user)
        if(logged_user):
            if(logged_user[0].password == request.POST['password']):
                request.session['user'] = logged_user[0].name
                return redirect('/success')
        else:
            return redirect('/')

def add_message(request):
    if request.method == 'POST':
        posted = User.objects.get(name = request.session['user'])
        Message.objects.create(message=request.POST['message'], poster=posted)
        print("Message created!")
        return redirect('/success')

def like(request, id):
    liked_message = Message.objects.get(id=id)
    user = User.objects.get(name = request.session['user'])
    liked_message.user_who_liked.add(user)
    return redirect('/success')
