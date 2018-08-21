from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import UserRegisterForm,LoginForm

def homeview(request):
    return render(request, 'account/home.html')

class UserRegister(View):
    template = 'account/register.html'
    def get(self,request):
        form= UserRegisterForm()
        return render(request, self.template, {'form': form})
    #if this is a POST request, we need to process form data
    def post(self,request):
        if request.method == 'POST':
        #create a form and populate it with the input data
            form = UserRegisterForm(request.POST)

            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                return HttpResponse('Thanks')
            else:
                form = UserRegisterForm()
            return render(request, 'account/register.html', {'form': form})

class UserLogin(View):
    template = 'account/login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template, {'form': form })

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            formData = form.cleaned_data
            email = formData['email']
            password = formData['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                return HttpResponse('Logged in hehe')
                login(request, user)
            else:
                return HttpResponse('Lolw tf bro')
        return render(request, self.template, {'form': form})


# Create your views here.
