public class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> nums = new Stack<Integer>();
        for (int i = 0; i < tokens.length; i ++) {
            String op = tokens[i];
            if (op.equals("+")) {
                nums.push(nums.pop() + nums.pop());
                continue;
            }
            if (op.equals("-")) {
                int num = nums.pop();
                nums.push(nums.pop() - num);
                continue;
            }
            if (op.equals("*")) {
                nums.push(nums.pop() * nums.pop());
                continue;
            }
            if (op.equals("/")) {
                int num = nums.pop();
                nums.push(nums.pop() / num);
                continue;
            }
            nums.push(Integer.parseInt(op));
        }
        return nums.pop();
    }
}
