# Cho k= 45 và Plaintext = PhanThiMongThuong.
# Mã hóa thay thế bằng phép toán cộng - Z26. 
def Ma_Hoa_Cong(Plaintext, k):
    ciphertext = ""  

    for text in Plaintext:
        if text.isalpha():
            base = ord('A') if text.isupper() else ord('a')
            encrypted = (ord(text) - base + k) % 26
            ciphertext += chr(encrypted + base)
        else:
            ciphertext += text   # Nếu không phải chữ cái thì giữ nguyên

    return ciphertext

P = "PhanThiMongThuong"
k = 45

C = Ma_Hoa_Cong(P, k)
print("Bản mã ban đầu/Plaintext là: ", P)   
print ("Khoá/Key là: ",k)
print("Bản mã sau khi mã hóa/Ciphertext là: ",C) 



