#include <limits>

struct DijkstraNode {
  int index;
  int distance;
};

class Solution {
 public:
  vector<vector<int>> constructAdjacencyList(const vector<string>& bank) {
    vector<char> genoms = {'A', 'C', 'G', 'T'};

    vector<vector<int>> adj_list(bank.size());
    unordered_map<string, size_t> bank_items;

    for (size_t index = 0; index < bank.size(); ++index) {
      bank_items[bank[index]] = index;
    }

    for (size_t index = 0; index < bank.size(); ++index) {
      auto current_item = bank[index];

      for (size_t char_index = 0; char_index < current_item.length();
           ++char_index) {
        auto original_char = current_item[char_index];

        for (auto replacement : genoms) {
          if (replacement != original_char) {
            current_item[char_index] = replacement;

            if (bank_items.find(current_item) != bank_items.end()) {
              adj_list[index].push_back(bank_items[current_item]);
            }
          }
        }

        current_item[char_index] = original_char;
      }
    }

    return adj_list;
  }

  int calculateMinDistance(vector<vector<int>> adj_list, int start_index,
                           int end_index) {
    vector<bool> visited(adj_list.size());

    vector<int> distances(adj_list.size(), std::numeric_limits<int>::max());
    distances[start_index] = 0;

    auto comparator = [](const DijkstraNode& lhs, const DijkstraNode& rhs) {
      return lhs.distance < rhs.distance;
    };
    std::priority_queue<DijkstraNode, vector<DijkstraNode>,
                        decltype(comparator)>
        heap(comparator);

    heap.push({start_index, 0});

    while (!heap.empty()) {
      auto node = heap.top();
      heap.pop();

      if (visited[node.index]) {
        continue;
      }

      visited[node.index] = true;

      for (auto neighbor_index : adj_list[node.index]) {
        if (visited[neighbor_index]) {
          continue;
        }

        if (distances[neighbor_index] > distances[node.index] + 1) {
          distances[neighbor_index] = distances[node.index] + 1;
          heap.push({neighbor_index, distances[neighbor_index]});
        }
      }
    }

    if (visited[end_index]) {
      return distances[end_index];
    }

    return -1;
  }

  int getItemIndex(const vector<string>& bank, const string& item) {
    for (size_t index = 0; index < bank.size(); ++index) {
      if (bank[index] == item) {
        return static_cast<int>(index);
      }
    }
    return -1;
  }

  int minMutation(const string& start, const string& end,
                  vector<string>& bank) {
    bank.push_back(start);

    int start_index = static_cast<int>(bank.size()) - 1;
    int end_index = getItemIndex(bank, end);

    if (end_index == -1) {
      return end_index;
    }

    auto adj_list = constructAdjacencyList(bank);

    auto min_distance = calculateMinDistance(adj_list, start_index, end_index);

    return min_distance;
  }
};