'''main module do encoding and decofind text using fernet, and PBKDF2'''
from cryptography.fernet import InvalidToken
from consol import Console

encoder = Console()
encoder.args_parameters()

try:
    if encoder.args.encrypt:
        print(encoder.encrypting())
    elif encoder.args.decrypt:
        print(encoder.decrypting())
    else:
        print('no parameters added')
except InvalidToken:
    print('\n', '-'*15, 'Encode error: wrong password or non-encoded object', '-'*15, '\n')
