"""
Useless code to narrow down the number of failed python attempts to generate a list at random from 0 to nums
"""


import random

# This generates a list of random numbers from 0 to nums


def generate_random_list(nums):
    random_list = []    # random list
    while len(random_list) <= nums:
        random_num = random.randint(0, nums)
        random_list.append(random_num)
    return random_list

# This is the failed attempts counter


def counter_try(nums):
    attempts = 0
    attempts_max = 100000    # Maximum number of attempts
    tg_list = list(range(nums + 1))    # The list we are looking for
    if nums > 0:
        while generate_random_list(nums) != tg_list:
            attempts += 1
            if attempts >= attempts_max:
                return"Your attempts are over"
            if attempts % 1000 == 0:
                print(f"Gone {attempts} failed attempts.")
    return f'To find {tg_list} it took: {attempts} tries'


print(counter_try(5))
