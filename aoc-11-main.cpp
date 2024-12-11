#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

int main() {
    std::ifstream input("input-11");
    if (!input) {
        std::cerr << "Failed to open input file." << std::endl;
        return 1;
    }

    std::string line;
    std::getline(input, line);
    
    std::vector<int> stones;
    std::stringstream ss(line);
    int number;
    while (ss >> number) {
        stones.push_back(number);
    }

    std::cout << "after iteration: 0\n";
    for (int stone : stones) {
        std::cout << stone << " ";
    }
    std::cout << "\n";

    for (int iteration = 0; iteration < 75; ++iteration) {
        std::cout << "iteration: " << iteration << "/75\n";
        for (size_t count = 0; count < stones.size(); ) {
            if (stones[count] == 0) {
                stones[count] = 1;
            } else if (std::to_string(stones[count]).length() % 2 == 0) {
                std::string stoneStr = std::to_string(stones[count]);
                size_t length = stoneStr.length();

                int firstHalf = std::stoi(stoneStr.substr(0, length / 2));
                int secondHalf = std::stoi(stoneStr.substr(length / 2));

                stones.erase(stones.begin() + count);
                stones.insert(stones.begin() + count, secondHalf);
                stones.insert(stones.begin() + count, firstHalf);

                count += 2; // Move to the next pair of stones after processing the split.
            } else {
                stones[count] *= 2024;
                ++count; // Move to the next stone.
            }
        }
    }

    int result1 = stones.size();
    std::cout << "result1: " << result1 << "\n";

    return 0;
}
