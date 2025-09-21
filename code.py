class Solution:
    def equalPartition(self, arr):
        # code here
        
        # def dfs(i, target, arr):
            
        #     if target == 0:
        #         return True
        #     if len(arr) - i -1 <= 0:
        #         return False
                
        #     return (dfs(i+1, target-arr[i], arr) or dfs(i+1, target,arr))
        
        # sum = 0
        # for num in arr:
        #     sum += num
        
        # if sum%2 == 1:
        #     return False
            
        # target = sum//2
        
        # return dfs(0, target, arr)
        
        
        dp = set()
        dp.add(0)
        target = sum(arr)//2
        if sum(arr)%2 == 1:
            return False
        
        for i in range(len(arr)):
            tmpDp = set()
            for num in dp:
                tmpDp.add(num)
                tmpDp.add(num+arr[i])
            if target in tmpDp:
                return True
            dp = tmpDp
            # print(dp)
        return False