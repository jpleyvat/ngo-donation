from django.shortcuts import render

def homepage(request):

    context = {}  #I made a card view that displays the events(donations) when

    return render(request, "Home.html", context)