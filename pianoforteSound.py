import pygame
import time

# Inizializzazione del modulo pygame
pygame.init()

# Configurazione della finestra di visualizzazione
win_width = 800
win_height = 400
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Piano virtuale")

# Definizione dei colori
white = (255, 255, 255)
black = (0, 0, 0)

# Definizione delle dimensioni dei tasti
key_width = win_width // 14
key_height = win_height // 2

# Definizione delle posizioni dei tasti
key_positions = {
    pygame.K_a: (0, 0),
    pygame.K_s: (key_width, 0),
    pygame.K_d: (key_width * 2, 0),
    pygame.K_f: (key_width * 3, 0),
    pygame.K_g: (key_width * 4, 0),
    pygame.K_h: (key_width * 5, 0),
    pygame.K_j: (key_width * 6, 0),
    pygame.K_k: (key_width * 7, 0),
    pygame.K_l: (key_width * 8, 0),
    pygame.K_SEMICOLON: (key_width * 9, 0),
    pygame.K_QUOTE: (key_width * 10, 0),
    pygame.K_RETURN: (key_width * 11, 0),
    pygame.K_w: (key_width * 1 - key_width // 4, key_height - key_height // 2),
    pygame.K_e: (key_width * 2 - key_width // 4, key_height - key_height // 2),
    pygame.K_t: (key_width * 4 - key_width // 4, key_height - key_height // 2),
    pygame.K_y: (key_width * 5 - key_width // 4, key_height - key_height // 2),
    pygame.K_u: (key_width * 6 - key_width // 4, key_height - key_height // 2),
    pygame.K_o: (key_width * 8 - key_width // 4, key_height - key_height // 2),
    pygame.K_p: (key_width * 9 - key_width // 4, key_height - key_height // 2),
}

# Definizione delle note corrispondenti ai tasti
key_notes = {
    pygame.K_a: "C",
    pygame.K_s: "D",
    pygame.K_d: "E",
    pygame.K_f: "F",
    pygame.K_g: "G",
    pygame.K_h: "A",
    pygame.K_j: "B",
    pygame.K_k: "C",
    pygame.K_l: "D",
    pygame.K_SEMICOLON: "E",
    pygame.K_QUOTE: "F",
    pygame.K_RETURN: "G",
    pygame.K_w: "C#",
    pygame.K_e: "D#",
    pygame.K_t: "F#",
    pygame.K_y: "G#",
    pygame.K_u: "A#",
    pygame.K_o: "C#",
    pygame.K_p: "D#",
}

# Caricamento dei suoni delle note
note_sounds = {}
for note in key_notes.values():
    sound = pygame.mixer.Sound(note + ".wav")
    note_sounds[note] = sound

# Lista delle note correntemente suonate
playing_notes = []

# Funzione per disegnare i tasti
def draw_keys():
    window.fill(white)

    for key in key_positions:
        key_rect = pygame.Rect(key_positions[key], (key_width, key_height))
        pygame.draw.rect(window, black, key_rect)

    pygame.display.update()

# Funzione per suonare la nota
def play_sound(note):
    if note in note_sounds:
        sound = note_sounds[note]
        sound.play()

# Ciclo di gioco principale
def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key in key_notes:
                    note = key_notes[event.key]
                    if note not in playing_notes:
                        playing_notes.append(note)
                        play_sound(note)

            if event.type == pygame.KEYUP:
                if event.key in key_notes:
                    note = key_notes[event.key]
                    if note in playing_notes:
                        playing_notes.remove(note)

        draw_keys()

    pygame.quit()

# Avvio del programma
if __name__ == "__main__":
    main()
