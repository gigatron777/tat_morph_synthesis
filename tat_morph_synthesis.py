#*- coding: utf-8 -*-
def is_vowel(c):
    return c.lower() in ('а', 'о', 'у', 'ы', 'ә', 'ө', 'и', 'ү', 'э', 'е')

def is_vowel_soft(c):
    return c.lower() in ('ә', 'ө', 'и', 'ү', 'э', 'е')

def is_vowel_hard(c):
    return c.lower() in ('а', 'о', 'у', 'ы')

def is_cons(c):
    return not is_vowel(c)

def is_word_soft(s):
    if s[-1] == 'ь':
        return True
    if s[-1] == 'ъ':
        return False
    t = s[::-1]
    for i in range(len(t)):
        if t[i] == 'е': #because каен is not soft
            if i < len(t) - 1:
                if t[i + 1] == 'а':
                    return False
        if is_vowel(t[i]):
            return True if is_vowel_soft(t[i]) else False

def is_word_hard(s):
    return not is_word_soft(s)

class Noun: #poss - possessive
    
    def __str__(self):
        return self.letters  
    
    def apply_poss(self):
        if is_vowel(self.letters[-1]):
            if is_word_soft(self.letters):
                if self.poss == 'p1s':
                    self.letters += 'м'
                if self.poss == 'p2s':
                    self.letters += 'ң'
                if self.poss == 'p3s':
                    self.letters += 'се'
                if self.poss == 'p1p':
                    self.letters += 'без'
                if self.poss == 'p2p':
                    self.letters += 'гез'
                if self.poss == 'p3p':
                    self.letters += 'нәре' if self.letters[-1] in ('м', 'н', 'ң') else 'ләре'
            else:
                if self.poss == 'p1s':
                    self.letters += 'м'
                if self.poss == 'p2s':
                    self.letters += 'ң'
                if self.poss == 'p3s':
                    self.letters += 'сы'
                if self.poss == 'p1p':
                    self.letters += 'быз'
                if self.poss == 'p2p':
                    self.letters += 'гыз'
                if self.poss == 'p3p':
                    self.letters += 'нары' if self.letters[-1] in ('м', 'н', 'ң') else 'лары'
        else:
            if self.poss != 'p3p':
                if self.letters[-1] == 'к':
                    self.letters = self.letters[:-1] + 'г'
                if self.letters[-1] == 'п':
                    self.letters = self.letters[:-1] + 'б'
                if self.letters[-1] in ('у', 'ү'):
                    self.letters = self.letters[:-1] + 'в'
                
            if is_word_soft(self.letters):
                if self.letters[-1] == 'ь' and self.poss != 'p3p':
                    self.letters = self.letters[:-1]
                if self.poss == 'p1s':
                    self.letters += 'ем'
                if self.poss == 'p2s':
                    self.letters += 'ең'
                if self.poss == 'p3s':
                    self.letters += 'е'
                if self.poss == 'p1p':
                    self.letters += 'ебез'
                if self.poss == 'p2p':
                    self.letters += 'егез'
                if self.poss == 'p3p':
                    self.letters += 'нәре' if self.letters[-1] in ('м', 'н', 'ң') else 'ләре'
            else:
                if self.poss == 'p1s':
                    self.letters += 'ым'
                if self.poss == 'p2s':
                    self.letters += 'ың'
                if self.poss == 'p3s':
                    self.letters += 'ы'
                if self.poss == 'p1p':
                    self.letters += 'ыбыз'
                if self.poss == 'p2p':
                    self.letters += 'ыгыз'
                if self.poss == 'p3p':
                    self.letters += 'нары' if self.letters[-1] in ('м', 'н', 'ң') else 'лары'
        
        self.letters = self.letters.replace('йы', 'е')#Тукайым -> Тукаем
        self.letters = self.letters.replace('йе', 'е')
        pass
    
    def apply_case(self):
        if self.case == 'acc':
            self.apply_accusative()
        if self.case == 'dat':
            self.apply_dative()
        if self.case == 'abl':
            self.apply_ablative()
        if self.case == 'loc':
            self.apply_locative()
        if self.case == 'gen':
            self.apply_generative()
        #if self.case == 'ins':
            #self.apply_instrumental()
    
    def apply_plural(self):
        if self.letters[-1] in ('м', 'н', 'ң'):
            self.letters += 'нар' if is_word_hard(self.letters) else 'нәр'
        else:
            self.letters += 'лар' if is_word_hard(self.letters) else 'ләр'

    def apply_locative(self):
        if is_vowel(self.letters[-1]) or self.letters[-1] in ('ж', 'җ', 'з', 'й', 'л', 'м', 'н', 'ң', 'р'):
            if self.poss in ('p3s', 'p3p'):
                self.letters += 'н'
            self.letters += 'да' if is_word_hard(self.letters) else 'дә'
        else:
            self.letters += 'та' if is_word_hard(self.letters) else 'тә'
                
    def apply_ablative(self):
        if self.poss != 'none':
            if self.poss in ('p1p', 'p2p'):
                self.letters += 'дан' if is_word_hard(self.letters) else 'дән'
            else:
                if self.poss in ('p3s', 'p3p'):
                    self.letters += 'ннан' if is_word_hard(self.letters) else 'ннән'
                else:
                    self.letters += 'нан' if is_word_hard(self.letters) else 'нән'
        else:
            if self.letters[-1] in ('м', 'н', 'ң'):
                self.letters += 'нан' if is_word_hard(self.letters) else 'нән'
            else:
                if self.letters[-1] in ('ж', 'җ', 'з', 'й', 'л', 'р') or is_vowel(self.letters[-1]):
                    self.letters += 'дан' if is_word_hard(self.letters) else 'дән'
                else:
                    self.letters += 'тан' if is_word_hard(self.letters) else 'тән'

    
    def apply_dative(self):
        if self.poss != 'none':
            if self.poss in ('p1s', 'p2s'):
                self.letters += 'а' if is_word_hard(self.letters) else 'ә'
            if self.poss in ('p1p', 'p2p'):
                self.letters += 'га' if is_word_hard(self.letters) else 'гә'
            if self.poss in ('p3s', 'p3p'):
                self.letters += 'на' if is_word_hard(self.letters) else 'нә'
        else:
            if self.letters[-1] in ('ж', 'җ', 'з', 'й', 'л', 'р', 'м', 'н', 'ң') or is_vowel(self.letters[-1]):
                self.letters += 'га' if is_word_hard(self.letters) else 'гә'
            else:
                self.letters += 'ка' if is_word_hard(self.letters) else 'кә'
        pass
    
    def apply_generative(self):
        self.letters += 'ның' if is_word_hard(self.letters) else 'нең'
        pass
    
    def apply_accusative(self):
        if self.poss != 'none':
            if self.poss in ('p3s', 'p3p'):
                self.letters += 'н' if is_word_hard(self.letters) else 'н'
            else:
                self.letters += 'ны' if is_word_hard(self.letters) else 'не'
        else:
            self.letters += 'ны' if is_word_hard(self.letters) else 'не'
        pass
    
    def __init__(self, letters, number, poss, case):
        self.letters = letters
        self.number = number
        self.poss = poss
        self.case = case
        
        if self.number == 'pl':
            self.apply_plural()   
        if self.poss != 'none':
            self.apply_poss()
        if self.case != 'nom':
            self.apply_case()    

