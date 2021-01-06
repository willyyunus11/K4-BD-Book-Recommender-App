from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'recommendation.html')
  
def firstRating(request):
  return render(request, 'first_rating.html')