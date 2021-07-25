endpoint = "http://localhost:5000"

# Fill in the correct API key
api_key = "scientist007"

# Create the web API’s URL
authenticated_endpoint = "{}/{}".format(endpoint, api_key)

# Get the web API’s reply to the endpoint
api_response = requests.get(authenticated_endpoint).json()
pprint.pprint(api_response)

# Create the API’s endpoint for the shops
shops_endpoint = "{}/{}/{}/{}".format(endpoint,
                                      api_key, "diaper/api/v1.0", "shops")
shops = requests.get(shops_endpoint).json()
print(shops)

# Create the API’s endpoint for items of the shop starting with a "D"
items_of_specific_shop_URL = "{}/{}/{}/{}/{}".format(
    endpoint, api_key, "diaper/api/v1.0", "items", "DM")
products_of_shop = requests.get(items_of_specific_shop_URL).json()
pprint.pprint(products_of_shop)

"""
<script.py> output:
    {'apis': [{'description': 'list the shops available',
               'url': '<api_key>/diaper/api/v1.0/shops'},
              {'description': 'list the items available in shop',
               'url': '<api_key>/diaper/api/v1.0/items/<shop_name>'}]}
    {'shops': ['Aldi', 'Kruidvat', 'Carrefour', 'Tesco', 'DM']}
    {'items': [{'brand': 'Huggies',
                'countrycode': 'DE',
                'currency': 'EUR',
                'date': '2019-02-01',
                'model': 'newborn',
                'price': 6.8,
                'quantity': 40},
               {'brand': 'Huggies',
                'countrycode': 'AT',
                'currency': 'EUR',
                'date': '2019-02-01',
                'model': 'newborn',
                'price': 7.2,
                'quantity': 40}]}
                """
