class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str1 = ''
        new = []
        for i in digits:
            str1 = str1 + str(i)
        emp = int(str1) + 1
        emp1 = str(emp)
        for i in range(len(emp1)):
            new.append(int(emp1[i]))
        return new
        
        