print ("Masasukan Operasi +, -, *, /, exit.")

command = ''


while command != "Exit":
    command = input('Operasi ')

    if command == 'exit':
        break

    if command != '+' and command != '-' and command != '*'and command != '/' :
        print('Perintah tidak dikenali')
        continue

    a = int(input('Angka Pertama : '))
    b = int(input('Angka Kedua : ' ))

    if command == "+" :
        result = a + b

    elif command == '-':
        result = a - b

    elif command == '/':
        result = a / b

    elif command == '*':
        result = a * b

    print(f"Hasil : {result}")
    

print('Terimakasih Telah Menggunakan aplikasi kami')