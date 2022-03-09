def validate(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits_of - digits_of(card_number)
    odd_digits = digits_of[-1::-2]
    even_digits = digits_of[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

if validate(input("Enter Number \n"))==0:
    print("Valid")
else:
    print("Invalid")