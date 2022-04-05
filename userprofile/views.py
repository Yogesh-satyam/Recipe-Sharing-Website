from django.shortcuts import render, HttpResponse
def profile(request):
    return render(request,"userprofile/Profile.html")
