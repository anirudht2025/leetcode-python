class Solution:
    def countBits(self, n: int) -> list[int]:
        result = [0] * (n + 1)

        for i in range(1, n + 1):
            result[i] = result[i >> 1] + (i & 1)

        return result

# class Solution:
#     def countBits(self, n: int) -> list[int]:
#         result = []

#         for i in range(n + 1):
#             count = 0
#             num = i

#             while num:
#                 count += num & 1
#                 num >>= 1

#             result.append(count)

#         return result
