''''
import hashlib

def crackHash(inputHash):

    try:
        passfile = open("dictionary1.txt", "r")

    except:
        print("Could not find")

    for password in passFile:
        encPass = password.encode("utf-8")
        digest = hashlib.md5(encPass.strip()).hexdigest()
        if digest == inputPass:
            print("Password Found: " + password)
            
if __name__ == '__main__':
        crackHash("3a8b7b53ab2be90f457869961f475aab:9997:1001")
'''

import hashlib

wordList =input("wordlist: ")
crackingHash=input("hash: ")

wlistlines=open(wordList, "r").readlines()

for i in range(0,len(wlistlines)):
    hashToReverse=hashlib.md5(wlistlines[i].replace("\n","").encode()).hexdigest()

    if crackingHash == hashToReverse:
        print("password is: "+wlistlines[i].replace("\n",""))
        exit()
print("password not found")
