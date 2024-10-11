from django.contrib.auth.signals import user_logged_in,user_logged_out
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from Auth_app.models import Contact
from django.dispatch import receiver

#receiver function
def login_success(sender,request,user,**kwargs):
    print(" i am user logged in signal rec. func")
    print(sender)
    print(f"user: {user}")
    print(f"request: {request}")
    print(f"kwargs: {kwargs}")

    #access email id from the user 
    #write logic to send the email


#connect the signal
#signal.connect(reciever,sender)
user_logged_in.connect(login_success,sender=User)


@receiver(user_logged_out,sender=User)
def logout_success(sender,request,user,**kwargs):
    print("i am user logged out signal rec. func")
    print(sender)
    print(f"user: {user}")
    print(f"request: {request}")
    print(f"kwargs: {kwargs}")


@receiver(pre_save,sender=Contact)
def pre_save_receiver(sender,**kwargs):
    print("i am pre_save signal rec. func")
    print(sender)
    print(f"kwargs: {kwargs}")
  
    