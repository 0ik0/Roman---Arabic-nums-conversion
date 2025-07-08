class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
       
        
        m = 0
        for i in range(len(list(s)) - 1):  
            
            if dict[list(s)[i]] >= dict[list(s)[i + 1]]:
                m += dict[list(s)[i]]
            else:    
                m = m - dict[list(s)[i]]
                        
        m += dict[list(s)[len(list(s)) - 1]]

        return m
