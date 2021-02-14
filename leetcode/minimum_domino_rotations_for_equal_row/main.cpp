class Solution {
public:
    int minDominoRotations(vector<int>& A, vector<int>& B) {
        unordered_map<int, int> a_counter;
        unordered_map<int, int> b_counter;
        
        for (const auto& element : A) {
            ++a_counter[element];
        }
        for (const auto& element : B) {
            ++b_counter[element];
        }
        
        int most_popular_value = -1;
        int most_popular_counts = 0;
        bool most_popular_from_a = true;
        for (const auto& [key, value] : a_counter) {
            if (value > most_popular_counts) {
                most_popular_counts = value;
                most_popular_value = key;
            }
        }
        
        for (const auto& [key, value] : b_counter) {
            if (value > most_popular_counts) {
                most_popular_counts = value;
                most_popular_value = key;
                most_popular_from_a = false;
            }
        }
        
        if (most_popular_counts * 2 < A.size()) {
            return -1;
        }
        
        vector<int>* main_row = nullptr;
        vector<int>* sub_row = nullptr;
        
        if (most_popular_from_a) {
            main_row = &A;
            sub_row = &B;
        } else {
            main_row = &B;
            sub_row = &A;
        }
        
        for (auto index = 0; index < main_row->size(); ++index) {
            if ((*main_row)[index] != most_popular_value
                && (*sub_row)[index] != most_popular_value) {
                return -1;
            }
        }
        
        return A.size() - most_popular_counts;
    }
};