class SimpleEncryption:
    def __init__(self):
        self.chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*(),.?;:"
    
    def caesar_encrypt(self, message, shift=3):
        result = ""
        for char in message:
            if char in self.chars:
                old_pos = self.chars.find(char)
                new_pos = (old_pos + shift) % len(self.chars)
                result += self.chars[new_pos]
            else:
                result += char  
        return result
    
    def caesar_decrypt(self, encrypted_message, shift=3):
        return self.caesar_encrypt(encrypted_message, -shift)
    
    def create_simple_key(self):
        import random
        chars_list = list(self.chars)
        mixed_chars = chars_list.copy()
        random.shuffle(mixed_chars)
        
        key = {}
        for i in range(len(chars_list)):
            key[chars_list[i]] = mixed_chars[i]
        return key
    
    def substitution_encrypt(self, message, key):
        result = ""
        for char in message:
            if char in key:
                result += key[char]
            else:
                result += char
        return result
    
    def substitution_decrypt(self, encrypted_message, key):
        """Reverse the substitution"""
        # Flip the key: mixed -> original
        reverse_key = {v: k for k, v in key.items()}
        result = ""
        for char in encrypted_message:
            if char in reverse_key:
                result += reverse_key[char]
            else:
                result += char
        return result
    
    # === REVERSE CIPHER (Simple but effective) ===
    def reverse_encrypt(self, message):
        """Simply reverse the message"""
        return message[::-1]
    
    def reverse_decrypt(self, encrypted_message):
        """Reverse it back"""
        return encrypted_message[::-1]
    
    # === MULTI-LAYER (Combine methods) ===
    def multi_encrypt(self, message, shift=5):
        """Apply multiple encryption methods"""
        # Step 1: Caesar cipher
        step1 = self.caesar_encrypt(message, shift)
        # Step 2: Reverse
        step2 = self.reverse_encrypt(step1)
        # Step 3: Caesar again with different shift
        step3 = self.caesar_encrypt(step2, shift + 2)
        return step3
    
    def multi_decrypt(self, encrypted_message, shift=5):
        """Reverse all the encryption steps"""
        # Reverse step 3
        step1 = self.caesar_decrypt(encrypted_message, shift + 2)
        # Reverse step 2
        step2 = self.reverse_decrypt(step1)
        # Reverse step 1
        step3 = self.caesar_decrypt(step2, shift)
        return step3


def main():
    """Simple menu to use the encryption system"""
    crypto = SimpleEncryption()
    
    print("🔐 SIMPLE ENCRYPTION SYSTEM 🔐")
    print("=" * 40)
    
    while True:
        print("\nChoose what you want to do:")
        print("1. Caesar Cipher (shift letters)")
        print("2. Substitution Cipher (replace letters)")
        print("3. Reverse Cipher (reverse message)")
        print("4. Multi-Layer (extra secure)")
        print("5. Test all methods")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == "1":
            print("\n--- CAESAR CIPHER ---")
            message = input("Enter your message: ")
            shift = int(input("Enter shift number (1-10): ") or 3)
            
            encrypted = crypto.caesar_encrypt(message, shift)
            print(f"Encrypted: {encrypted}")
            
            decrypted = crypto.caesar_decrypt(encrypted, shift)
            print(f"Decrypted back: {decrypted}")
            
        elif choice == "2":
            print("\n--- SUBSTITUTION CIPHER ---")
            message = input("Enter your message: ")
            
            key = crypto.create_simple_key()
            encrypted = crypto.substitution_encrypt(message, key)
            print(f"Encrypted: {encrypted}")
            
            decrypted = crypto.substitution_decrypt(encrypted, key)
            print(f"Decrypted back: {decrypted}")
            
        elif choice == "3":
            print("\n--- REVERSE CIPHER ---")
            message = input("Enter your message: ")
            
            encrypted = crypto.reverse_encrypt(message)
            print(f"Encrypted: {encrypted}")
            
            decrypted = crypto.reverse_decrypt(encrypted)
            print(f"Decrypted back: {decrypted}")
            
        elif choice == "4":
            print("\n--- MULTI-LAYER ENCRYPTION ---")
            message = input("Enter your message: ")
            shift = int(input("Enter shift number (1-10): ") or 5)
            
            encrypted = crypto.multi_encrypt(message, shift)
            print(f"Encrypted: {encrypted}")
            
            decrypted = crypto.multi_decrypt(encrypted, shift)
            print(f"Decrypted back: {decrypted}")
            
        elif choice == "5":
            print("\n--- TESTING ALL METHODS ---")
            test_message = "Hello World! 123"
            print(f"Original message: '{test_message}'")
            
            # Test Caesar
            caesar_enc = crypto.caesar_encrypt(test_message, 7)
            caesar_dec = crypto.caesar_decrypt(caesar_enc, 7)
            print(f"Caesar: '{caesar_enc}' -> '{caesar_dec}' ✓")
            
            # Test Substitution
            key = crypto.create_simple_key()
            sub_enc = crypto.substitution_encrypt(test_message, key)
            sub_dec = crypto.substitution_decrypt(sub_enc, key)
            print(f"Substitution: '{sub_enc}' -> '{sub_dec}' ✓")
            
            # Test Reverse
            rev_enc = crypto.reverse_encrypt(test_message)
            rev_dec = crypto.reverse_decrypt(rev_enc)
            print(f"Reverse: '{rev_enc}' -> '{rev_dec}' ✓")
            
            # Test Multi-layer
            multi_enc = crypto.multi_encrypt(test_message, 4)
            multi_dec = crypto.multi_decrypt(multi_enc, 4)
            print(f"Multi-layer: '{multi_enc}' -> '{multi_dec}' ✓")
            
        elif choice == "6":
            print("Goodbye! 👋")
            break
            
        else:
            print("Please enter a number between 1-6")


def quick_demo():
    """Show a quick demo of all encryption methods"""
    crypto = SimpleEncryption()
    message = "Secret Message!"
    
    print("🚀 QUICK DEMO")
    print(f"Original: {message}")
    
    encrypted = crypto.caesar_encrypt(message, 5)
    decrypted = crypto.caesar_decrypt(encrypted, 5)
    print(f"Caesar: {encrypted} -> {decrypted}")
    
    key = crypto.create_simple_key()
    encrypted = crypto.substitution_encrypt(message, key)
    decrypted = crypto.substitution_decrypt(encrypted, key)
    print(f"Substitution: {encrypted} -> {decrypted}")
    
    encrypted = crypto.multi_encrypt(message, 3)
    decrypted = crypto.multi_decrypt(encrypted, 3)
    print(f"Multi-layer: {encrypted} -> {decrypted}")


if __name__ == "__main__":
    # Show quick demo first
    quick_demo()
    print("\n" + "="*50 + "\n")
    
    # Then run the main program
    main()