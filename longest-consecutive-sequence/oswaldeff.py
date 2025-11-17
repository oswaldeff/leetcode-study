class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 중복 제거: O(n)
        unique_numbers = set(nums)

        longest_sequence_length = 0  # 최장 연속 구간 길이

        # 전체 숫자 순회: O(n)
        for number in unique_numbers:
            # 연속 구간의 시작점 판별: O(1)
            if number - 1 not in unique_numbers:  # number가 시작점일 때만 실행
                current_value = number
                current_sequence_length = 1

                # 연속된 숫자 탐색: O(n) (모든 숫자는 최대 1회씩만 확인)
                while current_value + 1 in unique_numbers:
                    current_value += 1
                    current_sequence_length += 1

                # 최댓값 갱신: O(1)
                if longest_sequence_length < current_sequence_length:
                    longest_sequence_length = current_sequence_length

        # 전체 시간복잡도: O(n)
        return longest_sequence_length
