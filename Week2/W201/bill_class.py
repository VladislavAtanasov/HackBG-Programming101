class Bill(object):
    def __init__(self, amount):
        self.amount = amount

    def __int__(self):
        return self.amount

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __repr__(self):
        return "{}$ bill".format(self.amount)

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.amount)

class BatchBill(Bill):
    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def __getitem__(self, index):
        return self.bills[index]

    def total(self):
        total_sum = 0
        for bill in self.bills:
            total_sum += int(bill)
        return total_sum

    def __int__(self):
        return self.total()

class CashDesk():
    def __init__(self):
        self.vault = []

    def take_money(self, currency):
        self.vault.append(currency)

    def total(self):
        result = 0
        for money in self.vault:
            result += int(money)
        return result

    def inspect(self):
        print("We have a total of " + str(self.total()) + "$ in the desk\n" + "We have the following count of bills, sorted in ascending order:\n")
        values = [10, 20, 50, 100, 100, 100]
        string = ""
        bills = [Bill(value) for value in values]
        batch = BatchBill(bills)
        for bill in batch:
            if repr(bill) not in string:
                string += repr(bill) +  " - " + str(values.count(int(bill))) + "\n"
        return string


def main():
    a = Bill(5)
    b = Bill(10)
    c = Bill(5)
    money_holder = {}
    money_holder[str(a)] = 1
    for a in money_holder:
        if a in money_holder:
            money_holder[str(a)] += 1
    print(money_holder)
    values = [10, 20, 50, 100, 100, 100]
    bills = [Bill(value) for value in values]
    batch = BatchBill(bills)
    for bill in batch:
        print(bill)
    desk = CashDesk()
    desk.take_money(batch)
    desk.take_money(Bill(10))
    print(desk.total())
    print(desk.inspect())

if __name__ == '__main__':
    main()



