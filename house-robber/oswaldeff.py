class Solution:
    def rob(self, nums: List[int]) -> int:
        # 점화식:
        # dp(i) = max(dp(i-2) + nums[i], dp(i-1))
        # 인접한 집은 털 수 없으므로, 직전 집을 털지 않은 경우(dp(i-2))와
        # 직전까지의 최대값(dp(i-1)) 중 더 큰 값을 선택

        prev2 = 0
        prev1 = 0
        result = 0

        for index, value in enumerate(nums):
            if index == 0:
                result = value
                prev1 = result  # dp(0)
            elif index == 1:
                result = max(value, prev1)
                prev2 = result  # dp(1)
            else:
                result = max(prev1 + value, prev2)
                prev1, prev2 = prev2, result  # 다음 반복을 위해 이동

        return result

# Top-Down(재귀: 중복 계산 발생) 
# Bottom-Up(반복문: 낮은 단계부터 차례로 계산 → 효율적)
