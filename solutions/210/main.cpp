class Solution {
private: 
    vector<vector<int>> edges; 
    vector<int> indeg; 
    vector<int> result; 
public: 
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        edges.resize(numCourses); 
        indeg.resize(numCourses); 

        for (const auto& info: prerequisites) {
            edges[info[1]].push_back(info[0]);
            indeg[info[0]]++;
        }

        // can also use stack<int> q, not compulsory to use a queue 
        queue<int> q; 
        for (int i = 0; i < numCourses; i++) {
            if (indeg[i] == 0) q.push(i);
        }

        while (!q.empty()) {
            int u = q.front(); 
            q.pop(); 
            result.push_back(u);
            for (int v: edges[u]) {
                --indeg[v];
                if (indeg[v] == 0) q.push(v); 
            }
        }

        if (result.size() == numCourses) return result; 
        else return {}; 
    }
};