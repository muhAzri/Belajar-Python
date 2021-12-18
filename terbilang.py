numbers = input("Masukang angka : ")

numbers_map = {
    '0' : "Kosong",
    '1' : "Satu",
    '2' : "Dua",
    '3' : "Tiga",
    '4' : "Empat",
    '5' : "Lima",
    '6' : "Enam",
    '7' : "Tujuh",
    '8' : "Delapan",
    '9' : "Sembilan",
}

output = ''

for n in numbers :
    pronounce = numbers_map.get(n, 'Invalid')
    
    output = output + pronounce + ' '

print (output)
