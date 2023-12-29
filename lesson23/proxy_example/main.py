from lesson23.proxy_example.csv_reader import CSVReader
from lesson23.proxy_example.csv_proxy_reader import CSVProxyReader

csv_reader = CSVReader('example.csv')
reader = CSVProxyReader(csv_reader)
print(reader.read())
print(reader.read())
print()