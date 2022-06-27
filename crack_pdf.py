# crack encrypted pdf files

import pikepdf 
from tqdm import tqdm

#import and load a password list
passwords = [ line.strip() for line in open("password_list.txt")]

#iterate over every password in the password_list
for password in tqdm(passwords, "Decrypting the PDF"):
    try: 
        #open the pdf file you would like
        with pikepdf.open("your_pdf.pdf", password=password) as pdf:
            #if the password is found, break the loop
            print ("Password for the pdf found",password)
            break
    except pikepdf._qpdf.PasswordError as e:
        #if you find the wrong password continue the loop
        continue
