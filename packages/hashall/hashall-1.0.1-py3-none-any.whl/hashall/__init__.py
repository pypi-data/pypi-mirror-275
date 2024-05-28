# Copyright (c) 2024 Khiat Mohammed Abderrezzak
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Author: Khiat Mohammed Abderrezzak <khiat.abderrezzak@gmail.com>


"""Sophisticate Hashed Data Structures"""


__all__: list = ["hlist", "htuple", "hbytes", "hbytearray"]


from word2number.w2n import word_to_num


class hlist(list):
    def __getitem__(self: "hlist", index: int | str):
        if isinstance(index, str):
            index: str = index.strip()
        try:
            return super().__getitem__(index)
        except TypeError as e0:
            pass
        try:
            return super().__getitem__(int(index))
        except ValueError as e1:
            pass
        if len(index) > 1:
            try:
                if index[0] == "-":
                    return super().__getitem__(-word_to_num(index))
                elif index[0] == "+":
                    return super().__getitem__(word_to_num(index[1:]))
                else:
                    return super().__getitem__(word_to_num(index))
            except ValueError as e2:
                raise KeyError(index) from None
        else:
            raise KeyError(index)

    def __setitem__(self: "hlist", index: int | str, value: object):
        if isinstance(index, str):
            index: str = index.strip()
        try:
            return super().__setitem__(index, value)
        except TypeError as e3:
            pass
        try:
            return super().__setitem__(int(index), value)
        except ValueError as e4:
            pass
        if len(index) > 1:
            try:
                if index[0] == "-":
                    return super().__setitem__(-word_to_num(index), value)
                elif index[0] == "+":
                    return super().__setitem__(word_to_num(index[1:]), value)
                else:
                    return super().__setitem__(word_to_num(index), value)
            except ValueError as e5:
                raise KeyError(index) from None
        else:
            raise KeyError(index)


class htuple(tuple):
    def __getitem__(self: "htuple", index: int | str):
        if isinstance(index, str):
            index: str = index.strip()
        try:
            return super().__getitem__(index)
        except TypeError as e6:
            pass
        try:
            return super().__getitem__(int(index))
        except ValueError as e7:
            pass
        if len(index) > 1:
            try:
                if index[0] == "-":
                    return super().__getitem__(-word_to_num(index))
                elif index[0] == "+":
                    return super().__getitem__(word_to_num(index[1:]))
                else:
                    return super().__getitem__(word_to_num(index))
            except ValueError as e8:
                raise KeyError(index) from None
        else:
            raise KeyError(index)

    def __setitem__(self: "htuple", index: int | str, value: object):
        if isinstance(index, str):
            index: str = index.strip()
        try:
            return super().__setitem__(index, value)
        except TypeError as e9:
            pass
        try:
            return super().__setitem__(int(index), value)
        except ValueError as e10:
            pass
        if len(index) > 1:
            try:
                if index[0] == "-":
                    return super().__setitem__(-word_to_num(index), value)
                elif index[0] == "+":
                    return super().__setitem__(word_to_num(index[1:]), value)
                else:
                    return super().__setitem__(word_to_num(index), value)
            except ValueError as e11:
                raise KeyError(index) from None
        else:
            raise KeyError(index)


class hstr(str):
    def __getitem__(self: "hstr", index: int | str):
        if isinstance(index, str):
            index: str = index.strip()
        try:
            return super().__getitem__(index)
        except TypeError as e12:
            pass
        try:
            return super().__getitem__(int(index))
        except ValueError as e13:
            pass
        if len(index) > 1:
            try:
                if index[0] == "-":
                    return super().__getitem__(-word_to_num(index))
                elif index[0] == "+":
                    return super().__getitem__(word_to_num(index[1:]))
                else:
                    return super().__getitem__(word_to_num(index))
            except ValueError as e14:
                raise KeyError(index) from None
        else:
            raise KeyError(index)

    def __setitem__(self: "hstr", index: int | str, value: object):
        if isinstance(index, str):
            index: str = index.strip()
        try:
            return super().__setitem__(index, value)
        except TypeError as e15:
            pass
        try:
            return super().__setitem__(int(index), value)
        except ValueError as e16:
            pass
        if len(index) > 1:
            try:
                if index[0] == "-":
                    return super().__setitem__(-word_to_num(index), value)
                elif index[0] == "+":
                    return super().__setitem__(word_to_num(index[1:]), value)
                else:
                    return super().__setitem__(word_to_num(index), value)
            except ValueError as e17:
                raise KeyError(index) from None
        else:
            raise KeyError(index)


class hbytes(bytes):
    def __getitem__(self: "hbytes", index: int | str):
        if isinstance(index, str):
            index: str = index.strip()
        try:
            return super().__getitem__(index)
        except TypeError as e18:
            pass
        try:
            return super().__getitem__(int(index))
        except ValueError as e19:
            pass
        if len(index) > 1:
            try:
                if index[0] == "-":
                    return super().__getitem__(-word_to_num(index))
                elif index[0] == "+":
                    return super().__getitem__(word_to_num(index[1:]))
                else:
                    return super().__getitem__(word_to_num(index))
            except ValueError as e20:
                raise KeyError(index) from None
        else:
            raise KeyError(index)

    def __setitem__(self: "hbytes", index: int | str, value: object):
        if isinstance(index, str):
            index: str = index.strip()
        try:
            return super().__setitem__(index, value)
        except TypeError as e21:
            pass
        try:
            return super().__setitem__(int(index), value)
        except ValueError as e22:
            pass
        if len(index) > 1:
            try:
                if index[0] == "-":
                    return super().__setitem__(-word_to_num(index), value)
                elif index[0] == "+":
                    return super().__setitem__(word_to_num(index[1:]), value)
                else:
                    return super().__setitem__(word_to_num(index), value)
            except ValueError as e23:
                raise KeyError(index) from None
        else:
            raise KeyError(index)


class hbytearray(bytearray):
    def __getitem__(self: "hbytearray", index: int | str):
        if isinstance(index, str):
            index: str = index.strip()
        try:
            return super().__getitem__(index)
        except TypeError as e24:
            pass
        try:
            return super().__getitem__(int(index))
        except ValueError as e25:
            pass
        if len(index) > 1:
            try:
                if index[0] == "-":
                    return super().__getitem__(-word_to_num(index))
                elif index[0] == "+":
                    return super().__getitem__(word_to_num(index[1:]))
                else:
                    return super().__getitem__(word_to_num(index))
            except ValueError as e26:
                raise KeyError(index) from None
        else:
            raise KeyError(index)

    def __setitem__(self: "hbytearray", index: int | str, value: object):
        if isinstance(index, str):
            index: str = index.strip()
        try:
            return super().__setitem__(index, value)
        except TypeError as e27:
            pass
        try:
            return super().__setitem__(int(index), value)
        except ValueError as e28:
            pass
        if len(index) > 1:
            try:
                if index[0] == "-":
                    return super().__setitem__(-word_to_num(index), value)
                elif index[0] == "+":
                    return super().__setitem__(word_to_num(index[1:]), value)
                else:
                    return super().__setitem__(word_to_num(index), value)
            except ValueError as e29:
                raise KeyError(index) from None
        else:
            raise KeyError(index)


def _main() -> None:
    print("hashall")


if __name__ == "__main__":
    _main()
