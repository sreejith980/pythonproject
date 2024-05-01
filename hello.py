alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z']
direction = str(input("Type 'encode' or decode the lined and type 'decode' for dcode the lines: ").lower())
text = str(input("ender the string: ").lower())
shift = int(input("Type the shift number: "))
cipher_text = ""
normaltext = ""
if direction == "encode":
    for name in text:
        position = alphabet.index(name)
        new_position = int(position) + int(shift)
        new_leater = alphabet[new_position]
        cipher_text = cipher_text + new_leater
    print(cipher_text)
elif direction == "decode":
    for name in text:
        position = alphabet.index(name)
        new_position = int(position) - int(shift)
        new_leater = alphabet[new_position]
        cipher_text = cipher_text + new_leater
    print(cipher_text)