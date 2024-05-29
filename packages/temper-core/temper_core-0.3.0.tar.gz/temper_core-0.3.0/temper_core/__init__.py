"""
Implementation of many of the connected methods in temper.
"""

import sys
import logging
from abc import abstractmethod
from functools import reduce
from logging import getLogger, INFO
from math import copysign, inf, isclose, isinf, isnan, nan
from typing import (
    Union,
    Any,
    Callable,
    Iterable,
    NoReturn,
    TypeVar,
    Sequence,
    Generic,
    Protocol,
    Mapping,
    Optional,
    MutableSequence,
    cast,
)
from sys import float_info
from datetime import date as Date, datetime, timezone
from types import MappingProxyType

Unset = None
"Abstraction used for tracking unset args."


class TemperComparable(Protocol):
    """Base class for comparable temper objects."""

    __slots__ = ()

    @abstractmethod
    def __le__(self, other: object) -> bool:
        pass

    @abstractmethod
    def __lt__(self, other: object) -> bool:
        pass

    @abstractmethod
    def __ge__(self, other: object) -> bool:
        pass

    @abstractmethod
    def __gt__(self, other: object) -> bool:
        pass


T = TypeVar("T")
U = TypeVar("U")
C = TypeVar("C", bound="TemperComparable")


class TemperObject:
    "All user-defined classes include this marker class."
    __slots__ = ()


class TemperEnum(TemperObject):
    "Enum classes are user-defined classes additionally with this marker."
    __slots__ = ()


def get_static(reified_type, symbol=None) -> NoReturn:
    "There's no way to extract the class from a reified type at this time."
    raise NotImplementedError()


def temper_print(value: T) -> None:
    "Temper semantics for printing."
    if isinstance(value, str):
        print(value)
    else:
        print(repr(value))


def init_simple_logging():
    "Log all at INFO or higher to stdout without decoration."
    logging.basicConfig(
        handlers=[logging.StreamHandler(stream=sys.stdout)],
        level=INFO,
        format="%(message)s",
    )


class LoggingConsole(TemperObject):
    """One class per file to log data to the console."""

    __slots__ = ("logger",)

    def __init__(self, name: str):
        self.logger = getLogger(name)

    def log(self, message: str) -> None:
        """Log a message to the console."""
        self.logger.log(INFO, message)


def str_cat(*parts: str) -> str:
    "Concatenate parts into a single string."
    return "".join(map(str, parts))


def bubble() -> Any:
    "Raises an exception for Temper bubbling."
    raise RuntimeError()


def float_cmp(left: float, right: float):
    "Three way compares floats, caring about nan and sign of zeroes."
    if isnan(left):
        return 0 if isnan(right) else 1
    if isnan(right):
        return -1
    if left == 0 and right == 0:
        left = copysign(1.0, left)
        right = copysign(1.0, right)
    return (left > right) - (left < right)


def float_eq(left: float, right: float):
    "Checks if two floats are exactly equal, caring about nan and sign of zeros."
    return (left == right and copysign(1.0, left) == copysign(1.0, right)) or (
        isnan(left) and isnan(right)
    )


def float_not_eq(left: float, right: float):
    "Checks if two floats not are exactly equal, caring about nan and sign of zeros."
    return (left != right or copysign(1.0, left) != copysign(1.0, right)) and not (
        isnan(left) and isnan(right)
    )


def float_lt_eq(left: float, right: float) -> bool:
    "Checks if left <= right, caring about sign of zeros."
    return float_cmp(left, right) <= 0


def float_lt(left: float, right: float) -> bool:
    "Checks if left < right, caring about sign of zeros."
    return float_cmp(left, right) < 0


def float_gt_eq(left: float, right: float) -> bool:
    "Checks if left >= right, caring about sign of zeros."
    return float_cmp(left, right) >= 0


def float_gt(left: float, right: float) -> bool:
    "Checks if left <= right, caring about sign of zeros."
    return float_cmp(left, right) > 0


def generic_cmp(left: C, right: C) -> int:
    "Three way compares objects, caring about the sign of zeroes of floats."
    if isinstance(left, float) and isinstance(right, float):
        return float_cmp(left, right)
    return (left > right) - (left < right)


def generic_eq(left: T, right: T) -> bool:
    "Checks if two objects are exactly equal, caring about the sign of zeros of floats."
    if isinstance(left, float) and isinstance(right, float):
        return float_eq(left, right)
    return left == right


def generic_not_eq(left: T, right: T) -> bool:
    """
    Checks if two objects are not exactly equal, caring about the sign of zeros of
    floats.
    """
    if isinstance(left, float) and isinstance(right, float):
        return float_not_eq(left, right)
    return left != right


