class Vendor(object):
    def __init__(self, name, number, street):
        self._name = name
        self._number = number
        self._street = street

    @property
    def name(self):
        return self._name

    @property
    def number(self):
        return self._number

    @property
    def street(self):
        return self._street


class Customer(object):
    def __init__(self, name, address):
        self._name = name
        self._address = address

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address

class VendorAdapter(Vendor, Customer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def address(self):
        return '{} {}'.format(self.name, self.street)


MOCKVENDOR = (VendorAdapter('Steve', 46, 'Pendle'),)
CUSTOMER = MOCKVENDOR

def main():
    for cust in CUSTOMER:
        print(cust.name, cust.address)

if __name__ == '__main__':
    main()