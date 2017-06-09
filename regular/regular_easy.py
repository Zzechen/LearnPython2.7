import re

a = 'adfbg'
if re.match('a.',a):
    print ". match any true"
else:
    print ". match any false"

a = 'dfhhfdhd'
if re.match('\d{*}',a):
    print '* match all true'
else:
    print '* match all false'

a = '010'
if re.match('\d\d\d',a):
    print "\d match number true"
else:
    print "\d match number false"

a='a'
if re.match('\w',a):
    print '\w match letter true'
else:
    print '\w match letter false'

# \s to match a space
# {} to hint the number like {n,m}-->[n,m) or {n} --> n
a = '010 12345'
# a = '010 1234'
if re.match('\d{3}\s+\d{3,8}',a):
    print 'tel match true'
else:
    print 'tel match false'

a = '^\d'
# match a string begin with number
if re.match(a,'dd'):
    print True
else:
    print False
