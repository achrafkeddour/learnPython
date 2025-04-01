import app 
"""hadi execute tous ce qui dans le fichier app.py (sauf li rahou sous la condition if __name__ == '__main__')
par ce que lorsque on execute ce fichier 'app2.py' , pour le fichier app.py on a __name__ == 'app' 
                                                   , c pour le fichier app2.py li rahi __name__ == '__main__'
"""

app.greet() # l'appel manuel d'une fonction de app.py

app.main() # on peut appeller la fonction qui est protégé par la condition __name__ == '__main__' alors (mais manuellement)