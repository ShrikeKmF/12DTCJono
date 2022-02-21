class Bus:
    bus_list = []

    def __init__(self, number, route, driver):
        self.number = number
        self.route = route
        self.driver = driver
        Bus.bus_list.append(self)

    def print_info(self):
        for bus in Bus.bus_list:
            if bus == self:
                print(f"Bus Number is {bus.number} Bus Route is "
                      f"{bus.route} and Bus Driver is {bus.driver}")


b1 = Bus("01189998819991197253", "Y", "Greg")
b2 = Bus("3.141592653589793238462643383279502", "80", "Carl")
b3 = Bus("5.71828182845904543", "B", "Bob")

for bus in range(len(Bus.bus_list)):
    Bus.print_info(Bus.bus_list[bus])
