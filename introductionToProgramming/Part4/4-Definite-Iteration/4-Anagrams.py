# my solution
# def anagrams(word, word1):
#     listWord = []
#     listWord1 = []
#     if len(word) == len(word1):
#         for i in range(0, len(word)):
#             listWord.append(word[i])
#             listWord1.append(word1[i])
#         if sorted(listWord) == sorted(listWord1):
#             return True
#         else:
#             return False
#     else:
#         return False
    
# better solution
def anagrams(string1: str, string2: str):
    return sorted(string1) == sorted(string2)
    
# tests
print(anagrams("tame", "meta")) # True
print(anagrams("tame", "mate")) # True
print(anagrams("tame", "team")) # True
print(anagrams("tabby", "batty")) # False
print(anagrams("python", "java")) # False