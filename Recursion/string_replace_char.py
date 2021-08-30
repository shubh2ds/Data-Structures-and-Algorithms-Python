def replace_char(s,a,b):
  if len(s)==0:
    return s
  if s[0]==a:
    return b+replace_char(s[1:],a,b)
  else:
    return s[0]+replace_char(s[1:],a,b)
   

s="shubhan"
a="n"
b="m"
replace_char(s,a,b)
