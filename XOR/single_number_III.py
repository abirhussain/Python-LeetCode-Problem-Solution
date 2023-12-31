class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor, position, first_number, second_number = 0, 0, 0, 0

        # find the xor of single elements
        for num in nums:
            xor = xor ^ num
        
        # find the position of set bit
        while xor & (1<<position) == 0:
            position += 1

        # find the one solution number having 1 at position ${postion}
        for num in nums:
            if num&(1<<position):
                first_number ^= num

        # find the second number
        second_number = xor ^ first_number

        return [first_number, second_number]