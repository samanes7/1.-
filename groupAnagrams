def groupAnagrams(strs):
    anagrams = {}

    for s in strs:
        # مرتب کردن حروف رشته
        sorted_str = ''.join(sorted(s))
        
        # اگر کلید در دیکشنری وجود نداشت، یک لیست جدید ایجاد می‌کنیم
        if sorted_str not in anagrams:
            anagrams[sorted_str] = []
        
        # افزودن رشته به لیست مربوط به کلید
        anagrams[sorted_str].append(s)
    
    # تبدیل مقادیر دیکشنری به لیست
    return list(anagrams.values())

# مثال:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
