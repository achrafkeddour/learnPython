# local , Enclosed , Global , Built-in

def funct1():
    x="achraf" #x here is a local variable (local in a function)
    print(f"hello {x}")


def funct2():
    x=1
    def funct3():
        print(x) # for funct3 , x is an enclosed variable . But for funct2 , x is local
    funct3()

funct2()


a = 4 # a is a global variable for the function funct4
def funct4():
    print(a)
    

# built-in : Predefined by Python. (like when we use math.e or math.pi after importing math )


"""chat gpt example : """

x = "global"  # Global variable

def outer():
    x = "enclosing"  # Enclosing variable
    
    def inner():
        x = "local"  # Local variable 
        print(x)  # Will print "local" (lokan mandirouch x = 'local' , ra7 yedi 'enclosing' automatiquement )
    
    inner()
    print(x)  # Will print "enclosing"

outer()
print(x)  # Will print "global"
