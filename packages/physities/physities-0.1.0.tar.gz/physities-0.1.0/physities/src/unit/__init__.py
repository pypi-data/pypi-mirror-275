from physities.src.dimension import Dimension, BaseDimension
from physities.src.scale import Scale
from .unit import Unit


class Meter(Unit):
    scale = Scale(
        dimension=Dimension.new_length(),
        from_base_scale_conversions=(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0),
        rescale_value=1,
    )
    value = None


class Second(Unit):
    scale = Scale(
        dimension=Dimension.new_time(),
        from_base_scale_conversions=(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0),
        rescale_value=1,
    )
    value = None


class Kilogram(Unit):
    scale = Scale(
        dimension=Dimension.new_mass(),
        from_base_scale_conversions=(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0),
        rescale_value=1,
    )
    value = None


class Kelvin(Unit):
    scale = Scale(
        dimension=Dimension.new_temperature(),
        from_base_scale_conversions=(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0),
        rescale_value=1,
    )
    value = None


class Unity(Unit):
    scale = Scale(
        dimension=Dimension.new_amount(),
        from_base_scale_conversions=(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0),
        rescale_value=1,
    )
    value = None


class Ampere(Unit):
    scale = Scale(
        dimension=Dimension.new_electric_current(),
        from_base_scale_conversions=(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0),
        rescale_value=1,
    )
    value = None


class Candela(Unit):
    scale = Scale(
        dimension=Dimension.new_luminous_intensity(),
        from_base_scale_conversions=(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0),
        rescale_value=1,
    )
    value = None


# class Scalar(Unit):
#     scale = Scale(
#         dimension=Dimension.new_dimensionless(),
#         from_base_scale_conversions=(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0),
#         rescale_value=1,
#     )
#     value = None


# Length

Gigameter = 1000000000 * Meter
Megameter = 1000000 * Meter
Kilometer = 1000 * Meter
Hectometer = 100 * Meter
Decameter = 10 * Meter
Decimeter = 0.1 * Meter
Centimeter = 0.01 * Meter
Millimeter = 0.001 * Meter
Micrometer = 0.000001 * Meter
Nanometer = 0.000000001 * Meter
Foot = 0.3048 * Meter
Yard = 0.9144 * Meter
Inch = 0.0254 * Meter
Mile = 1609.34 * Meter
Furlong = 201.168 * Meter
Rod = 5.0292 * Meter

# Time

Nanosecond = 0.000000001 * Second
Microsecond = 0.000001 * Second
Millisecond = 0.001 * Second
Centisecond = 0.01 * Second
Decisecond = 0.1 * Second
Minute = 60 * Second
Hour = 3600 * Second
Day = 86400 * Second
Week = 604800 * Second
Month = 2628288 * Second
Year = 31557600 * Second
Decade = 315576000 * Second
Century = 3155760000 * Second
Millennium = 31_557_600_000 * Second

# Unit

Dozen = 12 * Unity
Moles = 6.02214076 * 10**23 * Unity
Pairs = 2 * Unity
Score = 20 * Unity

# Mass

Gigagram = 1000000 * Kilogram
Megagram = Tonne = 1000 * Kilogram
Hectogram = 0.1 * Kilogram
Decagram = 0.01 * Kilogram
Gram = 0.001 * Kilogram
Decigram = 0.0001 * Kilogram
Centigram = 0.00001 * Kilogram
Milligram = 0.000001 * Kilogram
Microgram = 0.000000001 * Kilogram
Nanogram = 0.000000000001 * Kilogram
Pound = 0.453592 * Kilogram
Ounce = 0.0283495 * Kilogram
Stone = 6.35029 * Kilogram
Carat = 0.0002 * Kilogram
Grain = 0.0000647989 * Kilogram
Slug = 14.5939 * Kilogram

# Eletric Current

Gigaampere = 1000000000 * Ampere
Megaampere = 1000000 * Ampere
Kiloampere = 1000 * Ampere
Milliampere = 0.001 * Ampere
Microampere = 0.000001 * Ampere
Nanoampere = 0.000000001 * Ampere

# Area

Gigameter2 = Gigameter * Gigameter
Megameter2 = Megameter * Megameter
Kilometer2 = Kilometer * Kilometer
Hectometer2 = Hectare = Hectometer * Hectometer
Decameter2 = Decameter * Decameter
Meter2 = Meter * Meter
Decimeter2 = Decimeter * Decimeter
Centimeter2 = Centimeter * Centimeter
Millimeter2 = Millimeter * Millimeter
Micrometer2 = Micrometer * Micrometer
Nanometer2 = Nanometer * Nanometer
Foot2 = Foot * Foot
Yard2 = Yard * Yard
Inch2 = Inch * Inch
Mile2 = Mile * Mile
Furlong2 = Furlong * Furlong
Rod2 = Rod * Rod
Acre = 4046.860107422 * Meter2

# Volume

Gigameter3 = Gigameter2 * Gigameter
Megameter3 = Megameter2 * Megameter
Kilometer3 = Kilometer2 * Kilometer
Hectometer3 = Hectometer2 * Hectometer
Decameter3 = Decameter2 * Decameter
Meter3 = Kiloliter = Meter2 * Meter
Decimeter3 = Liter = Decimeter2 * Decimeter
Centimeter3 = Milliliter = Centimeter2 * Centimeter
Millimeter3 = Millimeter2 * Millimeter
Micrometer3 = Micrometer2 * Micrometer
Nanometer3 = Nanometer2 * Nanometer
Foot3 = Foot2 * Foot
Yard3 = Yard2 * Yard
Inch3 = Inch2 * Inch
Mile3 = Mile2 * Mile
Furlong3 = Furlong2 * Furlong
Rod3 = Rod2 * Rod
Gallon = 3785.411784 * Milliliter
Pint = 473 * Milliliter
Barrel = 0.158987294928 * Meter3
