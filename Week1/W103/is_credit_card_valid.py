def to_number(digits):
    number=""
    for i in digits:
        number+=str(i)
    return number
def is_credit_card_valid(number):
    string = str(number)
    if len(string) % 2 != 0:
        new1 = sum([int(string[x]) for x in range(len(string)) if x%2==0])
        new2 = [int(string[x])*2 for x in range(len(string)) if x%2!=0]
        new3 = to_number(new2)
        new4 = sum([int(a) for a in new3])
        if (new1 + new4) % 10 == 0:
            return "A Valid Number"
        else:
            return "Not A Valid Number"
    else:
        return "Not A Valid Number"

print(is_credit_card_valid(79927398713))
print(is_credit_card_valid(79927398715))
