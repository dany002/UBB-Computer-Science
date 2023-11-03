#include <iostream>
#include <vector>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <queue>
#include <random>

std::vector<int> v1;
std::vector<int> v2;
int result = 0;
std::queue<int> partialProducts;
std::condition_variable productFlag;
std::mutex mutex;
bool producerDone = false;

// Function to fill a vector with random integers within a specified range
void fillVectorWithRandom(std::vector<int>& v, int size, int min, int max) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> distribution(min, max);

    for (int i = 0; i < size; i++) {
        v.push_back(distribution(gen));
    }
}

void printVector(const std::vector<int>& v, const std::string& name) {
    std::cout << name << ": ";
    for (const int& element : v) {
        std::cout << element << " ";
    }
    std::cout << std::endl;
}


void produce() {
    int product;
    std::unique_lock<std::mutex> lock(mutex);
    for (int index = 0; index < v1.size(); index++) {
        product = v1[index] * v2[index];
        std::cout << "Produced: " << product << std::endl;
        partialProducts.push(product);
        productFlag.notify_one();
    }
    producerDone = true;
    productFlag.notify_one();
}

void consume() {
    while (!producerDone) {
        std::unique_lock<std::mutex> lock(mutex);
        productFlag.wait(lock, [] { return producerDone; });
        result += partialProducts.front();
        partialProducts.pop();
        std::cout << "Partial sum: " << result << std::endl;
    }
    while (!partialProducts.empty()) {
        result += partialProducts.front();
        partialProducts.pop();
        std::cout << "Partial sum: " << result << std::endl;
    }
}

int main() {
    fillVectorWithRandom(v1, 5, 1, 100);
    fillVectorWithRandom(v2, 5, 1, 100);

    printVector(v1, "v1");
    printVector(v2, "v2");


    std::thread producer(produce);
    std::thread consumer(consume);

    producer.join();
    consumer.join();

    std::cout << "The result is " << result << std::endl;
    return 0;
}
