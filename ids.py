#This code implements a simple IDS system that takes a list of files and hashes them using SHA-1. 
# It then compares the hashes of the files with a pre-defined set of known hashes for those files. 
# If any of the file hashes do not match the known hash, the system raises an intrusion alert by printing a message to the console.

# Note: This is just a basic implementation and there are many ways to improve and extend it, such as including more sophisticated 
# methods of hashing, adding a database to store known hashes, or including more advanced intrusion detection algorithms.

import hashlib

def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

# This is just an example hash, it will be different for your files
known_hashes = {
   "program.exe": "4bd5e566fc0dc08aec2062e48f16b9f48d0ea06b",
   "document.txt": "3e23e8160039594a33894f6564e1b1348bbd7a00"
}

def detect_intrusion(file_hashes):
   for file, file_hash in file_hashes.items():
       if file_hash != known_hashes.get(file):
           print("Intrusion detected in file: " + file)

def main():
   hashes = {}
   files = ["program.exe", "document.txt"]
   for file in files:
       hashes[file] = hash_file(file)

   detect_intrusion(hashes)

if __name__ == '__main__':
   main()
