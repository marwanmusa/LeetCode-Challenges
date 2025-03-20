def merge_sort(nums):
    # bottom cases: empty or list of a single element.
    if len(nums) <= 1:
        return nums
    
    pivot = int(len(nums)/2)
    left_list = merge_sort(nums[0:pivot])
    right_list = merge_sort(nums[pivot:])
    return merge(left_list, right_list)

def merge(l: list, r: list):
    l_ptr = r_ptr = 0
    ret = []
    while l_ptr < len(l) and r_ptr < len(r):
        if l[l_ptr] < r[r_ptr]:
            ret.append(l[l_ptr])
            l_ptr += 1
        else:
            ret.append(r[r_ptr])
            r += 1
    
    # append wjat is remained in either of the lists
    ret.extend(l[l_ptr:])
    ret.extend(r[r_ptr:])

    return ret