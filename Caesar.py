#!/usr/bin/env python
# -*- coding: utf-8 -*-

class CaesarCipher(object):

    def shift_text(self,c,shift):        
        if 'A' <= c and c <= 'Z':
            return chr((ord(c) - ord('A') + int(shift)) % 26 + ord('A'))
        if 'a' <= c and c <= 'z':
            return chr((ord(c) - ord('a') + int(shift)) % 26 + ord('a'))    
        return c
    
    def encode(self,text,shift=13):
        g = [self.shift_text(c,shift) for c in list(text)]
        return ''.join(g)

    def decode(self,text,shift=13):
        g = [self.shift_text(c,-shift) for c in list(text)]
        return ''.join(g)

    def search(self,text):
        serch_list =[]            
        for count in range(26):
            g = [self.shift_text(c,count) for c in list(text)]
            new_caer = str(count) + ":" + ''.join(g)
            serch_list.append(new_caer)
        return serch_list


