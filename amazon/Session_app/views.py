from django.shortcuts import render
from . models import User
from django.http import JsonResponse
# Create your views here.


def login(request):
    if request.session.get('username'):
        return JsonResponse({
            "success": True,
            "message": f"{request.session.get('username')} is already logged in", 
        })
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user=User.objects.get(username=username)
            if user.password == password:
                request.session.set_expiry(20) #time 20 seconds
                request.session['username']=username
                return JsonResponse({
                    "success": True,
                    "message": "Login Successful"
                })
        except User.DoesNotExist:
            return JsonResponse({
                "error": "Invalid username or password"
            }, status=401)
        except Exception as e:
            return JsonResponse({
                "error": str(e)
            }, status=500)
    
    return render(request, 'Session_app/login.html')