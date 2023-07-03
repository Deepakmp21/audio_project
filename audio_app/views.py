# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.forms import ValidationError
# from .forms import UploadFileForm
from .models import AudioFile
from django.http import Http404
import datetime

def upload_file(request):
    # form = UploadFileForm(request.POST, request.FILES)

    if request.method=="POST":
        titlename=request.POST['tname']
        music=request.FILES['mname']
        size =music.size
        pics=request.FILES['image']


        
        # Convert bytes to megabytes
        size_mb = size / (1024 * 1024)

        # Round the result to two decimal places
        size_mb = round(size_mb, 2)


        newmusic=AudioFile.objects.create(title=titlename,file=music,size=size_mb,Image=pics)
        return redirect('audio_list')
    
    else:
        message="Please upload a audio"
        return render(request, "upload_file1.html", {'msg': message})



def audio_list(request):
    audio_files = AudioFile.objects.all()
    return render(request, "audio_list1.html", {'audio_files': audio_files})

def audio_detail(request, audio_file_id):
    try:
        audio_file = AudioFile.objects.get(id=audio_file_id)
    except AudioFile.DoesNotExist:
        raise Http404('Audio file not found')

    # Print the audio file title
    print(audio_file.title)

    # Print the audio file URL
    print(audio_file.file.url)

    print(audio_file.get_file_upload_date())

    return render(request, "audio_detail1.html", {'audio_file': audio_file})