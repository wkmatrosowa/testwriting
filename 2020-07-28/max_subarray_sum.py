def is_zero(arr):
    negatives = [el for el in arr if el < 0]
    if arr == []:
        return True
    elif len(negatives) == len(arr):
        return True


def max_subarray_sum(arr):
    if is_zero(arr):
        return 0
    else:
        x = [arr[a:b + 1] for a in range(len(arr)) for b in range(len(arr)) if a <= b]
        y = [sum(el) for el in x]
        return max(y)
