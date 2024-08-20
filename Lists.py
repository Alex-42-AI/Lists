# from time import time
if __name__ == '__main__':
    from DiscreteMath.Graphs import heapify, build_heap
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
        res = SortedList()
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
        return self.__value[item]
    def __setitem__(self, key, value):
        if key in self:
            self.remove(key)
        self.insert(value)
    def __add__(self, other):
        if isinstance(other, SortedList):
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
def heapsort(ll: [int]):
    build_heap(ll)
    h = len(ll)
    for i in range(len(ll) - 1, 0, -1):
        ll[0], ll[i] = ll[i], ll[0]
        h -= 1
        heapify(ll, 0, h, 1)
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
# def merge(l0, l1):
#     i, j = 0, 0
#     while i < len(l0) and j < len(l1):
#         if l0[i] < l1[j]:
#             i += 1
#         else:
#             l0.insert(i, l1[j])
#             j += 1
#     l0 += l1[j:]
# def merge_sort(nums: [float]) -> [float]:
#     if not nums[1:]:
#         return nums
#     mid = len(nums) // 2
#     fst = merge_sort(nums[:mid])
#     merge(fst,  merge_sort(nums[mid:]))
#     return fst
# def merge(l ,mid, h):
#     L = A[l:mid + 1]
#     R = A[mid + 1:h + 1]
#     i, j, k = 0, 0, l
#     while i < mid - l + 1 and j < h - mid:
#         if L[i] <= R[j]:
#             A[k] = L[i]
#             i += 1
#         else:
#             A[k] = R[j]
#             j += 1
#         k += 1
#     if i < mid - l + 1:
#         for j in range(i, mid - l + 1):
#             A[k] = L[j]
#             k += 1
# def merge_sort(l, h):
#     if l >= h:
#         return
#     mid = (h + l) // 2
#     merge_sort(l, mid)
#     merge_sort(mid + 1, h)
#     merge(l, mid, h)
# A = [-122, -83, 191, -434, 195, -360, 99, 389, 150, -317, 5, 176, 58, -103, 457, -487, -352, 485, 296, -359, 129, 115, -159, -371, 144, 340, 484, 310, 13, -367, 392, -267, 222, -389, -261, -62, 14, -494, -230, 333, -456, 332, -214, 223, 397, 91, 434, 175, -500, 466, 251, -136, 110, -152, -153, -185, 68, -362, 381, 134, -277, 443, 153, -256, 226, 488, 78, -67, -315, -77, -55, -273, 277, 48, 342, -470, -444, -472, 118, 189, -477, -330, 474, 484, -130, 328, 478, 98, -339, -192, -350, 25, -428, -159, 289, -266, -179, 340, 343, 394, 272, 41, -239, -2, -108, 143, -265, 440, -488, 414, 350, -212, -19, 472, -429, 2, -12, -437, 289, 366, -422, -323, 427, 249, 348, -89, 127, 1, -289, 16, 6, -315, 225, -211, -241, 4, -381, -371, -36, -56, 159, -15, 293, -224, 417, -204, -228, 209, -11, -451, 104, 62, 209, -24, 109, -190, 297, -135, 134, 389, 93, 308, 418, -413, 267, -463, 135, 433, 116, -105, 450, 255, -22, -89, -44, 153, 463, -195, -70, 20, 25, -336, 159, 258, 363, 398, 324, -335, 14, -442, 412, 222, 354, 55, -55, 286, -356, 496, -318, -278, -223, -431, -264, -335, -67, -59, -79, 383, 284, 110, 238, -330, -394, -413, 241, -345, 428, -186, 277, 246, 488, 386, 381, 434, 309, -80, -61, -298, -127, 113, 283, -91, 213, -231, 65, 344, -424, -302, -281, -456, -257, -89, 329, 476, -480, 298, 423, 42, 154, -460, -371, -94, 84, 390, -77, -90, -267, -148, -153, -406, 41, -401, -154, -420, -205, 62, -184, -243, -420, -169, 191, 396, 86, 214, -434, -326, -242, 387, 48, -462, -363, 73, 112, 202, 432, -221, 8, 275, -497, 304, 391, 427, -226, 274, 251, -374, -454, 367, -68, -399, -401, -396, 178, 57, 381, 334, 373, 307, -272, 386, -216, -225, 410, 438, -328, -180, 348, 67, -210, 82, -47, 326, -383, 6, 247, 221, 136, -57, 137, 295, -131, -273, -19, -207, -489, 151, 74, 400, 258, 287, 305, 319, 396, 89, -121, 330, -227, 185, -310, 63, -451, -229, -285, -414, -389, 16, 368, 246, -265, 498, -439, -385, -380, 264, -482, 490, -341, 88, 317, 493, -140, 80, 450, -497, -8, 45, -146, -419, -485, 65, -448, 306, 399, -236, -174, -264, -285, -498, -50, 16, -344, -288, 410, 241, -430, -252, 246, 70, 311, 72, 39, 54, 250, 31, -77, 275, 450, -336, 386, 367, -178, 272, 404, 426, -211, 149, 194, -36, 485, 157, 64, 274, -266, -432, -144, -65, -310, 459, -228, -29, -230, -128, 50, -426, 40, 299, 347, 375, -345, 377, -374, -114, 221, 213, 414, 95, -205, 476, 298, 190, -98, -384, 421, -438, -134, -100, 251, -15, 343, 399, -496, -250, 271, -383, -354, -152, 210, 54, -18, -262, -14, 222, 113, 266, 185, -379, -11, -489, -359, 200, -147, -267, 293, -258, 318, -98, -419, 366, 363, 401, 390, 41, 411, 255, -408, 420, -66, 380, -328, 139, 458, -354, 263, -405, -490, -349, 360, -82, -37, 173, -454, -422, 179, 352, 349, -126, 224, 145, 159, -141, 349, 289, 429, 369, 155, 243, 267, -311, 156, -463, -241, 443, 341, -374, 223, 500, 363, -27, -389, -71, -425, 467, -301, -131, -336, -116, 309, -411, 449, -481, -494, 404, 324, 14, 101, -87, -13, 458, 162, 75, 494, -28, -67, 475, -158, 55, -232, 106, -470, 72, 103, -258, 332, -122, 431, 67, -109, 460, -262, -446, 426, -106, -12, 456, 256, 102, -21, -353, 235, 459, -323, -52, 171, 377, -321, -396, 366, -195, 407, 380, -213, 37, -489, -280, -138, -228, 345, -325, -142, -250, 15, -409, -342, 240, 179, 384, 183, 394, -388, 54, -317, 290, -323, -484, -20, -316, -469, -221, -351, 335, 50, 381, 450, -254, 250, -496, -6, 234, -368, 32, 370, -8, -63, 45, 54, 332, -405, 383, -49, 96, -8, -132, 376, -318, -246, 437, 268, 282, 179, 60, 376, 388, -384, 102, 394, -49, -89, 355, -494, -341, -294, -163, -215, -85, -392, -326, -339, 129, -71, -244, 10, -77, 412, 219, -205, 461, 24, -86, 475, -90, -172, -153, -259, 327, 404, 107, 52, -232, 176, 168, 14, -222, 422, 184, 26, 55, 79, 428, 16, 277, -366, 234, 210, 420, 144, 231, 470, -62, 296, -74, -419, 456, -34, 417, -416, 379, 176, 428, -24, 91, -170, 116, -132, -421, -357, -358, 497, 279, 429, 159, -325, 49, -139, -134, -39, -285, -73, 172, -346, -484, 59, 20, -133, 148, -468, -309, -126, -12, -350, 70, -39, 3, -359, 267, 471, -263, 42, 204, -247, 188, 454, -369, -441, 135, 413, 39, -21, 142, -97, -250, 419, -416, -362, -261, -360, 156, 253, -28, -190, -198, 228, 354, 449, -82, 74, -296, -76, 448, 454, 245, -446, -419, -70, 122, -22, 188, 450, -362, 426, 328, -142, -158, -164, -20, 428, 293, -204, 151, 282, 196, 51, 395, 281, -179, -454, 177, -54, -162, 44, -170, 184, -65, 461, -153, -222, -81, -269, 97, -436, -61, 452, -191, 373, -406, 174, 245, -415, -57, 239, -73, 93, 76, 86, -245, 465, 394, -322, -224, 281, -120, 82, -306, -46, -40, 227, 187, -366, -373, 267, -386, -87, 136, -374, -227, -24, 198, 488, -393, -76, -291, -459, -250, 406, -344, 392, -8, 99, 245, -155, 457, -258, -299, -386, -281, -311, 498, 185, 74, -469, 224, -75, 482, 301, -387, -177, -234, 112, -5, 54, -465, -122, 420, -242, -451, -207, 259, 112, -270, -108, -16, 235, 218, -229, -67, 58, -97, -301, 57, -384, -291, 257, -292, 431, 316, -498, 76, 122, -495, 435, 275, 139, 164, -194, 146, 301, -252, 264, -34, -395, 389, 294, -209, 473, -324, 253, -313, 248, 241, 164, -382, -230, -405, -464, 310, -173, 163, -440, -390, -224, 413, 209, -389, 114, 379, 81, -277, -396, -103, 80, 203, -157, 29, 130, 488, 441, -355, 262, -465, -167, -188, -156, -293, -354, 88, -101, -137, 442, -327, 214, -340]
# A = [9, 6, 4, 1, 0, -2, -5]
# n = len(A)
# t = time()
# quick_sort(A)
# print(is_sorted(A))
# print(original([0, 1, 0, 2, 0, 0, 1, 2]))
# l = [2, 1, 5, 4, 7, 6, 9, 5, 6]
# heapsort(l)
# print(l)