class Solution {
public:
    int getSecondLargest(const std::vector<int>& arr) {
        int first = INT_MIN, second = INT_MIN;

        for (int num : arr) {
            if (num > first) {
                second = first;
                first = num;
            } else if (num > second && num < first) {
                second = num;
            }
        }
        
        return second == INT_MIN ? -1 : second;
    }
};
