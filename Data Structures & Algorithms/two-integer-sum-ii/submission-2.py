class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front = 0
        back = len(numbers) -1 

        while front < back:
            sum = numbers[front] + numbers[back]

            if sum == target:
                return [front+1 , back+1]

            if sum < target:
                front += 1

            if sum > target:
                back -= 1

        