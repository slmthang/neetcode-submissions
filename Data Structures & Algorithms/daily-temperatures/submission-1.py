class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            
            while (stack and (temperatures[i] > temperatures[stack[-1]])):
                j = stack.pop()
                res[j] = i-j
            
            stack.append(i)

            
        
        return res




        # for i in range(len(temperatures)):
        #     count = 0
        #     found = False
        #     for j in range(i + 1, len(temperatures)):
        #         count += 1
        #         if (temperatures[j] > temperatures[i]):
        #             found = True
        #             break;

        #     if found:
        #         res.append(count)
        #     else:
        #         res.append(0)


        return res
            


            