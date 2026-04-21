import pygame
import sys
import math
import random
import time

pygame.init()

# ---------------- SCREEN ----------------
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HCI Polyline + Fitts Experiment")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

font = pygame.font.SysFont(None, 28)

# ---------------- STATE ----------------
mode = "start"

# ---------------- DATA ----------------
polys = []
current_poly = []

# ---------------- FITTS DATA ----------------
target_pos = None
start_time = 0
logs = []


# ---------------- FUNCTIONS ----------------
def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


def find_nearest_point(pos):
    for poly in polys:
        for i, point in enumerate(poly):
            if distance(point, pos) < 10:
                return poly, i
    return None, None


def new_target():
    global target_pos, start_time
    target_pos = (
        random.randint(50, WIDTH - 50),
        random.randint(50, HEIGHT - 50)
    )
    start_time = time.time()


# ---------------- MAIN LOOP ----------------
while True:
    screen.fill(WHITE)

    # ---------------- START SCREEN ----------------
    if mode == "start":
        screen.blit(font.render("HCI Polyline + Fitts Experiment", True, BLACK), (200, 200))
        screen.blit(font.render("Press F = Start Experiment", True, BLUE), (240, 260))
        screen.blit(font.render("Press E = Edit Mode", True, BLACK), (270, 300))

    # ---------------- EDIT MODE ----------------
    elif mode == "edit":

        # draw polylines
        for poly in polys:
            if len(poly) > 1:
                pygame.draw.lines(screen, BLACK, False, poly, 2)
            for p in poly:
                pygame.draw.circle(screen, RED, p, 5)

        # UI text
        screen.blit(font.render("B = New Polyline", True, BLACK), (20, 20))
        screen.blit(font.render("Left Click = Add Point", True, BLACK), (20, 50))
        screen.blit(font.render("Right Click = Finish Polyline", True, BLACK), (20, 80))
        screen.blit(font.render("D = Delete Point", True, BLACK), (20, 110))

    # ---------------- FITTS MODE ----------------
    elif mode == "fitts":

        if target_pos:
            pygame.draw.circle(screen, BLUE, target_pos, 20)

        if len(logs) > 0:
            avg_time = sum([t for _, t in logs]) / len(logs)
            avg_dist = sum([d for d, _ in logs]) / len(logs)

            screen.blit(font.render(
                f"Avg Time: {round(avg_time,2)}s  Avg Dist: {int(avg_dist)}px",
                True, BLACK), (20, 20))

        screen.blit(font.render("Click BLUE target", True, BLACK), (20, 50))

    # ---------------- EVENTS ----------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # KEY EVENTS
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_f:
                mode = "fitts"
                logs = []
                new_target()

            if event.key == pygame.K_e:
                mode = "edit"

            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

            # B = new polyline
            if event.key == pygame.K_b:
                current_poly = []
                polys.append(current_poly)

            # D = delete nearest point (FIXED)
            if event.key == pygame.K_d and mode == "edit":
                mouse_pos = pygame.mouse.get_pos()

                poly, index = find_nearest_point(mouse_pos)
                if poly is not None and index is not None:
                    poly.pop(index)

        # MOUSE EVENTS
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            # ---------------- EDIT MODE ----------------
            if mode == "edit":

                if event.button == 1:  # left click
                    if polys:
                        polys[-1].append(pos)

                if event.button == 3:  # right click
                    current_poly = []

            # ---------------- FITTS MODE ----------------
            elif mode == "fitts":
                if target_pos:
                    dist = distance(pos, target_pos)
                    t = time.time() - start_time
                    logs.append((dist, t))
                    new_target()

    pygame.display.update()