def generic_lt_eq(left: C, right: C) -> bool:
    "Checks if two left <= right, caring about the sign of zeros of floats."
    if isinstance(left, float) and isinstance(right, float):
        return float_lt_eq(left, right)
    return left <= right


def generic_lt(left: C, right: C) -> bool:
    "Checks if two left <=right, caring about the sign of zeros of floats."
    if isinstance(left, float) and isinstance(right, float):
        return float_lt(left, right)
    return left < right


def generic_gt_eq(left: C, right: C) -> bool:
    "Checks if two left >= right, caring about the sign of zeros of floats."
    if isinstance(left, float) and isinstance(right, float):
        return float_gt_eq(left, right)
    return left >= right


def generic_gt(left: C, right: C) -> bool:
    "Checks if two left > right, caring about the sign of zeros of floats."
    if isinstance(left, float) and isinstance(right, float):
        return float_gt(left, right)
    return left > right


def arith_int_div(dividend: int, divisor: int) -> int:
    "Performs division on int, resulting in an int."
    # TODO Inline?
    return dividend // divisor


def arith_dub_div(dividend: float, divisor: float) -> float:
    """
    Performs division on Float64 (python float); dub stands for "double", like
    the c datatype.
    """
    # TODO Inline?
    return dividend / divisor


def arith_int_mod(dividend: int, divisor: int) -> int:
    """
    Performs remainder on ints, raising an error if divisor is zero.
    arith_int_mod(5, 3) == 2
    arith_int_mod(-5, -3) == 1
    arith_int_mod(5, -3) == -1
    arith_int_mod(-5, -3) == -2
    """
    return dividend % divisor


def arith_dub_mod(dividend: float, divisor: float) -> float:
    "Performs remainder on floats, raising an error if it fails."
    return dividend % divisor


def isinstance_int(val: T) -> bool:
    "Python bool is a subclass of int, but Temper treats them as separate types."
    return isinstance(val, int) and not isinstance(val, bool)


def isinstance_char(val: T) -> bool:
    "Temper char are represented as single character strings."
    return isinstance(val, str) and len(val) == 1


def cast_none(val: Union[T, None]) -> T:
    "Checks that value is not None."
    if val is None:
        raise TypeError()
    return val


def cast_by_type(val: Any, py_type: type):
    "Cast to a python type by an isinstance check."
    if isinstance(val, py_type):
        return val
    else:
        raise TypeError()


def cast_by_test(val: T, predicate: Callable[[T], bool]) -> Any:
    "This cast validates that a temper function meets some predicate, e.g. callable."
    if not predicate(val):
        raise ValueError()
    return val


class Label(BaseException):
    "A label enables labled breaks with reasonably readable python."
    __slots__ = ()

    def __enter__(self) -> "Label":
        return self

    def continue_(self) -> "Label":
        "Continue to this label."
        raise self

    def break_(self) -> "Label":
        "Break out of this label."
        raise self

    def __exit__(self, _exc_type: type, exc: BaseException, _traceback: Any) -> bool:
        return exc is self


class LabelPair(BaseException):
    "Handles an edge case in the semantics of labeled breaks."
    __slots__ = ("continuing",)
    continuing: "InnerLabel"

    def __init__(self):
        self.continuing = InnerLabel()

    def __enter__(self) -> "LabelPair":
        return self

    def break_(self) -> "LabelPair":
        "Break out of this label."
        raise self

    def continue_(self) -> "InnerLabel":
        "Continue to this label."
        raise self.continuing

    def __exit__(self, _exc_type: type, exc: BaseException, _exc_tb: Any) -> bool:
        return exc is self


class InnerLabel(BaseException):
    "Continue part of a LabelPair."
    __slots__ = ()

    def __enter__(self):
        return None

    def __exit__(self, exc_type: type, exc_val: BaseException, exc_tb: Any) -> bool:
        return exc_val is self


class Symbol(object):
    "A Temper Symbol."

    __slots__ = ("_text",)
    _text: str

    def __init__(self, text):
        self._text = text

    @property
    def text(self) -> str:
        "Returns the text of the symbol."
        return self._text

    def __eq__(self, other) -> bool:
        if isinstance(other, Symbol):
            raise NotImplementedError()
        return self._text == other._text

    def __hash__(self) -> int:
        return hash(self._text)

    def __repr__(self) -> str:
        return f"symbol({self.text!r})"

    def __str__(self) -> str:
        return self._text


