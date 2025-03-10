import getpass
from product import Product
from cart import Cart
from order import Order
from customer import Customer

# Kullanıcı adı ve şifre işlemleri
def update_password():
    global name, password
    while True:
        name = input('Kullanıcı adınızı girin: ')
        password = input('Şifrenizi girin: ') 
        reenter_password = input('Şifrenizi tekrar girin: ')  

        if password == reenter_password:
            print('Kullanıcı adı ve şifre oluşturuldu. Tebrikler!')
            break
        else:
            print('Şifre hatası! Lütfen tekrar deneyin.')

def log_in():
    failure_num = 0
    while True:
        input1 = input('Kullanıcı adınızı girin: ')
        input2 = getpass.getpass('Şifrenizi girin: ')

        if input1 == name and input2 == password:
            print("Giriş başarılı!")
            break

        failure_num += 1
        if failure_num == 3:
            print('** Çok fazla hatalı giriş yaptınız! **')
            exit()

# Ana menü işlemleri
def display_main_menu():
    print("\n=== Ana Menü ===")
    print("1. Ürün Ekle")
    print("2. Ürün Çıkar")
    print("3. Sepeti Görüntüle")
    print("4. Sepeti Tamamla")
    print("5. Çıkış")

def handle_product_selection(cart, product1, product2):
    print(f"Mevcut ürünler: {product1}, {product2}")
    product_choice = input("Hangi ürünü eklemek istersiniz? (Telefon/Laptop): ").strip()
    quantity = int(input("Kaç adet eklemek istersiniz? "))
    if product_choice == "Telefon":
        cart.add_product(product1, quantity)
    elif product_choice == "Laptop":
        cart.add_product(product2, quantity)
    else:
        print("Geçersiz ürün!")

def main():
    # Ürünlerin oluşturulması
    product1 = Product("Telefon", 5000, 10)
    product2 = Product("Laptop", 10000, 5)

    # Sepet oluşturuluyor
    cart = Cart()

    # Kullanıcı bilgisi
    name = input("Adınızı girin: ")
    email = input("E-posta adresinizi girin: ")

    # Müşteri oluşturuluyor
    customer = Customer(name, email)

    # Kullanıcı giriş işlemleri
    update_password()
    log_in()

    while True:
        display_main_menu()

        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            handle_product_selection(cart, product1, product2)
        elif choice == "2":
            remove_product_name = input("Çıkarmak istediğiniz ürünün adını girin: ").strip()
            cart.remove_product(remove_product_name)
        elif choice == "3":
            cart.display_cart()
        elif choice == "4":
            order = Order(customer, cart)
            order.place_order()
            break
        elif choice == "5":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
