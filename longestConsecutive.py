def longestConsecutive(nums):
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # اگر num آغازگر یک دنباله جدید باشد
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # دنباله متوالی را بررسی می‌کنیم
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

# مثال:
nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))  # خروجی: 4 (دنباله: [1, 2, 3, 4])
