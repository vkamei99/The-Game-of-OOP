from moviepy.editor import VideoFileClip

# Caminho para o vídeo
video_path = '/mnt/data/Valkyries (God Of War Soundtrack).mp4'

# Carregar o vídeo
video_clip = VideoFileClip(video_path)

# Extrair o áudio do vídeo
audio_clip = video_clip.audio

# Caminho para salvar o áudio MP3
audio_path = '/mnt/data/Valkyries (God Of War Soundtrack).mp3'

# Salvar o áudio em formato MP3
audio_clip.write_audiofile(audio_path)

# Fechar os clipes para liberar recursos
audio_clip.close()
video_clip.close()

# Caminho do arquivo MP3 criado
audio_path
