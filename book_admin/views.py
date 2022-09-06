# Create your views here.
from django.shortcuts import render

# Create your views here.
def form(request):
    return render(request, 'darkpan-1.0.0/form.html')
def index(request):
    return render(request, 'darkpan-1.0.0/index.html')
def signin(request):
    return render(request, 'darkpan-1.0.0/signin.html')
def signup(request):
    return render(request, 'darkpan-1.0.0/signup.html')
def table(request):
    return render(request, 'darkpan-1.0.0/table.html')
def typography(request):
    return render(request, 'darkpan-1.0.0/typography.html')
def widget(request):
    return render(request, 'darkpan-1.0.0/widget.html')
def element(request):
    return render(request, 'darkpan-1.0.0/element.html')
def chart(request):
    return render(request, 'darkpan-1.0.0/chart.html')
def button(request):
    return render(request, 'darkpan-1.0.0/button.html')
def four(request):
    return render(request, 'darkpan-1.0.0/404.html')
def blank(request):
    return render(request, 'darkpan-1.0.0/blank.html')
