# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render
import requests

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def error_500_view(request):
    """
    A view to render 500 error page if there is a server error such
    as the api failing
    Args:
        request (object): HTTP request object.
    Returns:
        Render 500error page
    """
    return render(request, '500error.html', status=500)


def index(request):
    try:
        baseurl = 'https://api.thecatapi.com/'
        endpoint = 'v1/breeds'
        token = "0f252955-75a3-4f82-9127-543420bd2525"

        headers = {'x-api-key': token}
        response = requests.get(
            baseurl + endpoint, headers=headers).json()

        if request.method == "POST":
            breed = request.POST['breed']
            for item in range(0, len(response)):
                if breed == response[item]['name']:
                    name = response[item]['name']
                    temperament = response[item]['temperament']
                    description = response[item]['description']
                    origin = response[item]['origin']
                    life_span = response[item]['life_span']
                    affection_level = response[item]['affection_level']
                    image_url = response[item]['image']['url']
                    wikipedia_url = response[item]['wikipedia_url']

                    context = {
                        'breed': breed,
                        'response': response,
                        'name': name,
                        'origin': origin,
                        'temperament': temperament,
                        'description': description,
                        'life_span': life_span,
                        'affection_level': affection_level,
                        'image_url': image_url, 
                        'wikipedia_url': wikipedia_url
                        }

                    return render(request, 'index.html', context)

        context = {'response': response}
        return render(request, 'index.html', context)

    except Exception:
        return render(request, '500error.html')
