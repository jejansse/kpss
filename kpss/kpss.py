#!/usr/bin/env python
# vim:fileencoding=utf-8



# This file was auto-generated on 2015-08-18 17:35:18 using
# version 0.1.0-2 of the sbl2py Snowball-to-Python compiler.

import sys

class _String(object):

    def __init__(self, s):
        self.chars = list(unicode(s))
        self.cursor = 0
        self.limit = len(s)
        self.direction = 1

    def __unicode__(self):
        return u''.join(self.chars)

    def __len__(self):
        return len(self.chars)

    def get_range(self, start, stop):
        if self.direction == 1:
            return self.chars[start:stop]
        else:
            n = len(self.chars)
            return self.chars[stop:start]

    def set_range(self, start, stop, chars):
        if self.direction == 1:
            self.chars[start:stop] = chars
        else:
            self.chars[stop:start] = chars
        change = self.direction * (len(chars) - (stop - start))
        if self.direction == 1:
            if self.cursor >= stop:
                self.cursor += change
                self.limit += change
        else:
            if self.cursor > start:
                self.cursor += change
            if self.limit > start:
                self.limit += change
        return True

    def insert(self, chars):
        self.chars[self.cursor:self.cursor] = chars
        if self.direction == 1:
            self.cursor += len(chars)
            self.limit += len(chars)
        return True

    def attach(self, chars):
        self.chars[self.cursor:self.cursor] = chars
        if self.direction == 1:
            self.limit += len(chars)
        else:
            self.cursor += len(chars)
        return True

    def set_chars(self, chars):
        self.chars = chars
        if self.direction == 1:
            self.cursor = 0
            self.limit = len(chars)
        else:
            self.cursor = len(chars)
            self.limit = 0
        return True

    def starts_with(self, chars):
        n = len(chars)
        r = self.get_range(self.cursor, self.limit)[::self.direction][:n]
        if not r == list(chars)[::self.direction]:
            return False
        self.cursor += n * self.direction
        return True

    def hop(self, n):
        if n < 0 or len(self.get_range(self.cursor, self.limit)) < n:
            return False
        self.cursor += n * self.direction
        return True

    def to_mark(self, mark):
        if self.direction == 1:
            if self.cursor > mark or self.limit < mark:
                return False
        else:
            if self.cursor < mark or self.limit > mark:
                return False
        self.cursor = mark
        return True


def stem(s):
    s = _String(s)
    _Program().r_stem(s)
    return unicode(s)

_g_v = set(u'aeiouy')
_g_v_WX = (_g_v | set(u'wx'))
_g_AOU = set(u'aou')
_g_AIOU = set(u'aiou')
_a_1 = ((u'ies', '', 2), (u'aus', '', 4), (u'nde', '', 6), (u"'s", '', 0), (u'es', '', 3), (u'en', '', 5), (u's', '', 1),)
_a_2 = ((u'lijke', '', 2), (u'ische', '', 3), (u'ieve', '', 10), (u'ene', '', 9), (u'je', '', 0), (u'ge', '', 1), (u'de', '', 4), (u'te', '', 5), (u'se', '', 6), (u're', '', 7), (u'le', '', 8),)
_a_3 = ((u'iteit', '', 1), (u'atie', '', 0), (u'heid', '', 2), (u'ster', '', 2), (u'rder', '', 3), (u'isme', '', 4), (u'erij', '', 4), (u'arij', '', 5), (u'sel', '', 2), (u'ing', '', 4), (u'fie', '', 6), (u'gie', '', 7), (u'tst', '', 8), (u'dst', '', 9),)
_a_4 = ((u'achtiger', '', 8), (u'achtigst', '', 8), (u'ioneel', '', 0), (u'lijker', '', 7), (u'lijkst', '', 7), (u'achtig', '', 8), (u'eriger', '', 9), (u'erigst', '', 9), (u'atief', '', 1), (u'baar', '', 2), (u'naar', '', 3), (u'laar', '', 4), (u'raar', '', 5), (u'tant', '', 6), (u'erig', '', 9), (u'end', '', 9),)
_a_5 = ((u'iger', '', 0), (u'igst', '', 0), (u'ig', '', 0),)
_a_6 = ((u'kt', '', 0), (u'ft', '', 1), (u'pt', '', 2),)
_a_7 = ((u'bb', '', 0), (u'cc', '', 1), (u'dd', '', 2), (u'ff', '', 3), (u'gg', '', 4), (u'hh', '', 5), (u'jj', '', 6), (u'kk', '', 7), (u'll', '', 8), (u'mm', '', 9), (u'nn', '', 10), (u'pp', '', 11), (u'qq', '', 12), (u'rr', '', 13), (u'ss', '', 14), (u'tt', '', 15), (u'vv', '', 16), (u'ww', '', 17), (u'xx', '', 18), (u'zz', '', 19), (u'v', '', 20), (u'z', '', 21),)
_a_8 = ((u'd', '', 0), (u't', '', 1),)

