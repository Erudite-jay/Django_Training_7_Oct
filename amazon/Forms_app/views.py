from django.shortcuts import render
from .forms import FileUploadFormClass
from .models import FileUpload
from django.http import JsonResponse

# Create your views here.

def file_upload_form(request):
    if request.method =='POST':
        form=FileUploadFormClass(request.POST, request.FILES)
        # file = request.FILES['file'] 

        if form.is_valid():
            # file_upload=FileUpload(name=form.cleaned_data['name'],file=file)
            # file_upload.save()
            form.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"error": form.errors})

    if request.method == "GET":
        form=FileUploadFormClass()
        return render(request, 'Forms_app/file.html', {'form': form})