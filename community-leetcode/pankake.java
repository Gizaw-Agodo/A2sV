class Solution {
    public List<Integer> pancakeSort(int[] A) {
        List<Integer> res = new ArrayList<>();
        int curr = A.length;
        while (curr > 0) {
            int ind = indexOf(curr, A);
            if (ind < curr - 1) {
                // put curr at index 0
                flip(ind + 1, A);
                res.add(ind + 1);
                // put curr at index curr - 1
                flip(curr, A);
                res.add(curr);
            }
            curr--;
        }
        return res;
    }
    
    public static int indexOf(int v, int[] A) {
        for (int i = 0; i < A.length; i++) {
            if (A[i] == v) {
                return i;
            }
        }
        return -1;
    }
    
    public static void flip(int k, int[] A) {
        int p = 0;
        while (k - 1 - p > p) {
            swap(p, k - 1 - p, A);
            p++;
        }
    }
    
    public static void swap(int a, int b, int[] A) {
        int x = A[a];
        A[a] = A[b];
        A[b] = x;
    }
}
