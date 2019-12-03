#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class CalculateMass:

    mass = [73910,
            57084,
            102852,
            134452,
            108006,
            134228,
            102765,
            60642,
            64819,
            54335,
            82480,
            135119,
            73027,
            107087,
            108254,
            111944,
            83790,
            128585,
            52889,
            53870,
            145120,
            96863,
            57105,
            97702,
            75324,
            70566,
            120914,
            95808,
            86568,
            143498,
            125093,
            71370,
            122889,
            67808,
            133643,
            52806,
            103532,
            126487,
            54807,
            121402,
            57580,
            75759,
            84225,
            102232,
            112367,
            95635,
            132871,
            102903,
            51997,
            74565,
            63674,
            97410,
            96965,
            55711,
            53547,
            117482,
            107957,
            108175,
            136622,
            144235,
            80407,
            78670,
            114870,
            145967,
            148646,
            75955,
            84293,
            129590,
            144067,
            142192,
            79117,
            123861,
            68546,
            148675,
            88932,
            91493,
            127808,
            96517,
            130687,
            137822,
            77726,
            110502,
            130509,
            98370,
            136008,
            142920,
            81358,
            112950,
            101057,
            86547,
            128714,
            135401,
            55903,
            66606,
            105404,
            55276,
            57427,
            101556,
            91111,
            79585]

    def __init__(self):
        first = self.first_part()
        second = self.second_part()
        print(first)
        print(second)

    # module = ((mass / 3) round down) - 2
    def calculate_module_fuel(self, data):
        result = (data/3) - 2
        return int(result)

    def first_part(self):
        return sum([self.calculate_module_fuel(num) for num in self.mass])

    def second_part(self):
        fuel_total = 0
        for module in self.mass:
            new_fuel = module
            while True:
                new_fuel = self.calculate_module_fuel(new_fuel)
                if new_fuel > 0:
                    fuel_total += new_fuel
                else:
                    break

        return fuel_total


if __name__ == "__main__":
    CalculateMass()
