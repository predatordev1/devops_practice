import string
def check_password_strength(input_string):
    c = 0
    if len(input_string)>=8:
        is_digit = any(char.isdigit() for char in input_string)
        is_lower = any(char.islower() for char in input_string)
        is_upper = any(char.isupper() for char in input_string)
        if (is_digit==is_lower==is_upper==True):
            return True
        else:
            return False
    else:
        return False
    
def is_special_character(input_string):
    for char in input_string:
        if char in string.punctuation:
            return True
    return False

input_string = str(input("Enter your password :"))
if (check_password_strength(input_string)==True & is_special_character(input_string)==True):
    print("Your password is stong")
else:
    print("Your is password weak. Please create a strong password")
