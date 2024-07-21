def mergeIntervals(intervals):
    # اگر لیست بازه‌ها خالی باشد، برگرداندن لیست خالی
    if not intervals:
        return []

    # مرتب‌سازی بازه‌ها بر اساس نقطه شروع
    intervals.sort(key=lambda x: x[0])

    # لیست نهایی برای نگهداری بازه‌های ادغام شده
    merged_intervals = [intervals[0]]

    for current in intervals:
        # بازه آخر در لیست نهایی
        last = merged_intervals[-1]

        # اگر بازه‌ها هم‌پوشانی داشته باشند
        if current[0] <= last[1]:
            # ادغام بازه‌ها
            merged_intervals[-1] = (last[0], max(last[1], current[1]))
        else:
            # اضافه کردن بازه جدید به لیست نهایی
            merged_intervals.append(current)

    return merged_intervals

# مثال:
intervals = [(1, 3), (2, 6), (8, 10)]
print(mergeIntervals(intervals))  # خروجی: [(1, 6), (8, 10)]
