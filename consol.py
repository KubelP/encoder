'''Argpars consol'''
import argparse
from cryptografer import Cryptografer
from salt import salt

class Console:
    '''class Consol is argpars controled consol. Is coupled with encding Cryptografer class '''
    def __init__(self):
        self.text = None
        self.parser = argparse.ArgumentParser(prog= 'Cryptographer',
        description= 'Encrypt and decrypt app')
        add_arg = self.parser.add_argument('text',
                            help='put text to encrypt or decrypt')
        ass_arg = self.parser.add_argument('password',
                            help='password used for encryption and decryption')
        add_arg = self.parser.add_argument('-e', '--encrypt',
                            action='store_true',help='if you want to encrypt')
        add_arg = self.parser.add_argument('-d', '--decrypt',
                            action='store_true', help='if you want to decrypt')
        self.args = self.parser.parse_args()

    def args_parameters(self):
        '''args_parameters method puts text to encrypt as argument for Cryptografer object'''
        bytes_args = bytes(self.args.text, 'utf-8')
        bytes_password = bytes(self.args.password, 'utf-8')
        self.text = Cryptografer(bytes_password, salt, bytes_args)
        return self.text

    def encrypting(self):
        '''ecrypting method'''
        self.text.kdf()
        encrypted = self.text.encrypt().decode('utf-8')
        return f'\nencrypted text\n ----- {encrypted} -----\n' 

    def decrypting(self):
        '''decrypting method'''
        self.text.kdf()
        decrypted = self.text.decrypt().decode('utf-8')
        return f'\ndecrypted text\n ----- {decrypted} -----\n' 
