
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter in alphabet:

            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

        else:
            output_text += letter
    print(f"Here is the {encode_or_decode}d result: {output_text}")
    play_loop = input("Would you like to play again? 'y' for yes and 'n' for no.\n").lower()
    if play_loop == "y":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(original_text=text, shift_amount= shift, encode_or_decode =direction)
    else:
        print("Goodbye")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)



