
def OneTimePad(Plaintext, Key):
    # 𝐸(𝑘,𝑚) = 𝑘 ⊕ 𝑚 → 𝑐.
	ciphertext = Plaintext ^ Key
	return ciphertext


def find_key(plaintext, ciphertext):
    return plaintext ^ ciphertext

plaintexts = (39853840534792837491, 64897348582397483930, 56283849582057392234, 29440380830575204857)
ciphertexts = (55802619614357762173, 13253755395686117623, 29103354247030841838, 20345633853066261022)

dict = {}
for plaintext in plaintexts:
    for ciphertext in ciphertexts:
        key = find_key(plaintext, ciphertext)
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 1
            
for key, cnt in dict.items():
    if cnt == 4:
        print(f'Key: {key}')