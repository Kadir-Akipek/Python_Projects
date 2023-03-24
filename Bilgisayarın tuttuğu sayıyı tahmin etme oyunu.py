import random 

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"1 ile {x} arasında bir tamsayı tahmin ediniz: "))
        if guess < random_number:
            print("Üzgünüm, Tuttuğunuz sayı çok küçük. Tekrar deneyiniz: ")
        elif guess > random_number:
             print("Üzgünüm, Tuttuğunuz sayı çok büyük. Tekrar deneyiniz: ")

    print(f"Tebrikler. Doğru tahmin ettiniz, sayımız {random_number}")

guess(10)