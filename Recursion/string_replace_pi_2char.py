def replace_pi(s):
  if len(s)==0 or len(s)==1:
    return s
  if s[0:2]=="pi":
    return "3.7"+replace_pi(s[2:])
  else:
    return s[0]+replace_pi(s[1:])
s="shubhpishubhpi"
replace_pi(s)
