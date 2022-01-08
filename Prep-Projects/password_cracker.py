# A basic Password Cracking tool.  
#testing
#construct logic for a basic password cracking

import crypt 
import optparse

def test_password(crypt_password, dname):
    salt = crypt_password[0:2]
    dict_File = open(dname, 'r')
    for word in dict_File.readlines():
        word = word.strip ('\n')
        cryptWorld = crypt.crypt(word,salt)
        if (cryptWorld == crypt_password):
            print "Password Cracked: "+word+"\n"
            return
    print "Password Not Found. \n"
    return