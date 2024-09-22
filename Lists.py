class SortedList:
    def __init__(self, f=lambda x: x):
        self.__f, self.__value = f, []

    def value(self):
        return self.__value

    def f(self, el=None):
        return self.__f if el is None else self.__f(el)

    def pop(self, index: int = -1):
        return self.__value.pop(index)

    def insert(self, el):
        low, high, f_el = 0, len(self), self.f(el)
        while low < high:
            mid = (low + high) // 2
            if f_el == self.f(self[mid]):
                self.__value.insert(mid, el)
                return self
            if f_el < self.f(self[mid]):
                high = mid
            else:
                if low == mid + 1:
                    break
                low = mid + 1
        self.__value.insert(high, el)
        return self

    def remove(self, el):
        low, high, f_el = 0, len(self), self.f(el)
        while low < high:
            mid = (low + high) // 2
            if f_el == self.f(self[mid]):
                if el == self[mid]:
                    self.pop(mid)
                    return True
                i, j, still = mid - 1, mid + 1, True
                while still:
                    still = False
                    if i >= 0 and self.f(self[i]) == f_el:
                        if el == self[i]:
                            self.pop(i)
                            return True
                        i -= 1
                        still = True
                    if j < len(self) and self.f(self[j]) == f_el:
                        if el == self[j]:
                            self.pop(j)
                            return True
                        j += 1
                        still = True
                return False
            if f_el < self.f(self[mid]): high = mid
            else:
                if low == mid:
                    return False
                low = mid

    def copy(self):
        res = SortedList(self.f())
        res.__value = self.value()
        return res

    def merge(self, other):
        if isinstance(other, SortedList):
            if any([self.f(el) != other.f(el) for el in self.value() + other.value()]):
                raise ValueError("Sorting functions of both lists are different!")
            res = self.copy()
            for el in other.value():
                res.insert(el)
            return res

    def __call__(self, el):
        return self.f(el)

    def __len__(self):
        return len(self.value())

    def __contains__(self, item):
        low, high, f_item = 0, len(self), self.f(item)
        while low < high:
            mid = (low + high) // 2
            if f_item == self.f(self[mid]):
                if item == self[mid]:
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
            if f_item < self.f(self[mid]):
                high = mid
            else:
                if low == mid:
                    return False
                low = mid

    def __bool__(self):
        return bool(self.value())

    def __getitem__(self, item: int | slice):
        if isinstance(item, slice):
            res = SortedList(self.f())
            res.__value = self.value()[item]
            return res
        return self.value()[item]

    def __setitem__(self, i: int, value):
        self.remove(self[i]), self.insert(value)

    def __add__(self, other):
        return self.merge(other)

    def __eq__(self, other):
        if isinstance(other, SortedList):
            return self.value() == other.value()
        return self.__value == other

    def __str__(self):
        return 'S' + str(self.value())

    def __repr__(self):
        return str(self)


def original(data: [int], starter: int = 0, jump: int = 1):
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


def bubble_sort(array: iter):
    for i in range(len(array)):
        for j in range(len(array[i + 1:])):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]


def partition(array: iter, low: int, high: int):
    pivot, i = array[high], low - 1
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = pivot, array[i + 1]
    return i + 1


def quick_sort(array: iter, low=0, high=-1):
    if high == -1:
        high = len(array) - 1
    if low < high:
        pivot = partition(array, low, high)
        quick_sort(array, low, pivot - 1), quick_sort(array, pivot + 1, high)


def is_sorted(l: [float]) -> bool:
    for i in range(0, len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True


def heapify(ll: [int], l: int, h: int, i: int, f=max):
    left, right = l + 2 * (i - l), l + 2 * (i - l) + 1
    res = i
    if left <= h and ll[i - 1] != f(ll[left - 1], ll[i - 1]):
        res = left
    if right <= h and ll[res - 1] != f(ll[right - 1], ll[res - 1]):
        res = right
    if res != i:
        ll[i - 1], ll[res - 1] = ll[res - 1], ll[i - 1]
        heapify(ll, res - l - 1, h, res, f)


def build_heap(ll: [int], h: int = 0):
    if not h:
        h = len(ll)
    for i in range(h // 2, 0, -1):
        heapify(ll, 0, h, i)


def heapsort(ll: [int]):
    build_heap(ll)
    h = len(ll)
    for i in range(len(ll) - 1, 0, -1):
        ll[0], ll[i] = ll[i], ll[0]
        h -= 1
        heapify(ll, 0, h, 1)


def merge_sort(A: [float]):
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
