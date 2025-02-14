from pytube import YouTube

def baixar_video(url, pasta_destino="."):
    try:
        # Cria um objeto YouTube com a URL fornecida
        yt = YouTube(url)

        # Seleciona o stream de vídeo com a maior resolução
        stream = yt.streams.get_highest_resolution()

        print(f"Iniciando o download do vídeo: {yt.title}")

        # Faz o download do vídeo para a pasta destino
        stream.download(pasta_destino)

        print(f"Download concluído! O vídeo foi salvo em {pasta_destino}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    # URL do vídeo do YouTube
    video_url = input("Digite a URL do vídeo do YouTube: ")
    # Pasta onde o vídeo será salvo (opcional)
    pasta_destino = input("Digite o diretório de destino (pressione Enter para o diretório atual): ")

    # Chama a função de download
    baixar_video(video_url, pasta_destino)