class StringSlice:
    "Substrings of various types, can be used to read charCodes."
    __slots__ = ()

    def __iter__(self):
        raise NotImplementedError()

    def advance(self, count: int) -> "StringSlice":
        "Move the cursor forward by the given number of characters."
        raise NotImplementedError()

    def intersect(self, other: "StringSlice") -> "StringSlice":
        "The code units that are both in self and in other"
        raise NotImplementedError()

    def exclude_after(self, other: "StringSlice") -> "StringSlice":
        "The code units in this before the left of other"
        raise NotImplementedError()

    def _left_plus(self, count):
        raise NotImplementedError()

    def __bool__(self) -> bool:
        raise NotImplementedError()

    def __len__(self) -> int:
        raise NotImplementedError()

    def __str__(self) -> str:
        raise NotImplementedError()

    def has_at_least(self, count: int) -> int:
        "Checks if the length is enough."
        return count <= 0 or self._left_plus(count) != -1

    def read(self) -> int:
        "Get a the current head's code point, depending on the slice type."
        try:
            return next(iter(self))
        except StopIteration as exc:
            # Maybe appropriate type?
            # See https://docs.python.org/3/library/exceptions.html#StopIteration
            raise RuntimeError() from exc

    @property
    def length(self) -> int:
        "Temper's version of len()."
        return len(self)

    def to_string(self) -> str:
        "Temper's version of str()."
        return str(self)

    @property
    def is_empty(self) -> bool:
        "Checks if the current slice is empty (eg. if read would fail)."
        return not self


class Utf8StringSlice(StringSlice):
    "Implementation of a StringSlice that advances over utf8 codePoints."
    __slots__ = ("_content", "_left", "_right")
    _left: int
    _right: int
    _content: str

    def __init__(self, left: int, right: int, content: str):
        if left >= right:
            left = 0
            right = 0
            content = ""
        self._left = left
        self._right = right
        self._content = content

    def __iter__(self) -> Iterable[int]:
        left, right, content = self._left, self._right, self._content
        if left < right:
            idx, sub = left >> 2, left & 3
            ridx, rsub = right >> 2, right & 3
            # Iterate over every but the last code point in range.
            # The loop that follows iterates over bytes up to rsub in the last.
            while idx < ridx:
                code_point = ord(content[idx])
                size = _utf8_size(code_point)
                for byte_index in range(sub, size):
                    yield _utf8_byte_of(code_point, byte_index, size)
                idx, sub = idx + 1, 0
            if rsub:
                code_point = ord(content[idx])
                size = _utf8_size(code_point)
                for byte_index in range(sub, rsub):
                    yield _utf8_byte_of(code_point, byte_index, size)

    def __bool__(self) -> bool:
        return self._left < self._right

    def __len__(self) -> int:
        left, right, content = self._left, self._right, self._content
        num = -(left & 3) + (right & 3)
        for i in range(left >> 2, right >> 2):
            num += _utf8_size(ord(content[i]))
        return num

    def _left_plus(self, count: int) -> int:
        left, content = self._left, self._content
        len_content = len(content)
        idx, sub = left >> 2, left & 3

        while count > 0 and idx < len_content:
            rem = _utf8_size(ord(content[idx])) - sub
            if rem > count:
                sub += count
                count = 0
            else:
                count -= rem
                sub = 0
                idx += 1

        return -1 if count else min(idx << 2 | sub, self._right)

    def advance(self, count: int) -> "Utf8StringSlice":
        left, right, content = self._left_plus(count), self._right, self._content
        if left < 0:
            left, right, content = 0, 0, ""
        if left == self._left:
            return self
        return Utf8StringSlice(left, right, content)

    def limit(self, count: int) -> "Utf8StringSlice":
        "Similar to advance, but moves the end count away from the current advance"
        left, right, content = self._left, self._left_plus(count), self._content
        if left >= right:
            left, right, content = 0, 0, ""
        if right == self._right:
            return self
        return Utf8StringSlice(left, right, content)

    def intersect(self, other: StringSlice) -> "Utf8StringSlice":
        content, left, right = self._content, self._left, self._right
        other_typed = cast(Utf8StringSlice, other)
        other_left, other_right = other_typed._left, other_typed._right

        # Derivation of this in StringSliceHelpers
        if other_left >= right:
            new_left = right
            new_right = right
        elif other_right <= left:
            new_left = left
            new_right = left
        else:
            new_left = max(left, other_left)
            new_right = min(right, other_right)

        if new_left == left and new_right == right:
            return self
        else:
            return Utf8StringSlice(new_left, new_right, content)

    def exclude_after(self, other: StringSlice) -> "Utf8StringSlice":
        content, left, right = self._content, self._left, self._right
        other_typed = cast(Utf8StringSlice, other)
        other_left = other_typed._left
        new_right = max(left, min(right, other_left))
        if right == new_right:
            return self
        else:
            return Utf8StringSlice(left, new_right, content)

    def to_json(self):
        "Convert the Object into a JSON-compatable form."
        left, right, content = self._left, self._right, self._content
        return {"left": left, "right": right, "content": content}

    def __str__(self) -> str:
        left, right, content = self._left, self._right, self._content
        if left >= right:
            return ""
        lidx, lsub = left >> 2, left & 3
        ridx, rsub = right >> 2, right & 3
        pre, post = "", ""
        if lsub:
            pre = "\ufffd"
            lidx += 1
        if rsub:
            if ridx - 1 >= lidx:
                post = "\ufffd"
            else:
                pre = "\ufffd"
        return pre + content[lidx:ridx] + post


