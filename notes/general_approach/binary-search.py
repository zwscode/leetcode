# 基本二分搜索
def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            # 直接返回
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    # 直接返回
    return -1


# 寻找左侧边界的二分搜索，开区间写法
def left_bound(nums, target):
    left, right = 0, len(nums)
    if right == 0:
        return -1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            # 锁定左侧边界
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    # 检查left越界情况
    if left >= len(nums) or nums[left] != target:
        return -1
    return left


# 寻找右侧边界的二分搜索，开区间写法
def right_bound(nums, target):
    left, right = 0, len(nums)
    if right == 0:
        return -1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            # 锁定右侧边界
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    # 检查越界情况
    if left == 0 or nums[left - 1] != target:
        return -1
    return left - 1


# 寻找左侧边界的二分搜索，闭区间写法
def left_bound2(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            # 锁定左侧边界
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    # 检查left越界情况
    if left >= len(nums) or nums[left] != target:
        return -1
    return left

# 寻找右侧边界的二分搜索，闭区间写法
def right_bound2(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            # 锁定右侧边界
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    # 检查right越界情况
    if right < 0 or nums[right] != target:
        return -1
    return right