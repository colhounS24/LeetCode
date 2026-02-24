class Solution:
    def convert(s: str, n: int) -> str:
        indexes = Solution.row_action(len(s),n)

        rows = [""] * n

        for index, char in zip(indexes, s):
            rows[index] += char
        
        final_string = ""
        for row in rows:
            final_string += row

        return final_string

    @staticmethod
    def row_action(string_length, num_rows) -> list[int]:

        current_row = 0
        indexes = []
        for _ in range(string_length):
            indexes.append(current_row)
            if current_row == 0:
                direction = 1
            elif current_row == num_rows -1:
                direction = -1

            current_row += direction
        return indexes

print(Solution.convert("PAYPALISHIRING",3))