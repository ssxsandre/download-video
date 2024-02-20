from django.shortcuts import render
from pytube import YouTube

def download_video(request):
    if request.method == 'POST':
        url = request.POST.get("video_url")
        yt = YouTube(url)
        video_stream = yt.streams.get_medium_resolution()
        video_stream.download()
        return render(request, 'download.html', { 'video_download_complete': True, 'video_url': video_stream.default_filename })
    return render(request, 'download.html')
