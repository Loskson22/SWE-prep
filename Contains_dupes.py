class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #counter = []
        #for i in range(self.size):
        #    if i in nums:
        #        counter[i]+=1
        #for i in range (counter.size):
        #    if counter[i] >=2:
        #        return true
        #return false
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        
        #counts = Counter(nums)  # Count occurrences of each number
        #for count in counts.values():
        #    if count >= 2:
        #        return True
        #return False