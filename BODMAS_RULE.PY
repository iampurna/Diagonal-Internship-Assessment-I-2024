# The Bodmas rule follows the order of the BODMAS acronym ie  B – Brackets, O – Order of powers or 
#roots, D – Division, M – Multiplication A – Addition, and S – Subtraction. Mathematical expressions 
#with multiple operators need to be solved from left to right in the order of BODMAS.

def calculate_expression(expression):
    return eval(expression)

if __name__ == "__main__":
    expression = "3 * (2 + 4) + 5"
    result = calculate_expression(expression)
    print("Result:", result)