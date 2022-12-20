from django.shortcuts import render


def sslview(request):
    return render(request, "index.html")

