class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = []
        for i in range(len(temperatures)):
            count = 0
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    count = j - i
                    break
            temp_stack.append(count)
        return temp_stack

                

        #     while True:
        #         print(count + i)
        #         if count == len(temperatures):
        #             temp_stack.append(0)
        #             break
        #         elif count + i >= len(temperatures):
        #             temp_stack.append(0)
        #             break
        #         elif temperatures[i] < temperatures[i + count]:
        #             temp_stack.append(count)
        #             count = 1
        #             break
        #         else:
        #             count += 1
        # return temp_stack
        