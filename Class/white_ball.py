import pygame


"""
@Author :   StarFr0zen
            KoddaZz

white_ball.py : Script correspondant à la gestion de la boule blanche
"""

RAYON = 10 # taille balle
LONGUEUR_ECRAN = 1000 # taille longueur écran de jeu (x)
LARGEUR_ECRAN = 500 # taille largeur écran de jeu (y)

fenetre = pygame.display.set_mode((LONGUEUR_ECRAN, LARGEUR_ECRAN))
fenetre.fill([0, 0, 0])

class White_Ball:
    def __init__(self):
        self.x = LONGUEUR_ECRAN / 4
        self.y = LARGEUR_ECRAN / 2
        self.dx = 0
        self.dy = 0
        self.couleur = (255,255,255)
        self.taille = RAYON
        self.hitbox_white_ball = pygame.Rect(self.x, self.y, self.taille, self.taille)
        self.coeff_frottement = 0.999

    def deplacements(self):
        pygame.draw.circle(fenetre, (51, 153, 0), (self.x, self.y), self.taille)
        self.x += self.dx * self.coeff_frottement
        self.y += self.dy * self.coeff_frottement

        if self.y < self.taille or self.y > LARGEUR_ECRAN - self.taille:
            self.dy = -self.dy
        if self.x < self.taille or self.x > LONGUEUR_ECRAN - self.taille:
            self.dx = -self.dx
        pygame.draw.circle(fenetre, self.couleur, (self.x, self.y), self.taille)


# CODE TEMPORAIRE POUR DES TEST

