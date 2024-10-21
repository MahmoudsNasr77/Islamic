import requests
from django.shortcuts import render

def display_hadiths_data(request):
    try:
        response = requests.get('http://127.0.0.1:8000/api/')
        response.raise_for_status()  # Check if request was successful
        data = response.json()  # Parse the JSON data
    except requests.exceptions.RequestException as e:
        # Handle the exception
        data = {"error": "Unable to fetch data from API"}

    return render(request, 'hadiths.html', {'data': data})
def display_hadiths(request, id):
    try:
        response = requests.get(f'http://127.0.0.1:8000/api/retrieve/{id}/')
        response.raise_for_status()  # Check if the request was successful
        data = response.json()  # Parse the JSON data
    except requests.exceptions.RequestException as e:
        data = {"error": "Unable to fetch data from API"}

    return render(request, 'hadithssingly.html', {'data': data})