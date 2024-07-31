'''
1 >> Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except
nums[i].
'''
# from copy import deepcopy
# from array import*
# nums=array('i',[1,2,3,4,5])
# for i in range(len(nums)):
#     product=1    
#     arr1 = deepcopy(nums)
#     arr1.pop(i)
#     for num in arr1:
#         product *= num    
#     print(product)

'''
2 >> Given an integer array nums, move all O's to the end of it while maintaining the relative order of the non-zero elements. 
Note that you must do this in-place without making a copy of the array.
'''
# from array import*
# nums=array('i',[1,2,0,3,0,4,5])
# n = len(nums)
# for i in range(1,n):
#     if nums[i]== 0:
#         nums.pop(i)
'''
       here you can have to options either you can add zeros in left or in the right 
'''
#         nums.insert(0,0)
#         #nums.append(0)

# print(nums)
'''           SWAP method      
'''
# def move_zeroes(nums):
#     last_non_zero_found_at = 0
#     for current in range(len(nums)):
#         if nums[current] == 0:
#             print(nums[last_non_zero_found_at], nums[current])
#             nums[last_non_zero_found_at], nums[current] = nums[current], nums[last_non_zero_found_at]
#             last_non_zero_found_at += 1
# nums = [0, 1, 0, 3, 0,12,0]
# move_zeroes(nums)
# print(nums)

'''
    You are given an array of prices where prices[i] is the price of a given stock on an ith day. You want to maximise your profit by 
    choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you 
    can achieve from this transaction, If you cannot achieve any profit, return 0.
'''
# from array import*
# prices = array('f',[25.38, 67.12, 59.45, 13.78, 99.34, 20.59, 87.42, 14.39, 76.52, 30.26])
# if not prices:
#     print(0)

# min_price = float('inf') # Initialize min_price to a very high value
# max_profit = 0
# max_profit_index = -1
# print(min_price)
# for i in range(len(prices)):
#     price = prices[i]
#     if price < min_price:
#         min_price = price
#         min_price_index = i
#     profit = price - min_price
#     if profit > max_profit:
#         max_profit = profit
#         max_profit_index = i

# print("profit:",max_profit,"day:", max_profit_index + 1)

'''4. The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
Given an array of integers nums, find the next permutation of nums.
The replacement must be in place and use only constant extra memory.
'''
# def next_permutation(nums):
#     # Step 1: Find the pivot
#     pivot = -1
#     for i in range(len(nums) - 2, -1, -1):
#         if nums[i] < nums[i + 1]:
#             pivot = i
#             break

#     # If no pivot is found, reverse the whole array
#     if pivot == -1:
#         nums.reverse()
#         return

#     # Step 2: Find the rightmost successor to the pivot
#     for i in range(len(nums) - 1, pivot, -1):
#         if nums[i] > nums[pivot]:
#             # Step 3: Swap with the pivot
#             nums[i], nums[pivot] = nums[pivot], nums[i]
#             break

#     # Step 4: Reverse the suffix
#     nums[pivot + 1:] = reversed(nums[pivot + 1:])


# nums = [1, 3, 2]
# next_permutation(nums)
# print(nums) 

'''
Given an array of integers and an integer target, return indices of the two numbers such that they add up to target.
'''
# from array import array

# def sum_indices(arr, target):
#     two_indices = []
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)): 
#             if arr[i] + arr[j] == target:
#                 two_indices.append([i, j])
#     return two_indices

# arr = array('i', [1, 3, 2, 5, 4])
# target = 5
# print(sum_indices(arr, target))

'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are
(i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container, such that the container contains the most
water. Return the maximum amount of water a container can store.
'''
# from array import array
# height =array('i', [1, 8, 6, 2, 5, 4, 8, 3, 7])
# n = len(height)
# area = []
# for i in range(n-1):
#     for j in range(i+1,n):
#         width= j - i
#         height_container= min(height[i], height[j])
#         current = width * height_container
#         area.append(current)

# area = sorted(area)
# print(area[-1])

'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.
'''
# from collections import Counter
# nums = ['blue','orange','white','blue','red','white','orange']

# count_colors = Counter(nums)

# pairs=[]
# singles = []

# for colors, count in count_colors.items():
#     if count > 1 :
#         pairs.extend([colors]*(count//2*2))
#     else:
#         singles.append(colors)

# sort_colors = pairs + singles  

# print(sort_colors)

'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is 
greater than or equal to target. If there is no such subarray, return 0 instead.
'''

# def subArray(nums, target):
#     n = len(nums)
#     min_len = float('inf') 
#     cur_sum = 0
#     start = 0

#     for end in range(n):
#         cur_sum += nums[end]

#         while cur_sum>=target:
#             min_len = min(min_len,end-start+1)
#             cur_sum -= nums[start]
#             start+=1
#     return min_len if min_len != float('inf') else 0

# nums = [2, 3, 1, 2, 4, 3]
# target = 7
# print(subArray(nums, target)) 

'''
You are given two integer arrays nums1 and nums2, sorted in non- decreasing order, and two integers m and n, representing the number of 
elements in nums1 and nums2 respectively. Merge nums1 and nums2 into a single array sorted in non-decreasing order.
'''
# # from array import array
# # nums1 = array('i',[1,2,3,4,5])
# # nums2 = array('i',[6,7,8,9,10])
# # m,n=5,5

# # nums3  = nums1 + nums2
# # print(nums3)

# def merge(nums1, m, nums2, n):
#     p1 = m - 1
#     p2 = n - 1
#     p = m + n - 1
    
#     # Merge in reverse order
#     while p1 >= 0 and p2 >= 0:
#         if nums1[p1] > nums2[p2]:
#             nums1[p] = nums1[p1]
#             p1 -= 1
#         else:
#             nums1[p] = nums2[p2]
#             p2 -= 1
#         p -= 1
    
#     # If there are remaining elements in nums2, copy them
#     while p2 >= 0:
#         nums1[p] = nums2[p2]
#         p2 -= 1
#         p -= 1


# nums1 = [1, 2, 3, 6, 8,0,0,0]
# m = 5
# nums2 = [2, 5, 6]
# n = 3
# merge(nums1, m, nums2, n)
# print(nums1)