class Utf16StringSlice(StringSlice):
    "Implementation of a StringSlice that advances over utf16 codePoints."
    __slots__ = ("_content", "_left", "_right")
    _left: int
    _right: int
    _content: str

    def __init__(self, left: int, right: int, content: str):
        if left >= right:
            left = 0
            right = 0
            content = ""
        self._left = left
        self._right = right
        self._content = content

    def __iter__(self) -> Iterable[int]:
        left, right, content = self._left, self._right, self._content
        lidx, lsub = left >> 1, left & 1
        ridx, rsub = right >> 1, right & 1
        idx = lidx
        if lsub and idx < ridx:
            code_point = ord(content[idx])
            yield 0xDC00 | ((code_point - 0x1_0000) & 0x3FF)
            idx += 1
        while idx < ridx:
            code_point = ord(content[idx])
            if code_point < 0x1_0000:
                yield code_point
            else:
                code_point -= 0x1_0000
                yield 0xD800 | ((code_point >> 10) & 0x3FF)
                yield 0xDC00 | (code_point & 0x3FF)
            idx += 1
        if rsub and idx == ridx:
            code_point = ord(content[idx])
            yield (0xD800 | (((code_point - 0x1_0000) >> 10) & 0x3FF))

    def __bool__(self) -> bool:
        return bool(self._content)

    def __len__(self) -> int:
        left, right, content = self._left, self._right, self._content
        lidx, lsub = left >> 1, left & 1
        ridx, rsub = right >> 1, right & 1
        num = rsub + ridx - lidx
        if lsub:
            lidx += 1
        for i in range(lidx, ridx):
            code_point = ord(content[i])
            if code_point > 0x1_0000:
                num += 1
        return num

    def _left_plus(self, count: int) -> int:
        left, content = self._left, self._content
        if count <= 0:
            return left
        len_content = len(content)
        idx, sub = left >> 1, left & 1

        while count > 0 and idx < len_content:
            rem = _utf16_size(content[idx]) - sub
            if rem > count:
                sub += count
                count = 0
            else:
                count -= rem
                sub = 0
                idx += 1

        return -1 if count else min(idx << 1 | sub, self._right)

    def advance(self, count: int) -> "Utf16StringSlice":
        left, right, content = self._left_plus(count), self._right, self._content
        if left < 0:
            left, right, content = 0, 0, ""
        if left == self._left:
            return self
        return Utf16StringSlice(left, right, content)

    def limit(self, count: int) -> "Utf16StringSlice":
        "Similar to advance, but moves the end count away from the current advance"
        left, right, content = self._left, self._left_plus(count), self._content
        if left >= right:
            left, right, content = 0, 0, ""
        if right == self._right:
            return self
        return Utf16StringSlice(left, right, content)

    def intersect(self, other: StringSlice) -> "Utf16StringSlice":
        content, left, right = self._content, self._left, self._right
        other_typed = cast(Utf16StringSlice, other)
        other_left, other_right = other_typed._left, other_typed._right

        # Derivation of this in StringSliceHelpers
        if other_left >= right:
            new_left = right
            new_right = right
        elif other_right <= left:
            new_left = left
            new_right = left
        else:
            new_left = max(left, other_left)
            new_right = min(right, other_right)

        if new_left == left and new_right == right:
            return self
        else:
            return Utf16StringSlice(new_left, new_right, content)

    def exclude_after(self, other: StringSlice) -> "Utf16StringSlice":
        content, left, right = self._content, self._left, self._right
        other_typed = cast(Utf16StringSlice, other)
        other_left = other_typed._left
        new_right = max(left, min(right, other_left))
        if right == new_right:
            return self
        else:
            return Utf16StringSlice(left, new_right, content)

    def to_json(self):
        "Convert the Object into a JSON-compatable form."
        left, right, content = self._left, self._right, self._content
        return {"left": left, "right": right, "content": content}

    def __str__(self) -> str:
        left, right, content = self._left, self._right, self._content
        if left == right:
            # It's ok to split a pair if left and right are together
            return ""
        lidx, lsub = left >> 1, left & 1
        ridx, rsub = right >> 1, right & 1
        if lsub:
            pre = "\ufffd"
            lidx += 1
        else:
            pre = ""
        if rsub:
            post = "\ufffd"
        else:
            post = ""
        return pre + content[lidx:ridx] + post


