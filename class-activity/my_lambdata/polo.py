# attributes
# methods

class Polo():
    def __init__(self, color, size, price=99.00, style="normal fit"):
        self.color = color
        self.size = size
        self.price = price
        self.style = style

    def fold(self):
        print(f"Folding the {self.size.upper()} {self.color.upper()} polo here!")



if __name__ == "__main__":
    polo = Polo("Blue", "Large", 99.99)
    print(polo.size, polo.color, polo.price)
    polo.fold()

    polo = Polo("Yellow", "Small", 69.99)
    print(polo.size, polo.color, polo.price)
    polo.fold()


