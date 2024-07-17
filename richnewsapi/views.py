from django.shortcuts import render
from django.http import JsonResponse
import requests
from rest_framework.decorators import api_view, APIView


# Create your views here.
@api_view(['GET'])
def fetch_data(request):
    API_KEY = 'hidden'
    scan = request.query_params.get('lookup', None)
    url = f"http://eventregistry.org/api/v1/article/getArticles?actions=getArticles&keyword={scan}&articlePage=1&articleCount=10&resultType=articles&dataType=news&forceMaxDataTimeWindow=7&language=en&api_key=&apiKey={API_KEY}"
    if scan:
        response =requests.get(url)
        print(response)
        data = response.json()
        print(data)
        return JsonResponse(data)
    return JsonResponse({'error': 'Failed to fetch article'})

        

api_key = "hidden"
class NewsAPI(APIView):
    def get(self, request):
        search = request.query_params.get('keyword', None)
        
        if search:
            url = f"https://newsapi.org/v2/everything?q={search}&apiKey={api_key}"
            response = requests.get(url)
            data = response.json()
            return JsonResponse(data)
        else:
            return JsonResponse({'error':"Info can't be fetched"})

    

