from math import sqrt, modf
import hashlib


def isPrime(n):
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c = c + 1
    return c == 2


def rightRotate(string, places):
    return string[len(string) - places:] + string[:len(string) - places]


def rightShift(string, places):
    return '0' * places + string[:len(string) - places]


def messageSchedule(w):
    for i in range(16, 64):
        s0 = int(rightRotate(w[i - 15], 7), 2) ^ int(rightRotate(w[i - 15], 18), 2) ^ int(rightShift(w[i - 15], 3), 2)

        s1 = int(rightRotate(w[i - 2], 17), 2) ^ int(rightRotate(w[i - 2], 19), 2) ^ int(rightShift(w[i - 2], 10), 2)

        new_wi = int(w[i - 16], 2) + s0 + int(w[i - 7], 2) + s1
        new_wi = new_wi % (2 ** 32)
        new_wi = '{0:08b}'.format(new_wi)
        new_wi = '0' * (32 - len(new_wi)) + new_wi

        w[i] = new_wi


def compression(w, H, k):
    a, b, c, d, e, f, g, h = list(H.values())

    for i in range(64):
        s1 = int(rightRotate(e, 6), 2) ^ int(rightRotate(e, 11), 2) ^ int(rightRotate(e, 25), 2)
        ch = (int(e, 2) & int(f, 2)) ^ ((~(int(e, 2))) & int(g, 2))
        temp1 = int(h, 2) + s1 + ch + int(k[i], 16) + int(w[i], 2)
        temp1 = temp1 % (2 ** 32)
        s0 = int(rightRotate(a, 2), 2) ^ int(rightRotate(a, 13), 2) ^ int(rightRotate(a, 22), 2)
        maj = (int(a, 2) & int(b, 2)) ^ (int(a, 2) & int(c, 2)) ^ (int(b, 2) & int(c, 2))
        temp2 = s0 + maj
        temp2 = temp2 % (2 ** 32)
        h = g
        g = f
        f = e
        e = int(d, 2) + temp1
        e = e % (2 ** 32)
        e = '{0:08b}'.format(e)
        d = c
        c = b
        b = a
        a = temp1 + temp2
        a = a % (2 ** 32)
        a = '{0:08b}'.format(a)
        a = "0" * (32 - len(a)) + a
        b = "0" * (32 - len(b)) + b
        c = "0" * (32 - len(c)) + c
        d = "0" * (32 - len(d)) + d
        e = "0" * (32 - len(e)) + e
        f = "0" * (32 - len(f)) + f
        g = "0" * (32 - len(g)) + g
        h = "0" * (32 - len(h)) + h

    return a, b, c, d, e, f, g, h


def convertToSHA256(string):
    values = [ord(x) for x in list(string)]  # String to ASCII
    values = ['{0:08b}'.format(x) for x in values]  # ASCII to Binary
    inp_length = len(values) * 8
    values.append('10000000')
    while len(values) * 8 % 512 != 0:  # Pad 0's until data is multiple of 512
        values.append('00000000')
    del values[-9:-1]
    be_length = list(map('{0:08b}'.format, list((inp_length).to_bytes(8, byteorder="big"))))
    values.extend(be_length)
    H = {}
    c = 0
    n = 0
    while len(H) < 8:
        if isPrime(n):
            H[c] = hex(int(modf(sqrt(n))[0] * (1 << 32)))
            c += 1
        n += 1
    k = {}
    c = 0
    n = 0
    while len(k) < 64:
        if isPrime(n):
            k[c] = hex(int(modf(n ** (1 / 3))[0] * (1 << 32)))
            c += 1
        n += 1
    message_block = []
    message_block.extend(["".join(values)[i:i + 32] for i in range(0, 512, 32)])
    message_block.extend(['0' * 32 for _ in range(48)])
    rightRotate("00110010", 2)
    rightShift("101010", 3)
    messageSchedule(message_block)
    H = {x: int(y, 16) for x, y in list(H.items())}
    H = {x: '{0:08b}'.format(y) for x, y in list(H.items())}
    H = {x: "0" * (32 - len(y)) + y for x, y in list(H.items())}
    var = compression(message_block, H, k)
    for i in range(8):
        H[i] = int(H[i], 2) + int(var[i], 2)
        H[i] = H[i] % (2 ** 32)
        H[i] = '{0:08b}'.format(H[i])
    calculated_sha256 = "".join(["{:x}".format(int(x, 2)) for x in H.values()])
    return calculated_sha256


real_sha256 = hashlib.sha256("hello".encode('utf-8')).hexdigest()
print(real_sha256 == convertToSHA256('hello'))
