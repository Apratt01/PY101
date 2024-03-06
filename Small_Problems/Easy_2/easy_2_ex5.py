CALCULATIONS = ['+', '-', '*', '/', '//', '%', '**']

def prompt(message):
    print(f"==> {message}")

def math(float1, float2, calc_type):
    match calc_type:
        case '+':  return float1 + float2
        case '-':  return float1 - float2
        case '*':  return float1 * float2
        case '/':  return float1 / float2
        case '//': return float1 // float2
        case '%':  return float1 % float2
        case '**': return float1 ** float2

def get_number():
    prompt("Enter the first number: ")
    float1 = float(input())
    
    prompt("Enter the second number: ")
    float2 = float(input())
    
    return float1, float2
    
def output(float1, float2):
    for calc_type in CALCULATIONS:
        calculate = (f"{float1} {calc_type} {float2}")
        result = math(float1, float2, calc_type)
        prompt(f"{calculate} = {result}")
    
def main():
    float1, float2 = get_number()
    output(float1, float2)

main()