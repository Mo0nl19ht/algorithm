def encode(c):
    encoded = ord(c)+3
    if encoded > ord('Z'):
        return chr(encoded-ord('Z')+ord('A')-1)
    return chr(encoded)
def decode(c):
    decoded = ord(c)-3
    if decoded < ord('A'):
        return chr(decoded-ord('A')+ord('Z')+1)
    return chr(decoded)
arr = list(input())
print("".join(list(map(decode,arr))))

