import random
import sys

ssnList = []

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

numberOfCodes = None
cardOption = None
i = int(0)
currentCardNumber = int(0)
activeCards = []
usedCards = []

try:
    cardOption = int(input("Card type:\n1. Visa\n2. Mastercard\n3. Discover Card\n4. Social Security Number\n5. Amazon Gift Card\n"))
except KeyboardInterrupt:
    print("\nExiting")
    exit()
except:
    print("\nInvalid input")
    exit()

try:
    if len(sys.argv) > 1:
        numberOfCodes = sys.argv[1]
        numberOfCodes = int(numberOfCodes)
    else:
        numberOfCodes = int(input("Number of cards to generate: "))
except KeyboardInterrupt:
    print("\nExiting")
    exit()
except:
    print("\nInvalid input")
    exit()

if cardOption == 1:
    while len(activeCards) < numberOfCodes:
        try:
            currentCardNumber = int(random.randint(100000000000000, 999999999999999))
            currentCardNumber = str("4" + str(currentCardNumber))
            currentCardNumber = int(currentCardNumber)
            result = is_luhn_valid(currentCardNumber)
            if currentCardNumber in usedCards:
                pass
            else:
                i += 1
                if result == True:
                    print(f"\rValid Visa Card found: {len(activeCards):,}", end='')
                    activeCards.append(currentCardNumber)
                    usedCards.append(currentCardNumber)
                else:
                    usedCards.append(currentCardNumber)
        except KeyboardInterrupt:
            print("\n" + str(activeCards).replace(',', '\n').replace('[', '').replace(']', ''))
            exit()
    print("\n" + str(activeCards).replace(',', '\n').replace('[', '').replace(']', ''))
if cardOption == 2:
    while len(activeCards) < numberOfCodes:
        try:
            currentCardNumber = random.randint(100000000000000, 999999999999999)
            currentCardNumber = str("5" + str(currentCardNumber))
            currentCardNumber = int(currentCardNumber)
            result = is_luhn_valid(currentCardNumber)
            if currentCardNumber in usedCards:
                pass
            else:
                i += 1
                if result == True:
                    print(f"\rValid Mastercards found: {len(activeCards):,}", end='')
                    activeCards.append(currentCardNumber)
                    usedCards.append(currentCardNumber)
                else:
                    usedCards.append(currentCardNumber)
        except KeyboardInterrupt:
            print("\n" + str(activeCards).replace(',', '\n').replace('[', '').replace(']', ''))
            exit()
    print("\n" + str(activeCards).replace(',', '\n').replace('[', '').replace(']', ''))
if cardOption == 3:
    while len(activeCards) < numberOfCodes:
        try:
            currentCardNumber = random.randint(100000000000000, 999999999999999)
            currentCardNumber = str("6" + str(currentCardNumber))
            currentCardNumber = int(currentCardNumber)
            result = is_luhn_valid(currentCardNumber)
            if currentCardNumber in usedCards:
                pass
            else:
                i += 1
                if result == True:
                    print(f"\rValid Discover Cards found: {len(activeCards):,}", end='')
                    activeCards.append(currentCardNumber)
                    usedCards.append(currentCardNumber)
                else:
                    usedCards.append(currentCardNumber)
        except KeyboardInterrupt:
            print("\n" + str(activeCards).replace(',', '\n').replace('[', '').replace(']', ''))
            exit()
    print("\n" + str(activeCards).replace(',', '\n').replace('[', '').replace(']', ''))
if cardOption == 4:
    while len(activeCards) < numberOfCodes:
        try:
            suffix1 = random.randint(1, 899)
            suffix2 = random.randint(1, 99)
            suffix3 = random.randint(1, 999)
            if suffix1 == 666:
                suffix1 += 1
            suffixSum = f"{suffix1:03d}"
            suffixSum += f"-{suffix2:02d}"
            suffixSum += f"-{suffix3:04d}"
            currentCardNumber = suffixSum.replace('-', '')
            currentCardNumber = int(currentCardNumber)
            result = is_luhn_valid(currentCardNumber)
            if currentCardNumber in usedCards:
                pass
            else:
                i += 1
                if result == True:
                    print(f"\rValid Social Security Numbers found: {len(activeCards):,}", end='')
                    activeCards.append(currentCardNumber)
                    usedCards.append(currentCardNumber)
                    ssnList.append(suffixSum)
                else:
                    usedCards.append(currentCardNumber)
        except KeyboardInterrupt:
            print("\n" + str(ssnList).replace(',', '\n').replace('[', '').replace(']', ''))
            exit()
        except:
            pass
    print("\n" + str(ssnList).replace(',', '\n').replace('[', '').replace(']', ''))
if cardOption == 5:
    while len(activeCards) < numberOfCodes:
        try:
            currentCardNumber = random.randint(11111111111111111, 99999999999999999)
            currentCardNumber = str("17" + str(currentCardNumber))
            currentCardNumber = int(currentCardNumber)
            result = is_luhn_valid(currentCardNumber)
            if currentCardNumber in usedCards:
                pass
            else:
                i += 1
                if result == True:
                    print(f"\rValid Amazon Gift Cards found: {len(activeCards):,}", end='')
                    activeCards.append(currentCardNumber)
                    usedCards.append(currentCardNumber)
                else:
                    usedCards.append(currentCardNumber)
        except KeyboardInterrupt:
            print("\n" + str(activeCards).replace(',', '\n').replace('[', '').replace(']', ''))
            exit()
        except:
            pass
    print("\n" + str(activeCards).replace(',', '\n').replace(']', '').replace('[', ''))
