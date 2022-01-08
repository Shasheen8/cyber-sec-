# A basic Password Cracking tool.  
#testing
#construct logic for a basic password cracking

import crypt 
import optparse

def test_password(crypt_password, dict_name):
    salt = crypt_password[0:2]
    dict_File = open(dict_name, 'r')
    for word in dict_File.readlines():
        word = word.strip ('\n')
        cryptWorld = crypt.crypt(word,salt)
        if (cryptWorld == crypt_password):
            print "Password Found: "+word+"\n"
            return
    print "Password Not Found. \n"
    return

def main():
    passwordFile = open(password_name)
    for line in passwordFile.readlines():
        if ":" in line:
            user = line.split (":")[0]
            crypt_password = line.split(":")[1].strip('')
            print "Cracking Password: "+user
            test_password(crypt_password, dict_name)


main()