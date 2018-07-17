from django.shortcuts import render
from .models import Image
import datetime as dt

# Create your views here.
def home(request):
    photos = Image.get_all()
    date = dt.date.today
    return render(request, 'home.html', {"date":date, "photos": photos})

def image(request, image_id):
    image = Image.get_image(image_id)
    return render(request, 'image.html', {"image": image})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        query = request.GET.get("image")
        results = Image.search(query)
        message = f"{query}"

        return render(request, 'results.html', {"message":message,"results": results})

    else:
        message = "Search not found. What images are you looking for? Search here."
        return render(request, 'results.html', {"message": message})
