import math

print('Enter card number: ')
card = int(input())
length = int(math.log10(card)) + 1
if length == 16:
    card = str(card)
    digits = []
    for i in range(15):
        digits.append(int(card[i]))
        if i % 2 == 0:
            digits[i] *= 2
    sum = 0
    for i in range(15):
        if digits[i] > 9:
            digits[i] = (digits[i] // 10) + (digits[i] % 10)
        sum += digits[i]
    if (sum + int(card[15])) % 10 == 0:
        print('Valid card number')
    else:
        print('Oops, the card is invalid!')
else:
    print('Incorrect card length')
