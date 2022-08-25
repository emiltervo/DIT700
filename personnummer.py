# personnummber()
import datetime

# Användaren skriver in ett personnummer
n = input("Skriv ditt personnummer: ")

# Tar bort blanksteg och bindestreck
new = n.replace(" ", "").replace("-", "")
# print(new)

# Separerar år/månad/dag
year = new[:2]
month = new[2:4]
day = new[4:6]

# Skapar en lista med datum
datum = [year, month, day]
# print(datum)

# Kollar ifall datumet är korrekt
isValidDate = True
try:
    datetime.datetime(int(year), int(month), int(day))

except ValueError:
    isValidDate = False
if(isValidDate):
    print("The date of birth is valid ..")
else:
    print("The date of birth is not valid..")

# Implementer luhn algoritmen och printar valid ifall nummret är jämnt delbart med 10


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
    print(f"Kontrollsiffran är: {checksum}")
    return checksum % 10


print('Valid') if luhn_checksum(new) == 0 else print('Invalid')
