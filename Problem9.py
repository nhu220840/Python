num = int(input("Please type a 3-digit positive integer: "))
while True:
    if num > 999 or num < 100:
        print(num, "is not 3-digit positive integer")
        num = int(input("Please type a 3-digit positive integer again: "))
    else:
        f = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        s = [
            "ten",
            "eleven",
            "twelve",
            "thirteen",
            "fourteen",
            "fifteen",
            "sixteen",
            "seventeen",
            "eighteen",
            "nineteen",
        ]
        t = [
            "",
            "",
            "twenty",
            "thirty",
            "forty",
            "fifty",
            "sixty",
            "seventy",
            "eighty",
            "ninety",
        ]

        firstNum = num // 100
        secondNum = num % 100 // 10
        thirdNum = num % 10

        speech = f[firstNum] + " hundered "
        if secondNum == 0 and num % 100 != 0:
            speech += "and " + f[thirdNum]
        elif secondNum == 1:
            speech += "and " + s[thirdNum]
        else:
            speech = speech + t[secondNum] + " " + f[thirdNum]
        print("English word representation for", num, "is:", speech)
        break
