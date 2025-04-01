"""
When a Python file is run directly, the __name__ variable is set to "__main__".
When a Python file is imported as a module into another script, the __name__ variable is set to the name of the file (without .py).
So, if __name__ == "__main__": checks if the script is being run directly or if it’s being imported
"""


def greet():
    print("hello world !")
    
print("this code will always run") # ghir nrouh l code akhour wnktb 'import name_ta3_had_module' elle s'execute automatiquement

def main():
    greet()
    


# this means beli la fonction main() (ay 7aja sous cette condition) man9drch nexecutiha juste par 'import module'
if __name__ == '__main__': 
    main()