# Dictionary for numbers
# sd:single digits, tp: tens place digits, tp2: between 10 and 20, zn: zero numbers
sd = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven",
      "8": "eight", "9": "nine"}
tp = {"0": "", "2": "twenty", "3": "thirty", "4": "fourty", "5": "fifty", "6": "sixty", "7": "seventy", "8": "eighty",
      "9": "ninety"}
tp2 = {"10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen", "15": "fifteen",
       "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen"}
zn = {2: "hundred", 3: "thousand"}

num = input('Enter a number up to 5 digits \n')
length = len(num)
t = "thousand"
h = "hundred"
zero_counter = 1
IntNum = int(num)
NumWord = ''

# Checking the Number of Zeroes in a Number
if num.endswith("0"):
    for i in num[::-1]:
        if i == "0":
            zero_counter += 1
        if i != "0":
            zero_counter -= 1


# Checking Functions
def TwoDigits(num):
    if 10 <= IntNum < 20:
        NumWord = tp2[num]
    else:
        NumWord = tp[num[0]] + ' ' + sd[num[1]]
    return NumWord.replace("zero",'')


# Three Digits
def ThreeDigits(num):
    HundredsWord = sd[num[0]] + ' ' + h + ' '
    RemainingNum = num[1:]
    NumWord = HundredsWord
    if RemainingNum == "00":
        return NumWord
    return HundredsWord + (TwoDigits(RemainingNum))


# Four Digits
def FourDigits(num):
    ThousandsWord = sd[num[0]] + ' ' + t + ' '
    RemainingNum = num[1:]
    NumWord = ThousandsWord
    if RemainingNum[0] == "0":
        return ThousandsWord + (TwoDigits(RemainingNum[1:]))
    else:
        return ThousandsWord + (ThreeDigits(RemainingNum))


# Five Digits
def FiveDigits(num):
    if num.startswith("1"):
        if num[1] == "0":
            TenThousandsWord = "ten thousand "
        else:
            TenThousandsWord = tp2[num[0:2]] + ' ' + t
    else:
        TenThousandsWord = tp[num[0]] + ' ' + sd[num[1]] + ' ' + t + ' '
    RemainingNum = num[2:]
    NumWord = TenThousandsWord
    if RemainingNum == "000":
        return NumWord
    return (TenThousandsWord + (ThreeDigits(RemainingNum)))


# Calling Functions

if length == 1:
    print(sd[num])

if length == 2:
    print(TwoDigits(num))

if length == 3:
    IntNum = int(num[1:])
    if zero_counter == 2:
        print(sd[num[0]], h)
    else:
        print(ThreeDigits(num))

if length == 4:
    IntNum = int(num[2:])
    if zero_counter == 3:
        print(sd[num[0]], t)
    else:
        print(FourDigits(num))

if length == 5:
    IntNum = int(num[3:])
    if zero_counter == 4:
        if num.startswith("1"):
            print("ten thousand")
        else:
            print(tp[num[0]], t)
    else:
       NumWord = FiveDigits(num)
       NumWord2 = NumWord.replace("zero hundred",'')
       print(NumWord2.replace("zero",''))
