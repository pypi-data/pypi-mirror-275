from math import prod
from dataclasses import dataclass

from kobject import Kobject

from physities.src.dimension import Dimension
from physities.src.dimension.base_dimensions import BaseDimension


@dataclass(frozen=True, slots=True)
class Scale(Kobject):
    """
    dimension:

    from_base_scale_conversions:

    rescale_value:
    """

    dimension: Dimension
    from_base_scale_conversions: tuple[
        float | int,
        float | int,
        float | int,
        float | int,
        float | int,
        float | int,
        float | int,
    ]
    rescale_value: float | int

    @classmethod
    def new(
        cls,
        dimension: Dimension = None,
        from_base_scale_conversions: tuple[
            float, float, float, float, float, float, float
        ] = None,
        rescale_value: float = None,
    ):
        if from_base_scale_conversions is None:
            from_base_scale_conversions = (1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        if rescale_value is None:
            rescale_value = 1
        if dimension is None:
            dimension = Dimension.new_dimensionless()

        return cls(
            dimension=dimension,
            from_base_scale_conversions=from_base_scale_conversions,
            rescale_value=rescale_value,
        )

    @property
    def is_dimensionless(self) -> bool:
        if not self.dimension.get_dimensions():
            return True
        return False

    @property
    def conversion_factor(self) -> float:
        return self.rescale_value * prod(self.from_base_scale_conversions)

    @staticmethod
    def __get_annulled_dimension(
        dimension_1: Dimension, dimension_2: Dimension, result_dimension: Dimension
    ) -> list[
        BaseDimension,
        BaseDimension,
        BaseDimension,
        BaseDimension,
        BaseDimension,
        BaseDimension,
        BaseDimension,
    ]:
        set_1 = set(dimension_1.get_dimensions())
        set_2 = set(dimension_2.get_dimensions())
        set_3 = set(result_dimension.get_dimensions())
        return list((set_1 - set_3).union(set_2 - set_3))

    @staticmethod
    def __fit_scale_and_dimension(
        dimension_instance: Dimension,
        from_base_scale_conversions: tuple[
            float, float, float, float, float, float, float
        ],
        value: float,
        rescale_value: float,
    ):
        dimension = dimension_instance.get_dimensions()
        if len(dimension) == 1:
            index = dimension.pop()
            from_base_scale_conversions_list = list(from_base_scale_conversions)
            from_base_scale_conversions_list[index] *= rescale_value
            new_from_base_scale_conversions = tuple(from_base_scale_conversions_list)
            return 1, new_from_base_scale_conversions
        return rescale_value * value, from_base_scale_conversions

    def __eq__(self, other):
        if isinstance(other, Scale):
            if self.dimension == other.dimension and self.conversion_factor == other.conversion_factor:
                return True
        return False

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_value, new_from_base_scale_conversions = self.__fit_scale_and_dimension(
                dimension_instance=self.dimension,
                from_base_scale_conversions=self.from_base_scale_conversions,
                rescale_value=other,
                value=self.rescale_value,
            )
            return Scale(
                dimension=self.dimension,
                from_base_scale_conversions=new_from_base_scale_conversions,
                rescale_value=new_value,
            )
        if isinstance(other, Scale):
            new_dimension = self.dimension + other.dimension
            new_from_base_scale_conversions_list = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
            rescale_factor = 1
            for i in BaseDimension:
                xxx = (
                    self.from_base_scale_conversions[i]
                    * other.from_base_scale_conversions[i]
                )
                if new_dimension.get(i) == 0 and (
                    self.dimension.get(i) != 0 or other.dimension.get(i) != 0
                ):
                    rescale_factor *= xxx
                    new_from_base_scale_conversions_list[i] = 1
                else:
                    new_from_base_scale_conversions_list[i] = xxx
            new_value, new_from_base_scale_conversions = self.__fit_scale_and_dimension(
                dimension_instance=new_dimension,
                from_base_scale_conversions=tuple(new_from_base_scale_conversions_list),
                rescale_value=self.rescale_value,
                value=rescale_factor,
            )
            return Scale(
                dimension=new_dimension,
                from_base_scale_conversions=new_from_base_scale_conversions,
                rescale_value=new_value,
            )
        raise TypeError(
            f"{Scale} can only be multiplied by {Scale}, {int} or {float}. This operation is not implemented for {type(other)}."
        )

    def __rmul__(self, other):
        try:
            to_return = Scale.__mul__(self, other)
        except TypeError as e:
            raise e
        return to_return

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            new_value, new_from_base_scale_conversions = self.__fit_scale_and_dimension(
                dimension_instance=self.dimension,
                from_base_scale_conversions=self.from_base_scale_conversions,
                rescale_value=1 / other,
                value=self.rescale_value,
            )
            return Scale(
                dimension=self.dimension,
                from_base_scale_conversions=new_from_base_scale_conversions,
                rescale_value=new_value,
            )
        if isinstance(other, Scale):
            new_dimension = self.dimension - other.dimension
            new_from_base_scale_conversions_list = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
            rescale_factor = 1
            for i in BaseDimension:
                xxx = (
                    self.from_base_scale_conversions[i]
                    / other.from_base_scale_conversions[i]
                )
                if new_dimension.get(i) == 0 and (
                    self.dimension.get(i) != 0 or other.dimension.get(i) != 0
                ):
                    rescale_factor *= xxx
                    new_from_base_scale_conversions_list[i] = 1
                else:
                    new_from_base_scale_conversions_list[i] = xxx
            new_value, new_from_base_scale_conversions = self.__fit_scale_and_dimension(
                dimension_instance=new_dimension,
                from_base_scale_conversions=tuple(new_from_base_scale_conversions_list),
                rescale_value=self.rescale_value,
                value=rescale_factor,
            )
            return Scale(
                dimension=new_dimension,
                from_base_scale_conversions=new_from_base_scale_conversions,
                rescale_value=new_value,
            )
        raise TypeError(
            f"{Scale} can only be divided by {Scale}, {int} or {float}. This operation is not implemented for {type(other)}."
        )

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            new_dimension = self.dimension * -1
            new_rescale_value = 1 / self.rescale_value
            new_from_base_scale_conversions_list = [
                1 / self.from_base_scale_conversions[i] for i in BaseDimension
            ]
            new_value, new_from_base_scale_conversions = self.__fit_scale_and_dimension(
                dimension_instance=new_dimension,
                from_base_scale_conversions=tuple(new_from_base_scale_conversions_list),
                rescale_value=new_rescale_value,
                value=other,
            )
            return Scale(
                dimension=new_dimension,
                from_base_scale_conversions=new_from_base_scale_conversions,
                rescale_value=new_value,
            )
        raise TypeError(
            f"{Scale} can only divide {Scale}, {int} or {float}. This operation is not implemented for {type(other)}."
        )

    def __pow__(self, power, modulo=None):
        if isinstance(power, (int, float)):
            new_dimension = self.dimension * power
            new_from_base_scale_conversions = tuple(
                i**power for i in self.from_base_scale_conversions
            )
            new_rescale_value = self.rescale_value**power
            return Scale(
                dimension=new_dimension,
                from_base_scale_conversions=new_from_base_scale_conversions,
                rescale_value=new_rescale_value,
            )
        raise TypeError(
            f"{Scale} can only be powered by {int} or {float}. This operation is not implemented for {type(power)}."
        )
