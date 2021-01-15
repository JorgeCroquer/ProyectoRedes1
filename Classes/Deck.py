from Card import Card


# clase para el mazo

class Deck:
    def __init__(self):
        self.cards = []

        colours = ["Rojo","Verde","Azul","Amarillo", "Comodin"]
        values = [1,2,3,4,5,6,7,8,9,"Doble manotazo", "Reversa", "Tira un color"]

        wilds = ["Cambia color", "Ataque"]

        for colour in colours:
            if colour == "Comodin":
                    for wild in wilds:
                        card = Card (colour, wild)
                        self.cards.append(card)
                        self.cards.append(card)
                        self.cards.append(card)
                        self.cards.append(card)
            else:
                for value in values:        
                    card = Card(colour, value)
                    self.cards.append(card)
                    self.cards.append(card)

        card = Card("Comodin","Cuádruple manotazo")
        self.cards.append(card)


                





    

