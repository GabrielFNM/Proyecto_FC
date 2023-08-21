from django.shortcuts import render

# Create your views here.

def menu(request):
    return render(request,"core/menu.html");
def contact(request):
    return render(request,"core/contact.html");


