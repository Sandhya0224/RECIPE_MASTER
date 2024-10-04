from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserCreationform,Authenticationform


# Create your views here.
@login_required(login_url="/login_user/")
def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        Recipe.objects.create(
             recipe_name=recipe_name,
             recipe_description=recipe_description,
             recipe_image=recipe_image,
        )
        return redirect('/')
    queryset = Recipe.objects.all()

    if request.GET.get('search_food'):
        queryset = Recipe.objects.filter(recipe_name__icontains = request.GET.get('search_food'))

    context = {'recipes':queryset}
    return render(request,'recipe.html',context)
    
def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/')

def update_recipe(request, id):
    queryset = Recipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        if recipe_image:
            queryset.recipe_image = recipe_image
        queryset.save()
        return redirect('/')
    context = {'recipe':queryset}
    return render(request, 'updated_recipe.html', context)


def register_user(request):
    form = UserCreationform()
    context = {'form':form}
    if request.method == 'POST':
        form = UserCreationform(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            return redirect('/login_user/')
    return render(request, 'register.html',context)

def login_user(request):
    form = Authenticationform()
    context = {'form':form}
    if request.method == 'POST':
        form = Authenticationform(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username)
            print(password)
            user = authenticate(username=username,password=password)
            print(user)
            if user:
                login(request,user)
                return redirect('/')
    return render(request, 'login.html',context)


def logout_user(request):
    logout(request)
    return redirect('/login_user/')
            
        