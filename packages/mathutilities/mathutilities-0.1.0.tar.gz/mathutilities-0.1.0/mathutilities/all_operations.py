from .operations import add,subtract,multiply,divide
from .geometry import circle_area,circle_circumference

def all_op(a,b):
    result= {"Addition":add(a,b),
                            "Subtraction":subtract(a,b),
                            "Multiplication":multiply(a,b),
                            "Division":divide(a,b)}
    return result
