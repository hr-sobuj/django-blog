from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib import messages
from App_Login.forms import UserRegistrationForm,UserProfileUpdate
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from App_Login.forms import AddProfileForm
from django.urls import reverse_lazy

# Create your views here.
def Registration(request):
    registration_form=UserRegistrationForm()
    if request.method=="POST":
        registration_form=UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            messages.success(request, "The Subscriber has been successfully added")
            return HttpResponseRedirect(reverse('App_Blog:blog_list' ))
            
    else:
        messages.error(request, "Sorry the data has not been entered to the database")
    dict={'registration_form':registration_form}
    return render(request, 'App_Login/registration.html', context=dict)
    
def LoginView(request):
    form=AuthenticationForm()
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('App_Login:profile' ))
    dict={"form":form}
    return render(request, 'App_Login/login.html', context=dict)

def ProfileView(request):
    if request.user.is_authenticated:
        dict={}
        return render(request, 'App_Login/profile.html', context=dict)
    else:
       return HttpResponseRedirect(reverse('index' )) 

def LogoutView(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(reverse('index' ))
    else:
        return HttpResponseRedirect(reverse('App_Login:login' )) 

def UpdateProfileView(request):
    if request.user.is_authenticated:
        form=UserProfileUpdate(instance=request.user)
        if request.method=="POST":
            form=UserProfileUpdate(request.POST,instance=request.user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('App_Login:profile', ))
                
        dict={"form":form}
        return render(request, 'App_Login/update.html', context=dict)
    else:
        return HttpResponseRedirect(reverse('App_Login:login' )) 
def ChangePassword(request):
    current_user = request.user
    flag=False 
    if request.user.is_authenticated:
        form=PasswordChangeForm(current_user)
        if request.method=="POST":
            form=PasswordChangeForm(current_user, data=request.POST)
            # print("xxxxxxxx")
            if form.is_valid():
                form.save()
                # print("TRUE")
                flag=True
                return HttpResponseRedirect(reverse_lazy('App_Login:login', ))
                
        dict={"form":form,"flag":flag}
        return render(request, 'App_Login/change_password.html', context=dict)
    else:
        return HttpResponseRedirect(reverse('App_Login:login' ))

def AddProfilePicView(request):
    current_user=request.user
    form = AddProfileForm()
    if request.method=='POST':
        form=AddProfileForm(request.POST,request.FILES)
        if form.is_valid():
            user_obj=form.save(commit=False)
            user_obj.user=current_user
            user_obj.save()
            return HttpResponseRedirect(reverse('App_Login:profile' ))

    dict={"form":form}
    return render(request, "App_Login/pro_pic.html", context=dict)
    
def UpdataProfilePicView(request):
    current_user=request.user
    form=AddProfileForm(instance=current_user.user_profile)
    if request.method=="POST":
        form=AddProfileForm(request.POST,request.FILES,instance=current_user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile' ))
    dict={"form":form}
    return render(request, "App_Login/pro_pic.html", context=dict)
    