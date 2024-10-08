def decode_message(s: str, p: str) -> bool:
   
    memo = {}
    
    def dfs(i, j):
       
        if i == len(s) and j == len(p):
            return True
       
        if j == len(p):
            return False
        
        if (i, j) in memo:
            return memo[(i, j)]
        
       match = i < len(s) and (p[j] == s[i] or p[j] == '?')
        
         if p[j] == '*':
          
            memo[(i, j)] = dfs(i, j + 1) or (i < len(s) and dfs(i + 1, j))
            return memo[(i, j)]
        
        if match:
            memo[(i, j)] = dfs(i + 1, j + 1)
            return memo[(i, j)]
        
         memo[(i, j)] = False
         return False
    
    return dfs(0, 0)
