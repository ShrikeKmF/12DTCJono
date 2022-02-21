LEN, UP_MIN, LOW_MIN = 26, 65, 97


def getchar(ch, key, enc):
    if not ch.isalpha():
        return ch
    key = key if enc else -key
    (min, max) = (UP_MIN, UP_MIN + LEN) if ch.isupper() else (
    LOW_MIN, LOW_MIN + LEN)
    idx = ord(ch) + key
    mul = 1 if idx < min else (-1 if idx > max else 0)
    return chr(idx + mul * LEN)


def encdec(message, key, enc):
    result = []
    for i in message:
        result.append(getchar(i, key, enc))
    return ''.join(result)


print('Enter the message : ', end='')
message, key = input(), 0
while not (0 < key < LEN):
    print('Enter key [1-25]  : ', end='')
    key = int(input())
encMsg = encdec(message, key, True)
print('Encrypted message : %s' % encMsg)
decMsg = encdec(encMsg, key, False)
print('Decrypted message : %s' % decMsg)
