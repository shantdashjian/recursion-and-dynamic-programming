def can_construct(s, word_list):
    if len(s) == 0:
        return True
    result = False
    for word in word_list:
        if word == s:
            result = True
            break
        if word == s[: len(word)]:
            result = result or can_construct(s[len(word) :], word_list)
    return result

# O((n ^ m) * m) time | O(m * m) space

print(can_construct("ab", ["a", "b"])) 
print(can_construct("applepenapple", ["apple","pen"])) 
print(can_construct("skateboard", ["bo","rd", "ate", "t", "ska", "sk", "boar"])) 
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e", 
    "ee", 
    "eee", 
    "eeee", 
    "eeeee", 
    "eeeeee", 
    "eeeeeee", 
    "eeeeeeee", 
    ])) 