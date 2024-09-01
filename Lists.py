class SortedList:
    def __init__(self, f=lambda x: x):
        self.__f = f
        self.__value = []
        self.__i = -1
    def pop(self, index: int = -1):
        res = self.__value.pop(index)
        return res
    def insert(self, el):
        low, high = 0, len(self)
        while low < high:
            mid = (low + high) // 2
            if self.__f(el) == self.__f(self[mid]):
                self.__value.insert(mid, el)
                return
            if self.__f(el) < self.__f(self[mid]):
                high = mid
            else:
                if low == mid + 1:
                    break
                low = mid + 1
        self.__value.insert(high, el)
    def remove(self, el):
        low, high = 0, len(self)
        while low < high:
            mid = (low + high) // 2
            if self.__f(el) == self.__f(self[mid]):
                if el == self[mid]:
                    self.pop(mid)
                    return True
                i, j, still = mid - 1, mid + 1, True
                while still:
                    still = False
                    if i >= 0 and self.__f(self[i]) == self.__f(el):
                        if el == self[i]:
                            self.pop(i)
                            return True
                        i -= 1
                        still = True
                    if j < len(self) and self.__f(self[j]) == self.__f(el):
                        if el == self[j]:
                            self.pop(j)
                            return True
                        j += 1
                        still = True
                return False
            if self.__f(el) < self.__f(self[mid]):
                high = mid
            else:
                if low == mid:
                    return False
                low = mid
    def copy(self):
        res = SortedList(self.__f)
        for el in self:
            res.insert(el)
        return res
    def __len__(self):
        return len(self.__value)
    def __contains__(self, item):
        low, high = 0, len(self)
        while low < high:
            mid = (low + high) // 2
            if self.__f(item) == self.__f(self[mid]):
                if item == self[mid]:
                    return True
                i, j = mid - 1, mid + 1
                while True:
                    if i >= 0 and self.__f(self[i]) == self.__f(item):
                        if item == self[i]:
                            return True
                        i -= 1
                        continue
                    if j < len(self) and self.__f(self[j]) == self.__f(item):
                        if item == self[j]:
                            return True
                        j += 1
                        continue
                    break
                return False
            if self.__f(item) < self.__f(self[mid]):
                high = mid
            else:
                if low == mid:
                    return False
                low = mid
    def __bool__(self):
        return bool(self.__value)
    def __iter__(self):
        return self
    def __next__(self):
        if self.__i + 1 == len(self):
            self.__i = -1
            raise StopIteration()
        self.__i += 1
        return self[self.__i]
    def __getitem__(self, item: int | slice):
        if isinstance(item, slice):
            res = SortedList(self.__f)
            res.__value = self.__value[item]
            return res
        return self.__value[item]
    def __setitem__(self, i: int, value):
        self.remove(self[i]), self.insert(value)
    def __add__(self, other):
        if isinstance(other, SortedList):
            if any([self.__f(el) != other.__f(el) for el in self.__value + other.__value]):
                raise ValueError("Sorting functions of both lists are different!")
            res = self.copy()
            for el in other:
                res.insert(el)
            return res
    def __eq__(self, other):
        return self.__value == other
    def __str__(self):
        return str(self.__value)
    def __repr__(self):
        return str(self)
def original(data: [int], starter: int = 0, jump: int = 1):
    for i in range(len(data)):
        if data[i] > i:
            raise ValueError
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
    if l + left <= h and ll[l + i - 1] != f(ll[l + left - 1], ll[l + i - 1]):
        res = left
    if l + right <= h and ll[l + res - 1] != f(ll[l + right - 1], ll[l + res - 1]):
        res = right
    if res != i:
        ll[l + i - 1], ll[l + res - 1] = ll[l + res - 1], ll[l + i - 1]
        heapify(ll, l, h, res, f)
def build_heap(ll: [int], h: int = 0):
    if not h:
        h = len(ll)
    for i in range(h // 2, 2, -1):
        heapify(ll, 2, h, i)
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
        helper(l, mid)
        helper(mid + 1, h)
        merge(l, mid, h)
    helper(0, len(A) - 1)
