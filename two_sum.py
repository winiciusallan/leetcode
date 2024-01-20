class Solution:
    def twoSum_brute_force(self, nums: List[int], target: int) -> List[int]:
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    sum = nums[i] + nums[j]
                    if sum == target:
                        return [i, j]
            return

    def twoSum_hash_map(self, nums: List[int], target: int) -> List[int]:
            visited = {}

            for i in range(len(nums)):
                compl = target - nums[i]
                if compl in visited:
                    return [i, visited[compl]]
                visited[nums[i]] = i
            return
