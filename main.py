import django
import requests

with open("requirements.txt", 'w') as file:
    file.write('requests, django')

with open("requirements.txt", 'r', encoding='utf-8') as file:
    print(file.readline()) 