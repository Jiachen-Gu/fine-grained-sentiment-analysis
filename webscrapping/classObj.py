class def_dictionary(dict):

    def __init__(self):
        self = dict()

        # Function to add key:value
    def add(self, key, value):
        self[key] = value


import re
import inflect
import unicodedata
from contractions import CONTRACTION_MAP


class pre_process:

    def __init__(self, text_name, text_review):
        self.Name = text_name
        self.Review = text_review

    def __remove_whitespcace__(self):
        self.Name = re.sub(r"^\s+|\s+$", "", self.Name)
        self.Review = re.sub(r"^\s+|\s+$", "", self.Review)

    # convert to lower case
    def toLowerCase(self):
        """
        :type str: str
        """
        res = ""
        res2 = ""
        self.Review = res.join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in self.Review)
        self.Name = res2.join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in self.Name)

    def expandContractions(self, contraction_mapping=CONTRACTION_MAP):
        """
        :type contraction_map: map
        """
        contractions_pattern = re.compile('({})'.format('|'.join(contraction_mapping.keys())),
                                          flags=re.IGNORECASE | re.DOTALL)

        def expand_match(contraction):
            match = contraction.group(0)
            first_char = match[0]
            expanded_contraction = contraction_mapping.get(match) \
                if contraction_mapping.get(match) \
                else contraction_mapping.get(match.lower())
            expanded_contraction = first_char + expanded_contraction[1:]
            return expanded_contraction

        expanded_text = contractions_pattern.sub(expand_match, self.Review)
        expanded_text = re.sub("'", "", expanded_text)

        # remove_accented_chars
        expanded_text = unicodedata.normalize('NFKD', expanded_text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        self.Review = expanded_text

    def replace_numbers_to_char(self):
        """Replace all interger occurrences in list of tokenized words with textual representation"""
        p = inflect.engine()
        new_words = ""
        words = self.Review
        for word in words.split(" "):
            if word.isdigit():
                new_word = p.number_to_words(word)
                new_words += new_word + " "
            else:
                new_words += word + " "
        self.Review = new_words

    def removePuntuation(self): # removing punctuation
        self.Review = re.sub(r'[^\w\s]', '', self.Review)

    def replace_and_symbol(self): # replace and symbol
        self.Review = re.sub(r'&', 'and', self.Review)

    def removeNumber(self):
        self.Review = re.sub("^\d+\s|\s\d+\s|\s\d+$", " ", self.Review)

    def removeNewLine(self): # Remove new line \n
        self.Review = re.sub("\n", " ", self.Review)

    def removeCarriageChar(self): # remove carriage chracter \r
        self.Review = re.sub("\r", "", self.Review)

    def removeEmptySpace(self): # remove empty spaces
        self.Review = re.sub("  ", " ", self.Review)

    def deleteDigits(self): # delete digits
        self.Review = re.sub("\d+", "", self.Review)

    def reformat_airbnb(self): # making text consistent
        self.Review = re.sub("air bnb", "airbnb", self.Review)



