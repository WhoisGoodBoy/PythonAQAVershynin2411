from lesson23.proxy_example.reader import Reader


class CSVProxyReader(Reader):
    def __init__(self, csv_reader):
        self.result = ""
        self.reader = csv_reader
        self.is_actual = False

    def read(self):
        if self.is_actual:
            return self.result
        else:
            self.result = self.reader.read()
            self.is_actual = True
            return self.result


