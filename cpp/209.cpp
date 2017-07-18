#include <iostream>
#include <vector>
using namespace std;
class Solution {
    public:
    int minSubArrayLen(int s, vector<int>& nums){
        int n = nums.size();
        if (n == 0)
            return 0;
        int ans = INT_MAX;
        vector<int> sums(n + 1, 0);
        for (int i = 1; i <= n; i++)
            sums[i] = sums[i - 1] + nums[i - 1];
        for (int i = 1; i <= n; i++){
            int to_find = s + sums[i - 1];
            auto bound = lower_bound(sums.begin(), sums.end(), to_find);
            cout << bound - sums.begin() << endl;
            if (bound != sums.end()){
                ans = min(ans, static_cast<int>(bound - (sums.begin() + i - 1)));
            }
        }
        return (ans != INT_MAX) ? ans : 0;
    }
};

int main (){
	vector<int> nums{2,3,4,2,4,3};
	cout << Solution().minSubArrayLen(1, nums);
	return 0;
}
