import pygame
import sys
import math

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Polyline Editor")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

polys = []
current_poly = []
mode = None
selected_point = None

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def find_nearest_point(pos):
    for poly in polys:
        for point in poly:
            if distance(point, pos) < 10:
                return poly, point
    return None, None

while True:
    screen.fill(WHITE)

    # Draw polylines
    for poly in polys:
        if len(poly) > 1:
            pygame.draw.lines(screen, BLACK, False, poly, 2)
        for point in poly:
            pygame.draw.circle(screen, RED, point, 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                current_poly = []
                polys.append(current_poly)
            elif event.key == pygame.K_d:
                mode = 'delete'
            elif event.key == pygame.K_m:
                mode = 'move'
            elif event.key == pygame.K_r:
                pass  # auto redraw
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if mode == 'delete':
                poly, point = find_nearest_point(pos)
                if poly and point:
                    poly.remove(point)

            elif mode == 'move':
                poly, point = find_nearest_point(pos)
                if poly and point:
                    selected_point = point

            else:
                if polys:
                    polys[-1].append(pos)

        if event.type == pygame.MOUSEBUTTONUP:
            selected_point = None

        if event.type == pygame.MOUSEMOTION:
            if selected_point:
                for poly in polys:
                    for i, p in enumerate(poly):
                        if p == selected_point:
                            poly[i] = event.pos
                            selected_point = event.pos

    pygame.display.update()