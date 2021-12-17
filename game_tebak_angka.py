trying = 0
secret_number = 1
limit = 3 

while trying < limit:
    guess_number = input('Masukan Angka Tebakan (1-9) ')
    guess_number = int(guess_number)

    if guess_number == secret_number:
        print("Selamat Kamu Menang")
        break

    trying += 1