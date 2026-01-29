import day8logo

print(day8logo.logo)

alphabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]


def caesar(original_text, shift_amount, encode_or_decode):
    outputText = ""
    for i in original_text:
        if i not in alphabet:
            outputText += i
        else:
            if encode_or_decode == "encode":
                newIndex = (alphabet.index(i) + shift_amount) % len(alphabet)
                outputText += alphabet[newIndex]
            else:
                newIndex = (alphabet.index(i) - shift_amount)% len(alphabet)
                outputText += alphabet[newIndex]
    
    print(f"Here is the {encode_or_decode}d result: {outputText}")

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number: "))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")
    
