class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if word == abbr:
            return True
        word_ptr = abbr_ptr = 0
        if len(abbr) > len(word):
            return False
        count = ''
        left_ptr = 0

        while word_ptr < len(word) and abbr_ptr < len(abbr):
            if abbr[abbr_ptr].isalpha():
                count = ''
                if word[word_ptr] != abbr[abbr_ptr]:
                    return False
                abbr_ptr += 1
                word_ptr += 1
            else:
                while abbr_ptr < len(abbr) and (not abbr[abbr_ptr].isalpha()):
                    if abbr[abbr_ptr] == '0' and not count:
                        return False
                    count += abbr[abbr_ptr]
                    abbr_ptr += 1 
                word_ptr += int(count)
        return word_ptr == len(word) and abbr_ptr == len(abbr)

        