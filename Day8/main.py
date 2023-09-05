import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',\
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
def caesar(text, shift, direction):
    caesar_text = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        try:
            indx = alphabet.index(char)
            caesar_text += alphabet[(indx + shift) % len(alphabet)]
        except ValueError:
            caesar_text += char
    return caesar_text

def main():
    print(art.logo)
    should_continue = True
    while should_continue:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        result = caesar(text, shift, direction)
        print(f"Here's the {direction}d result: {result}")
        
        answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if answer == 'no':
            should_continue = False
            print("Good Bye!")


if __name__ == "__main__":
    main()