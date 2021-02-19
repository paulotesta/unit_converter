import requests
import json

CONFIG_FILENAME = 'config.json'

MASS = "m"
TEMPERATURE = "t"
LENGHT = "l"
VOLUME = "v"
CURRENCY = "c"
choice_base_units = (MASS, TEMPERATURE, LENGHT, VOLUME, CURRENCY)


def main():
    print("Welcome to unit converter")
    while True:
        print("What type of unit you would like to convert? [M]ass, " +
              "[T]emperature, [L]ength, [V]olume or [C]urrency?")
        unit = input()
        unit = unit.lower()
        if unit == MASS:
            mass()
            continue
        elif unit == TEMPERATURE:
            temperature()
            continue
        elif unit == LENGHT:
            lenght()
            continue
        elif unit == VOLUME:
            volume()
            continue
        elif unit == CURRENCY:
            currency()
            continue
        else:
            print("Type of unit not recognized, please try again.")
            continue


def mass():
    print("Please select the starting unit: [S]tone, [P]ound, [O]unce or " +
          "[K]ilogram")
    start = input().lower()
    print("Please present the ammount:")
    start_amount = input()
    start_amount = float(start_amount)
    print("Please select the destination unit: [S]tone, [P]ound, [O]unce or " +
          "[K]ilogram")
    end = input().lower()

    if start == "s":
        if end == "p":
            result_multiply(start_amount, 14, "lb")
        elif end == "o":
            result_multiply(start_amount, 224, "oz")
        elif end == "k":
            result_multiply(start_amount, 6.35, "kg")
        else:
            print("Original and final units are the same, the amount is: " +
                  "%0.2fst" % start_amount)
    elif start == "p":
        if end == "s":
            result_divide(start_amount, 14, "st")
        elif end == "o":
            result_divide(start_amount, 16, "oz")
        elif end == "k":
            result_divide(start_amount, 2.205, "kg")
        else:
            print("Original and final units are the same, the amount is: " +
                  "%0.2flb" % start_amount)
    elif start == "o":
        if end == "p":
            result_divide(start_amount, 16, "lb")
        elif end == "s":
            result_divide(start_amount, 224, "oz")
        elif end == "k":
            result_divide(start_amount, 35.274, "kg")
        else:
            print("Original and final units are the same, the amount is: " +
                  "%0.2foz" % start_amount)
    elif start == "k":
        if end == "p":
            result_multiply(start_amount, 2.205, "lb")
        elif end == "s":
            result_divide(start_amount, 6.35, "st")
        elif end == "o":
            result_multiply(start_amount, 35.274, "oz")
        else:
            print("Original and final units are the same, the amount is: " +
                  "%0.2fkg" % start_amount)
    else:
        print("Please select one of the valid units, try again.")


def temperature():
    print("Please select the original unit: [C]elsuis, [F]ahrenheit or " +
          "[K]elvin")
    start = input().lower()
    print("Please present the ammount:")
    start_amount = input()
    print("Please select the destination unit: [C]elsuis, [F]ahrenheit or " +
          "[K]elvin")
    end = input().lower()

    if start == "c":
        if end == "f":
            end_amount = (float(start_amount) * 9/5) + 32
            print("The converted amount is: %0.2fºF" % end_amount)
        elif end == "k":
            end_amount = float(start_amount) + 273
            print("The converted amount is: %0.2fK" % end_amount)
        else:
            print("Original and final units are the same, the amount is: " +
                  "%0.2fºC" % float(start_amount))
    elif start == "f":
        if end == "c":
            end_amount = (float(start_amount) - 32) * 5/9
            print("The converted amount is: %0.2fºC" % end_amount)
        elif end == "k":
            end_amount = ((float(start_amount) - 32) * 5/9) + 273
            print("The converted amount is: %0.2fK" % end_amount)
        else:
            print("Original and final units are the same, the amount is: " +
                  "%0.2fºF" % float(start_amount))
    elif start == "k":
        if end == "c":
            end_amount = float(start_amount) - 273
            print("The converted amount is: %0.2fºC" % end_amount)
        elif end == "f":
            end_amount = ((float(start_amount) - 273) * 9/5) + 32
            print("The converted amount is: %0.2fºF" % end_amount)
        else:
            print("Original and final units are the same, the amount is: " +
                  "%0.2fK" % float(start_amount))
    else:
        print("Please select one of the valid units, try again.")


