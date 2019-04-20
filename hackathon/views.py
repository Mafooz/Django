from django.shortcuts import render
from django.http import HttpResponse
from hackathon.forms import RegistrationForm
from django.contrib.auth import authenticate, logout,login
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	return render(request,'registration/index.html')


def signup(request):
	form = RegistrationForm(request.POST)
	if form.is_valid():
		print("valid")
		user = form.save(commit=False)
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user.set_password(password)
		user.save()
		user = authenticate(username=username, password=password)
		if user is not None:
			print(user)
			if user.is_active:
				print(user)
				login(request,user)
				return render(request, 'home/home.html')

	return render(request, 'registration/signup.html',{'form':form})

@login_required
def home(request):
	return render(request,'home/home.html')