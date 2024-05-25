from typing import List

class SpecialWordMasker:
    """
    This class masks special words in a text.

    :param special_words: List of special words to mask
    :param target_word: Word to mask in special words
    :param replacement_char: Character to replace the target word with

    >>> masker = MaskSpecialWords(['New York', 'El Nino'], ' ', '•')
    >>> masker.mask_special_char_in_words('New York is affected by El Nino.')
    'New•York is affected by El•Nino.'
    """
    def __init__(self, special_words: List[str], target_word: str, replacement_char: str):
        import re
        
        self.special_words = special_words
        self.target_word = target_word
        self.replacement_char = replacement_char
        self.patterns = [re.compile(r'\b' + re.escape(word) + r'\b') for word in special_words]

    def mask_words(self, text: str) -> str:
        """
        This function masks special words in a text.

        :param text: Text to mask special words in

        :return: Text with special words masked
        """
        for i, word in enumerate(self.special_words):
            masked_word = word.replace(self.target_word, self.replacement_char)
            text = self.patterns[i].sub(masked_word, text)
        return text
    
    def __repr__(self):
        return f'<SpecialWordMasker(special_words={self.special_words}, target_word={self.target_word}, replacement_char={self.replacement_char})>'
