from methods.products import *

canape1 = Canape(materiau = "Cuir",
        couleur = "Blanc",
        dimension = '200x100x80',
        cost = 1000,
        price = 2000,
        marque = "OKLM")

canape2 = Canape(materiau = "Tissu",
        couleur = "Bleu",
        dimension = '150x90x70',
        cost = 800,
        price = 1600,
        marque = "SIESTA")

chaise1 = Chaise(materiau = "Plastique",
        couleur = "Rouge",
        dimension = '50x50x70',
        cost = 50,
        price = 100,
        marque = "PEPOUSE")

chaise2 = Chaise(materiau = "Métal",
        couleur = "Gris",
        dimension = '60x60x80',
        cost = 75,
        price = 150,
        marque = "PEPOUSE")

table2 = Table(materiau = "Bois",
        couleur = "Chêne",
        dimension = '150x80x75',
        cost = 250,
        price = 500,
        marque = "TEX")

table1 = Table(materiau = "Verre",
        couleur = "Transparent",
        dimension = '120x60x75',
        cost = 350,
        price = 700,
        marque = "TEX")

print(table1.dimension, chaise2.marque, canape1.price)