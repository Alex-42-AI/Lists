from __future__ import annotations

from typing import SupportsFloat, Callable


class SortedList:
    def __init__(self, *args: SupportsFloat, f: Callable = lambda x: x):
        self.__f, self.__value = f, []
        for arg in args:
            self.insert(arg)

    @property
    def value(self) -> list[SupportsFloat]:
        return self.__value

    @property
    def f(self) -> Callable:
        return self.__f

    def pop(self, index: int = -1) -> SupportsFloat:
        return self.__value.pop(index)

    def copy(self) -> SortedList:
        res = SortedList(f=self.f)
        res.__value = self.__value.copy()
        return res

    def insert(self, x: SupportsFloat) -> SortedList:
        try:
            low, high, f_x = 0, len(self), self.f(x)
            while low < high:
                mid = (low + high) // 2
                if f_x == (f_mid := self.f(self[mid])):
                    self.__value.insert(mid, x)
                    return self
                if f_x < f_mid:
                    high = mid
                else:
                    if low == mid:
                        break
                    low = mid + 1
            self.__value.insert(high, x)
        except (ValueError, TypeError):
            pass
        return self

    def remove(self, x: SupportsFloat) -> SortedList:
        try:
            low, high, f_x = 0, len(self), self.f(x)
            while low < high:
                mid = (low + high) // 2
                if f_x == (f_mid := self.f(mid_el := self[mid])):
                    if x == mid_el:
                        self.pop(mid)
                        return self
                    i, j, still = mid - 1, mid + 1, True
                    while still:
                        still = False
                        if i >= 0 and self.f(self[i]) == f_x:
                            if x == self[i]:
                                self.pop(i)
                                return self
                            i -= 1
                            still = True
                        if j < len(self) and self.f(self[j]) == f_x:
                            if x == self[j]:
                                self.pop(j)
                                return self
                            j += 1
                            still = True
                    return self
                if f_x < f_mid:
                    high = mid
                else:
                    if low == mid:
                        return self
                    low = mid
        except (ValueError, TypeError):
            pass
        return self

    def merge(self, other: SortedList) -> SortedList:
        res = self.copy()
        for x in other:
            res.insert(x)
        return res

    __call__: Callable = f

    def __len__(self) -> int:
        return len(self.value)

    def __contains__(self, item: SupportsFloat) -> bool:
        try:
            low, high, f_item = 0, len(self), self.f(item)
            while low < high:
                mid = (low + high) // 2
                if f_item == (f_mid := self.f(el_mid := self[mid])):
                    if item == el_mid:
                        return True
                    i, j = mid - 1, mid + 1
                    while True:
                        if i >= 0 and self.f(self[i]) == f_item:
                            if item == self[i]:
                                return True
                            i -= 1
                            continue
                        if j < len(self) and self.f(self[j]) == f_item:
                            if item == self[j]:
                                return True
                            j += 1
                            continue
                        break
                    return False
                if f_item < f_mid:
                    high = mid
                else:
                    if low == mid:
                        return False
                    low = mid
            return False
        except TypeError:
            return False

    def __bool__(self) -> bool:
        return bool(self.value)

    def __getitem__(self, item: int | slice) -> SupportsFloat | SortedList:
        if isinstance(item, slice):
            res = SortedList(f=self.f)
            res.__value = self.__value[item]
            return res
        return self.value[item]

    def __setitem__(self, i: int, value: SupportsFloat) -> SortedList:
        self.remove(self[i])
        return self.insert(value)

    def __add__(self, other: SortedList) -> SortedList:
        return self.merge(other)

    def __eq__(self, other: SortedList) -> bool:
        if isinstance(other, SortedList):
            return {x: self.value.count(x) for x in self} == {x: other.value.count(x) for x in other}
        return self.__value == other

    def __str__(self) -> str:
        return "S" + str(self.value)

    __repr__: str = __str__


def original(data: list[float], starter: int = 0, jump: int = 1):
    for i in range(len(data)):
        if data[i] > i:
            raise ValueError("Wrong data given!")
    sorted_res = []
    for index in range(len(data)):
        curr = index
        curr -= data[index]
        sorted_res.insert(curr, index)
    res = [0] * len(data)
    for index in range(len(sorted_res)):
        res[sorted_res[index]] = index * jump + starter
    return res


def bubble_sort(array: list[float]):
    for i in range(len(array)):
        for j in range(len(array[i + 1:])):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]


def partition(array: list[float], low: int, high: int):
    pivot, i = array[high], low - 1
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = pivot, array[i + 1]
    return i + 1


def quick_sort(array: list[float], low: int = 0, high: int = -1):
    if high == -1:
        high = len(array) - 1
    if low < high:
        pivot = partition(array, low, high)
        quick_sort(array, low, pivot - 1), quick_sort(array, pivot + 1, high)


def is_sorted(l: list[SupportsFloat]) -> bool:
    for i in range(0, len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True


def heapify(ll: list[int], l: int, h: int, i: int, f=max):
    left, right = 2 * i - l, 2 * i - l + 1
    res = i
    if left <= h and (el := ll[i - 1]) != f(ll[left - 1], el):
        res = left
    if right <= h and (el := ll[res - 1]) != f(ll[right - 1], el):
        res = right
    if res != i:
        ll[i - 1], ll[res - 1] = ll[res - 1], ll[i - 1]
        heapify(ll, res - l - 1, h, res, f)


def build_heap(ll: list[int], h: int = 0):
    if not h:
        h = len(ll)
    for i in range(h // 2, 0, -1):
        heapify(ll, 0, h, i)


def heapsort(ll: list[int]):
    build_heap(ll)
    h = len(ll)
    for i in range(len(ll) - 1, 0, -1):
        ll[0], ll[i] = ll[i], ll[0]
        h -= 1
        heapify(ll, 0, h, 1)


def merge_sort(A: list[float]):
    def merge(l, mid, h):
        L = A[l:mid + 1]
        R = A[mid + 1:h + 1]
        i, j, k = 0, 0, l
        while i < mid - l + 1 and j < h - mid:
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        if i < mid - l + 1:
            for j in range(i, mid - l + 1):
                A[k] = L[j]
                k += 1

    def helper(l, h):
        if l >= h:
            return
        mid = (h + l) // 2
        helper(l, mid), helper(mid + 1, h), merge(l, mid, h)

    helper(0, len(A) - 1)
