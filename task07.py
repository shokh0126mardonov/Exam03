class StringTools:
    def __init__(self,words):
         self.words = words
    
    @staticmethod
    def is_palindrome(text):
        if text == text[::-1]:
            return True
        else:
            return False
        
    @classmethod
    def from_sentence(cls,text: str):
           words = text.split()
           return cls(words)
       
print(StringTools.is_palindrome("level"))
st = StringTools.from_sentence("I love Python")
print(st.words)
