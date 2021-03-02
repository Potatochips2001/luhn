import sys

if len(sys.argv) > 1:
    creditCardNumber = sys.argv[1]
else:
    try:
        creditCardNumber = int(input("Card number: "))
    except:
        print("Invalid input")
        exit()

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0

result = is_luhn_valid(creditCardNumber)
if (result == True):
    print("Card valid!")
else:
    print("Card invalid")
