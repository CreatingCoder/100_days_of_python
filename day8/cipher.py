  
alphabet = ['a', 'b', 'c','d', 'e', 'f','g', 'h', 'i','j', 'k', 'l','m', 'n', 'o','p', 'q', 'r','s', 't', 'u','v', 'w', 'x','y', 'z', 'a', 'b', 'c','d', 'e', 'f','g', 'h', 'i','j', 'k', 'l','m', 'n', 'o','p', 'q', 'r','s', 't', 'u','v', 'w', 'x','y', 'z']

direction = input("Type 'encode' to encrypt, 'decode' to decrypt: \n")
text = input('Type your message: ').lower()
shift = (int(input('Type the shift number:\n')))%26

def encrypt(plain_text, shift_amount):
    cipher_text = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(cipher_text)
    
    
def decrypt(encrypted_text, shift_amount):
    decrypted_text = ''
    for letter in encrypted_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        decrypted_text += new_letter
    print(decrypted_text)
        
if(direction == 'encode'):
    encrypt(plain_text = text, shift_amount = shift)

elif(direction == 'decode'):
    decrypt(encrypted_text = text, shift_amount = shift)
    
    


    
