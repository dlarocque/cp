class Solution {
public:
    int maxArea(vector<int>& height) {
        int water = 0;
        int l = 0;
        int r = height.size() - 1;
        
        while(l < r) {
            int h = min(height[l], height[r]);
            water = max(water, (r - l) * h);
            
            // iterate over the smaller of the two containers
            // since we can't find a larger area unless the smaller of
            // the two containers can be replaced by the other containers
            // 
            // If we find a container that is larger than the smaller one, we 
            // then continue the same process on the other side.
            //
            // This solutions optimality comes from skipping over all of the 
            // containers that can not result in a larger area
            while (height[l] <= h && l < r) l++;
            while (height[r] <= h && l < r) r--;
        }
        
        return water;
    
