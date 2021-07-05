/*
// Definition for Employee.
class Employee {
public:
    int id;
    int importance;
    vector<int> subordinates;
};
*/

class Solution {
public:
    int getImportance(vector<Employee*> employees, int id) {
        // map all id's to respective employees
        int importance_sum = 0;
        unordered_map<int, Employee*> map;
        
        // map all the id's to employees so we have O(1) access given their ID
        for(auto employee : employees) {
            map[employee->id] = employee;
        }
        
        DFS(map, id, importance_sum);
        return importance_sum;
    }
    
    void DFS(unordered_map<int, Employee*>& map, int id, int& importance_sum) {
        importance_sum += map[id]->importance;
        
        for(auto employee : map[id]->subordinates) {
            DFS(map, employee, importance_sum);
        }
    }
    
};
