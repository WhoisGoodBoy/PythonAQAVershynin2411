from lesson23.proxy_example.reader import Reader


class CSVReader(Reader):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename) as file:
            text = file.read()
            return text