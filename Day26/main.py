import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (_, row) in df.iterrows()}

has_next = True
while has_next:
    name = input("Enter your name: ").upper()
    if name == "QUIT" or name == "EXIT":
        has_next = False
    else:
        print([nato_dict[c] for c in name if c in nato_dict])
    