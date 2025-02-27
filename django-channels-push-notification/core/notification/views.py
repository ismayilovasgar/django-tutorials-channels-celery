from django.shortcuts import render

# Create your views here.

def notification_page_view(request):
    return render(request, "notification_page.html") 

def notification_page_view_me(request):
    return render(request, "notification_page_me.html") 