class CodePointStringSlice(StringSlice):
    "Implementation of a StringSlice that advances over complete utf32 codePoints."
    __slots__ = ("_content", "_left", "_right")
    _left: int
    _right: int
    _content: str

    def __init__(self, left: int, right: int, content: str):
        if left >= right:
            content = ""
            left = 0
            right = 0
        self._left = left
        self._right = right
        self._content = content

    def __iter__(self) -> Iterable[int]:
        left, right, content = self._left, self._right, self._content
        for i in range(left, right):
            yield ord(content[i])

    def __len__(self) -> int:
        return self._right - self._left

    def __bool__(self) -> bool:
        return bool(self._content)

    def _left_plus(self, count: int) -> int:
        left = self._left + count
        return -1 if left > len(self._content) else min(left, self._right)

    def advance(self, count: int) -> "CodePointStringSlice":
        if count <= 0:
            result = self
        else:
            left, right, content = self._left_plus(count), self._right, self._content
            if left < 0:
                left, right, content = 0, 0, ""
            result = CodePointStringSlice(left, right, content)
        return result

    def limit(self, count: int) -> "CodePointStringSlice":
        "Similar to advance, but moves the end count away from the current advance"
        if count <= 0:
            result = CodePointStringSlice(0, 0, "")
        else:
            left, right, content = self._left, self._left_plus(count), self._content
            if right <= self._left:
                left, right, content = 0, 0, ""
            result = CodePointStringSlice(left, right, content)
        return result

    def intersect(self, other: StringSlice) -> "CodePointStringSlice":
        content, left, right = self._content, self._left, self._right
        other_typed = cast(CodePointStringSlice, other)
        other_left, other_right = other_typed._left, other_typed._right

        # Derivation of this in StringSliceHelpers
        if other_left >= right:
            new_left = right
            new_right = right
        elif other_right <= left:
            new_left = left
            new_right = left
        else:
            new_left = max(left, other_left)
            new_right = min(right, other_right)

        if new_left == left and new_right == right:
            return self
        else:
            return CodePointStringSlice(new_left, new_right, content)

    def exclude_after(self, other: StringSlice) -> "CodePointStringSlice":
        content, left, right = self._content, self._left, self._right
        other_typed = cast(CodePointStringSlice, other)
        other_left = other_typed._left
        new_right = max(left, min(right, other_left))
        if right == new_right:
            return self
        else:
            return CodePointStringSlice(left, new_right, content)

    def __str__(self) -> str:
        return self._content[self._left : self._right]

    def to_json(self):
        "Convert the Object into a JSON-compatable form."
        return {"left": self._left, "right": self._right, "content": self._content}


class DenseBitVector(object):
    "An expandable bitvector backed by a bytearray."
    __slots__ = ("_bytearray",)

    def __init__(self, capacity: int):
        "Capacity is in bits."
        self._bytearray = bytearray((capacity + 7) >> 3)

    def __bool__(self) -> bool:
        "Test if any bit is set."
        return bool(rb"\0" in self._bytearray)

    def __bytes__(self) -> bytes:
        "Convert the bit vector into a read-only bytes value."
        return bytes(self._bytearray.rstrip(b"\0"))

    def get(self, idx: int) -> bool:
        "Read a bit from the vector as a boolean; or false if out of bounds."
        if idx < 0:
            return False
        byte_index = idx >> 3
        if byte_index >= len(self._bytearray):
            return False
        return bool(self._bytearray[byte_index] & (1 << (idx & 7)))

    def set(self, idx: int, bit: bool):
        "set a bit in the bit vector, expanding the vector as needed."
        if idx < 0:
            raise IndexError()
        byte_array = self._bytearray
        byte_size = len(byte_array)
        byte_index = idx >> 3
        if byte_index >= byte_size:
            byte_array.extend(b"\0" * (byte_index + 1 - byte_size))
        mask = 1 << (idx & 7)
        if bit:
            byte_array[byte_index] |= mask
        else:
            byte_array[byte_index] &= ~mask


# Constructors


def string_utf8(string: str) -> Utf8StringSlice:
    "Implements connected method String::utf8."
    return Utf8StringSlice(0, len(string) << 2, string)


def string_utf16(string: str) -> Utf16StringSlice:
    "Implements connected method String::utf16."
    return Utf16StringSlice(0, len(string) << 1, string)


