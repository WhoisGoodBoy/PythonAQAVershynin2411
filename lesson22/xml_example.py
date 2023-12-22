from xml.etree import ElementTree


tree = ElementTree.parse('example.xml')
root = tree.getroot()
'''print(type(root))
for genre in root:
    print(genre)
    for decade in genre:
        print(decade)

decoded_to_string = ElementTree.tostring(root).decode()
changed_string = decoded_to_string.replace('<year>2000</year>', '<year>2001</year>')
encoded_result = ElementTree.fromstring(changed_string)
print(type(encoded_result))
'''
for movie in root.iter("movie"):
    print(movie.attrib["title"])
    for child in movie.findall("*"):
        print(child.tag + " " + child.text)


class Movie():
    def __init__(self, title, format, year, rating, description):
        self.title = title
        self.format = format
        self.year = year
        self.rating = rating
        self.description = description

    @classmethod
    def from_xml(cls, path:str):
        tree = ElementTree.parse(path)
        root = tree.getroot()
        listofmovies = []
        for movie in root.iter("movie"):
            child_list = {}
            for child in movie:
                child_list[child.tag] = child.text
            listofmovies.append(cls(movie.attrib["title"],movie.attrib["title"], **child_list))
        return listofmovies



movies = Movie.from_xml('example.xml')
print(movies)