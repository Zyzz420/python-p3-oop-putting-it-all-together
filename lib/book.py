class Book:
    def __init__(self, title, page_count):
        self._title = title
        self._page_count = None
        self.page_count = page_count

    def get_title(self):
        return self._title

    def get_page_count(self):
        return self._page_count

    def set_page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    title = property(get_title)
    page_count = property(get_page_count, set_page_count)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")