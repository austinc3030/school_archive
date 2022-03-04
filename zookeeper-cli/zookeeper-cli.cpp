// ----------------------------------------------------------------------------
// Name: zookeeper-cli.cpp
// Abstract: This is the zookeeper-cli executable
// ----------------------------------------------------------------------------
#include <iostream>
#include "zoo.h"



// ----------------------------------------------------------------------------
// Name: main()
// Abstract: The main method of the zookeeper-cli.exe
// ----------------------------------------------------------------------------
int main()
{

    zoo_main();
    
    std::cout << "\n\n\n\n";

    system("pause");

} // End main()