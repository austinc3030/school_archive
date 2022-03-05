// ----------------------------------------------------------------------------
// Name: zookeeper-ui.cpp
// Abstract: This is the zookeeper-ui.exe
// ----------------------------------------------------------------------------
#include <iostream>
#include "ui.h"
#include <boost/locale.hpp>



// ----------------------------------------------------------------------------
// Name: main
// Abstract: The main method of the zookeeper-ui executable
// ----------------------------------------------------------------------------
int main()
{
    using namespace boost::locale;
    generator gen;
    //One of these linses should be uncommented to allow switching locales
    //std::locale::global(gen("de_DE.UTF - 8");
    std::locale::global(gen(""));


    ui_main();

    std::cout << translate("\n\n UI Started \n\n");

    system("pause");

} // End main()