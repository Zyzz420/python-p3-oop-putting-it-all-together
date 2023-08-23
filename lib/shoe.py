
class Shoe:
    def __init__(self, brand, size):
        self._brand = brand
        self._size = None
        self.size = size
        self._condition = "New"

    def get_brand(self):
        return self._brand

    def get_size(self):
        return self._size

    def set_size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    brand = property(get_brand)
    size = property(get_size, set_size)

    def cobble(self):
        print("Your shoe is as good as new!")
        self._condition = "New" 

    @property
    def condition(self):
        return self._condition