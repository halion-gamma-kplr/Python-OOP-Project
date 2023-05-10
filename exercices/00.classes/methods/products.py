class Product :
    def __init__(self, cost, price, marque) :
        self.cost = cost
        self.price = price
        self.marque = marque

class Meubles(Product) :
    def __init__(self, cost, price, marque, materiau, couleur, dimension) :
        super().__init__(cost,price,marque)
        self.materiau = materiau
        self.couleur = couleur
        self.dimension = dimension 
    
class Canape(Product) :
    def __init__(self, cost, price, marque, materiau, couleur, dimension) :
        super().__init__(cost,price,marque)
        self.materiau = materiau
        self.couleur = couleur
        self.dimension = dimension 

class Chaise(Product) :
    def __init__(self, cost, price, marque, materiau, couleur, dimension) :
        super().__init__(cost,price,marque)
        self.materiau = materiau
        self.couleur = couleur
        self.dimension = dimension 
    
class Table(Product) :
    def __init__(self, cost, price, marque, materiau, couleur, dimension) :
        super().__init__(cost,price,marque)
        self.materiau = materiau
        self.couleur = couleur
        self.dimension = dimension 