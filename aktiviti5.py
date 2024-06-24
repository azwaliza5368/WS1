import random

no_tel="0174881004"
def cubateka():
    """Mula permainan teka makanan kegemaran."""
    #print("****Cuba teka makanan kegemaran saya!****")
    #print("")
    #print("2. chicken chop")
    #print("3. satay")
    #print("4. laksa")
    #print("5. nasi tomato")
    #print("6. spagetti")
    #print("7. sushi")
    

    
    pilihan = [
        "nasi ayam",
        "chicken chop",
        "satay",
        "laksa",
        "nasi tomato",
        "spagetti",
        "sushi"
    ]    
    print(pilihan)
    x =random.choice(pilihan)
    bil_cuba = 4
    cuba=0
    teka = None
    #print(x)
    while bil_cuba:
        teka = str(input("Sila teka makanan kegemaran saya dari senarai makanan di atas : "))
        print("")
        
        if x == teka:
            print(f"Tekaan anda tepat!!.Tahniah! Anda memang seorang yang bijak!".format(teka))
            print("Anda boleh menghubungi nombor ini",no_tel,"untuk saya belanja anda makan makanan kegemaran saya!")
            break
        else:
            print(f"Alamak tekaan anda salah! Sila cuba lagi.".format(teka))
            print(f"Anda masih ada {bil_cuba} peluang lagi untuk meneka.")
            print("")
            bil_cuba -= 1
        if bil_cuba == 0:
            print("")
            print(f"Peluang tamat. Makanan kegemaran saya yang sebenarnya ialah {x}.".format(teka))
        
cubateka()