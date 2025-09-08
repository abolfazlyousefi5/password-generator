import random
import string

# --- character sets ---
lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbols = "!@#$%^&*()_-+=/~`<>?."
numbers = "0123456789"

all_character = lower + upper + symbols + numbers

while True:
    print("Choose An Option : \n\t1)Create a Password\n\t2)Exit")
    choice = input("Your Choice : ")
    
    if choice == "1":
        length = int(input("Enter The Length Of Password : "))
        
        if length <= len(all_character):
            # unique characters (no repetition)
            password = "".join(random.sample(all_character, length))
        else:
            # allow repetition if requested length is too long
            password = "".join(random.choices(all_character, k=length))
        
        print("Generated Password:", password, "\n")
    
    elif choice == "2":
        print("Goodbye!")
        break
    
    else:
        print("Your Choice Is Wrong!\n")
