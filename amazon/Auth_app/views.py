from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Contact
from .serializers import ContactSerializer

# Create your views here.


def print_hello(request):
    return HttpResponse("hello i am first view")

def home_page(request):
    return render(request, 'Auth_app/index.html')


def user_data(request):
    if request.method == 'GET':
        try:
            all_users = Contact.objects.all() # queryset
            serializer_data=ContactSerializer(all_users,many=True) #data in serialized form ~= json format
            return JsonResponse(serializer_data.data,safe=False)
        except Exception as e:
            return JsonResponse({
                "error": str(e)
            },status=500)
