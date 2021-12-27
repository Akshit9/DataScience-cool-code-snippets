from collections import defaultdict

Basket = defaultdict(lambda: 'Not Found')

Basket['Book'] = 'Machine Learning Book'
Basket['Food'] = 'Apple'
Basket['Accessories'] = 'Mobile'

print(Basket['Accessories'])

print(Basket['Car keys'])
