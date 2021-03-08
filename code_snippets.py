

snippets = { "cin" : """
```cpp
int readInteger() {
  std::cout << "Enter an integer: ";
  int x = 0;
  // while reading into x fails
  while (not (std::cin >> x)) {
    std::cout << "Bad entry, try again: ";
    // clear the error state
    std::cin.clear();
    // throw away the bad input
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    // the loop will then try to read into `x` again
  }
  ```
  """,
"random" : """
  ```cpp
#include <random>
#include <iostream>
 
int main()
{
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> distrib(1, 6);
 
    for (int n=0; n<10; ++n)
        std::cout << distrib(gen) << ' ';
    std::cout << '\\n';
}
```
"""
}