class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for operation in operations:
            if operation == '+':
                value = record[-1]+record[-2]
                record.append(value)
            elif operation == 'C':
                record.pop()
            elif operation == 'D':
                value = record[-1]
                record.append(2*value)
            else:
                record.append(int(operation))
        return sum(record)
        