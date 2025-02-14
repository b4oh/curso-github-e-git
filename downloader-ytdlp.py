import yt_dlp

def baixar_video(url, pasta_destino="."):
    try:
        ydl_opts = {
            'outtmpl': f'{pasta_destino}/%(title)s.%(ext)s',  # Define o nome e o caminho do arquivo
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Iniciando o download do vídeo...")
            ydl.download([url])
            print(f"Download concluído!")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    video_url = input("Digite a URL do vídeo do YouTube: ")
    pasta_destino = input("Digite o diretório de destino (pressione Enter para o diretório atual): ")
    baixar_video(video_url, pasta_destino)
