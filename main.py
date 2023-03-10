class people(object):
    def __init__(self, name="", dependent=0):
        self.name = name
        self.dependent = dependent

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) >= 3:
            self.name = new_name
        else:
            print("-Error: invalid type.")

    def get_dependent(self):
        return self.dependent

    def set_dependent(self, new_dependent):
        if isinstance(new_dependent, str) and len(new_dependent) >= 3:
            self.dependent = new_dependent
        else:
            print('-Error: invalid type.')

    def __str__(self):
        date = (f"Student: {self.name}, dependent : {self.dependent}")
        print(date)


class professor(people):
    def __init__(self, name="", dependent=0, amt_class=0):
        super().__init__(name, dependent)
        self.amt_class = amt_class

    def get_amt_class(self):
        return self.amt_class

    def set_amt_class(self, new_amtclass):
        if isinstance(new_amtclass, str) and len(new_amtclass) >= 3:
            self.amt_class = new_amtclass
        else:
            print("-Error: invalid type.")

    def __str__(self):
        date1 = (f"Professor: {self.name}, classes : {self.dependent}")
        print(date1)


class employee(people):
    def __init__(self, name="", dependent=0, salary=0.0):
        super().__init__(name, dependent)
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        if isinstance(new_salary, str) and len(new_salary) >= 3:
            self.salary = new_salary
        else:
            print("-Error: invalid type.")


if __name__ == '__main__':
    p = people('John', 0)
    p.__str__()
    p1 = professor('Mr. Michael', 5)
    p1.__str__()
    p1.set_name('Mrs. Ana')
    print(f"Name: {p1.get_name()}")
    print

    # p1 = professor("Mr. Gabriel", 1, 5)
    # p1.__str__()