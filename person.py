from address import Address

class Person:
    def __init__(self, firstName, lastName, dob, phoneNum, address):
        self.first_name = firstName
        self.last_name = lastName
        self.date_of_birth = dob
        self.phoneNum = phoneNum
        self.addresses = []

        if isinstance(address, Address):
            self.addresses.append(address)
        elif isinstance(address,  list):
            for entry in address:
                if not isinstance(entry, Address):
                    raise NameError("Invalid Address...")

            self.addresses = address
        else:
            raise NameError("Invalid Address...")

    def add_address(self, address):
        if not isinstance(address, Address):
            raise NameError("Invalid address...")

        self.addresses = address
    