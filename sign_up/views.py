from django.shortcuts import render, redirect
from .models import Account
from django.http import HttpResponse

def signUp(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        password = request.POST.get('password')
        hobbies = request.POST.getlist('hobbies')
        source_of_income = request.POST.get('source_of_income')
        income = request.POST.get('income')
        profile_pic = request.FILES.get('profile_pic')
        age = request.POST.get('age')
        bio = request.POST.get('bio')

        Account.objects.create(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            email=email,
            password=password,
            hobbies=",".join(hobbies),
            source_of_income=source_of_income,
            income=income,
            profile_pic=profile_pic,
            age=age,
            bio=bio
        )

        return HttpResponse("success")

    return render(request, 'sign_up/register.html')