import java.util.Arrays;

public class MostFrequentElement {
    public int maxFrequency(int[] nums, int k) {
        Arrays.sort(nums);
        long sum=0;
        int max=1, i=0, j;
        for(j=0;j<nums.length;++j){
            sum+=nums[j];
            while(sum+k<(long)nums[j]*(j-i+1)){
                sum-=nums[i];
                i++;
            }
            max=Math.max(max,j-i+1);
        }
        return max;
    }
}
