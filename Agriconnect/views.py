from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def pricing(request):
    return render(request,'pricing.html')
def fertilizerCalculator(request):
    return render(request,'fertilizerCalculator.html')
def weather(request):
    return render(request,'weather.html')