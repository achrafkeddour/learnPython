"""match case"""

day = 'sunday'

match day:
    case "friday" | "saturday":
        is_weekend = True
    case "sunday" | "monday" | "tuesday" | "wednesday" | "thursday":
        is_weekend = False
    case _:
        is_weekend = False
        print("hada machi nhar ta3 el week hahaha")
    
print(f"the state of is_weekend is : {is_weekend}")