def string_code_points(string: str) -> CodePointStringSlice:
    "Implements connected method String::codePoints."
    return CodePointStringSlice(0, len(string), string)


# Connected methods


def int_to_float64(value: int) -> float:
    "Implements connected method Int::toFloat64."
    # TODO Inline?
    return float(value)


def int_to_float64_unsafe(value: int) -> float:
    "Implements connected method Int::toFloat64Unsafe."
    try:
        return float(value)
    except OverflowError:
        return -inf if value < 0 else inf


def int_to_string(num, radix: int = 10) -> str:
    "Implements connected method Int::toString."
    if not 2 <= radix < 36:
        raise ValueError()
    elif radix == 10:
        return str(num)
    elif radix == 16:
        return f"{num:x}"
    elif radix == 8:
        return f"{num:o}"
    else:

        def seq(rem):
            if rem == 0:
                yield "0"

            while rem:
                yield "0123456789abcdefghijklmnopqrstuvwxyz"[rem % radix]
                rem //= radix

            if num < 0:
                yield "-"

        return "".join(reversed(list(seq(abs(num)))))


def float64_max(x: float, y: float) -> float:
    "Implements connected method Float64::max."
    # Already returns nan if x is nan.
    return nan if isnan(y) else max(x, y)


def float64_min(x: float, y: float) -> float:
    "Implements connected method Float64::min."
    # Already returns nan if x is nan.
    return nan if isnan(y) else min(x, y)


def float64_near(
    x: float,
    y: float,
    rel_tol: Optional[float] = Unset,
    abs_tol: Optional[float] = Unset,
) -> float:
    "Implements connected method Float64::near."
    # This exactly matches isclose behavior, but matching our forwarding our
    # optionals to python named args is awkward, so duplicate the logic.
    # TODO We could possibly inline usage of isclose instead of this logic.
    if rel_tol is Unset:
        rel_tol = 1e-9
    if abs_tol is Unset:
        abs_tol = 0.0
    return isclose(x, y, rel_tol=rel_tol, abs_tol=abs_tol)


def float64_sign(x: float) -> float:
    "Implements connected method Float64::sign."
    return x if isnan(x) or x == 0.0 else copysign(1.0, x)


def float64_to_int(value: float) -> int:
    "Implements connected method Float64::toInt."
    # Potentially much more expensive in Python than other backends.
    # TODO Should we tighten the limits for float to int?
    # TODO Inline if we don't tighten limits?
    return int(value)


def float64_to_int_unsafe(value: float) -> int:
    "Implements connected method Float64::toIntUnsafe."
    # Potentially much more expensive in Python than other backends.
    # TODO Should we tighten the limits for float to int?
    try:
        return int(value)
    except OverflowError:
        # There's not really a good option for infinity or whatnot, but using
        # the extreme float values, which work in my experience, are at least
        # no smaller than for other float values.
        return int(copysign(float_info.max, value))
    except ValueError:
        # Happens for NaN, but for any other such case, also use what we want.
        return 0


def float64_to_string(value: float) -> str:
    "Implements connected method Float64::toString."
    if value == inf:
        return "Infinity"
    elif value == -inf:
        return "-Infinity"
    elif isnan(value):
        return "NaN"
    else:
        return str(value)


def boolean_to_string(value: bool) -> str:
    "Turns a stirng into a boolean (lowercase like temper)."
    return "true" if value else "false"


def date_to_string(value: Date) -> str:
    "Turns a date into a string, YYYY-MM-DD."
    return f"{value.year:04d}-{value.month:02d}-{value.day:02d}"


utc = timezone.utc


def date_today() -> Date:
    "Gets today's date as in UTC+0."
    return datetime.now(utc).date()


def years_between(start: Date, end: Date) -> int:
    year_delta = end.year - start.year
    month_delta = end.month - start.month
    if month_delta < 0 or (month_delta == 0 and end.day < start.day):
        year_delta -= 1
    return year_delta


def string_split(string: str, separator: str) -> Sequence[str]:
    "split a string, returning a list of elements."
    return tuple(string.split(separator)) if separator else tuple(string)


def string_to_float64(string: str) -> float:
    "Convert string to float following Temper rules"
    # Presume the common case, which also handles "NaN" and "Infinity".
    result = float(string)
    trimmed = string.strip()
    # But guard against things not in Temper.
    if (
        trimmed.startswith(".")
        or trimmed.endswith(".")
        or (isnan(result) and string != "NaN")
        or (isinf(result) and not string.endswith("Infinity"))
    ):
        raise ValueError(string)
    return result


