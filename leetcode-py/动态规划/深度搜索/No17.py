from typing import List

#这类题建议使用回溯法
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         if not digits:
#             return []
        
#         phonemap = {'2':['a','b','c'],
#                  '3':['d','e','f'],
#                  '4':['g','h','i'],
#                  '5':['j','k','l'],
#                  '6':['m','n','o'],
#                  '7':['p','q','r','s'],
#                  '8':['t','u','v'],
#                  '9':['w','x','y','z']}
        
#         res = []
#         lenth = len(digits)

#         def backtrack(conbination,index):
#             if index == lenth:
#                 res.append(conbination)
#             else:
#                 for character in phonemap[digits[index]]:
#                     backtrack(conbination+character,index+1)

#         backtrack("",0)
#         return res

# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:

#         phonemap = {'2':['a','b','c'],
#                  '3':['d','e','f'],
#                  '4':['g','h','i'],
#                  '5':['j','k','l'],
#                  '6':['m','n','o'],
#                  '7':['p','q','r','s'],
#                  '8':['t','u','v'],
#                  '9':['w','x','y','z']}

#         length = len(digits)
#         res = []
#         self.string = ""        # 这里使用self. 是应为防止backtrack递归时候认为string为局部变量从而引发报错

#         def backtrack(i):
#             if i == length:
#                 res.append(self.string)
#                 return
            
#             for letter in phonemap[digits[i]]:
#                 self.string += letter
#                 backtrack(i+1)
#                 self.string = self.string[:-1]
#         if digits:
#             backtrack(0)

#         return res

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        length = len(digits)
        if length == 0:
            return []
        
        phonemap = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}

        res = []

        path = [""] * length    # 这里使用列表字符串巧妙避免递归后清理现场

        def trackback(i):
            if i == length:
                res.append("".join(path))
                return
            for letter in phonemap[digits[i]]:
                path[i] = letter
                trackback(i+1)

        trackback(0)

        return res

