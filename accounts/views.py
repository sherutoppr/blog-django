from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages           # to sent message that generate in any view like warning, success
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm , UserUpdateForm ,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):

    if request.method == 'POST':
         form = UserRegisterForm(request.POST)
         if form.is_valid():
             form.save()
             username = form.cleaned_data.get('username')
             messages.success(request,f'Account Created for {username}! ')
             return redirect('/')

    else:
         form = UserRegisterForm()
    return render(request,"register.html",{'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile has been updated! ')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance = request.user)          #instance filled the current data in form
        p_form = ProfileUpdateForm(instance = request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'profile.html',context)


# def login(request):
#
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = auth.authenticate(username = username,password = password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect('/')
#         else:
#             messages.info(request,'invalid credential !!!')
#             return redirect('login')
#     else:
#         return render(request,'login.html')
#
#
# def logout(request):
#     auth.logout(request)
#     return redirect('/')