def list_filter(lst: Sequence[T], predicate: Callable[[T], bool]) -> Sequence[T]:
    "Filter a list of elements, aborting on no-result."
    return tuple(i for i in lst if predicate(i))


def list_get(lst: Sequence[T], index: int) -> T:
    "Get an item from a list by index."
    if index < 0:  # Prohibit python index semantics
        raise IndexError()
    return lst[index]


def list_get_or(lst: Sequence[T], index: int, default: T) -> T:
    "Get an item from a list by index with a default."
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return default


def list_builder_add(
    lst: MutableSequence[T], elem: T, at: Optional[int] = Unset
) -> None:
    "Append a single element to a list."
    lst_len: int = len(lst)
    if at is Unset or at == lst_len:
        lst.append(elem)
    else:
        if at < 0 or at > lst_len:
            raise IndexError()
        lst.insert(at, elem)


def list_builder_add_all(
    lst: MutableSequence[T], elems: Sequence[T], at: Optional[int] = Unset
) -> None:
    "Append multiple elements to a list."
    lst_len: int = len(lst)
    if at is Unset or at == lst_len:
        lst.extend(elems)
    else:
        if at < 0 or at > lst_len:
            raise IndexError()
        lst[at:at] = elems


def list_join(lst: Sequence[T], separator: str, stringifier: Callable[[T], str]) -> str:
    "Join a list of items after converting them to strings."
    return separator.join(stringifier(i) for i in lst)


def list_map(lst: Sequence[T], func: Callable[[T], U]) -> Sequence[U]:
    "Map a list of elements."
    return tuple(func(i) for i in lst)


def list_builder_remove_last(lst: MutableSequence[T]) -> T:
    "Pops and returns the last item, if any, else raises."
    # TODO Inline?
    return lst.pop()


def list_builder_reverse(lst: MutableSequence[T]):
    "Reverses a list in place."
    lst.reverse()


def list_builder_splice(
    lst: MutableSequence[T],
    index: Optional[int] = Unset,
    remove_count: Optional[int] = Unset,
    new_values: Optional[Sequence[T]] = Unset,
) -> Sequence[T]:
    "Remove some items and insert others."
    # Work through defaults and bounds.
    if index is Unset or index < 0:
        index = 0
    if remove_count is Unset:
        remove_count = len(lst)
    elif remove_count < 0:
        remove_count = 0
    # Now take care of business.
    end_index = index + remove_count
    result = tuple(lst[index:end_index])
    lst[index:end_index] = () if new_values is Unset else new_values
    return result


def list_builder_set(lst: MutableSequence[T], idx: int, val: T) -> None:
    "set a list element, bubbling if out of bounds, or void on success."
    if idx < 0:
        raise IndexError()
    lst[idx] = val


def list_map_dropping(
    lst: Sequence[T], func: Callable[[T], Union[T, NoReturn]]
) -> Sequence[T]:
    "Map a list of elements, omitting any for which func raises any Exception."
    results = []
    for entry in lst:
        try:
            value = func(entry)
        except Exception:
            continue
        results.append(value)
    return tuple(results)


def list_slice(
    lst: Sequence[T], start_inclusive: int, end_exclusive: int
) -> Sequence[T]:
    "Almost exactly a Python slice, but indices are constrained to be >= 0."
    # TODO(tjp): Cheaper to always say tuple here, or separate out for ListBuilder use?
    return tuple(lst[max(start_inclusive, 0) : max(end_exclusive, 0)])


def listed_reduce(lst: Sequence[T], accumulate: Callable[[T, T], T]) -> T:
    return reduce(accumulate, lst)


def listed_reduce_from(
    lst: Sequence[T], initial: U, accumulate: Callable[[U, T], U]
) -> U:
    return reduce(accumulate, lst, initial)


def listed_to_list(lst: Sequence[T]) -> Sequence[T]:
    if isinstance(lst, tuple):
        return lst
    else:
        return tuple(lst)


def deque_remove_first(deq):
    "Defer to deque.popleft, except bubbling when the deque is empty."
    return deq.popleft()


def dense_bit_vector_set(instance: DenseBitVector, idx: int, bit: bool) -> None:
    "sets a bit within a dense bit vector."
    instance.set(idx, bit)


Key = TypeVar("Key")
Value = TypeVar("Value")


class Pair(Generic[Key, Value]):
    """
    A pair of a key and a value.
    Often used as Map entries
    """

    key: Key
    value: Value
    __slots__ = ("key", "value")

    def __init__(self, key: Key, value: Value) -> None:
        self.key = key
        self.value = value

    def __subscript__(self, index: int) -> Union[Key, Value]:
        if index == 0:
            return self.key
        elif index == 1:
            return self.value
        else:
            raise IndexError()


