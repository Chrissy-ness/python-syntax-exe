def sum_nums(nums):
    """Given list of numbers, return sum of those numbers.

    For example:
      sum_nums([1, 2, 3, 4])

    Should return (not print):
      10
    """  
    sum_all = 0

    for num in nums:
      sum_all += num
    
    print(sum_all)
