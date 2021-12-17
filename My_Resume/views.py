from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html',{})

def about_page(request):
    return render(request, 'about.html',{})

def skills_page(request):
    return render(request, 'skills.html',{})

def achievements_page(request):
    return render(request, 'service.html',{})

def portofolio_page(request):
    return render(request, 'portofolio.html',{})

def certification_page(request):
    return render(request, 'mycertifications.html',{})
