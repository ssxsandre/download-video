from django.shortcuts import render, redirect
from pytube import YouTube

from .forms import VideoForm

def download_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            video_url = form.cleaned_data['url']
            
            try:
                yt = YouTube(video_url)
                
                # Obtém todas as opções de stream disponíveis
                streams = yt.streams.filter(progressive=True)
                
                # Renderiza o template para mostrar as opções de qualidade
                return render(request, 'download.html', {'yt': yt, 'streams': streams})
            
            except Exception as e:
                error_message = f"Erro ao processar o vídeo: {str(e)}"
                return render(request, 'error.html', {'error_message': error_message})
    else:
        form = VideoForm()
    
    return render(request, 'index.html', {'form': form})