import random                        
def generate_password(length):
    list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"

    selected_char = random.sample(list_of_chars, length)
   
    pass_str = "".join(selected_char)  

    return pass_str  

if __name__ == "__main__":  
    
    length = int(input("Please enter the length of the password: "))

    pass_str = generate_password(length)

    print("A randomly generated password is:", pass_str)