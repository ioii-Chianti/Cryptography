from Crypto.Util.number import bytes_to_long, getPrime, long_to_bytes
from secret import Plaintext

Secret = bytes_to_long(Plaintext)
# Hint
KeySample = [74089417067, 114994172407, 72102631451, 108096169151, 133358729069, 72064476409, 100851509809, 135254530223, 96197997583, 76329142727, 79484969159, 101335858829, 108564152173, 108718891481, 133662033419, 118536692983, 86811334123, 90392968811, 100580257727, 107864071597, 106493926789, 70555994903, 120277737059, 98947022101]
LeftBlockSample = [465774765420, 145977150047, 374879796932, 440198491264, 172306527995, 349760367894, 454032621332, 204582664243, 384024977288, 415242867636, 171838080507, 387311613576, 436876430846, 166910362651, 387542804540, 429381069356, 147556968167, 367560775968, 424205074860, 138442405683, 394640730930, 425506668932, 174435869089, 376044535366]
RightBlockSample = [145977150047, 374879796932, 440198491264, 172306527995, 349760367894, 454032621332, 204582664243, 384024977288, 415242867636, 171838080507, 387311613576, 436876430846, 166910362651, 387542804540, 429381069356, 147556968167, 367560775968, 424205074860, 138442405683, 394640730930, 425506668932, 174435869089, 376044535366, 447121433330]

def FeistelFunction(RightBlock, Key):
    Result = RightBlock ^ Key
    return Result

def Feistel(PlaintextBlock, Keys):
    rounds = 24
    Keys = Keys[:]
    LeftBlockSample = []
    RightBlockSample = []
    InitialLeftBlock = int(str(PlaintextBlock)[:12])
    InitialRightBlock = int(str(PlaintextBlock)[12:])
    CurrentLeftBlock = InitialLeftBlock
    CurrentRightBlock = InitialRightBlock
    LeftBlockSample.append(CurrentLeftBlock)
    RightBlockSample.append(CurrentRightBlock)
    # Round 0 to 23
    for i in range(0, rounds):
        NextLeftBlock = CurrentRightBlock
        NextRightBlock = FeistelFunction(CurrentRightBlock, Keys[i]) ^ CurrentLeftBlock
        CurrentLeftBlock = NextLeftBlock
        CurrentRightBlock = NextRightBlock
        LeftBlockSample.append(CurrentLeftBlock)
        RightBlockSample.append(CurrentRightBlock)
    # after last round
    Ciphertext = str(CurrentLeftBlock) + str(CurrentRightBlock)
    print("The Left Block sample:", LeftBlockSample)
    print("The Right Block sample:", RightBlockSample)
    return Ciphertext

# Keys = [ getPrime(37) for i in range(24) ] # getPrime return a 2^37 bits
# Ciphertext = Feistel(Secret, Keys)
# print("The Ciphertext:", Ciphertext)

def FeistelReverse(left_samples, right_samples, keys_samples):
    rounds = 24
    current_left = left_samples[-1]
    current_right = right_samples[-1]

    for i in range(rounds):
        # Reverse the Feistel function
        next_right = current_left
        next_left = right_samples[rounds - i - 1] ^ (current_right ^ next_right)
        current_left = next_left
        current_right = next_right

    plaintext = (current_left << 48) + current_right
    return long_to_bytes(plaintext)

plaintext = FeistelReverse(LeftBlockSample, RightBlockSample, KeySample)
print("The Plaintext:", bytes_to_long(plaintext))