a = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
b = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
morse_code_map = {'a': '.-', 'c': '-.-.', 'b': '-...', 'e': '.', 'd': '-..', 'g': '--.', 'f': '..-.', 'i': '..',
                  'h': '....', 'k': '-.-', 'j': '.---', 'm': '--', 'l': '.-..', 'o': '---', 'n': '-.',
                  'q': '--.-', 'p': '.--.', 's': '...', 'r': '.-.', 'u': '..-', 't': '-', 'w': '.--', 'v': '...-',
                  'y': '-.--', 'x': '-..-', 'z': '--..'}

class Solution:

    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        transformations_count = 0
        transformations_set = set()
        for word in words:
            transformed_word = self.transform_word(word)
            if transformed_word not in transformations_set:
                transformations_set.add(transformed_word)

            else:
                transformations_count+=1

        return transformations_count

    def transform_word(self,word):
        transformed_word = ""
        for letter in word:
            transformed_word += morse_code_map[letter]

        return transformed_word






a = Solution()
b = a.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
print(b)






