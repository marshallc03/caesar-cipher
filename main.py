import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(in_text, shift_amount, encode_decode):
  out_text = ""
  if encode_decode == "decode":
      shift_amount *= -1
  for char in in_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      out_text += alphabet[new_position]
    else:
      out_text += char  
  print(f"Your {encode_decode}d message is {out_text}")

cipher_on = True

while cipher_on:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(in_text=text, shift_amount=shift, encode_decode=direction)
  
  repeat = input("Would you like to run again? Type 'y' or 'n':\n")
  if repeat.lower() == 'y':
    caesar(in_text=text, shift_amount=shift, encode_decode=direction)
  elif repeat.lower() == 'n':
    print("Goodbye")
  else:
    print("Pick a valid option.")
    print(repeat)

shift = shift % 26

caesar(in_text=text, shift_amount=shift, encode_decode=direction)