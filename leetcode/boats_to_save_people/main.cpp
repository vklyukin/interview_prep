#include <algorithm>

class Solution {
 public:
  int numRescueBoats(vector<int>& people, int limit) {
    vector<int> weight_counts(limit + 1, 0);

    for (auto weight : people) {
      ++weight_counts[weight];
    }

    int num_of_boats = 0;

    size_t left_index = 0;
    size_t right_index = limit;

    while (left_index <= right_index) {
      if (left_index + right_index <= limit) {
        auto num_of_boats_to_take =
            std::min(weight_counts[left_index], weight_counts[right_index]);

        if (left_index == right_index && num_of_boats_to_take > 1 &&
            left_index * 2 <= limit) {
          num_of_boats_to_take /= 2;
        }

        weight_counts[left_index] -= num_of_boats_to_take;

        if (weight_counts[right_index] != 0) {
          weight_counts[right_index] -= num_of_boats_to_take;
        }

        num_of_boats += num_of_boats_to_take;
      } else {
        auto num_of_boats_to_take = weight_counts[right_index];

        if (right_index <= limit / 2) {
          num_of_boats_to_take /= 2;
        }

        num_of_boats += weight_counts[right_index];

        weight_counts[right_index] = 0;
      }

      while (left_index <= limit && weight_counts[left_index] == 0) {
        ++left_index;
      }

      while (right_index > 0 && weight_counts[right_index] == 0) {
        --right_index;
      }
    }

    return num_of_boats;
  }
};
