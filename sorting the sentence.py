class solution(object):
  def sortsentence(self ,s):
    s = s.split()
    n= len(s)
    r= [node]*n
    for i in range(n):
      word = s[i]
      r[int(word[-1]-1)] =word[:-1]
   return ''.join(r)
