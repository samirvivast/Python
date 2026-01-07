import pygame
import time
import random

# Inicializar Pygame
pygame.init()

# Codigo de colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
#rojo = (213, 50, 80)
#verde = (0, 255, 0)
#azul = (50, 153, 213)

# Dimensiones de la ventana
ancho = 600
alto = 400

# Configuración de la ventana
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego de la Serpiente Python")

# Reloj
reloj = pygame.time.Clock()

# Tamaño de bloque de la serpiente
tamano_bloque = 20
velocidad_serpiente = 15

# Fuente o tipografia
fuente = pygame.font.SysFont("Arial", 25)
fuentemensaje = pygame.font.SysFont("Arial", 35)
fuente_puntuacion = pygame.font.SysFont("Arial", 20)


def mi_puntuacion(puntos):
    valor = fuente_puntuacion.render("Puntuación: " + str(puntos), True, blanco)
    ventana.blit(valor, [0, 0])


def nuestra_serpiente(tamano_bloque, lista_serpiente):
    for x in lista_serpiente:
        pygame.draw.rect(ventana, blanco, [x[0], x[1], tamano_bloque, tamano_bloque])


def mensaje(msg, color):
    mesg = fuentemensaje.render(msg, True, color)
    ventana.blit(mesg, [ancho / 6, alto / 6])

def opcion1(msg, color):
    mesg = fuente.render(msg, True, color)
    ventana.blit(mesg, [ancho / 6, alto / 2])

def opcion2(msg, color):
    mesg = fuente.render(msg, True, color)
    ventana.blit(mesg, [ancho / 6, alto / 3])

def opcion3(msg, color):
    mesg = fuente.render(msg, True, color)
    ventana.blit(mesg, [ancho / 9, alto / 1.5])

def juego():
    game_over = False
    game_close = False

    # Posición inicial de la serpiente
    x1 = ancho / 2
    y1 = alto / 2

    # Cambio en dirección
    x1_cambio = 0
    y1_cambio = 0

    lista_serpiente = []
    largo_serpiente = 1

    # Posición inicial de la comida
    comida_x = round(random.randrange(0, ancho - tamano_bloque) / 20.0) * 20.0
    comida_y = round(random.randrange(0, alto - tamano_bloque) / 20.0) * 20.0

    while not game_over:

        while game_close:
            ventana.fill(negro)
            mensaje("Has perdido :(", blanco)
            opcion1("Presiona C para Reintentar", blanco)
            opcion2("Presiona Q para Salir", blanco)
            opcion3("Creado por Samir Vivas | 2025 | bryansamir@gmail.com", blanco)
            
            mi_puntuacion(largo_serpiente - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        juego()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_cambio = -tamano_bloque
                    y1_cambio = 0
                elif event.key == pygame.K_RIGHT:
                    x1_cambio = tamano_bloque
                    y1_cambio = 0
                elif event.key == pygame.K_UP:
                    y1_cambio = -tamano_bloque
                    x1_cambio = 0
                elif event.key == pygame.K_DOWN:
                    y1_cambio = tamano_bloque
                    x1_cambio = 0

        # Si la serpiente toca los bordes
        if x1 >= ancho or x1 < 0 or y1 >= alto or y1 < 0:
            game_close = True

        x1 += x1_cambio
        y1 += y1_cambio
        ventana.fill(negro)
        pygame.draw.rect(ventana, blanco, [comida_x, comida_y, tamano_bloque, tamano_bloque])
        lista_cabeza = []
        lista_cabeza.append(x1)
        lista_cabeza.append(y1)
        lista_serpiente.append(lista_cabeza)
        if len(lista_serpiente) > largo_serpiente:
            del lista_serpiente[0]

        # Si la serpiente choca consigo misma
        for x in lista_serpiente[:-1]:
            if x == lista_cabeza:
                game_close = True

        nuestra_serpiente(tamano_bloque, lista_serpiente)
        mi_puntuacion(largo_serpiente - 1)

        pygame.display.update()

        # Si la serpiente come la comida
        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, ancho - tamano_bloque) / 20.0) * 20.0
            comida_y = round(random.randrange(0, alto - tamano_bloque) / 20.0) * 20.0
            largo_serpiente += 1

        reloj.tick(velocidad_serpiente)

    pygame.quit()
    quit()


juego()
