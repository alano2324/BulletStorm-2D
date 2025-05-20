import pygame
import json
import sys

# Inicjalizacja Pygame
pygame.init()

# Ekran
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BulletStorm 2D")

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (100, 100, 100)

# Czcionka
font_large = pygame.font.SysFont("Arial", 50)
font_small = pygame.font.SysFont("Arial", 30)

# Załaduj tłumaczenia
def load_language(lang_code):
    try:
        with open(f"lang/{lang_code}.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Brak pliku języka: {lang_code}.json")
        return {}

# Dostępne języki
LANGUAGES = {
    "pl": "Polski",
    "en": "English",
    "de": "Deutsch",
    "uk": "Українська",
    "sk": "Slovenčina"
}

# Ekran wyboru języka
def language_selection():
    selected_lang = None
    while not selected_lang:
        screen.fill(BLACK)
        
        title = font_large.render("Wybierz język / Select language", True, WHITE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))
        
        y_offset = 200
        for lang_code, lang_name in LANGUAGES.items():
            lang_text = font_small.render(lang_name, True, WHITE)
            lang_rect = pygame.Rect(WIDTH // 2 - 100, y_offset, 200, 40)
            
            if lang_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, RED, lang_rect, 2)
                if pygame.mouse.get_pressed()[0]:
                    selected_lang = lang_code
            else:
                pygame.draw.rect(screen, GRAY, lang_rect, 2)
            
            screen.blit(lang_text, (lang_rect.centerx - lang_text.get_width() // 2, y_offset + 5))
            y_offset += 60
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    return selected_lang

# Główna pętla gry
def main():
    lang_code = language_selection()
    translations = load_language(lang_code)
    
    # Przykładowe użycie tłumaczeń
    game_title = translations.get("game_title", "BulletStorm 2D")
    play_text = translations.get("play_button", "PLAY")
    
    running = True
    while running:
        screen.fill(BLACK)
        
        # Wyświetl tytuł gry w wybranym języku
        title = font_large.render(game_title, True, WHITE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))
        
        # Przycisk "Graj"
        play_rect = pygame.Rect(WIDTH // 2 - 100, 300, 200, 50)
        pygame.draw.rect(screen, RED, play_rect)
        play_label = font_small.render(play_text, True, WHITE)
        screen.blit(play_label, (play_rect.centerx - play_label.get_width() // 2, play_rect.centery - play_label.get_height() // 2))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    print("Rozpoczęto grę!")  # Tutaj przejdziesz do głównej gry
    
    pygame.quit()

if __name__ == "__main__":
    main()