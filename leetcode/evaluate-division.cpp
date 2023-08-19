#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<vector<string>> adj;
    unordered_map<string, unordered_map<string, float>> adj;
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        vector<double> results = vector<double>();
        // Create adjacency matrix
        adj = vector<vector<string>>(); // Do we have to do nested initialization?   
       
        // Traverse equations and fill in bidirectional graph 
        for (int i = 0; i < equations.size(); ++i) {
            string x = equations[i][0];
            string y = equations[i][1];
            double value = values[i]; 

            adj[x][y] = value;
            adj[y][x] = 1 / value; // Problem clarifies that divide by zero is not possible
        }

        // Resolve queries
        for (int i = 0; i < queries.size(); ++i) {
            // TODO: convert strings to floats
            string x = equations[i][0];
            string y = equations[i][1];
        
            // Graph traversal to evaluate query
            float result = evaluateQuery(x, y);
            results.push_back(result);
        } 

    }

    float evaluateQuery(float ) {
        
    }
}
