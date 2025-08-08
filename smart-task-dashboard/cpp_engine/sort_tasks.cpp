#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>

struct Task
{
    std::string name;
    std::string date;
};

bool compareByDate(const Task &a, const Task &b)
{
    return a.date < b.date;
}

int main()
{
    std::ifstream inFile("../data/tasks.txt");
    std::vector<Task> tasks;
    std::string line;

    while (getline(inFile, line))
    {
        std::stringstream ss(line);
        std::string task, date;
        if (getline(ss, task, '|') && getline(ss, date))
        {
            tasks.push_back({task, date.substr(1)}); // remove space
        }
    }

    std::sort(tasks.begin(), tasks.end(), compareByDate);

    std::ofstream outFile("../data/tasks.txt"); // overwrite file
    for (const auto &task : tasks)
    {
        outFile << task.name << " | " << task.date << "\n";
    }

    std::cout << "Tasks sorted by date.\n";
    return 0;
}
