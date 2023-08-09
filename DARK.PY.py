
import urllib.request
import sys

def abrir_site_repetidamente(url, num_repeticoes, intervalo_segundos):
    for _ in range(num_repeticoes):
        try:
            response = urllib.request.urlopen(url)
            conteudo = response.read().decode('utf-8')
            print(f"Acesso bem-sucedido a {url}")
        except urllib.error.URLError as e:
            print(f"Erro ao acessar o site: {e}")
        
        time.sleep(intervalo_segundos)

if __name__ == "__main__":

    draw_text = input("Escreva a url:  ") # Substitua pelo URL do site alvo
    num_repeticoes = 10
    intervalo_segundos = 5
    
    print(f"DarkPy iniciando ataques a {draw_text}...")
    abrir_site_repetidamente(draw_text, num_repeticoes, intervalo_segundos)
    print("Ataques concluídos. DarkPy satisfeito.")
    



if __name__ == "__main__":
    main()
