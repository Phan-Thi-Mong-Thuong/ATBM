# Cho k= 45 và Plaintext = PhanThiMongThuong.
# Hãy mã hóa theo thuật toán Ceasar bằng ngôn ngữ Python

def Ma_Hoa_Ceasar(Plaintext, k):
    KetQuaMaHoa = ""
    k = k % 26  

    for text in Plaintext:
        if text.isalpha():  
            ASCII = ord('A') if text.isupper() else ord('a')
            Ciphertext = chr((ord(text) - ASCII + k) % 26 + ASCII)
            KetQuaMaHoa += Ciphertext
        else:
            KetQuaMaHoa += text     #Nếu không phải chữ cái thì giữ nguyên
    return KetQuaMaHoa


Plaintext = "Phan Thi Mong Thuong"
k= 45
MaHoa = Ma_Hoa_Ceasar(Plaintext, k)
print("Bản mã ban đầu/Plaintext là: ", Plaintext)
print("Bản mã sau khi mã hóa/Ciphertext là: ",MaHoa)    
