message = input('>>> ')

emoji_map = {
    ":)" : '😀',
    ":(" : '🙁',
    "-_-" : '😑'
}

words = message.split(" ")

output = ''

for w in words :
    output = output + emoji_map.get(w, w) + ' '

print (output)