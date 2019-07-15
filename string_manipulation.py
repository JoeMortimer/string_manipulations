class StringManipulation():
    # A class where you input a string and then can run a variety of string attributes
    
    def __init__(self, str_in):
        self.str_in = str_in
        
    def count_words(self):
        return(len(self.str_in.split()))
    
    def reverse(self):
        return(self.str_in[::-1])
    
    def num_of_vowels(self):
        vowels = ('a','e','i', 'o', 'u')
        num = 0
        for i in self.str_in:
            if i in vowels:
                num+=1
                
        return(num)
    
    def palindrome(self):
        #returns true if is the same forward as backwards e.g. racecar
        return self.str_in == self.str_in[::-1]
    
    def pig_latin(self):
    
        """a method of rearanging the english language. If the word begins with a vowel - 'ay' is added
        to the end of the word. If the word begins with a constant - the constant is moved to the end of the 
        word and 'ay' is then added to the end"""
        
        vowels = ('a','e','i', 'o', 'u','A','E','I','O', 'U')
        out = ''
        for word in self.str_in.split():
            if word[0] in vowels:
                out += word + 'ay '
            else:
                out += word[1:] + word[0] +'ay '
                
        return(out)
