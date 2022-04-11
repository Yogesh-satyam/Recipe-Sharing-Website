from django.shortcuts import render, HttpResponse


def userprofile(request):
    return render(request,'userprofile/userprofile.html')
