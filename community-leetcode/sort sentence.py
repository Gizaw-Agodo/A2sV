class Solution:
  def sortSentence(self, s: str) -> str:
    p = [(w[:-1], int(w[-1])) for w in s.split()]
    p.sort(key=lambda x : x[1])
    return " ".join((w for w, _ in p))
