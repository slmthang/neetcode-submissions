class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        arr = []

        for op in operations:

            if (op == '+'):
                arr.append(arr[len(arr) -1] + arr[len(arr) -2])
            
            elif (op == 'D'):
                arr.append(arr[len(arr)-1] * 2)
            
            elif (op=='C'):
                arr.pop()
            else:
                arr.append(int(op))
        
        return sum(arr)
