from os import urandom

def genkey(N):
    return urandom(N)

if __name__ == '__main__':
    print("input messege:", end="")
    message = input()

    key = genkey(len(message))
    print("key:", key)

    print(message.encode('utf-8'))
    cypherTex = bytes([a ^ b for a, b in zip(message.encode('utf-8'), key)])
    print(cypherTex)

#refer from https://en.wikipedia.org/wiki/XOR_cipher