def lenght():
    print("Please select the starting unit: [K]ilomenter, [M]ile, [Y]ard, " +
          "[F]oot or [I]nch")
    start = input().lower()
    print("Please present the ammount:")
    start_amount = input()
    start_amount = float(start_amount)
    print("Please select the destination unit: [K]ilomenter, [M]ile, " +
          "[Y]ard, [F]oot or [I]nch")
    end = input().lower()

    if start == "k":
        if end == "m":
            result_divide(start_amount, 1.609, "mi")
        elif end == "y":
            result_multiply(start_amount, 1094, "yd")
        elif end == "f":
            result_multiply(start_amount, 3281, "ft")
        elif end == "i":
            result_multiply(start_amount, 3937, "in")
        elif end == "k":
            print("Original and final units are the same, the amount is: " +
                  "%0.2fkm" % start_amount)
        else:
            print("Unit not recognized, please try again.")
    elif start == "m":
        if end == "k":
            result_multiply(start_amount, 1.609, "km")
        elif end == "y":
            result_divide(start_amount, 1760, "yd")
        elif end == "f":
            result_divide(start_amount, 5280, "yd")
        elif end == "i":
            result_divide(start_amount, 63360, "in")
        elif end == "m":
            print("Original and final units are the same, the amount is: " +
                  "%0.2fmi" % start_amount)
        else:
            print("Unit not reconizable, please try again.")
    elif start == "y":
        if end == "k":
            result_divide(start_amount, 1094, "km")
        elif end == "m":
            result_divide(start_amount, 1760, "mi")
        elif end == "f":
            result_multiply(start_amount, 3, "ft")
        elif end == "i":
            result_multiply(start_amount, 36, "in")

        elif end == "y":
            print("Original and final units are the same, the amount is: " +
                  "%0.2fyd" % start_amount)
        else:
            print("Unit not reconizable, please try again.")
    elif start == "f":
        if end == "k":
            result_divide(start_amount, 3281, "km")
        elif end == "m":
            result_divide(start_amount, 5280, "mi")
        elif end == "y":
            result_divide(start_amount, 3, "yd")
        elif end == "i":
            result_multiply(start_amount, 12, "in")
        elif end == "f":
            print("Original and final units are the same, the amount is: " +
                  "%0.2fft" % start_amount)
        else:
            print("Unit not reconizable, please try again.")
    elif start == "i":
        if end == "k":
            result_divide(start_amount, 39370, "km")
        elif end == "m":
            result_divide(start_amount, 63360, "mi")
        elif end == "y":
            result_divide(start_amount, 36, "yd")
        elif end == "f":
            result_divide(start_amount, 12, "ft")
        elif end == "i":
            print("Original and final units are the same, the amount is: " +
                  "%0.2fin" % start_amount)
        else:
            print("Unit not reconizable, please try again.")
    else:
        print("Please select one of the valid units, try again.")


def volume():
    print("Please select the starting unit: [L]itre, [F]luid Ounce, " +
          "Imperial [G]allon, or Imperial [P]int")
    start = input().lower()
    print("Please present the ammount:")
    start_amount = input()
    start_amount = float(start_amount)
    print("Please select the destination unit: [L]itre, [F]luid Ounce, " +
          "Imperial [G]allon, or Imperial [P]int")
    end = input().lower()

    if start == "l":
        if end == "f":
            result_multiply(start_amount, 33.814, "oz")
        elif end == "g":
            result_divide(start_amount, 4.546, "gal")
        elif end == "p":
            result_multiply(start_amount, 1.76, "pt")
        elif end == "l":
            print("Original and final units are the same, the amount is: " +
                  "%0.2fl" % start_amount)
        else:
            print("Unit not reconizable, please try again.")
    elif start == "f":
        if end == "l":
            result_divide(start_amount, 33.814, "l")
        elif end == "g":
            result_divide(start_amount, 154, "gal")
        elif end == "p":
            result_divide(start_amount, 19.215, "pt")
        elif end == "f":
            print("Original and final units are the same, the amount is: " +
                  "%0.2foz" % start_amount)
        else:
            print("Unit not reconizable, please try again.")
    elif start == "g":
        if end == "f":
            result_multiply(start_amount, 154, "oz")
        elif end == "l":
            result_multiply(start_amount, 4.546, "l")
        elif end == "p":
            result_multiply(start_amount, 8, "pt")
        elif end == "g":
            print("Original and final units are the same, the amount is: " +
                  "%0.2fgal" % start_amount)
        else:
            print("Unit not reconizable, please try again.")
    elif start == "p":
        if end == "l":
            result_divide(start_amount, 1.76, "l")
        elif end == "f":
            result_multiply(start_amount, 20, "oz")
        elif end == "g":
            result_divide(start_amount, 8, "gal")
        elif end == "p":
            print("Original and final units are the same, the amount is: " +
                  "%0.2fpt" % start_amount)
        else:
            print("Unit not reconizable, please try again.")
    else:
        print("Please select one of the valid units, try again.")


def currency():
    with open(CONFIG_FILENAME) as config_file:
        data = json.load(config_file)
    currency_url = "http://data.fixer.io/api/latest?access_key={}&format=1".\
                   format(data['key'])
    response = requests.get(currency_url)
    response = response.json()

    print("Please select the starting currency as a 3 letter international " +
          "code i.e.: GBP for British Pounds.")
    start = input().upper()
    print("Please present the ammount:")
    start_amount = input()
    start_amount = float(start_amount)
    print("Please select the destination currency as a 3 letter " +
          "international code")
    end = input().upper()

    if not (start in response['rates'] and end in response['rates']):
        print("Currencies not present in database, please try again.")
    else:
        conversion = (response['rates'][end] / response['rates'][start] *
                      start_amount)
        print("%0.2f %s in %s in todays conversion is %0.2f" % (start_amount,
              start, end, conversion))


def result_multiply(start_amount, multiply, unit):
    end_amount = start_amount * multiply
    print("The converted amount is: %0.2f %s" % (end_amount, unit))


def result_divide(start_amount, divide, unit):
    end_amount = start_amount / divide
    print("The converted amount is: %0.2f %s" % (end_amount, unit))


main()
