import re

class MyString:
    def __init__(self,*args):
        self.string = ""

        if len(args) == 0:
            self.string = ""

        elif type(args[0]) == list:
            # print(args[0])
            for i in args[0]:
                self.string += i
            # print(self.string)

        elif type(args[0]) == MyString:
            self.string = args[0]


    def length(self):
        return len(self.string)
    

    def char_at(self,index):
        return self.string[index]
    
    def substring(self, *args):
        if len(args) == 2:
            return self.string[args[0]:args[1]]
        else:
            return self.string[args[0]:]
    
    # def chstring(self, beginIndex, endIndex):
    #     return self.string[beginIndex:endIndex]

    def compare_to(self, anotherString):
        return (self.string > anotherString.string) - (self.string < anotherString.string)
    
    
    
    def compare_to_ignore_case(self, str):
        str1 = self.to_lower_case()
        # str2 = str.to_lower_case() 

        return str1 == str
    
    def equals_ignore_case(self, anotherString):
        str1 = self.to_lower_case()
        str2 = anotherString.to_lower_case()

        return str1 == str2

    def concat(self, s):
        return self.string + s.string
    
    def replace(self, oldChar, newChar):
        r = ""
        for i in self.string:
            if i == oldChar:
                r += newChar
            else:
                r += i
        return r
    

    def replace_seq(self, target, replacement):
        i = 0
        l = len(self.string)
        r = ""
        while i < l:
            # print(i, target, len(target.string))
            s = self.string[i:len(target.string)+i]
            if s == target.string:
                r += replacement.string
                i += len(target.string)
            else:
                r += self.string[i]
                i += 1
        return r
    

    def replace_all(self, regex, replacement):
        s = re.sub(regex, replacement.string, self.string)
        return s
    
    def replace_first(self, regex, replacement:'MyString'):
        s = re.sub(regex, replacement.string, self.string, count=1)
        return s
            
        
    def contains(self, s):
        if s.string in self.string:
            return True
        return False

    def index_of(self, ch):
        return self.index_of_from(ch, 0)
        
        
    def index_of_from(self, ch, fromIndex):
        s = ch.string if isinstance(ch, MyString) else str(ch)
        index = self.string.find(s, fromIndex)
        if index != -1:
            return index
        else:
            return -1
        # for i in range(fromIndex, len(self.string)):
        #     if self.string[i] == ch:
        #         return i
            

    def last_index_of_from(self, ch, formIndex):
        s = ch.string if isinstance(ch, MyString) else str(ch)
        index = self.string.rfind(s, 0, formIndex + 1)
        if index != -1:
            return index
        else:
            return -1

    def last_index_of(self, ch):
        return self.last_index_of_from(ch, self.length() - 1)


    def is_empty(self):
        return len(self.string) == 0
    
    def to_char_array(self):
        lst = []
        for i in self.string:
            lst.append(i)
        return lst
    
    def to_lower_case(self):
        r = ""
        for i in self.string:
            if i >= 'A' and i <= 'Z':
                r += chr(ord(i) + 32)
            else:
                r += i
        return r
    

    def to_upper_case(self):
        r = ""
        for i in self.string:
            if i >= 'a' and i <= 'z':
                r += chr(ord(i) - 32)
            else:
                r += i
        return r

    def trim(self):
        start = 0
        end = len(self.string) - 1
        
        while start <= end and self.string[start] == ' ':
            start += 1
        
        while end >= start and self.string[end] == ' ':
            end -= 1
        
        return self.string[start:end + 1]
    

    def starts_with_from(self, ch, fromIndex):
        n = ch.length()
        return self.string[fromIndex:fromIndex + n] == ch.string
    
    def starts_with(self, ch):
        return self.starts_with_from(ch,0)
    
    def split(self, ch: 'MyString'):
        ch_str = ""

        if isinstance(ch, MyString):
            ch_str = ch.string  

        k = []
        for i in self.string:
            if i == ch_str:
                continue
            k.append(i)
        
        return k


    def split_limit(self, ch, limit):
        ch_str = ""

        if isinstance(ch, MyString):
            ch_str = ch.string  
        else: 
            ch_str = str(ch)

        x = self.string.split(ch_str)

        r = x[:limit-1]
        a = ""
        for i in range(limit - 1, len(x)):
            if i > limit - 1:
                a += ","
            a += x[i]
        r.append(a)

        return r

    def __str__(self) -> str:
        return f"{self.string}"