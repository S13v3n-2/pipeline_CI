import os

a = 2

print("coucou", a)

secret = os.getenv("SECRET_API_TOKEN")

if secret:
    print("Le secret est accessible au script Python")
else:
    print("Le secret n'est pas accessible")