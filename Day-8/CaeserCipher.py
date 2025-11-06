from CaeserCipher_art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(start_text, shift_amount, cipher_direction) :
    end_text = ""

    if cipher_direction == "decode" :
            shift_amount *= -1      
    
    for char in start_text :
        
        if char in alphabet :
            index_value = alphabet.index(char)
        
            new_index_value = index_value + shift_amount
            end_text += alphabet[new_index_value]

        else :
            end_text += char    

    print(f"The {cipher_direction}d text is {end_text}")

should_continue = True

while should_continue :

    direction = input("Type 'endcode' to encrypt, type 'decode' to decrypt:\n")

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26   


    caeser(start_text = text, shift_amount = shift, cipher_direction = direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no" :
        should_continue = False
        print("Good Bye!")
