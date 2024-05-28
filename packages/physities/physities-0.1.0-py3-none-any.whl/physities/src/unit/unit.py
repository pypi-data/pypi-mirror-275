from typing import Self


from physities.src.scale.scale import Scale


class MetaUnit(type):
    scale: Scale

    def __hash__(self):
        return hash(self.scale)

    def __eq__(self, other):
        if isinstance(other, MetaUnit) and self.scale.dimension == other.scale.dimension and self.scale.conversion_factor == other.scale.conversion_factor:
            return True
        return False

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_scale = self.scale * other
            return type(self)(f"Unit", (Unit,), {"scale": new_scale, "value": None})
        if isinstance(other, MetaUnit):
            new_scale = self.scale * other.scale
            return type(f"Unit", (Unit,), {"scale": new_scale, "value": None})
        raise TypeError(
            f"{self} only allows multiplication by {self}, {int}, and {float}"
        )

    def __rmul__(self, other):
        try:
            to_return = MetaUnit.__mul__(self, other)
        except TypeError as e:
            raise e
        return to_return

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            new_scale = self.scale / other
            return type(f"Unit", (Unit,), {"scale": new_scale, "value": None})
        if isinstance(other, MetaUnit):
            new_scale = self.scale / other.scale
            return type(f"Unit", (Unit,), {"scale": new_scale, "value": None})
        raise TypeError(f"{self} only allows division by {self}, {int}, and {float}")

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            new_scale = other / self.scale
            return type(f"Unit", (Unit,), {"scale": new_scale, "value": None})
        raise TypeError(f"{self} can divide only {self}, {int} and {float}")

    def __pow__(self, power, modulo=None):
        if isinstance(power, (int, float)):
            new_scale = self.scale**power
            return type(f"Unit", (Unit,), {"scale": new_scale, "value": None})
        raise TypeError(f"{self} can only be powered by {int} and {float}")

    def __add__(self, other):
        raise TypeError(f"Units with translated scale are not allowed yet.")

    def __sub__(self, other):
        raise TypeError(f"Units with translated scale are not allowed yet.")

    def __radd__(self, other):
        raise TypeError(f"Units with translated scale are not allowed yet.")

    def __rsub__(self, other):
        raise TypeError(f"Units with translated scale are not allowed yet.")


class Unit(metaclass=MetaUnit):
    scale: Scale
    value: float | int

    def __init__(self, value: float | int):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, Unit) and self.scale.dimension == other.scale.dimension:
            if self.value == other.convert(self).value:
                return True
        return False

    def __repr__(self):
        dimension = self.scale.dimension.show_dimension()
        if not dimension:
            return f"{self.value} (Scalar)"
        return f"{self.value} ({dimension})"

    def __str__(self):
        return f"{self.value}"

    def __add__(self, other):
        if isinstance(other, Unit):
            if self.scale.dimension == other.scale.dimension:
                new_value = self.value + other.convert(self).value
                new_instance = type(self)(new_value)
                new_instance.scale = self.scale
                return new_instance
            raise TypeError(f"Dimensions do not match {self.scale.dimension} != {other.scale.dimension}")
        raise TypeError(f"{type(other)} is not from type {type(self)}")

    def __sub__(self, other):
        if isinstance(other, Unit):
            if self.scale.dimension == other.scale.dimension:
                new_value = self.value - other.convert(self).value
                new_instance = type(self)(new_value)
                new_instance.scale = self.scale
                return new_instance
            raise TypeError(f"Dimensions do not match {self.scale.dimension} != {other.scale.dimension}")
        raise TypeError(f"{type(other)} is not from type {type(self)}")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_value = self.value * other
            new_instance = type(self)(new_value)
            new_instance.scale = self.scale
            return new_instance
        if isinstance(other, Unit):
            new_scale = self.scale * other.scale
            new_value = self.value * other.value
            if new_scale.is_dimensionless:
                new_value *= new_scale.conversion_factor
                new_scale = Scale.new()
            new_instance = type(self)(new_value)
            new_instance.scale = new_scale
            return new_instance
        raise TypeError(f"{type(self)} can be multiplied only by {type(self)}, {float} and {int}")

    def __rmul__(self, other):
        try:
            to_return = Unit.__mul__(self, other)
        except TypeError as e:
            raise e
        return to_return

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            new_value = self.value / other
            new_instance = type(self)(new_value)
            new_instance.scale = self.scale
            return new_instance
        if isinstance(other, Unit):
            new_scale = self.scale / other.scale
            new_value = self.value / other.value
            if new_scale.is_dimensionless:
                new_value *= new_scale.conversion_factor
                new_scale = Scale.new()
            new_instance = type(self)(new_value)
            new_instance.scale = new_scale
            return new_instance
        raise TypeError(f"{type(self)} only allows division by {type(self)}, {int} and {float}")

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            new_value = other / self.value
            new_scale = 1 / self.scale
            new_instance = type(self)(new_value)
            new_instance.scale = new_scale
            return new_instance
        raise TypeError(f"{type(self)} can divide only {type(self)}, {int} and {float}")

    def __pow__(self, power, modulo=None):
        if isinstance(power, (int, float)):
            new_value = self.value**power
            new_instance = type(self)(new_value)
            new_scale = self.scale**power
            new_instance.scale = new_scale
            return new_instance
        raise TypeError(f"{type(self)} can only be powered by {int} and {float}")

    def to_si(self):
        new_value = self.value * self.scale.conversion_factor
        new_instance = type(self)(new_value)
        new_scale = Scale.new(dimension=self.scale.dimension)
        new_instance.scale = new_scale
        return new_instance

    def convert(self, unit: MetaUnit | Self) -> Self:
        if isinstance(unit, (MetaUnit, Unit)):
            if self.scale.dimension == unit.scale.dimension:
                new_value = (
                    self.value * self.scale.conversion_factor / unit.scale.conversion_factor
                )
                new_instance = type(self)(new_value)
                new_instance.scale = unit.scale
                return new_instance
            raise TypeError("Dimensions do not match")
        raise TypeError(f"Invalid param type {type(unit)} != {type(MetaUnit)}")

