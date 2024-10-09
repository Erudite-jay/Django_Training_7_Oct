from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Contact
from .serializers import ContactSerializer
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def print_hello(request):
    return HttpResponse("hello i am first view")

def home_page(request):
    return render(request, 'Auth_app/index.html')


@csrf_exempt
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

    if request.method == "POST":
        input_data = json.loads(request.body) #json 
        serializer_data = ContactSerializer(data=input_data) #creating serializer object -> creating queryset
        try:
            if serializer_data.is_valid():
                serializer_data.save() #saving to database
                return JsonResponse({
                    "Success": True,
                    "message": "Data saved successfully",

                    "data": serializer_data.data
                    }, status=201)
            else:
                return JsonResponse(serializer_data.errors, status=400)
        except Exception as e:
            return JsonResponse({
                "error": str(e)
            },status=500)

@csrf_exempt
def single_user_data(request,pk):
    if request.method == 'GET':
        try:
            user = Contact.objects.get(pk=pk)
            serializer_data = ContactSerializer(user)
            return JsonResponse(serializer_data.data, safe=False)
        except Contact.DoesNotExist:
            return JsonResponse({
                "error": "User not found"
            },status=404)
        except Exception as e:
            return JsonResponse({
                "error": str(e)
            },status=500)

    if request.method == 'PUT':
        try:
            user = Contact.objects.get(pk=pk)
            input_data = json.loads(request.body)
            serializer_data = ContactSerializer(user, data=input_data)

            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse({
                    "Success": True,
                    "message": "Data updated successfully",
                    "data": serializer_data.data
                    }, status=200)
            else:
                return JsonResponse(serializer_data.errors, status=400)
        except Exception as e:
            return JsonResponse({
                "error": str(e)
            },status=500)

    if request.method == 'PATCH':
        try:
            user = Contact.objects.get(pk=pk)
            input_data = json.loads(request.body)
            serializer_data = ContactSerializer(user,data=input_data,partial=True)

            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse({
                    "Success": True,
                    "message": "Data updated successfully",
                    "data": serializer_data.data
                    }, status=200)
            else:
                return JsonResponse(serializer_data.errors, status=400)
        except Exception as e:
            return JsonResponse({
                "error": str(e)
            },status=500)

    if request.method == 'DELETE':
        try:
            user = Contact.objects.get(pk=pk)
            user.delete()
            return JsonResponse({
                "Success": True,
                "message": "Data deleted successfully"
            }, status=204)
        except Exception as e:
            return JsonResponse({
                "error": str(e)
            },status=500)