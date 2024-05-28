from dataclasses import dataclass
from typing import Self



from physities.src.dimension.base_dimensions import BaseDimension

SYMBOLS = {
    BaseDimension.LENGTH: "L",
    BaseDimension.MASS: "m",
    BaseDimension.TIME: "t",
    BaseDimension.TEMPERATURE: "T",
    BaseDimension.AMOUNT: "N",
    BaseDimension.ELECTRIC_CURRENT: "I",
    BaseDimension.LUMINOUS_INTENSITY: "Iᵥ",
}

NUMBER_STR_TO_POWER_STR = {
    "0": "⁰",
    "1": "¹",
    "2": "²",
    "3": "³",
    "4": "⁴",
    "5": "⁵",
    "6": "⁶",
    "7": "⁷",
    "8": "⁸",
    "9": "⁹",
    ".": "ˑ",
}


@dataclass(frozen=True, slots=True)
class Dimension:
    dimensions_tuple: tuple[
        float,
        float,
        float,
        float,
        float,
        float,
        float,
    ]

    @property
    def length(self):
        return self.dimensions_tuple[BaseDimension.LENGTH]

    @property
    def mass(self):
        return self.dimensions_tuple[BaseDimension.MASS]

    @property
    def temperature(self):
        return self.dimensions_tuple[BaseDimension.TEMPERATURE]

    @property
    def time(self):
        return self.dimensions_tuple[BaseDimension.TIME]

    @property
    def amount(self):
        return self.dimensions_tuple[BaseDimension.AMOUNT]

    @property
    def electric_current(self):
        return self.dimensions_tuple[BaseDimension.ELECTRIC_CURRENT]

    @property
    def luminous_intensity(self):
        return self.dimensions_tuple[BaseDimension.LUMINOUS_INTENSITY]

    @classmethod
    def new_time(cls, power: float = None) -> Self:
        return cls.__new_base_unit(base_unit=BaseDimension.TIME, power=power)

    @classmethod
    def new_length(cls, power: float = None) -> Self:
        return cls.__new_base_unit(base_unit=BaseDimension.LENGTH, power=power)

    @classmethod
    def new_temperature(cls, power: float = None) -> Self:
        return cls.__new_base_unit(base_unit=BaseDimension.TEMPERATURE, power=power)

    @classmethod
    def new_mass(cls, power: float = None) -> Self:
        return cls.__new_base_unit(base_unit=BaseDimension.MASS, power=power)

    @classmethod
    def new_amount(cls, power: float = None) -> Self:
        return cls.__new_base_unit(base_unit=BaseDimension.AMOUNT, power=power)

    @classmethod
    def new_electric_current(cls, power: float = None) -> Self:
        return cls.__new_base_unit(
            base_unit=BaseDimension.ELECTRIC_CURRENT, power=power
        )

    @classmethod
    def new_luminous_intensity(cls, power: float = None) -> Self:
        return cls.__new_base_unit(
            base_unit=BaseDimension.LUMINOUS_INTENSITY, power=power
        )

    @classmethod
    def new_dimensionless(cls) -> Self:
        return Dimension(dimensions_tuple=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0))

    @classmethod
    def __new_base_unit(cls, base_unit: BaseDimension, power: float = None):
        if power is None:
            power = 1
        elif not isinstance(power, (int, float)):
            raise TypeError("The exponentiation must be a int or a float.")
        dimensions_tuple = [0.0 for _ in BaseDimension]
        dimensions_tuple[base_unit] = power
        return cls.new_instance(dimensions_tuple=tuple(dimensions_tuple))

    @classmethod
    def new_instance(
        cls,
        dimensions_tuple: tuple[float, float, float, float, float, float, float],
    ):
        return Dimension(dimensions_tuple=dimensions_tuple)

    def get_dimensions(self):
        return [
            BaseDimension(i)
            for i in range(len(self.dimensions_tuple))
            if self.dimensions_tuple[i] != 0
        ]

    def get(self, index: BaseDimension):
        return self.dimensions_tuple[index]

    def __add__(self, other):
        if isinstance(other, Dimension):
            dimensions_tuple = tuple(
                sum(i) for i in zip(self.dimensions_tuple, other.dimensions_tuple)
            )
            return Dimension(dimensions_tuple=dimensions_tuple)
        else:
            raise TypeError("Dimension only allow addition between same instance.")

    def __radd__(self, other):
        try:
            to_return = self.__add__(other)
        except TypeError as e:
            raise e
        return to_return

    def __sub__(self, other):
        if isinstance(other, Dimension):
            negative_other_dimensions_tuple = tuple(-i for i in other.dimensions_tuple)
            dimensions_tuple = tuple(
                sum(i)
                for i in zip(self.dimensions_tuple, negative_other_dimensions_tuple)
            )
            return Dimension(dimensions_tuple=dimensions_tuple)
        else:
            raise TypeError("Dimension only allow subtraction between same instance.")

    def __rsub__(self, other):
        try:
            to_return = self.__sub__(other)
        except TypeError as e:
            raise e
        return to_return

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            dimensions_tuple = tuple(other * i for i in self.dimensions_tuple)
            return Dimension(dimensions_tuple=dimensions_tuple)
        else:
            raise TypeError("Dimension only allow multiplication with int or floats.")

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            dimensions_tuple = tuple(other * i for i in self.dimensions_tuple)
            return Dimension(dimensions_tuple=dimensions_tuple)
        else:
            raise TypeError("Dimension only allow multiplication with int or floats.")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            dimensions_tuple = tuple(i / other for i in self.dimensions_tuple)
            return Dimension(dimensions_tuple=dimensions_tuple)
        else:
            raise TypeError("Dimension only allow division by int or floats.")

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            dimensions_tuple = tuple(other / i for i in self.dimensions_tuple)
            return Dimension(dimensions_tuple=dimensions_tuple)
        else:
            raise TypeError("Dimension only allow division by int or floats.")

    def __eq__(self, other):
        if isinstance(other, Dimension) or issubclass(type(other), Dimension):
            if other.dimensions_tuple == self.dimensions_tuple:
                return True
        return False

    def __pow__(self, power, modulo=None):
        raise TypeError("Exponentiation with Dimension is not allowed.")

    def __rpow__(self, power):
        raise TypeError("Exponentiation with Dimension is not allowed.")

    def show_dimension(self):
        numerator = ""
        denominator = ""
        for i in range(len(self.dimensions_tuple)):
            is_numerator = True
            power = self.dimensions_tuple[i]
            if power == 0:
                continue
            if power < 0:
                is_numerator = False
                power = abs(power)
            power_str = "".join([NUMBER_STR_TO_POWER_STR[i] for i in str(power)])
            if is_numerator:
                numerator += f"{SYMBOLS[BaseDimension(i)]}{power_str}"
            else:
                denominator += f"{SYMBOLS[BaseDimension(i)]}{power_str}"
        if not denominator:
            to_print = f"{numerator}"
            print()
        elif not numerator:
            to_print = f"1 / {denominator}"
            print()
        else:
            to_print = f"{numerator} / {denominator}"
        # print(to_print)
        return to_print
