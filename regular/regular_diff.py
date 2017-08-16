import re
a = '[0-9a-zA-Z\_]'
# match a number/letter/_   such as  re.match(a,'a')==False,re.match(a,'0')==True,re.match(a,'_')==True
if re.match(a,'a'):
    print True
else:
    print False

a = '[0-9a-zA-Z\_]+'
#match at least a learn_string include a number/letter/_  such as re.match(a,'a100') et..
if re.match(a,'_'):
    print True
else:
    print False

a='[a-zA-Z\_][0-9a-zA-Z\_]*'
#match a learn_string that begin with a letter/_ and behind with any number/letters/_    this is Python legal field
if re.match(a,'_init'):
    print True
else:
    print False

a='[a-zA-Z\_][0-9a-zA-Z\_]{0,5}'
#match a learn_string that length is [1,20]--(1+19)
if re.match(a,'sddfasdhfhdghjfsdaggjdfdda'):
    print True
else:
    print False