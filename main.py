class Cipher:
    def __init__(self, key):
        if (key < 0) or (key > 255):
            raise Exception("Key must be integer in range [0; 255]")
        self.key = key

    # Зашифровує 1 байт
    def encrypt_byte(self, data_byte):
        return data_byte ^ self.key

    # Розшифровує 1 байт
    def decrypt_byte(self, encrypted_data_byte):
        return encrypted_data_byte ^ self.key


if __name__ == '__main__':
    # Зчитуємо вміст файлу "secret.txt"
    with open("secret.txt", 'rb') as file:
        file_content = file.read()

    encrypted_content = bytearray(0)
    cipher_instance = Cipher(42)

    # Шифруємо кожен байт та додаємо до encrypted_content
    try:
        for byte in file_content:
            encrypted_byte = cipher_instance.encrypt_byte(byte)
            encrypted_content.append(encrypted_byte)
    except ValueError as e:
        print(f"Exception occurred: {e}")

    # Записуємо зашифрований контент у файл "encryptedSecret.txt"
    with open("encryptedSecret.txt", 'wb') as encrypted_file:
        encrypted_file.write(encrypted_content)

    # Розшифровуємо дані з "encryptedSecret.txt"
    decrypted_content = bytearray(0)
    try:
        for byte in encrypted_content:
            decrypted_byte = cipher_instance.decrypt_byte(byte)
            decrypted_content.append(decrypted_byte)
    except ValueError as e:
        print(f"Exception occurred: {e}")

    # Записуємо розшифровані дані у файл "revealedSecret.txt"
    with open("revealedSecret.txt", 'wb') as revealed_file:
        revealed_file.write(decrypted_content)

    # Перевіряємо, чи файли "secret.txt" та "revealedSecret.txt" мають однаковий вміст
    with open("secret.txt", 'rb') as original_file, open("revealedSecret.txt", 'rb') as revealed_file:
        original_content = original_file.read()
        revealed_content = revealed_file.read()

        if original_content == revealed_content:
            print("Encryption and decryption were successful!")
        else:
            print("Encryption or decryption failed.")
