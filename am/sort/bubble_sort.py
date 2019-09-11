arr = [3, 6, 1, 12, 30, 5, 21, 56, 2, 27, 34, 21]


def bubble_sort(arr):
    print(len(arr))
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            print(i, j)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(arr)


# bubble_sort(arr)


def selection_sort(arr):

    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:

                min_index = j

        arr[min_index], arr[i] = arr[i], arr[min_index]
    print(arr)


# selection_sort(arr)


arr = [3, 6, 1, 12, 30, 5, 21, 56, 2, 27, 34, 21, 32]


def insertion_sort(arr):
    """插入排序"""
    # 第一层for表示循环插入的遍数
    for i in range(1, len(arr)):
        # 设置当前需要插入的元素
        current = arr[i]
        # 与当前元素比较的比较元素
        pre_index = i - 1
        while pre_index >= 0 and arr[pre_index] > current:
            # 当比较元素大于当前元素则把比较元素后移
            arr[pre_index + 1] = arr[pre_index]
            # 往前选择下一个比较元素
            pre_index -= 1
        # 当比较元素小于当前元素，则将当前元素插入在 其后面
        arr[pre_index + 1] = current

    print(arr)


# insertion_sort(arr)


def insertion_sort(arr):

    for i in range(1, len(arr)):
        cou = arr[i]

        index = i -1
        while index >= 0 and arr[index] > cou:
            arr[index+1] = arr[index]
            index -= 1

        arr[index + 1] = cou




def merge_sort(arr):
    """归并排序"""
    if len(arr) == 1:
        return arr
    # 使用二分法将数列分两个
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    # 使用递归运算

    # [3, 6, 1, 12, 30, 5]
    # [21, 56, 2, 27, 34, 21, 32]

    return marge(merge_sort(left), merge_sort(right))


def marge(left, right):
    """排序合并两个数列"""
    result = []
    # 两个数列都有值

    while len(left) > 0 and len(right) > 0:

        # 左右两个数列第一个最小放前面
        if left[0] <= right[0]:
            result.append(left.pop(0))
            # print(result)
        else:
            result.append(right.pop(0))
            # print(result)
    # 只有一个数列中还有值，直接添加
    result += left
    result += right
    # print(a)
    return result


merge_sort(arr)

#
# left = [3, 6, 1, 12, 30, 5]
# result = []
# result.append(left.pop(0))
# print(result)
# print(left)


arr = [3, 6, 1, 12, 30, 5, 21, 56, 2, 27, 34, 21, 32]


def shell_sort(arr):
    """希尔排序"""
    # 取整计算增量（间隔）值
    gap = len(arr) // 2
    while gap > 0:
        # 从增量值开始遍历比较
        for i in range(gap, len(arr)):
            j = i
            current = arr[i]
            # 元素与他同列的前面的每个元素比较，如果比前面的小则互换
            while j - gap >= 0 and current < arr[j - gap]:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = current
        # 缩小增量（间隔）值
        gap //= 2
    return arr