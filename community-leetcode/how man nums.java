#include <bits/stdc++.h>
using namespace std;
vector<int> smallerNumbersThanCurrent(vector<int>& nums) 
{
    int count[101];
    memset(count,0,sizeof(count));
    for(auto& i:nums)
    {
        count[i]++;
    }
    for(int i=1;i<=100;i++)
    {
        count[i]=count[i-1]+count[i];
    }
    vector<int> ans;
    for(int i=0;i<nums.size();i++)
    {
        if(nums[i]==0)    ans.push_back(0);
        else    ans.push_back(count[nums[i]-1]);
    }
    return ans;
}
int main() 
{
    vector<int> nums{ 8 , 1, 2 , 2 , 3 }; 
    vector<int> ans=smallerNumbersThanCurrent(nums);
    
    for(auto val:ans) cout<<val<<" ";
    cout<<endl;
    
    return 0;  
}
