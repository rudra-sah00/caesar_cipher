alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(""" ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88          """)
print("""                                                             
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88                                             """)
def encrypt(fn_text, fn_shift):
    encrypted_text = ""
    for i in fn_text:
        if i in alphabet:
            index = alphabet.index(i)
            new_index = (fn_shift + index) % 26
            new_word = alphabet[new_index]
            encrypted_text += new_word
        else:
            encrypted_text += i
    print("Your encoded text is : ", encrypted_text)
def decrypt(fn_text,fn_shift):
    decrypted_text = ""
    for i in fn_text:
        if i in alphabet:
            index = alphabet.index(i)
            new_index = (index - fn_shift) % 26
            new_word = alphabet[new_index]
            decrypted_text += new_word
        else:
            decrypted_text += i
    print("Your decoded text is : ", decrypted_text)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to ENCRYPT or 'decode' to DECRYPT:\n")
    if direction == "encode":
        shift = int(input("Type the shift number :\n"))
        text = input("Type your Message :\n").lower()
        encrypt(fn_text=text, fn_shift=shift)
    elif direction == "decode":
        shift = int(input("Type the shift number :\n"))
        text = input("Type your Message :\n").lower()
        decrypt(fn_text=text, fn_shift=shift)
    else:
        print("Please type a valid input")

    final_message = input("Type 'yes' if you want to continue again. Otherwise type 'no'.\n").lower()
    if final_message == "no":
        should_continue = False