class _Program(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.s_ch = _String('')
        self.i_x = 0
        self.i_p1 = 0
        self.i_p2 = 0
        self.b_Y_found = True
        self.b_stemmed = True
        self.b_GE_removed = True

    def r_R1(self, s):
        r = True
        self.i_x = s.cursor  ##
        r = True             ## setmark
        if r:
            r = self.i_x >= self.i_p1  # >=
        return r
    
    def r_R2(self, s):
        r = True
        self.i_x = s.cursor  ##
        r = True             ## setmark
        if r:
            r = self.i_x >= self.i_p2  # >=
        return r
    
    def r_V(self, s):
        r = True
        var1 = len(s) - s.cursor                                       ##
        var0 = len(s) - s.cursor                                 ##    #
        if s.cursor == s.limit:                ##                #     #
            r = False                          #                 #     #
        else:                                  #                 #     #
            r = s.chars[s.cursor - 1] in _g_v  # grouping check  #     #
        if r:                                  #                 # or  # test
            s.cursor -= 1                      ##                #     #
        if not r:                                                #     #
            s.cursor = len(s) - var0                             #     #
            r = s.starts_with(u'ij')  # character check          ##    #
        s.cursor = len(s) - var1                                       ##
        return r
    
    def r_VX(self, s):
        r = True
        var3 = len(s) - s.cursor                                           ##
        r = s.hop(1)  # next                                               #
        if r:                                                              #
            var2 = len(s) - s.cursor                                 ##    #
            if s.cursor == s.limit:                ##                #     #
                r = False                          #                 #     #
            else:                                  #                 #     #
                r = s.chars[s.cursor - 1] in _g_v  # grouping check  #     # test
            if r:                                  #                 # or  #
                s.cursor -= 1                      ##                #     #
            if not r:                                                #     #
                s.cursor = len(s) - var2                             #     #
                r = s.starts_with(u'ij')  # character check          ##    #
        s.cursor = len(s) - var3                                           ##
        return r
    
    def r_C(self, s):
        r = True
        var5 = len(s) - s.cursor                                                  ##
        var4 = len(s) - s.cursor                     ##                           #
        r = s.starts_with(u'ij')  # character check  #                            #
        if not r:                                    # not                        #
            s.cursor = len(s) - var4                 #                            #
        r = not r                                    ##                           #
        if r:                                                                     #
            if s.cursor == s.limit:                    ##                         # test
                r = False                              #                          #
            else:                                      #                          #
                r = s.chars[s.cursor - 1] not in _g_v  # negative grouping check  #
            if r:                                      #                          #
                s.cursor -= 1                          ##                         #
        s.cursor = len(s) - var5                                                  ##
        return r
    
    def r_lengthen_V(self, s):
        r = True
        var13 = len(s) - s.cursor                                                                                                      ##
        if s.cursor == s.limit:                       ##                                                                               #
            r = False                                 #                                                                                #
        else:                                         #                                                                                #
            r = s.chars[s.cursor - 1] not in _g_v_WX  # negative grouping check                                                        #
        if r:                                         #                                                                                #
            s.cursor -= 1                             ##                                                                               #
        if r:                                                                                                                          #
            self.left = s.cursor  ##                                                                                                   #
            r = True              ## [                                                                                                 #
            if r:                                                                                                                      #
                var12 = len(s) - s.cursor                                                                                        ##    #
                if s.cursor == s.limit:                  ##                                                                      #     #
                    r = False                            #                                                                       #     #
                else:                                    #                                                                       #     #
                    r = s.chars[s.cursor - 1] in _g_AOU  # grouping check                                                        #     #
                if r:                                    #                                                                       #     #
                    s.cursor -= 1                        ##                                                                      #     #
                if r:                                                                                                            #     #
                    self.right = s.cursor  ##                                                                                    #     #
                    r = True               ## ]                                                                                  #     #
                    if r:                                                                                                        #     #
                        var7 = len(s) - s.cursor                                                    ##                           #     #
                        var6 = len(s) - s.cursor                                              ##    #                            #     #
                        if s.cursor == s.limit:                    ##                         #     #                            #     #
                            r = False                              #                          #     #                            #     #
                        else:                                      #                          #     #                            #     #
                            r = s.chars[s.cursor - 1] not in _g_v  # negative grouping check  #     #                            #     #
                        if r:                                      #                          # or  # test                       #     #
                            s.cursor -= 1                          ##                         #     #                            #     #
                        if not r:                                                             #     #                            #     #
                            s.cursor = len(s) - var6                                          #     #                            #     #
                            r = (s.cursor == s.limit)  # atlimit                              ##    #                            #     #
                        s.cursor = len(s) - var7                                                    ##                           #     #
                if not r:                                                                                                        #     #
                    s.cursor = len(s) - var12                                                                                    #     #
                    r = s.starts_with(u'e')  # character check                                                                   #     #
                    if r:                                                                                                        #     #
                        self.right = s.cursor  ##                                                                                #     #
                        r = True               ## ]                                                                              #     #
                        if r:                                                                                                    #     #
                            var11 = len(s) - s.cursor                                                                    ##      #     #
                            var8 = len(s) - s.cursor                                              ##                     #       #     #
                            if s.cursor == s.limit:                    ##                         #                      #       #     #
                                r = False                              #                          #                      #       #     #
                            else:                                      #                          #                      #       #     # do
                                r = s.chars[s.cursor - 1] not in _g_v  # negative grouping check  #                      #       #     #
                            if r:                                      #                          # or                   #       # or  #
                                s.cursor -= 1                          ##                         #                      #       #     #
                            if not r:                                                             #                      #       #     #
                                s.cursor = len(s) - var8                                          #                      #       #     #
                                r = (s.cursor == s.limit)  # atlimit                              ##                     #       #     #
                            if r:                                                                                        #       #     #
                                var9 = len(s) - s.cursor                                    ##                           #       #     #
                                if s.cursor == s.limit:                   ##                #                            #       #     #
                                    r = False                             #                 #                            #       #     #
                                else:                                     #                 #                            #       #     #
                                    r = s.chars[s.cursor - 1] in _g_AIOU  # grouping check  #                            #       #     #
                                if r:                                     #                 # not                        #       #     #
                                    s.cursor -= 1                         ##                #                            #       #     #
                                if not r:                                                   #                            #       #     #
                                    s.cursor = len(s) - var9                                #                            #       #     #
                                r = not r                                                   ##                           # test  #     #
                                if r:                                                                                    #       #     #
                                    var10 = len(s) - s.cursor                                                     ##     #       #     #
                                    r = s.hop(1)  # next                                                          #      #       #     #
                                    if r:                                                                         #      #       #     #
                                        if s.cursor == s.limit:                   ##                              #      #       #     #
                                            r = False                             #                               #      #       #     #
                                        else:                                     #                               #      #       #     #
                                            r = s.chars[s.cursor - 1] in _g_AIOU  # grouping check                #      #       #     #
                                        if r:                                     #                               #      #       #     #
                                            s.cursor -= 1                         ##                              #      #       #     #
                                        if r:                                                                     # not  #       #     #
                                            if s.cursor == s.limit:                    ##                         #      #       #     #
                                                r = False                              #                          #      #       #     #
                                            else:                                      #                          #      #       #     #
                                                r = s.chars[s.cursor - 1] not in _g_v  # negative grouping check  #      #       #     #
                                            if r:                                      #                          #      #       #     #
                                                s.cursor -= 1                          ##                         #      #       #     #
                                    if not r:                                                                     #      #       #     #
                                        s.cursor = len(s) - var10                                                 #      #       #     #
                                    r = not r                                                                     ##     #       #     #
                            s.cursor = len(s) - var11                                                                    ##      ##    #
                if r:                                                                                                                  #
                    r = self.s_ch.set_chars(s.get_range(self.left, self.right))  # ->                                                  #
                    if r:                                                                                                              #
                        r = s.insert(self.s_ch.chars)  # insert                                                                        #
        s.cursor = len(s) - var13                                                                                                      #
        r = True                                                                                                                       ##
        return r
    
    def r_Step_1(self, s):
        r = True
        self.left = s.cursor  ##
        r = True              ## [
        if r:
            a_1 = None                                                                                               ##
            r = False                                                                                                #
            var15 = s.cursor                                                                                         #
            for var14, var18, var17 in _a_1:                                                                         #
                if s.starts_with(var14):                                                                             #
                    var16 = s.cursor                                                                                 #
                    r = (not var18) or getattr(self, var18)(s)                                                       #
                    if r:                                                                                            #
                      s.cursor = var16                                                                               #
                      a_1 = var17                                                                                    #
                      break                                                                                          #
                s.cursor = var15                                                                                     #
            if r:                                                                                                    #
                self.right = s.cursor  ##                                                                            #
                r = True               ## ]                                                                          #
                if r:                                                                                                #
                    if a_1 == 0:                                                                                     #
                        r = s.set_range(self.left, self.right, u'')  # delete                                        #
                    if a_1 == 1:                                                                                     #
                        r = self.r_R1(s)  # routine call                                                             #
                        if r:                                                                                        #
                            var19 = len(s) - s.cursor                   ##                                           #
                            r = s.starts_with(u't')  # character check  #                                            #
                            if r:                                       #                                            #
                                r = self.r_R1(s)  # routine call        # not                                        #
                            if not r:                                   #                                            #
                                s.cursor = len(s) - var19               #                                            #
                            r = not r                                   ##                                           #
                            if r:                                                                                    #
                                r = self.r_C(s)  # routine call                                                      #
                                if r:                                                                                #
                                    r = s.set_range(self.left, self.right, u'')  # delete                            #
                    if a_1 == 2:                                                                                     #
                        r = self.r_R1(s)  # routine call                                                             #
                        if r:                                                                                        #
                            r = s.set_range(self.left, self.right, u'ie')  # <-                                      #
                    if a_1 == 3:                                                                                     #
                        var21 = len(s) - s.cursor                                                        ##          #
                        var20 = len(s) - s.cursor                                                  ##    #           #
                        r = s.starts_with(u'ar')  # character check                                #     #           #
                        if r:                                                                      #     #           #
                            r = self.r_R1(s)  # routine call                                       #     #           #
                            if r:                                                                  #     #           #
                                r = self.r_C(s)  # routine call                                    #     #           #
                                if r:                                                              #     #           #
                                    self.right = s.cursor  ##                                      #     #           #
                                    r = True               ## ]                                    #     #           #
                                    if r:                                                          #     #           #
                                        r = s.set_range(self.left, self.right, u'')  # delete      #     #           #
                                        if r:                                                      #     #           #
                                            r = self.r_lengthen_V(s)  # routine call               # or  #           #
                        if not r:                                                                  #     #           #
                            s.cursor = len(s) - var20                                              #     #           #
                            r = s.starts_with(u'er')  # character check                            #     # or        #
                            if r:                                                                  #     #           #
                                r = self.r_R1(s)  # routine call                                   #     #           #
                                if r:                                                              #     #           #
                                    r = self.r_C(s)  # routine call                                #     #           #
                                    if r:                                                          #     #           #
                                        self.right = s.cursor  ##                                  #     #           #
                                        r = True               ## ]                                #     #           #
                                        if r:                                                      #     #           #
                                            r = s.set_range(self.left, self.right, u'')  # delete  ##    #           #
                        if not r:                                                                        #           #
                            s.cursor = len(s) - var21                                                    #           # among
                            r = self.r_R1(s)  # routine call                                             #           #
                            if r:                                                                        #           #
                                r = self.r_C(s)  # routine call                                          #           #
                                if r:                                                                    #           #
                                    r = s.set_range(self.left, self.right, u'e')  # <-                   ##          #
                    if a_1 == 4:                                                                                     #
                        r = self.r_R1(s)  # routine call                                                             #
                        if r:                                                                                        #
                            r = self.r_V(s)  # routine call                                                          #
                            if r:                                                                                    #
                                r = s.set_range(self.left, self.right, u'au')  # <-                                  #
                    if a_1 == 5:                                                                                     #
                        var26 = len(s) - s.cursor                                                              ##    #
                        var25 = len(s) - s.cursor                                                        ##    #     #
                        var23 = len(s) - s.cursor                                                  ##    #     #     #
                        var22 = len(s) - s.cursor                                          ##      #     #     #     #
                        r = s.starts_with(u'hed')  # character check                       #       #     #     #     #
                        if r:                                                              #       #     #     #     #
                            r = self.r_R1(s)  # routine call                               #       #     #     #     #
                            if r:                                                          #       #     #     #     #
                                self.right = s.cursor  ##                                  #       #     #     #     #
                                r = True               ## ]                                #       #     #     #     #
                                if r:                                                      # or    #     #     #     #
                                    r = s.set_range(self.left, self.right, u'heid')  # <-  #       #     #     #     #
                        if not r:                                                          #       #     #     #     #
                            s.cursor = len(s) - var22                                      #       #     #     #     #
                            r = s.starts_with(u'nd')  # character check                    #       #     #     #     #
                            if r:                                                          #       # or  #     #     #
                                r = s.set_range(self.left, self.right, u'')  # delete      ##      #     #     #     #
                        if not r:                                                                  #     #     #     #
                            s.cursor = len(s) - var23                                              #     #     #     #
                            r = s.starts_with(u'd')  # character check                             #     #     #     #
                            if r:                                                                  #     # or  #     #
                                r = self.r_R1(s)  # routine call                                   #     #     #     #
                                if r:                                                              #     #     #     #
                                    r = self.r_C(s)  # routine call                                #     #     #     #
                                    if r:                                                          #     #     # or  #
                                        self.right = s.cursor  ##                                  #     #     #     #
                                        r = True               ## ]                                #     #     #     #
                                        if r:                                                      #     #     #     #
                                            r = s.set_range(self.left, self.right, u'')  # delete  ##    #     #     #
                        if not r:                                                                        #     #     #
                            s.cursor = len(s) - var25                                                    #     #     #
                            var24 = len(s) - s.cursor                       ##                           #     #     #
                            r = s.starts_with(u'i')  # character check      #                            #     #     #
                            if not r:                                       # or                         #     #     #
                                s.cursor = len(s) - var24                   #                            #     #     #
                                r = s.starts_with(u'j')  # character check  ##                           #     #     #
                            if r:                                                                        #     #     #
                                r = self.r_V(s)  # routine call                                          #     #     #
                                if r:                                                                    #     #     #
                                    r = s.set_range(self.left, self.right, u'')  # delete                ##    #     #
                        if not r:                                                                              #     #
                            s.cursor = len(s) - var26                                                          #     #
                            r = self.r_R1(s)  # routine call                                                   #     #
                            if r:                                                                              #     #
                                r = self.r_C(s)  # routine call                                                #     #
                                if r:                                                                          #     #
                                    r = s.set_range(self.left, self.right, u'')  # delete                      #     #
                                    if r:                                                                      #     #
                                        r = self.r_lengthen_V(s)  # routine call                               ##    #
                    if a_1 == 6:                                                                                     #
                        r = s.set_range(self.left, self.right, u'nd')  # <-                                          ##
        return r
    
    def r_Step_2(self, s):
        r = True
        self.left = s.cursor  ##
        r = True              ## [
        if r:
            a_2 = None                                                                                                                       ##
            r = False                                                                                                                        #
            var28 = s.cursor                                                                                                                 #
            for var27, var31, var30 in _a_2:                                                                                                 #
                if s.starts_with(var27):                                                                                                     #
                    var29 = s.cursor                                                                                                         #
                    r = (not var31) or getattr(self, var31)(s)                                                                               #
                    if r:                                                                                                                    #
                      s.cursor = var29                                                                                                       #
                      a_2 = var30                                                                                                            #
                      break                                                                                                                  #
                s.cursor = var28                                                                                                             #
            if r:                                                                                                                            #
                self.right = s.cursor  ##                                                                                                    #
                r = True               ## ]                                                                                                  #
                if r:                                                                                                                        #
                    if a_2 == 0:                                                                                                             #
                        var38 = len(s) - s.cursor                                                                                      ##    #
                        var37 = len(s) - s.cursor                                                                                ##    #     #
                        var36 = len(s) - s.cursor                                                                          ##    #     #     #
                        var35 = len(s) - s.cursor                                                                    ##    #     #     #     #
                        var34 = len(s) - s.cursor                                                              ##    #     #     #     #     #
                        var33 = len(s) - s.cursor                                                        ##    #     #     #     #     #     #
                        var32 = len(s) - s.cursor                                                  ##    #     #     #     #     #     #     #
                        r = s.starts_with(u"'t")  # character check                                #     #     #     #     #     #     #     #
                        if r:                                                                      #     #     #     #     #     #     #     #
                            self.right = s.cursor  ##                                              #     #     #     #     #     #     #     #
                            r = True               ## ]                                            #     #     #     #     #     #     #     #
                            if r:                                                                  #     #     #     #     #     #     #     #
                                r = s.set_range(self.left, self.right, u'')  # delete              #     #     #     #     #     #     #     #
                        if not r:                                                                  #     #     #     #     #     #     #     #
                            s.cursor = len(s) - var32                                              #     #     #     #     #     #     #     #
                            r = s.starts_with(u'et')  # character check                            # or  #     #     #     #     #     #     #
                            if r:                                                                  #     #     #     #     #     #     #     #
                                self.right = s.cursor  ##                                          #     #     #     #     #     #     #     #
                                r = True               ## ]                                        #     #     #     #     #     #     #     #
                                if r:                                                              #     # or  #     #     #     #     #     #
                                    r = self.r_R1(s)  # routine call                               #     #     #     #     #     #     #     #
                                    if r:                                                          #     #     #     #     #     #     #     #
                                        r = self.r_C(s)  # routine call                            #     #     #     #     #     #     #     #
                                        if r:                                                      #     #     #     #     #     #     #     #
                                            r = s.set_range(self.left, self.right, u'')  # delete  ##    #     # or  #     #     #     #     #
                        if not r:                                                                        #     #     #     #     #     #     #
                            s.cursor = len(s) - var33                                                    #     #     #     #     #     #     #
                            r = s.starts_with(u'rnt')  # character check                                 #     #     #     #     #     #     #
                            if r:                                                                        #     #     # or  #     #     #     #
                                self.right = s.cursor  ##                                                #     #     #     #     #     #     #
                                r = True               ## ]                                              #     #     #     #     #     #     #
                                if r:                                                                    #     #     #     # or  #     #     #
                                    r = s.set_range(self.left, self.right, u'rn')  # <-                  ##    #     #     #     #     #     #
                        if not r:                                                                              #     #     #     #     #     #
                            s.cursor = len(s) - var34                                                          #     #     #     #     #     #
                            r = s.starts_with(u't')  # character check                                         #     #     #     #     #     #
                            if r:                                                                              #     #     #     # or  #     #
                                self.right = s.cursor  ##                                                      #     #     #     #     #     #
                                r = True               ## ]                                                    #     #     #     #     #     #
                                if r:                                                                          #     #     #     #     #     #
                                    r = self.r_R1(s)  # routine call                                           #     #     #     #     # or  #
                                    if r:                                                                      #     #     #     #     #     #
                                        r = self.r_VX(s)  # routine call                                       #     #     #     #     #     #
                                        if r:                                                                  #     #     #     #     #     #
                                            r = s.set_range(self.left, self.right, u'')  # delete              ##    #     #     #     #     #
                        if not r:                                                                                    #     #     #     #     #
                            s.cursor = len(s) - var35                                                                #     #     #     #     #
                            r = s.starts_with(u'ink')  # character check                                             #     #     #     #     #
                            if r:                                                                                    #     #     #     #     #
                                self.right = s.cursor  ##                                                            #     #     #     #     #
                                r = True               ## ]                                                          #     #     #     #     #
                                if r:                                                                                #     #     #     #     #
                                    r = s.set_range(self.left, self.right, u'ing')  # <-                             ##    #     #     #     #
                        if not r:                                                                                          #     #     #     #
                            s.cursor = len(s) - var36                                                                      #     #     #     #
                            r = s.starts_with(u'mp')  # character check                                                    #     #     #     #
                            if r:                                                                                          #     #     #     #
                                self.right = s.cursor  ##                                                                  #     #     #     #
                                r = True               ## ]                                                                #     #     #     #
                                if r:                                                                                      #     #     #     # among
                                    r = s.set_range(self.left, self.right, u'm')  # <-                                     ##    #     #     #
                        if not r:                                                                                                #     #     #
                            s.cursor = len(s) - var37                                                                            #     #     #
                            r = s.starts_with(u"'")  # character check                                                           #     #     #
                            if r:                                                                                                #     #     #
                                self.right = s.cursor  ##                                                                        #     #     #
                                r = True               ## ]                                                                      #     #     #
                                if r:                                                                                            #     #     #
                                    r = self.r_R1(s)  # routine call                                                             #     #     #
                                    if r:                                                                                        #     #     #
                                        r = s.set_range(self.left, self.right, u'')  # delete                                    ##    #     #
                        if not r:                                                                                                      #     #
                            s.cursor = len(s) - var38                                                                                  #     #
                            self.right = s.cursor  ##                                                                                  #     #
                            r = True               ## ]                                                                                #     #
                            if r:                                                                                                      #     #
                                r = self.r_R1(s)  # routine call                                                                       #     #
                                if r:                                                                                                  #     #
                                    r = self.r_C(s)  # routine call                                                                    #     #
                                    if r:                                                                                              #     #
                                        r = s.set_range(self.left, self.right, u'')  # delete                                          ##    #
                    if a_2 == 1:                                                                                                             #
                        r = self.r_R1(s)  # routine call                                                                                     #
                        if r:                                                                                                                #
                            r = s.set_range(self.left, self.right, u'g')  # <-                                                               #
                    if a_2 == 2:                                                                                                             #
                        r = self.r_R1(s)  # routine call                                                                                     #
                        if r:                                                                                                                #
                            r = s.set_range(self.left, self.right, u'lijk')  # <-                                                            #
                    if a_2 == 3:                                                                                                             #
                        r = self.r_R1(s)  # routine call                                                                                     #
                        if r:                                                                                                                #
                            r = s.set_range(self.left, self.right, u'isch')  # <-                                                            #
                    if a_2 == 4:                                                                                                             #
                        r = self.r_R1(s)  # routine call                                                                                     #
                        if r:                                                                                                                #
                            r = self.r_C(s)  # routine call                                                                                  #
                            if r:                                                                                                            #
                                r = s.set_range(self.left, self.right, u'')  # delete                                                        #
                    if a_2 == 5:                                                                                                             #
                        r = self.r_R1(s)  # routine call                                                                                     #
                        if r:                                                                                                                #
                            r = s.set_range(self.left, self.right, u't')  # <-                                                               #
                    if a_2 == 6:                                                                                                             #
                        r = self.r_R1(s)  # routine call                                                                                     #
                        if r:                                                                                                                #
                            r = s.set_range(self.left, self.right, u's')  # <-                                                               #
                    if a_2 == 7:                                                                                                             #
                        r = self.r_R1(s)  # routine call                                                                                     #
                        if r:                                                                                                                #
                            r = s.set_range(self.left, self.right, u'r')  # <-                                                               #
                    if a_2 == 8:                                                                                                             #
                        r = self.r_R1(s)  # routine call                                                                                     #
                        if r:                                                                                                                #
                            r = s.set_range(self.left, self.right, u'')  # delete                                                            #
                            if r:                                                                                                            #
                                r = s.attach(u'l')  # attach                                                                                 #
                                if r:                                                                                                        #
                                    r = self.r_lengthen_V(s)  # routine call                                                                 #
                    if a_2 == 9:                                                                                                             #
                        r = self.r_R1(s)  # routine call                                                                                     #
                        if r:                                                                                                                #
                            r = self.r_C(s)  # routine call                                                                                  #
                            if r:                                                                                                            #
                                r = s.set_range(self.left, self.right, u'')  # delete                                                        #
                                if r:                                                                                                        #
                                    r = s.attach(u'en')  # attach                                                                            #
                                    if r:                                                                                                    #
                                        r = self.r_lengthen_V(s)  # routine call                                                             #
                    if a_2 == 10:                                                                                                            #
                        r = self.r_R1(s)  # routine call                                                                                     #
                        if r:                                                                                                                #
                            r = self.r_C(s)  # routine call                                                                                  #
                            if r:                                                                                                            #
                                r = s.set_range(self.left, self.right, u'ief')  # <-                                                         ##
        return r
    
    def r_Step_3(self, s):
        r = True
        self.left = s.cursor  ##
        r = True              ## [
        if r:
            a_3 = None                                                                ##
            r = False                                                                 #
            var40 = s.cursor                                                          #
            for var39, var43, var42 in _a_3:                                          #
                if s.starts_with(var39):                                              #
                    var41 = s.cursor                                                  #
                    r = (not var43) or getattr(self, var43)(s)                        #
                    if r:                                                             #
                      s.cursor = var41                                                #
                      a_3 = var42                                                     #
                      break                                                           #
                s.cursor = var40                                                      #
            if r:                                                                     #
                self.right = s.cursor  ##                                             #
                r = True               ## ]                                           #
                if r:                                                                 #
                    if a_3 == 0:                                                      #
                        r = self.r_R1(s)  # routine call                              #
                        if r:                                                         #
                            r = s.set_range(self.left, self.right, u'eer')  # <-      #
                    if a_3 == 1:                                                      #
                        r = self.r_R1(s)  # routine call                              #
                        if r:                                                         #
                            r = s.set_range(self.left, self.right, u'')  # delete     #
                            if r:                                                     #
                                r = self.r_lengthen_V(s)  # routine call              #
                    if a_3 == 2:                                                      #
                        r = self.r_R1(s)  # routine call                              #
                        if r:                                                         #
                            r = s.set_range(self.left, self.right, u'')  # delete     #
                    if a_3 == 3:                                                      #
                        r = s.set_range(self.left, self.right, u'r')  # <-            #
                    if a_3 == 4:                                                      #
                        r = self.r_R1(s)  # routine call                              #
                        if r:                                                         #
                            r = s.set_range(self.left, self.right, u'')  # delete     #
                            if r:                                                     # among
                                r = self.r_lengthen_V(s)  # routine call              #
                    if a_3 == 5:                                                      #
                        r = self.r_R1(s)  # routine call                              #
                        if r:                                                         #
                            r = self.r_C(s)  # routine call                           #
                            if r:                                                     #
                                r = s.set_range(self.left, self.right, u'aar')  # <-  #
                    if a_3 == 6:                                                      #
                        r = self.r_R2(s)  # routine call                              #
                        if r:                                                         #
                            r = s.set_range(self.left, self.right, u'')  # delete     #
                            if r:                                                     #
                                r = s.attach(u'f')  # attach                          #
                                if r:                                                 #
                                    r = self.r_lengthen_V(s)  # routine call          #
                    if a_3 == 7:                                                      #
                        r = self.r_R2(s)  # routine call                              #
                        if r:                                                         #
                            r = s.set_range(self.left, self.right, u'')  # delete     #
                            if r:                                                     #
                                r = s.attach(u'g')  # attach                          #
                                if r:                                                 #
                                    r = self.r_lengthen_V(s)  # routine call          #
                    if a_3 == 8:                                                      #
                        r = self.r_R1(s)  # routine call                              #
                        if r:                                                         #
                            r = self.r_C(s)  # routine call                           #
                            if r:                                                     #
                                r = s.set_range(self.left, self.right, u't')  # <-    #
                    if a_3 == 9:                                                      #
                        r = self.r_R1(s)  # routine call                              #
                        if r:                                                         #
                            r = self.r_C(s)  # routine call                           #
                            if r:                                                     #
                                r = s.set_range(self.left, self.right, u'd')  # <-    ##
        return r
    
    def r_Step_4(self, s):
        r = True
        var54 = len(s) - s.cursor                                                                   ##
        self.left = s.cursor  ##                                                                    #
        r = True              ## [                                                                  #
        if r:                                                                                       #
            a_4 = None                                                                 ##           #
            r = False                                                                  #            #
            var45 = s.cursor                                                           #            #
            for var44, var48, var47 in _a_4:                                           #            #
                if s.starts_with(var44):                                               #            #
                    var46 = s.cursor                                                   #            #
                    r = (not var48) or getattr(self, var48)(s)                         #            #
                    if r:                                                              #            #
                      s.cursor = var46                                                 #            #
                      a_4 = var47                                                      #            #
                      break                                                            #            #
                s.cursor = var45                                                       #            #
            if r:                                                                      #            #
                self.right = s.cursor  ##                                              #            #
                r = True               ## ]                                            #            #
                if r:                                                                  #            #
                    if a_4 == 0:                                                       #            #
                        r = self.r_R1(s)  # routine call                               #            #
                        if r:                                                          #            #
                            r = s.set_range(self.left, self.right, u'ie')  # <-        #            #
                    if a_4 == 1:                                                       #            #
                        r = self.r_R1(s)  # routine call                               #            #
                        if r:                                                          #            #
                            r = s.set_range(self.left, self.right, u'eer')  # <-       #            #
                    if a_4 == 2:                                                       #            #
                        r = self.r_R1(s)  # routine call                               #            #
                        if r:                                                          #            #
                            r = s.set_range(self.left, self.right, u'')  # delete      #            #
                    if a_4 == 3:                                                       #            #
                        r = self.r_R1(s)  # routine call                               #            #
                        if r:                                                          #            #
                            r = self.r_V(s)  # routine call                            #            #
                            if r:                                                      #            #
                                r = s.set_range(self.left, self.right, u'n')  # <-     # among      #
                    if a_4 == 4:                                                       #            #
                        r = self.r_R1(s)  # routine call                               #            #
                        if r:                                                          #            #
                            r = self.r_V(s)  # routine call                            #            #
                            if r:                                                      #            #
                                r = s.set_range(self.left, self.right, u'l')  # <-     #            #
                    if a_4 == 5:                                                       #            #
                        r = self.r_R1(s)  # routine call                               #            #
                        if r:                                                          #            #
                            r = self.r_V(s)  # routine call                            #            #
                            if r:                                                      #            #
                                r = s.set_range(self.left, self.right, u'r')  # <-     #            # or
                    if a_4 == 6:                                                       #            #
                        r = self.r_R1(s)  # routine call                               #            #
                        if r:                                                          #            #
                            r = s.set_range(self.left, self.right, u'teer')  # <-      #            #
                    if a_4 == 7:                                                       #            #
                        r = self.r_R1(s)  # routine call                               #            #
                        if r:                                                          #            #
                            r = s.set_range(self.left, self.right, u'lijk')  # <-      #            #
                    if a_4 == 8:                                                       #            #
                        r = self.r_R1(s)  # routine call                               #            #
                        if r:                                                          #            #
                            r = s.set_range(self.left, self.right, u'')  # delete      #            #
                    if a_4 == 9:                                                       #            #
                        r = self.r_R1(s)  # routine call                               #            #
                        if r:                                                          #            #
                            r = self.r_C(s)  # routine call                            #            #
                            if r:                                                      #            #
                                r = s.set_range(self.left, self.right, u'')  # delete  #            #
                                if r:                                                  #            #
                                    r = self.r_lengthen_V(s)  # routine call           ##           #
        if not r:                                                                                   #
            s.cursor = len(s) - var54                                                               #
            self.left = s.cursor  ##                                                                #
            r = True              ## [                                                              #
            if r:                                                                                   #
                a_5 = None                                                                 ##       #
                r = False                                                                  #        #
                var50 = s.cursor                                                           #        #
                for var49, var53, var52 in _a_5:                                           #        #
                    if s.starts_with(var49):                                               #        #
                        var51 = s.cursor                                                   #        #
                        r = (not var53) or getattr(self, var53)(s)                         #        #
                        if r:                                                              #        #
                          s.cursor = var51                                                 #        #
                          a_5 = var52                                                      #        #
                          break                                                            #        #
                    s.cursor = var50                                                       #        #
                if r:                                                                      # among  #
                    self.right = s.cursor  ##                                              #        #
                    r = True               ## ]                                            #        #
                    if r:                                                                  #        #
                        if a_5 == 0:                                                       #        #
                            r = self.r_R1(s)  # routine call                               #        #
                            if r:                                                          #        #
                                r = self.r_C(s)  # routine call                            #        #
                                if r:                                                      #        #
                                    r = s.set_range(self.left, self.right, u'')  # delete  #        #
                                    if r:                                                  #        #
                                        r = self.r_lengthen_V(s)  # routine call           ##       ##
        return r
    
    def r_Step_7(self, s):
        r = True
        self.left = s.cursor  ##
        r = True              ## [
        if r:
            a_6 = None                                                      ##
            r = False                                                       #
            var56 = s.cursor                                                #
            for var55, var59, var58 in _a_6:                                #
                if s.starts_with(var55):                                    #
                    var57 = s.cursor                                        #
                    r = (not var59) or getattr(self, var59)(s)              #
                    if r:                                                   #
                      s.cursor = var57                                      #
                      a_6 = var58                                           #
                      break                                                 #
                s.cursor = var56                                            # among
            if r:                                                           #
                self.right = s.cursor  ##                                   #
                r = True               ## ]                                 #
                if r:                                                       #
                    if a_6 == 0:                                            #
                        r = s.set_range(self.left, self.right, u'k')  # <-  #
                    if a_6 == 1:                                            #
                        r = s.set_range(self.left, self.right, u'f')  # <-  #
                    if a_6 == 2:                                            #
                        r = s.set_range(self.left, self.right, u'p')  # <-  ##
        return r
    
    def r_Step_6(self, s):
        r = True
        self.left = s.cursor  ##
        r = True              ## [
        if r:
            a_7 = None                                                      ##
            r = False                                                       #
            var61 = s.cursor                                                #
            for var60, var64, var63 in _a_7:                                #
                if s.starts_with(var60):                                    #
                    var62 = s.cursor                                        #
                    r = (not var64) or getattr(self, var64)(s)              #
                    if r:                                                   #
                      s.cursor = var62                                      #
                      a_7 = var63                                           #
                      break                                                 #
                s.cursor = var61                                            #
            if r:                                                           #
                self.right = s.cursor  ##                                   #
                r = True               ## ]                                 #
                if r:                                                       #
                    if a_7 == 0:                                            #
                        r = s.set_range(self.left, self.right, u'b')  # <-  #
                    if a_7 == 1:                                            #
                        r = s.set_range(self.left, self.right, u'c')  # <-  #
                    if a_7 == 2:                                            #
                        r = s.set_range(self.left, self.right, u'd')  # <-  #
                    if a_7 == 3:                                            #
                        r = s.set_range(self.left, self.right, u'f')  # <-  #
                    if a_7 == 4:                                            #
                        r = s.set_range(self.left, self.right, u'g')  # <-  #
                    if a_7 == 5:                                            #
                        r = s.set_range(self.left, self.right, u'h')  # <-  #
                    if a_7 == 6:                                            #
                        r = s.set_range(self.left, self.right, u'j')  # <-  #
                    if a_7 == 7:                                            # among
                        r = s.set_range(self.left, self.right, u'k')  # <-  #
                    if a_7 == 8:                                            #
                        r = s.set_range(self.left, self.right, u'l')  # <-  #
                    if a_7 == 9:                                            #
                        r = s.set_range(self.left, self.right, u'm')  # <-  #
                    if a_7 == 10:                                           #
                        r = s.set_range(self.left, self.right, u'n')  # <-  #
                    if a_7 == 11:                                           #
                        r = s.set_range(self.left, self.right, u'p')  # <-  #
                    if a_7 == 12:                                           #
                        r = s.set_range(self.left, self.right, u'q')  # <-  #
                    if a_7 == 13:                                           #
                        r = s.set_range(self.left, self.right, u'r')  # <-  #
                    if a_7 == 14:                                           #
                        r = s.set_range(self.left, self.right, u's')  # <-  #
                    if a_7 == 15:                                           #
                        r = s.set_range(self.left, self.right, u't')  # <-  #
                    if a_7 == 16:                                           #
                        r = s.set_range(self.left, self.right, u'v')  # <-  #
                    if a_7 == 17:                                           #
                        r = s.set_range(self.left, self.right, u'w')  # <-  #
                    if a_7 == 18:                                           #
                        r = s.set_range(self.left, self.right, u'x')  # <-  #
                    if a_7 == 19:                                           #
                        r = s.set_range(self.left, self.right, u'z')  # <-  #
                    if a_7 == 20:                                           #
                        r = s.set_range(self.left, self.right, u'f')  # <-  #
                    if a_7 == 21:                                           #
                        r = s.set_range(self.left, self.right, u's')  # <-  ##
        return r
    
    def r_Step_1c(self, s):
        r = True
        self.left = s.cursor  ##
        r = True              ## [
        if r:
            a_8 = None                                                             ##
            r = False                                                              #
            var66 = s.cursor                                                       #
            for var65, var69, var68 in _a_8:                                       #
                if s.starts_with(var65):                                           #
                    var67 = s.cursor                                               #
                    r = (not var69) or getattr(self, var69)(s)                     #
                    if r:                                                          #
                      s.cursor = var67                                             #
                      a_8 = var68                                                  #
                      break                                                        #
                s.cursor = var66                                                   #
            if r:                                                                  #
                self.right = s.cursor  ##                                          #
                r = True               ## ]                                        #
                if r:                                                              #
                    r = self.r_R1(s)  # routine call                               #
                    if r:                                                          #
                        r = self.r_C(s)  # routine call                            #
                if r:                                                              #
                    if a_8 == 0:                                                   # among
                        var70 = len(s) - s.cursor                   ##             #
                        r = s.starts_with(u'n')  # character check  #              #
                        if r:                                       #              #
                            r = self.r_R1(s)  # routine call        # not          #
                        if not r:                                   #              #
                            s.cursor = len(s) - var70               #              #
                        r = not r                                   ##             #
                        if r:                                                      #
                            r = s.set_range(self.left, self.right, u'')  # delete  #
                    if a_8 == 1:                                                   #
                        var71 = len(s) - s.cursor                   ##             #
                        r = s.starts_with(u'h')  # character check  #              #
                        if r:                                       #              #
                            r = self.r_R1(s)  # routine call        # not          #
                        if not r:                                   #              #
                            s.cursor = len(s) - var71               #              #
                        r = not r                                   ##             #
                        if r:                                                      #
                            r = s.set_range(self.left, self.right, u'')  # delete  ##
        return r
    
    def r_Lose_prefix(self, s):
        r = True
        self.left = s.cursor  ##
        r = True              ## [
        if r:
            r = s.starts_with(u'ge')  # character check
            if r:
                self.right = s.cursor  ##
                r = True               ## ]
                if r:
                    var72 = s.cursor     ##
                    r = s.hop(3)  # hop  # test
                    s.cursor = var72     ##
                    if r:
                        while True:                                              ##
                            var73 = s.cursor                                     #
                            if s.cursor == s.limit:            ##                #
                                r = False                      #                 #
                            else:                              #                 #
                                r = s.chars[s.cursor] in _g_v  # grouping check  #
                            if r:                              #                 # goto
                                s.cursor += 1                  ##                #
                            if r or s.cursor == s.limit:                         #
                                s.cursor = var73                                 #
                                break                                            #
                            s.cursor = var73 + 1                                 ##
                        if r:
                            while True:                                                           ##
                                var74 = s.cursor                                                  #
                                if s.cursor == s.limit:                ##                         #
                                    r = False                          #                          #
                                else:                                  #                          #
                                    r = s.chars[s.cursor] not in _g_v  # negative grouping check  #
                                if r:                                  #                          # goto
                                    s.cursor += 1                      ##                         #
                                if r or s.cursor == s.limit:                                      #
                                    s.cursor = var74                                              #
                                    break                                                         #
                                s.cursor = var74 + 1                                              ##
                        if r:
                            self.b_GE_removed = True  ##
                            r = True                  ## set
                            if r:
                                r = s.set_range(self.left, self.right, u'')  # delete
        return r
    
    def r_Lose_infix(self, s):
        r = True
        r = s.hop(1)  # next
        if r:
            while True:                                          ##
                self.left = s.cursor  ##                         #
                r = True              ## [                       #
                if r:                                            #
                    r = s.starts_with(u'ge')  # character check  #
                    if r:                                        # gopast
                        self.right = s.cursor  ##                #
                        r = True               ## ]              #
                if r or s.cursor == s.limit:                     #
                    break                                        #
                s.cursor += 1                                    ##
            if r:
                var75 = s.cursor     ##
                r = s.hop(3)  # hop  # test
                s.cursor = var75     ##
                if r:
                    while True:                                              ##
                        var76 = s.cursor                                     #
                        if s.cursor == s.limit:            ##                #
                            r = False                      #                 #
                        else:                              #                 #
                            r = s.chars[s.cursor] in _g_v  # grouping check  #
                        if r:                              #                 # goto
                            s.cursor += 1                  ##                #
                        if r or s.cursor == s.limit:                         #
                            s.cursor = var76                                 #
                            break                                            #
                        s.cursor = var76 + 1                                 ##
                    if r:
                        while True:                                                           ##
                            var77 = s.cursor                                                  #
                            if s.cursor == s.limit:                ##                         #
                                r = False                          #                          #
                            else:                                  #                          #
                                r = s.chars[s.cursor] not in _g_v  # negative grouping check  #
                            if r:                                  #                          # goto
                                s.cursor += 1                      ##                         #
                            if r or s.cursor == s.limit:                                      #
                                s.cursor = var77                                              #
                                break                                                         #
                            s.cursor = var77 + 1                                              ##
                    if r:
                        self.b_GE_removed = True  ##
                        r = True                  ## set
                        if r:
                            r = s.set_range(self.left, self.right, u'')  # delete
        return r
    
    def r_measure(self, s):
        r = True
        var78 = s.cursor                          ##
        s.cursor = s.limit  ##                    #
        r = True            ## tolimit            #
        if r:                                     #
            self.i_p1 = s.cursor  ##              #
            r = True              ## setmark      # do
            if r:                                 #
                self.i_p2 = s.cursor  ##          #
                r = True              ## setmark  #
        s.cursor = var78                          #
        r = True                                  ##
        if r:
            var85 = s.cursor                                                                                      ##
            while True:                                                           ##                              #
                var79 = s.cursor                                                  #                               #
                if s.cursor == s.limit:                ##                         #                               #
                    r = False                          #                          #                               #
                else:                                  #                          #                               #
                    r = s.chars[s.cursor] not in _g_v  # negative grouping check  #                               #
                if r:                                  #                          # repeat                        #
                    s.cursor += 1                      ##                         #                               #
                if not r:                                                         #                               #
                    s.cursor = var79                                              #                               #
                    break                                                         #                               #
            r = True                                                              ##                              #
            if r:                                                                                                 #
                for var81 in xrange(1):                                                ##                         #
                    var80 = s.cursor                                         ##        #                          #
                    r = s.starts_with(u'ij')  # character check              #         #                          #
                    if not r:                                                #         #                          #
                        s.cursor = var80                                     #         #                          #
                        if s.cursor == s.limit:            ##                #         #                          #
                            r = False                      #                 # or      #                          #
                        else:                              #                 #         #                          #
                            r = s.chars[s.cursor] in _g_v  # grouping check  #         #                          #
                        if r:                              #                 #         #                          #
                            s.cursor += 1                  ##                ##        #                          #
                    if not r:                                                          #                          #
                        break                                                          #                          #
                if r:                                                                  #                          #
                    while True:                                                        #                          #
                        var81 = s.cursor                                               # atleast                  #
                        var80 = s.cursor                                         ##    #                          #
                        r = s.starts_with(u'ij')  # character check              #     #                          #
                        if not r:                                                #     #                          #
                            s.cursor = var80                                     #     #                          #
                            if s.cursor == s.limit:            ##                #     #                          #
                                r = False                      #                 # or  #                          #
                            else:                              #                 #     #                          #
                                r = s.chars[s.cursor] in _g_v  # grouping check  #     #                          #
                            if r:                              #                 #     #                          #
                                s.cursor += 1                  ##                ##    #                          #
                        if not r:                                                      #                          #
                            s.cursor = var81                                           #                          #
                            break                                                      #                          #
                    r = True                                                           ##                         #
                if r:                                                                                             #
                    if s.cursor == s.limit:                ##                                                     #
                        r = False                          #                                                      #
                    else:                                  #                                                      #
                        r = s.chars[s.cursor] not in _g_v  # negative grouping check                              #
                    if r:                                  #                                                      #
                        s.cursor += 1                      ##                                                     #
                    if r:                                                                                         #
                        self.i_p1 = s.cursor  ##                                                                  #
                        r = True              ## setmark                                                          #
                        if r:                                                                                     #
                            while True:                                                           ##              # do
                                var82 = s.cursor                                                  #               #
                                if s.cursor == s.limit:                ##                         #               #
                                    r = False                          #                          #               #
                                else:                                  #                          #               #
                                    r = s.chars[s.cursor] not in _g_v  # negative grouping check  #               #
                                if r:                                  #                          # repeat        #
                                    s.cursor += 1                      ##                         #               #
                                if not r:                                                         #               #
                                    s.cursor = var82                                              #               #
                                    break                                                         #               #
                            r = True                                                              ##              #
                            if r:                                                                                 #
                                for var84 in xrange(1):                                                ##         #
                                    var83 = s.cursor                                         ##        #          #
                                    r = s.starts_with(u'ij')  # character check              #         #          #
                                    if not r:                                                #         #          #
                                        s.cursor = var83                                     #         #          #
                                        if s.cursor == s.limit:            ##                #         #          #
                                            r = False                      #                 # or      #          #
                                        else:                              #                 #         #          #
                                            r = s.chars[s.cursor] in _g_v  # grouping check  #         #          #
                                        if r:                              #                 #         #          #
                                            s.cursor += 1                  ##                ##        #          #
                                    if not r:                                                          #          #
                                        break                                                          #          #
                                if r:                                                                  #          #
                                    while True:                                                        #          #
                                        var84 = s.cursor                                               # atleast  #
                                        var83 = s.cursor                                         ##    #          #
                                        r = s.starts_with(u'ij')  # character check              #     #          #
                                        if not r:                                                #     #          #
                                            s.cursor = var83                                     #     #          #
                                            if s.cursor == s.limit:            ##                #     #          #
                                                r = False                      #                 # or  #          #
                                            else:                              #                 #     #          #
                                                r = s.chars[s.cursor] in _g_v  # grouping check  #     #          #
                                            if r:                              #                 #     #          #
                                                s.cursor += 1                  ##                ##    #          #
                                        if not r:                                                      #          #
                                            s.cursor = var84                                           #          #
                                            break                                                      #          #
                                    r = True                                                           ##         #
                                if r:                                                                             #
                                    if s.cursor == s.limit:                ##                                     #
                                        r = False                          #                                      #
                                    else:                                  #                                      #
                                        r = s.chars[s.cursor] not in _g_v  # negative grouping check              #
                                    if r:                                  #                                      #
                                        s.cursor += 1                      ##                                     #
                                    if r:                                                                         #
                                        self.i_p2 = s.cursor  ##                                                  #
                                        r = True              ## setmark                                          #
            s.cursor = var85                                                                                      #
            r = True                                                                                              ##
        return r
    
    def r_stem(self, s):
        r = True
        self.b_Y_found = False  ##
        r = True                ## unset
        if r:
            self.b_stemmed = False  ##
            r = True                ## unset
            if r:
                var86 = s.cursor                                                ##
                self.left = s.cursor  ##                                        #
                r = True              ## [                                      #
                if r:                                                           #
                    r = s.starts_with(u'y')  # character check                  #
                    if r:                                                       #
                        self.right = s.cursor  ##                               #
                        r = True               ## ]                             # do
                        if r:                                                   #
                            r = s.set_range(self.left, self.right, u'Y')  # <-  #
                            if r:                                               #
                                self.b_Y_found = True  ##                       #
                                r = True               ## set                   #
                s.cursor = var86                                                #
                r = True                                                        ##
                if r:
                    var89 = s.cursor                                                               ##
                    while True:                                                          ##        #
                        var88 = s.cursor                                                 #         #
                        while True:                                              ##      #         #
                            var87 = s.cursor                                     #       #         #
                            if s.cursor == s.limit:            ##                #       #         #
                                r = False                      #                 #       #         #
                            else:                              #                 #       #         #
                                r = s.chars[s.cursor] in _g_v  # grouping check  #       #         #
                            if r:                              #                 #       #         #
                                s.cursor += 1                  ##                #       #         #
                            if r:                                                #       #         #
                                self.left = s.cursor  ##                         #       #         #
                                r = True              ## [                       # goto  #         #
                                if r:                                            #       #         #
                                    r = s.starts_with(u'y')  # character check   #       #         #
                                    if r:                                        #       # repeat  #
                                        self.right = s.cursor  ##                #       #         # do
                                        r = True               ## ]              #       #         #
                            if r or s.cursor == s.limit:                         #       #         #
                                s.cursor = var87                                 #       #         #
                                break                                            #       #         #
                            s.cursor = var87 + 1                                 ##      #         #
                        if r:                                                            #         #
                            r = s.set_range(self.left, self.right, u'Y')  # <-           #         #
                            if r:                                                        #         #
                                self.b_Y_found = True  ##                                #         #
                                r = True               ## set                            #         #
                        if not r:                                                        #         #
                            s.cursor = var88                                             #         #
                            break                                                        #         #
                    r = True                                                             ##        #
                    s.cursor = var89                                                               #
                    r = True                                                                       ##
                    if r:
                        r = self.r_measure(s)  # routine call
                        if r:
                            var94 = s.cursor                                        ##
                            var95 = len(s) - s.limit                                #
                            s.direction *= -1                                       #
                            s.cursor, s.limit = s.limit, s.cursor                   #
                            var90 = len(s) - s.cursor             ##                #
                            r = self.r_Step_1(s)  # routine call  #                 #
                            if r:                                 #                 #
                                self.b_stemmed = True  ##         # do              #
                                r = True               ## set     #                 #
                            s.cursor = len(s) - var90             #                 #
                            r = True                              ##                #
                            if r:                                                   #
                                var91 = len(s) - s.cursor             ##            #
                                r = self.r_Step_2(s)  # routine call  #             #
                                if r:                                 #             #
                                    self.b_stemmed = True  ##         # do          #
                                    r = True               ## set     #             #
                                s.cursor = len(s) - var91             #             #
                                r = True                              ##            #
                                if r:                                               # backwards
                                    var92 = len(s) - s.cursor             ##        #
                                    r = self.r_Step_3(s)  # routine call  #         #
                                    if r:                                 #         #
                                        self.b_stemmed = True  ##         # do      #
                                        r = True               ## set     #         #
                                    s.cursor = len(s) - var92             #         #
                                    r = True                              ##        #
                                    if r:                                           #
                                        var93 = len(s) - s.cursor             ##    #
                                        r = self.r_Step_4(s)  # routine call  #     #
                                        if r:                                 #     #
                                            self.b_stemmed = True  ##         # do  #
                                            r = True               ## set     #     #
                                        s.cursor = len(s) - var93             #     #
                                        r = True                              ##    #
                            s.direction *= -1                                       #
                            s.cursor = var94                                        #
                            s.limit = len(s) - var95                                ##
                            if r:
                                self.b_GE_removed = False  ##
                                r = True                   ## unset
                                if r:
                                    var97 = s.cursor                                  ##
                                    var96 = s.cursor                           ##     #
                                    r = self.r_Lose_prefix(s)  # routine call  #      #
                                    if r:                                      # and  #
                                        s.cursor = var96                       #      # do
                                        r = self.r_measure(s)  # routine call  ##     #
                                    s.cursor = var97                                  #
                                    r = True                                          ##
                                    if r:
                                        var99 = s.cursor                                       ##
                                        var100 = len(s) - s.limit                              #
                                        s.direction *= -1                                      #
                                        s.cursor, s.limit = s.limit, s.cursor                  #
                                        var98 = len(s) - s.cursor                        ##    #
                                        r = self.b_GE_removed  # boolean variable check  #     #
                                        if r:                                            #     # backwards
                                            r = self.r_Step_1c(s)  # routine call        # do  #
                                        s.cursor = len(s) - var98                        #     #
                                        r = True                                         ##    #
                                        s.direction *= -1                                      #
                                        s.cursor = var99                                       #
                                        s.limit = len(s) - var100                              ##
                                        if r:
                                            self.b_GE_removed = False  ##
                                            r = True                   ## unset
                                            if r:
                                                var102 = s.cursor                                 ##
                                                var101 = s.cursor                          ##     #
                                                r = self.r_Lose_infix(s)  # routine call   #      #
                                                if r:                                      # and  #
                                                    s.cursor = var101                      #      # do
                                                    r = self.r_measure(s)  # routine call  ##     #
                                                s.cursor = var102                                 #
                                                r = True                                          ##
                                                if r:
                                                    var104 = s.cursor                                      ##
                                                    var105 = len(s) - s.limit                              #
                                                    s.direction *= -1                                      #
                                                    s.cursor, s.limit = s.limit, s.cursor                  #
                                                    var103 = len(s) - s.cursor                       ##    #
                                                    r = self.b_GE_removed  # boolean variable check  #     #
                                                    if r:                                            #     # backwards
                                                        r = self.r_Step_1c(s)  # routine call        # do  #
                                                    s.cursor = len(s) - var103                       #     #
                                                    r = True                                         ##    #
                                                    s.direction *= -1                                      #
                                                    s.cursor = var104                                      #
                                                    s.limit = len(s) - var105                              ##
                                                    if r:
                                                        var109 = s.cursor                                                    ##
                                                        var110 = len(s) - s.limit                                            #
                                                        s.direction *= -1                                                    #
                                                        s.cursor, s.limit = s.limit, s.cursor                                #
                                                        var106 = len(s) - s.cursor            ##                             #
                                                        r = self.r_Step_7(s)  # routine call  #                              #
                                                        if r:                                 #                              #
                                                            self.b_stemmed = True  ##         # do                           #
                                                            r = True               ## set     #                              #
                                                        s.cursor = len(s) - var106            #                              #
                                                        r = True                              ##                             #
                                                        if r:                                                                #
                                                            var108 = len(s) - s.cursor                                 ##    # backwards
                                                            var107 = len(s) - s.cursor                           ##    #     #
                                                            r = self.b_stemmed  # boolean variable check         #     #     #
                                                            if not r:                                            # or  #     #
                                                                s.cursor = len(s) - var107                       #     #     #
                                                                r = self.b_GE_removed  # boolean variable check  ##    # do  #
                                                            if r:                                                      #     #
                                                                r = self.r_Step_6(s)  # routine call                   #     #
                                                            s.cursor = len(s) - var108                                 #     #
                                                            r = True                                                   ##    #
                                                        s.direction *= -1                                                    #
                                                        s.cursor = var109                                                    #
                                                        s.limit = len(s) - var110                                            ##
                                                        if r:
                                                            var113 = s.cursor                                                             ##
                                                            r = self.b_Y_found  # boolean variable check                                  #
                                                            if r:                                                                         #
                                                                while True:                                                     ##        #
                                                                    var112 = s.cursor                                           #         #
                                                                    while True:                                         ##      #         #
                                                                        var111 = s.cursor                               #       #         #
                                                                        self.left = s.cursor  ##                        #       #         #
                                                                        r = True              ## [                      #       #         #
                                                                        if r:                                           #       #         #
                                                                            r = s.starts_with(u'Y')  # character check  #       #         #
                                                                            if r:                                       # goto  #         #
                                                                                self.right = s.cursor  ##               #       #         #
                                                                                r = True               ## ]             #       # repeat  # do
                                                                        if r or s.cursor == s.limit:                    #       #         #
                                                                            s.cursor = var111                           #       #         #
                                                                            break                                       #       #         #
                                                                        s.cursor = var111 + 1                           ##      #         #
                                                                    if r:                                                       #         #
                                                                        r = s.set_range(self.left, self.right, u'y')  # <-      #         #
                                                                    if not r:                                                   #         #
                                                                        s.cursor = var112                                       #         #
                                                                        break                                                   #         #
                                                                r = True                                                        ##        #
                                                            s.cursor = var113                                                             #
                                                            r = True                                                                      ##
        return r
