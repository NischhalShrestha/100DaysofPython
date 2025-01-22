alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt & Type 'decode' to decrypt : \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

#this is the long version

# def caesar():
#     if direction == "encode":
#         def encrypt(original_text, shift_amount):
#             cipher_text = ""

#             for letter in original_text:
#                 shifted_position = alphabet.index(letter) + shift_amount
#                 shifted_position %= len(alphabet)
#                 cipher_text += alphabet[shifted_position]

#             print(f"the encoded result for the input is: {cipher_text}")

#         encrypt(original_text= text, shift_amount=shift)

#     elif direction == "decode":
#         def decrypt(original_text, shift_amount):
#             deciphered_text =""

#             for letter in original_text:
#                 shifted_position = alphabet.index(letter) - shift_amount
#                 shifted_position %= len(alphabet)
#                 deciphered_text += alphabet[shifted_position]

#             print(f"the decoded text is: {deciphered_text}")

#         decrypt(original_text=text, shift_amount=shift)

#     else:
#         print("Input Error")

# caesar()


#this is the short version

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:
        if encode_or_decode == 'decode':
            shift_amount *= -1
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result:  {output_text}")

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
