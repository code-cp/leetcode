class Solution {
public: 
    int minOperationsMaxProfit(vector<int>& customers, int boardingCost, int runningCost) {
        auto calcProf = [boardingCost, runningCost](int i, int onboard) {
            return boardingCost * onboard - runningCost * i;  
        }; 

        int wait, onboard, max_profit, max_cycle; 
        wait = onboard = max_profit = max_cycle = 0; 
        int max_cap = 4; 

        // NOTE, i starts at 1, not at 0 
        for (std::size_t i = 1; i <= customers.size(); ++i) {
            int cur = customers[i-1]; 
            // update the people in queue 
            wait += cur;
            int people = min(max_cap, wait);  
            onboard += people; 
            wait -= people; 

            // update profit 
            int profit = calcProf(i, onboard); 
            if (profit > max_profit) {
                max_profit = profit; 
                max_cycle = i; 
            }
        }

        int j = customers.size(); 
        while (wait > 0) {
            int people = min(max_cap, wait); 
            onboard += people; 
            wait -= people; 

            j += 1; 
            int profit = calcProf(j, onboard); 
            if (profit > max_profit) {
                max_profit = profit; 
                max_cycle = j; 
            }
        }

        if (max_profit > 0) return max_cycle; else return -1; 
    }
};