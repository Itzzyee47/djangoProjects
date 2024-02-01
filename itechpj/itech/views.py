from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from .models import *
from django.http import JsonResponse
from .forms import *
from django.views.generic.edit import CreateView, DeleteView, UpdateView


# Create your views here.

# The registreation page for new users.......
def index(request):
    template = 'index.html'
    form = regForm(request.POST or None)
    context = {'form': form}
    if request.method == "POST":
        un = request.POST['user_name']
        ue = request.POST['email']
        up = request.POST['password']
        ucp = request.POST['confrim_password']
        if up == ucp:
            if  User.objects.filter(username=un).exists():
                context = {'message':'user '+un+' already exist try loging in',
                           'form': form,
                           }
                return render(request,template,context)
            else:
                user = User.objects.create_user(username=un, email=ue, password=up)
                user.set_password(up)
                user.save()
                return redirect('login')
        else:
            context = {'message':'Passwords do not match',
                           'form': form,
                           }
            return render(request,template,context)
        
    return render(request,template,context)


# the login view for registered users to login to their accounts.......
def login(request):
    form = logForm(request.POST or None)
    context = {'form': form}
    
    if request.method == "POST":
        if form.is_valid():
            un = request.POST['user_name']                                                                                                                                                                              
            up = request.POST['password']
            us = User.objects.filter(username=un).exists()
            if us == True:
                user = auth.authenticate(request, username=un, password=up)
                if user is not None:
                    auth.login(request,user)
                    return redirect('home')
                else:
                     context = {'message': 'user name or password is incorrect '+un, 'form': form}
            else:
                context = {'message': 'no account found by name '+un, 'form': form}
    
    return render(request,'login.html',context)

# the view for the home page after login or signup/register......
@login_required(login_url = "/login")   #redirects unauthorised users...
def home(request):
    
    ur = request.user
    Udetails = ur_details.objects.get(user=ur)
    posts = post.objects.all().order_by('-date')
    context = {'details':Udetails, 'posts':posts}
    
    return render(request,'home.html',context)

#logs a user out and send them to the login page..
def logout(request):
    auth.logout(request)
    
    return redirect('login')

@login_required(login_url = "/login")   #redirects unauthorised users...
def Apost(request):
    
    ur = request.user
    Udetails = ur_details.objects.get(user=ur)
    form = postForm(request.POST, request.FILES)
    context = {'form':form,'details':Udetails}
    if request.method == 'POST' or 'pic' in request.FILES:
            if form.is_valid:
                P = post.objects.create(
                aurthor=request.user,
                title=request.POST['title'],
                pic=request.FILES.get('pic')
                )
                P.save()
                return redirect('home')
            else:
                context = {'form':form,'details':Udetails, 'message':"error posting update"}
            
    return render(request,'Apost.html',context)

@login_required
def like_post(request, id):
    ur = request.user
    p = post.objects.get(id=id)
    l, created = like.objects.get_or_create(user=ur, post=p)
    if not created:
        l.delete()
    return JsonResponse({'likes_count': l.count() })


@login_required
def add_comment(request, id):
    p = post.objects.get(id=id)
    content = request.POST.get('content')
    if content != " ":
        comment.objects.create(user=request.user, post=p, content=content)
    return redirect(view_post, id)

@login_required
def view_post(request, pk):
    p = post.objects.get(id=pk)
    ur = request.user
    Udetails = ur_details.objects.get(user=ur)
    comments = comment.objects.filter(post=pk).order_by('-created_at')
    cCount = comments.count()
    context = {'comment':comments, 'post':p, 'details':Udetails}
    content = request.POST.get('content')
    if content:
        comment.objects.create(user=request.user, post=p, content=content)
        return redirect(view_post, pk)
    else:
        pass
    
    return render(request, 'viewpost.html', context)


@login_required(login_url = "/login")   #redirects unauthorised users...
def profile(request):
    
    ur = request.user
    Udetails = ur_details.objects.get(user=ur)
    posts = post.objects.filter(aurthor=ur).order_by('-date')
    pL = len(posts)
    content = request.POST.get('content')
    if content:
        i = request.POST.get('id')
        p = post.objects.get(id=i)
        comment.objects.create(user=ur, post=p, content=content)
    context = {'details':Udetails, 'posts':posts, 'nPost':pL}
    
    return render(request,'profile.html',context)

            
@login_required(login_url = "/login")
def editprofile(request):
    ur = request.user
    Udetails = ur_details.objects.get(user=ur)
    U = User.objects.get(username=ur)
    form = eProfile(instance=U)    
    if request.method == 'POST':
        form = eProfile(request.POST, instance=U)
        
        if form.is_valid():
            form.save()
            return redirect(profile)
    else:
        form = eProfile(instance=U)
    
        return render(request, 'editprofile.html', context={'form': form, 'details': Udetails})
    
@login_required(login_url = "/login")
def editprofileD(request):
    ur = request.user
    Udetails = ur_details.objects.get(user=ur)
    form = eProfileD(instance=Udetails)    
    if request.method == 'POST':
        form = eProfileD(request.POST, instance=Udetails)
        
        if form.is_valid():
            form.save()
            return redirect(profile)
    else:
        form = eProfileD(instance=Udetails)
    
        return render(request, 'editprofile.html', context={'form': form, 'details': Udetails})
    
    