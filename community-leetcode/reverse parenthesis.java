class Solution {
     public String reverseParentheses(String s) {
         StringBuilder sb = new StringBuilder();
         Stack<StringBuilder> stack = new Stack<>();
          stack.push(new StringBuilder());
         for (char c : s.toCharArray()) {
              if (c == '(') {
                 stack.push(new StringBuilder());
              } else if (c == ')') {
                 StringBuilder top = stack.pop();
                 stack.peek().append(top.reverse());
            } else {
                 stack.peek().append(c);
             }
         }
         return stack.pop().toString();
     }
 }
