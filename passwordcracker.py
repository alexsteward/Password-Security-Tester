import hashlib
import itertools
import threading
import time

class PasswordCracker:
    def __init__(self, target_hash, hash_type, max_length):
        self.target_hash = target_hash
        self.hash_type = hash_type
        self.max_length = max_length
        self.found_password = None

    def hash_password(self, password):
        if self.hash_type == 'md5':
            return hashlib.md5(password.encode()).hexdigest()
        elif self.hash_type == 'sha1':
            return hashlib.sha1(password.encode()).hexdigest()
        elif self.hash_type == 'sha256':
            return hashlib.sha256(password.encode()).hexdigest()
        else:
            raise ValueError("Unsupported hash type")

    def brute_force(self):
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        for length in range(1, self.max_length + 1):
            for password in itertools.product(characters, repeat=length):
                password_str = ''.join(password)
                if self.hash_password(password_str) == self.target_hash:
                    self.found_password = password_str
                    print(f"Password found: {self.found_password}")
                    return
        print("Password not found.")

    def dictionary_attack(self, password_list):
        with open(password_list, 'r') as file:
            for password in file:
                password = password.strip()
                if self.hash_password(password) == self.target_hash:
                    self.found_password = password
                    print(f"Password found: {self.found_password}")
                    return
        print("Password not found.")

    def start_cracking(self, password_list):
        thread1 = threading.Thread(target=self.brute_force)
        thread2 = threading.Thread(target=self.dictionary_attack, args=(password_list,))
        
        thread1.start()
        thread2.start()
        
        thread1.join()  
        thread2.join()  

if __name__ == "__main__":
    target_hash = input("Enter the hash to crack: ")
    hash_type = input("Enter the hash type (md5, sha1, sha256): ")
    max_length = int(input("Enter the maximum password length: "))
    
    password_list = 'passwords.txt'
    
    cracker = PasswordCracker(target_hash, hash_type, max_length)
    start_time = time.time()
    cracker.start_cracking(password_list)
    end_time = time.time()
    print(f"Cracking completed in {end_time - start_time:.2f} seconds.")
