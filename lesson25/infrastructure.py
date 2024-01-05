import requests
import json
import random
headers = {'content-type':'application/json'}

url = 'https://api.restful-api.dev/objects'
names = ['Geralt', 'Persik','Murka', 'Murzik Vasylyovich']
colours = ['black', 'white', 'ginger']
mass = [3,4,5,6,7]

class Cat:
    def __init__(self):
        self.data={
                "name": names[random.randrange(len(names)-1)],
                "data": {
                    "colour": colours[random.randrange(len(colours)-1)],
                    "mass": mass[random.randrange(len(mass)-1)],
                }
            }
        object_body = json.dumps(self.data)
        object_response = requests.post(url=url, headers=headers, data=object_body)
        self._id=object_response.json()['id']
        self.created_time = object_response.json()['createdAt']

    #def return_cat_dict():
    #    return {'id': self._id, 'name': self.data['name'], 'data': self.data['data']}

def genrate_a_lot_of_cats():
    list_of_cats=[]
    for i in range(random.randint(3,6)):
        list_of_cats.append(Cat())
    return list_of_cats


def filter_cats_and_only_cats():
    list_of_generated_cats = genrate_a_lot_of_cats()
    base_url_for_filter = url+'?'
    for cat in list_of_generated_cats:
        if cat != list_of_generated_cats[-1]:
            base_url_for_filter += f'id={cat._id}&'
        else:
            base_url_for_filter += f'id={cat._id}'
    print(base_url_for_filter)
    cats_response = requests.get(base_url_for_filter)
    return cats_response.json(), list_of_generated_cats

#https://api.restful-api.dev/objects?id=3&id=5&id=10



def get_single_object(object_id):
    return requests.get(f'{url}/{object_id}')

def create_an_object():

    object_body = json.dumps(
        {
            "name": "Nokia5320",
            "data": {
                "year": 207,
                "price": 1849.99,
            }
        }
    )
    object_response = requests.post(url=url, headers=headers, data=object_body)
    return object_response


def update_the_object(object_id):
    headers = {'content-type': 'application/json'}
    updated_object_body = json.dumps({
            "name": "Nokia5320",
            "data": {
                "year": 207,
                "price": 1849.99,
                'monochrome':False
            }
        })
    updated_object = requests.put(f'{url}/{object_id}', headers=headers, data=updated_object_body)
    return updated_object


def patch_object(object_id):
    headers = {'content-type': 'application/json'}
    updated_object_body = json.dumps({
        "data": {'year':208}
    })
    return requests.patch(f'{url}/{object_id}', headers=headers, data=updated_object_body)

def delete_object(object_id):
    return requests.delete(f'{url}/{object_id}')