def map_constructor(
    entries: Sequence[Pair[Key, Value]]
) -> MappingProxyType[Key, Value]:
    "Implements Map's constructor."
    return MappingProxyType({entry.key: entry.value for entry in entries})


def map_builder_remove(builder: dict[Key, Value], key: Key) -> Value:
    "Implements MapBuilder's remove, which deletes an entry in a MapBuilder."
    # TODO Inline?
    return builder.pop(key)


def map_builder_set(builder: dict[Key, Value], key: Key, value: Value) -> None:
    "Sets entry on a MapBuilder."
    builder[key] = value


def mapped_has(mapped: Mapping[Key, Value], key: Key) -> bool:
    "Checks if a Mapped object has a Key key"
    # This can't be inlined well because order (mapped -> key) is swapped for
    # (key -> mapped). Which would be an issue if mapped and key were
    # expressions with SideEffects.
    return key in mapped


def mapped_to_map(mapped: Mapping[Key, Value]) -> MappingProxyType[Key, Value]:
    "Converts a Mapped to a Map."
    return MappingProxyType(dict(mapped))


def mapped_to_list(mapped: Mapping[Key, Value]) -> Sequence[Pair[Key, Value]]:
    "Implements .toList() for Mapping objects."
    return tuple(Pair(key, mapped[key]) for key in mapped.keys())


def mapped_to_list_builder(
    mapped: Mapping[Key, Value]
) -> MutableSequence[Pair[Key, Value]]:
    "Implements .toListBuilder() for Mapping objects."
    return list(Pair(key, mapped[key]) for key in mapped.keys())


def mapped_to_list_with(
    mapped: Mapping[Key, Value], func: Callable[[Key, Value], T]
) -> Sequence[T]:
    "Implements .toListWith{...} for Mapping objects."
    return tuple(func(key, mapped[key]) for key in mapped.keys())


def mapped_to_list_builder_with(
    mapped: Mapping[Key, Value], func: Callable[[Key, Value], T]
) -> MutableSequence[T]:
    "Implements .toListBuilderWith{...} for Mapping objects."
    return list(func(key, mapped[key]) for key in mapped.keys())


def mapped_for_each(
    mapped: Mapping[Key, Value], func: Callable[[Key, Value], None]
) -> None:
    "Implements .forEach {...} for Mapping objects."
    for key, value in mapped.items():
        func(key, value)


# Utility functions


def _utf8_size(code_point: int) -> int:
    if 0 <= code_point < 0o200:
        return 1
    elif 0o200 <= code_point < 0o4000:
        return 2
    elif 0o4000 <= code_point < 0o100000:
        return 3
    else:
        return 4


# never gets hit, so this is just to skip a check in the below function
_utf8_never = (0, 0, 0)

# (and_mask, or_mask, shift) triplets for each byte depending on the high 4 bits of a
# codepoint in UTF-8 encoding.
#
# | First code point | Last code point | Byte 0    | Byte 1    | Byte 2    | Byte 3    |
# | ---------------- | --------------- | --------- | --------- | --------- | --------- |
# | U+0000           | U+007F          | 0xxx_xxxx |           |           |           |
# | U+0080           | U+07FF          | 110x_xxxx | 10xx_xxxx |           |           |
# | U+0800           | U+FFFF          | 1110_xxxx | 10xx_xxxx | 10xx_xxxx |           |
# | U+10000          | U+10FFFF        | 1111_0xxx | 10xx_xxxx | 10xx_xxxx | 10xx_xxxx |
_utf8_byte_infos = (
    (0b0111_1111, 0, 0),
    _utf8_never,
    _utf8_never,
    _utf8_never,
    #
    (0b0001_1111, 0b1100_0000, 6),
    (0b0011_1111, 0b1000_0000, 0),
    _utf8_never,
    _utf8_never,
    #
    (0b0000_1111, 0b1110_0000, 12),
    (0b0011_1111, 0b1000_0000, 6),
    (0b0011_1111, 0b1000_0000, 0),
    _utf8_never,
    #
    (0b0000_0111, 0b1111_0000, 18),
    (0b0011_1111, 0b1000_0000, 12),
    (0b0011_1111, 0b1000_0000, 6),
    (0b0011_1111, 0b1000_0000, 0),
)


def _utf8_byte_of(code_point: int, byte_offset: int, n_bytes: int) -> int:
    and_mask, or_mask, shift = _utf8_byte_infos[(n_bytes - 1) * 4 + byte_offset]
    return ((code_point >> shift) & and_mask) | or_mask


def _utf16_size(char: str) -> int:
    return 1 + (ord(char) >= 0x10000)
