#!/usr/bin/python3
''''''


def find_peak(list_of_integers):
    if not list_of_integers:
        return

    left, right = 0, len(list_of_integers) - 1
    return binary_peak(list_of_integers, left, right)


def binary_peak(nums=[], left=0, right=0):
    if left == right:
        return nums[left]

    mid = (left + right) // 2

    if nums[mid] > nums[mid + 1]:
        return binary_peak(nums, left, mid)
    return binary_peak(nums, mid + 1, right)
