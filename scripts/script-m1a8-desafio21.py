# desafio 21
# Faça um programa em python que abra e reproduza o áudio de um arquivo MP3;

import pygame
pygame.init() # este método deve ser chamado antes de utilizar qualquer outra funcionalidade da biblioteca Pygame;
pygame.mixer.music.load('script-m1a8-desafio21.mp3')
pygame.mixer.music.play()
pygame.event.wait()


