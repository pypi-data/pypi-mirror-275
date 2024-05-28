"""Support for serializing and deserializing color values"""
import enum
from typing import cast, Literal, NoReturn, overload

from .space import Space
from .spec import CoordinateSpec


@overload
def _check(
    is_valid: Literal[False], entity: str, value: object, deficiency: str = ...
) -> NoReturn:
    ...
@overload
def _check(
    is_valid: bool, entity: str, value: object, deficiency: str = ...
) -> None | NoReturn:
    ...
def _check(
    is_valid: bool, entity: str, value: object, deficiency: str = 'is malformed'
) -> None | NoReturn:
    if not is_valid:
        raise SyntaxError(f'{entity} "{value}" {deficiency}')
    return


def parse_fn(color: str) -> tuple[str, CoordinateSpec]:
    entity = 'color in function notation'

    try:
        tag, _, args = color.partition('(')
        _check(len(args) > 0, entity, color, 'has no arguments')
        _check(args.endswith(')'), entity, color, 'misses closing parenthesis')
        _check(Space.is_tag(tag), entity, color, 'has unknown tag')
        space = Space.resolve(tag)
        number = int if space.integral else float
        coordinates = tuple(number(c.strip()) for c in args[:-1].split(','))
        correct_length = len(space.coordinates) == len(coordinates)
        _check(correct_length, entity, color, 'has wrong number of arguments')
        return tag, cast(CoordinateSpec, coordinates)
    except SyntaxError:
        raise
    except:
        _check(False, entity, color)


def parse_hex(color: str) -> tuple[str, tuple[int, int, int]]:
    """Parse the string specifying a color in hashed hexadecimal format."""
    entity = 'hex web color'

    try:
        _check(color.startswith('#'), entity, color, 'does not start with "#"')
        color = color[1:]
        digits = len(color)
        _check(digits in (3, 6), entity, color, 'does not have 3 or 6 digits')
        if digits == 3:
            color = ''.join(f'{d}{d}' for d in color)
        return 'rgb256', cast(
            tuple[int, int, int],
            tuple(int(color[n:n+2], base=16) for n in range(0, 6, 2)),
        )
    except SyntaxError:
        raise
    except:
        _check(False, entity, color)


def parse_x_rgb(color: str) -> tuple[str, tuple[float, float, float]]:
    """Parse the string specifying a color in X's rgb: format."""
    entity = 'X rgb color'

    try:
        _check(color.startswith('rgb:'), entity, color, 'does not start with "rgb:"')
        hexes = [(f'{h}{h}' if len(h) == 1 else h) for h in color[4:].split('/')]
        _check(len(hexes) == 3, entity, color, 'does not have three components')
        if max(len(h) for h in hexes) == 2:
            return 'rgb256', cast(
                tuple[int, int, int],
                tuple(int(h, base=16) for h in hexes)
            )
        else:
            return 'srgb', tuple(int(h, base=16) / 16 ** len(h) for h in hexes)
    except SyntaxError:
        raise
    except:
        _check(False, entity, color)


def parse_x_rgbi(color: str) -> tuple[str, tuple[float, float, float]]:
    """Parse the string specifying a color in X's rgbi: format."""
    entity = 'X rgbi color'

    try:
        _check(color.startswith('rgbi:'), entity, color, 'does not start with "rgbi:"')
        cs = [float(c) for c in color[5:].split('/')]
        _check(len(cs) == 3, entity, color, 'does not have three components')
        for c in cs:
            _check(0 <= c <= 1, entity, color, 'has non-normal component')
        return 'srgb', cast(tuple[float, float, float], tuple(cs))
    except SyntaxError:
        raise
    except:
        _check(False, entity, color)


class Format(enum.Enum):
    """
    A selector for a color output format.

    Attributes:
        FUNCTION: for ``<tag>(<coordinates>)`` notation
        HEX: for ``#<hex>`` notation
        CSS: for ``color()``, ``oklab()``, ``oklch()``, and ``rgb()`` notation
        X: for ``rgb:<hex>/<hex>/<hex>`` and ``rgbi:<float>/<float>/<float>``
            notation
    """
    FUNCTION = 'f'
    HEX = 'h'
    CSS = 'c'
    X = 'x'


def parse_format_spec(spec: str) -> tuple[Format, int]:
    """
    Parse a color format specifier.

    Format specifiers for colors consist of two optional components matching the
    regular expression ``(\\.\\d\\d?)?[cfhx]?``. Consistent with the conventions
    of the Python format mini-language, the precision for color coordinates
    comes before the format selector. Valid selectors are

      * *c* for CSS notation,
      * *f* for ``<tag>(<coordinates>)`` function notation,
      * *h* for ``#<hex>`` hexadecimal notation,
      * *x* for ``rgb:<hex>/<hex>/<hex>`` or ``rgbi:<float>/<float>/<float>``
        notation.

    All but *h* for hexadecimal notation may be prefixed with a precision. The
    default format is *f* for function notation and the default precision is 5.
    """
    format = Format.FUNCTION
    precision = None
    s = spec

    # Parse format selector
    if s:
        f = s[-1]
        if f in ('c', 'f', 'h', 'x'):
            format = Format(f)
            s = s[:-1]

    # Parse precision
    if s.startswith('.'):
        try:
            precision = int(s[1:])
        except:
            raise ValueError(f'malformed precision in "{spec}"')
        s = ''

    # Check for errors
    if s:
        raise ValueError(f'malformed color format "{spec}"')
    if format is Format.HEX and precision is not None:
        raise ValueError(f'"{spec}" provides precision for hex format')

    return format, precision or 5


def stringify(
    tag: str,
    coordinates: tuple[int] | tuple[float, float, float],
    format: Format = Format.FUNCTION,
    precision: int = 5
) -> str:
    """
    Format the tagged coordinates in the specified format and with the specified
    precision.
    """
    if format is Format.HEX:
        if tag != 'rgb256':
            ValueError(f"{tag} has no serialization in the web's hexadecimal format")
        return '#' + ''.join(f'{c:02x}' for c in coordinates)
    elif format is Format.X:
        if tag not in ('rgb256', 'srgb'):
            ValueError(f"{tag} has no serialization in X's rgb:/rgbi: formats")
        if all(isinstance(c, int) for c in coordinates):
            return 'rgb:' + '/'.join(f'{c:02x}' for c in coordinates)
        else:
            return 'rgbi:' + '/'.join(f'{float(c):.{precision}}' for c in coordinates)

    separator = ' ' if format is Format.CSS else ', '
    coordinate_text = separator.join(
        f'{c}' if isinstance(c, int) else f'{c:.{precision}}'
        for c in coordinates
    )

    if format is Format.FUNCTION:
        return f'{tag}({coordinate_text})'

    css_format = Space.resolve(tag).css_format
    if css_format is None:
        raise ValueError(f'{tag} has no CSS serialization')
    return css_format.format(coordinate_text)
