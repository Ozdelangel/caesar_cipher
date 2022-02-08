


def encrypt(plain, key):
    # plain: '12345'
    # key: 2
    # -> 34567
    encrypted_text = ''

    # first thing we need to be able to go through the plain text

    for character in plain:
        # print(f'plain char of {character} no yet shifted by {key}')
        encrypted_character = int(character)
        encrypted_character += key
        if encrypted_character > 9:
            encrypted_character = encrypted_character %10
        # print(f'encrypted char of {character} shifted by {key}')
        encrypted_text += str(encrypted_character)
    return encrypted_text
    # shift the plain text
    # store the shifted value 
    # return the shifted value
def decrypt(encrypted, key):
    return encrypt(encrypted, -key)
if __name__ == '__main__':
#    enc1 = encrypt('12345', 2)
#    assert enc1 == ('34567')

#    enc2 = encrypt('678', 2)
#    assert enc2 == ('890')

    enc4 = decrypt('34567', 2)
    assert enc4 == '12345'