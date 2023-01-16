public class Solution {
    public String largestNumber(int[] nums) {
        String[] snums = new String[nums.length];
        for (int i = 0; i < nums.length; i ++){
            snums[i] = "" + nums[i];
        } 
        Arrays.sort(snums, new Comparator<String>(){
            public int compare(String a, String b){
                String atob = a + b;
                String btoa = b + a;
                return btoa.compareTo(atob);
            }
        });
        String result = "";
        for (int i = 0; i < snums.length; i ++){ 
            result +=snums[i]; 
        } //remove front zeroes 
        while (result.length() > 1){
            if (result.charAt(0) == '0')
                result = result.substring(1);
            else
                break;
        }
        return result;
    }//largestNumber
}
