import random

def guessing_game():
    """Cipta permainan teka-teki makanan kegemaran menggunakan Python dan modul random."""
    print("-----------------------------------------------------------")
    print("****Selamat datang ke Permainan Teka Makanan Kegemaran!****")
    print("-----------------------------------------------------------")
    print("")

    # Senarai pilihan makanan
    food_options = [
        "1.nasi ayam",
        "2.chicken chop",
        "3.satay",
        "4.laksa",
        "5.nasi tomato",
        "6.spaghetti",
        "7.sushi"
    ]
    

    # Pilih makanan kegemaran secara rawak
    favorite_food = random.choice(food_options)

    # Bilangan percubaan
    attempts = 4

    while attempts:
        try:
            print(food_options) #memaparkan senarai makanan kegemaran
            guess_index = int(input("Teka makanan kegemaran saya dari senarai di atas (Sila taip nombor 1/2/3/4/5/6/7): "))
            if 1 <= guess_index <= len(food_options):
                guess = food_options[guess_index - 1]
                if guess.lower() == favorite_food:
                    print(f"Tahniah! Tekaan anda betul. Makanan kegemaran saya adalah {favorite_food}.")
                    break
                else:
                    print(f"Oops! Tekaan anda salah. Cuba lagi.")
                    print(f"Anda mempunyai {attempts} percubaan lagi.")
                    print("")
                    attempts -= 1
            else:
                print("Sila masukkan nombor yang betul antara 1 hingga 7.")
        except ValueError:
            print("Input tidak sah. Sila masukkan nombor yang betul.")

    if attempts == 0:
        print(f"Tiada percubaan lagi. Makanan kegemaran sebenar saya ialah {favorite_food}.")

# Panggil fungsi untuk bermain permainan teka-teki
guessing_game()
