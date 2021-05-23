from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import AdvertAddForm, sortChoice, RegisterForm
from .models import Advert
from django.db.models import Q

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        if request.user.is_authenticated:
            logout(request)
        form = RegisterForm()
    context = {'form':form,}
    return render(request, "register.html",context)

def loginView(request):
	if request.method == 'POST':
		form = AuthenticationForm(data = request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('profile')
	else:
		form = AuthenticationForm()
	context = {
		'form':form,
	}
	return render(request, 'login.html', context)

@login_required(login_url = 'login')
def logOut(request):
	if request.method == 'POST':
		logout(request)
	return redirect('home')

@login_required(login_url = 'login')
def profile(request):
    obj = User.objects.get(username = request.user)
    return render(request, "profile.html", {'obj':obj})

@login_required(login_url='login')
def advertAdd(request):
    if request.method == 'POST':
        form = AdvertAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = AdvertAddForm()
    context = {'form':form}
    return render(request,'advert.html',context)

@login_required(login_url = 'login')
def dynamicAdvert(request, id):
	obj = get_object_or_404(Advert, id = id)
	oldDate = obj.pubDate
	obj.viewsAmount += 1
	obj.pubDate = oldDate
	obj.save()
	context = {
		'obj' : obj
	}
	return render(request, "advert.html", context)


def home(request):
    return render(request, "home.html")

@login_required(login_url = 'login')
def advertList(request):
	searchQueryNavbar = request.GET.get('search_navbar', '')
	searchQueryVLpage = request.GET.get('search_vlpage', '')

	form = sortChoice(request.GET or request.POST)

	if searchQueryNavbar or searchQueryVLpage:
		if searchQueryNavbar:
			searchQuery = searchQueryNavbar
		else:
			searchQuery = searchQueryVLpage
		if form.is_valid():
			selected = form.cleaned_data.get("choice")
			if selected == 'viewsAmount':
				queryset = Advert.objects.filter(Q(name__icontains = searchQuery) | Q(salary__icontains = searchQuery) | Q(competences__icontains = searchQuery)).order_by('-viewsAmount')
			if selected == 'pubDate':
				queryset = Advert.objects.filter(Q(name__icontains = searchQuery) | Q(salary__icontains = searchQuery) | Q(competences__icontains = searchQuery)).order_by('-creationDate')
	else:
		queryset = Advert.objects.all().order_by('-pubDate')

	context = {
		'objectList':queryset,
		'form':form
	}
	return render(request, "advertList.html", context)

@login_required(login_url = 'login')
def profileView(request):
		obj = User.objects.get(username = request.user)
		return render(request, "profile.html", {'obj' : obj})
