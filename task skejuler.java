class Solution {
    class Node implements Comparable<Node>{
        public char c;
        public int count;
        public Node (char c, int count) {
            this.c = c;
            this.count = count;
        }
        public int compareTo(Node n) {
            return n.count - this.count;
        }
    }
    public int leastInterval(char[] tasks, int n) {
        PriorityQueue<Node> q = new PriorityQueue<Node>();
        HashMap<Character, Integer> count = new HashMap<Character, Integer>();
        for (int i = 0; i < tasks.length; i ++) {
            char task = tasks[i];
            if (!count.containsKey(task)) {
                count.put(task, 0);
            }
            count.put(task, count.get(task) + 1);
        }
        for (Character c:count.keySet()) {
            q.add(new Node(c, count.get(c)));
        }
        int res = 0;
        while (!q.isEmpty()) {
            List<Node> add = new LinkedList<Node>();
            for (int i = 0; i < n + 1; i ++) {
                if (q.isEmpty() && add.isEmpty()) {
                    break;
                }
                if (!q.isEmpty()) {
                    Node node = q.poll();
                    node.count --;
                    if (node.count != 0) {
                        add.add(node);
                    }
                }
                res ++;
            }
            for (Node node:add) {
                q.add(node);
            }
        }
        return res;
    }
}