if __name__ == "__main__":
    while True:
        print('Enter a tatar noun:')
        s = input()
        wrd = Noun(s, 'pl', 'none', 'nom')
        print(wrd)     
        print()
        
        wrd = Noun(s, 's', 'none', 'acc')
        print(wrd)
    
        wrd = Noun(s, 'pl', 'none', 'acc')
        print(wrd)  
        print()
        
        wrd = Noun(s, 's', 'none', 'dat')
        print(wrd)
    
        wrd = Noun(s, 'pl', 'none', 'dat')
        print(wrd)  
        print()
        
        wrd = Noun(s, 's', 'none', 'abl')
        print(wrd)
    
        wrd = Noun(s, 'pl', 'none', 'abl')
        print(wrd)   
        print()        
        
        wrd = Noun(s, 's', 'none', 'loc')
        print(wrd)
        
        wrd = Noun(s, 'pl', 'none', 'loc')
        print(wrd)    
        print()
        
        wrd = Noun(s, 's', 'none', 'gen')
        print(wrd)
    
        wrd = Noun(s, 'pl', 'none', 'gen')
        print(wrd)    
        print()        
        
        
        wrd = Noun(s, 's', 'p1s', 'nom')
        print(wrd)   
        
        wrd = Noun(s, 's', 'p2s', 'nom')
        print(wrd)  
        
        wrd = Noun(s, 's', 'p3s', 'nom')
        print(wrd)  
        
        wrd = Noun(s, 's', 'p1p', 'nom')
        print(wrd)  
        
        wrd = Noun(s, 's', 'p2p', 'nom')
        print(wrd)  
        
        wrd = Noun(s, 's', 'p3p', 'nom')
        print(wrd)
        #------------------------
        print()
        wrd = Noun(s, 's', 'p1s', 'acc')
        print(wrd)   
    
        wrd = Noun(s, 's', 'p2s', 'acc')
        print(wrd)  
    
        wrd = Noun(s, 's', 'p3s', 'acc')
        print(wrd)  
    
        wrd = Noun(s, 's', 'p1p', 'acc')
        print(wrd)  
    
        wrd = Noun(s, 's', 'p2p', 'acc')
        print(wrd)  
    
        wrd = Noun(s, 's', 'p3p', 'acc')
        print(wrd)        
        #------------------------
        print()
        wrd = Noun(s, 's', 'p1s', 'dat')
        print(wrd)   
    
        wrd = Noun(s, 's', 'p2s', 'dat')
        print(wrd)  
    
        wrd = Noun(s, 's', 'p3s', 'dat')
        print(wrd)  
    
        wrd = Noun(s, 's', 'p1p', 'dat')
        print(wrd)  
    
        wrd = Noun(s, 's', 'p2p', 'dat')
        print(wrd)  
    
        wrd = Noun(s, 's', 'p3p', 'dat')
        print(wrd)           
        
        #-----------------------
        print()
        wrd = Noun(s, 's', 'p1s', 'abl')
        print(wrd)   
    
        wrd = Noun(s, 's', 'p2s', 'abl')
        print(wrd)  
    
        wrd = Noun(s, 's', 'p3s', 'abl')
        print(wrd)  
    
        wrd = Noun(s, 's', 'p1p', 'abl')
        print(wrd)  
    
        wrd = Noun(s, 's', 'p2p', 'abl')
        print(wrd)  
    
        wrd = Noun(s, 's', 'p3p', 'abl')
        print(wrd)  
        
        #-----------------------
        print()
        wrd = Noun(s, 's', 'p1s', 'loc')
        print(wrd)   
    
        wrd = Noun(s, 's', 'p2s', 'loc')
        print(wrd)  
    
        wrd = Noun(s, 's', 'p3s', 'loc')
        print(wrd)  
    
        wrd = Noun(s, 's', 'p1p', 'loc')
        print(wrd)  
    
        wrd = Noun(s, 's', 'p2p', 'loc')
        print(wrd)  
    
        wrd = Noun(s, 's', 'p3p', 'loc')
        print(wrd)
        
        #-----------------------
        print()
        wrd = Noun(s, 's', 'p1s', 'gen')
        print(wrd)   
    
        wrd = Noun(s, 's', 'p2s', 'gen')
        print(wrd)  
    
        wrd = Noun(s, 's', 'p3s', 'gen')
        print(wrd)  
    
        wrd = Noun(s, 's', 'p1p', 'gen')
        print(wrd)  
    
        wrd = Noun(s, 's', 'p2p', 'gen')
        print(wrd)  
    
        wrd = Noun(s, 's', 'p3p', 'gen')
        print(wrd)            
    