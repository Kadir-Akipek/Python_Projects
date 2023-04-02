import random

def computer_guess(x):
    low = 1
    high = x
    feedback = " "
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"{guess} tuttuğunuz sayıdan çok yüksek ise (Y), çok düşük ise (K), doğru ise (C) yi girin: ").lower()
        if feedback == "y":
            high = guess - 1
        elif feedback == "k":
            low = guess + 1

    print(f"Bilgisayar sayınızı doğru tahmin etti cevap {guess} ")

computer_guess(10)
