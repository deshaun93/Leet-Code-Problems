class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewelsSet = self.createJewelsSet(J)
        # numberOfJewels = self.countJewels(S, jewelsSet)
        numberOfJewels = self.countJewels2(S, J)

        return numberOfJewels

    def createJewelsSet(self, J):
        jewels = set()
        for letter in J:
            jewels.add(letter)
            print(letter)
        return jewels

    def countJewels(self, stones, jewels):
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        return count

    def countJewels2(self, stones, jewels):
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        return count


s = Solution()
print(s.numJewelsInStones("aA", "aAAbbbb"))
