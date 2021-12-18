import marketplace.matematika

result = marketplace.matematika.plus(10,8)
print(result)

from marketplace import matematika

result = matematika.plus(10, 8)
print(result)

from marketplace.matematika import plus, minus

result = plus(10, 8)
print(result)

result = minus(10, 8)
print(result)