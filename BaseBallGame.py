class Solution:
    def __init__(self):
        self.first_val = None
        self.second_val = None
        self.points_to_add = None
        self.stack = []
        self.final_sum = 0

    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """''
        for string in ops:
            if self.represents_int(string):
                self.points_to_add = int(string)
                self.stack.append(self.points_to_add)
                self.final_sum += self.points_to_add
                self.points_to_add = None

            elif string == "+":
                self.sum_last_two_add_to_stack()

            elif string == "D":
                self.add_last_val_doubled_to_stack()

            elif string == "C":
                self.final_sum -= self.stack.pop()  # Remove last val from stack

        return self.final_sum

    def represents_int(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def sum_last_two_add_to_stack(self):
        if len(self.stack) > 0:
            self.first_val = self.stack.pop()

            if len(self.stack) > 0:
                self.second_val = self.stack.pop()

        if self.first_val is not None:
            self.points_to_add = self.first_val

        if self.points_to_add is not None:
            if self.second_val is not None:
                self.points_to_add = self.points_to_add + self.second_val
                self.stack.append(self.second_val)

            self.stack.append(self.first_val)

            self.final_sum += self.points_to_add
            self.stack.append(self.points_to_add)

        self.points_to_add = None
        self.first_val = None
        self.second_val = None

    def add_last_val_doubled_to_stack(self):
        if len(self.stack) > 0:
            self.points_to_add = self.stack[-1] + self.stack[-1]
            self.stack.append(self.points_to_add)
            self.final_sum += self.points_to_add