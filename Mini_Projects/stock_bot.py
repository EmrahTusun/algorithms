import random

def analyze_market(prices):
    """
    Fiyat listesini analiz eder ve maksimum karı bulur.
    Karmaşıklık: O(n) - Tek geçiş
    """
    if not prices or len(prices) < 2:
        return None, 0, 0, 0 # Yeterli veri yok

    min_price = float('inf') # Sonsuzluk (Başlangıç için)
    max_profit = 0
    
    buy_day = 0
    sell_day = 0
    
    # Geçici değişken (En düşük fiyatın gününü tutmak için)
    temp_buy_day = 0

    print(f"Fiyatlar Analiz Ediliyor: {prices}")
    print("-" * 40)

    for i, price in enumerate(prices):
        # 1. Adım: Yeni bir "en düşük" fiyat bulduk mu?
        if price < min_price:
            min_price = price
            temp_buy_day = i # Potansiyel alım günü
        
        #2. Adım: Şu anki karı hesapla
        current_profit = price - min_price
        
        #3. Adım: Bu kar rekor mu?
        if current_profit > max_profit:
            max_profit = current_profit
            buy_day = temp_buy_day #Gerçek alım günü
            sell_day = i           #Gerçek satım günü (bugün)

    return max_profit, buy_day, sell_day, min_price

def main():
    print("\nBORSA AL-SAT ROBOTU (O(n) Algoritması)")
    print("=" * 40)
    
    while True:
        print("\n1. Rastgele Piyasa Simülasyonu")
        print("2. Kendi Fiyatlarını Gir")
        print("3. Çıkış")
        
        choice = input("Seçiminiz: ")
        
        prices = []
        
        if choice == '1':
            #7 günlük rastgele borsa verisi üret (10$ ile 100$ arası)
            prices = [random.randint(10, 100) for _ in range(7)]
            
        elif choice == '2':
            try:
                user_input = input("Fiyatları virgülle girin (Örn: 7,1,5,3,6,4): ")
                prices = [int(x.strip()) for x in user_input.split(',')]
            except ValueError:
                print("Hatalı giriş! Sadece sayı girin.")
                continue
                
        elif choice == '3':
            print("Bol kazançlar!")
            break
        else:
            continue

        #Analizi Çalıştır
        profit, buy_at, sell_at, min_p = analyze_market(prices)

        if profit > 0:
            print("\nSONUÇ: Kâr Fırsatı Bulundu!")
            print(f"ALIM GÜNÜ: {buy_at + 1}. Gün (Fiyat: {prices[buy_at]}$)")
            print(f"SATIM GÜNÜ: {sell_at + 1}. Gün (Fiyat: {prices[sell_at]}$)")
            print(f"MAKSİMUM KÂR: {profit}$")
        else:
            print("\nSONUÇ: Piyasa hep düşüşte, alım yapma!")

if __name__ == "__main__":
    main()