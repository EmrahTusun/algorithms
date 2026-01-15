import sys
import os

""" Üst klasördeki 'Data_Structures' klasörüne erişim izni veriyoruz. 
Burada Python'un hazır dict yapısını kullanmayacağım.
Kendi yazdığım Data_Structures/hash_map.py dosyasını bu projenin içine import edip kullanacağım."""
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(os.path.join(parent_dir, "Data_Structures"))

# Kendi yazdığım Hash Table sınıfını çağırıyoruz!
try:
    from hash_map import HashTable
except ImportError:
    print("Hata: hash_map.py bulunamadı! Lütfen Data_Structures klasörünü kontrol et.")
    sys.exit(1)

def print_menu():
    print("\n" + "="*30)
    print(" HIZLI REHBER (Hash Map ile)")
    print("="*30)
    print("1. Kişi Ekle / Güncelle")
    print("2. Kişi Ara (Hızlı)")
    print("3. Kişi Sil")
    print("4. Çıkış")
    print("="*30)

def main():
    # Rehber için Hash Table oluşturuyoruz (Boyutu ihtiyaca göre artırılabilir)
    my_phonebook = HashTable(size=50)

    while True:
        print_menu()
        choice = input("Seçiminiz (1-4): ")

        if choice == '1':
            name = input("İsim: ").strip()
            number = input("Numara: ").strip()
            if name and number:
                my_phonebook.set(name, number)
                print(f"{name} rehbere eklendi.")
            else:
                print("İsim veya numara boş olamaz!")

        elif choice == '2':
            name = input("Aranacak İsim: ").strip()
            result = my_phonebook.get(name)
            if result:
                print(f"BULUNDU -> {name}: {result}")
            else:
                print("Kişi bulunamadı.")

        elif choice == '3':
            name = input("Silinecek İsim: ").strip()
            is_deleted = my_phonebook.remove(name)
            if is_deleted:
                print(f"{name} silindi.")
            else:
                print("Kişi bulunamadı.")

        elif choice == '4':
            print("Görüşmek üzere...")
            break
        else:
            print("Geçersiz seçim, tekrar dene.")

if __name__ == "__main__":
    main()