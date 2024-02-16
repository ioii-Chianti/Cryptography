def CaesarCipher(Plaintext,key):
    Ciphertext = ""

    # traverse Plaintext
    for i in range(len(Plaintext)):
        char = Plaintext[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            Ciphertext += chr((ord(char) + key - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            Ciphertext += chr((ord(char) + key - 97) % 26 + 97)

    return Ciphertext


# same as CaesarCipher()
def Encrypt(plaintext, key):
	ciphertext = ""
     
	for ch in plaintext:
		if (ch.isupper()):
			ciphertext += chr((ord(ch) + key - 65) % 26 + 65)
		else:
			ciphertext += chr((ord(ch) + key - 97) % 26 + 97)
               
	return ciphertext


def Decrypt(ciphertext, key):
    plaintext = ""

    for ch in ciphertext:
        flag = False
        if ch.isupper():
            ch = ch.lower()
            flag = True

        position = letters.find(ch)
        new_pos = (position - key) % 26
        new_ch = letters[new_pos]
        if flag:
            new_ch = new_ch.upper()
        plaintext += new_ch

    return plaintext


def frequency(str):
    str = str.lower()
    dict = {}

    for ch in str:
        keys = dict.keys()
        if ch in keys:
            dict[ch] += 1
        else:
            dict[ch] = 1

    return dict

letters = 'abcdefghijklmnopqrstuvwxyz'
ciphertexts = [
    "HvsQfmdhcufodvmWgHvsPsghTwszrWbHvsKcfzr",
    "GsqifwhmUcozgWgQcbtwrsbhwozwhmWbhsufwhmObrOjowzopwzwhm",
    "OhhoqygCtGsqifwhmWbqzirsGbccdwbuHfottwqObozmgwgCbHvfsohHcQcbtwrsbhwozwhm",
    "AcrwtwqohwcbAogeisforwbuFsdzomwbuFsdirwohwcbOfsWbhsfufwhmHvfsoh"
]
key = 14

for ciphertext in ciphertexts:
    print(f'Ciphertext: {ciphertext}')
    print(f' Plaintext: {Decrypt(ciphertext, key)}')
