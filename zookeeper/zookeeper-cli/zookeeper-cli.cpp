// ----------------------------------------------------------------------------
// Name: zookeeper-cli.cpp
// Abstract: This is the zookeeper-cli executable
// ----------------------------------------------------------------------------
#include <iostream>
#include "zoo.h"
#include <boost/locale.hpp>


// ----------------------------------------------------------------------------
// Name: main()
// Abstract: The main method of the zookeeper-cli.exe
// ----------------------------------------------------------------------------
int main()
{
    using namespace std;
    using namespace boost::locale;
    generator gen;

    //Specify location of dictionaries
    gen.add_messages_path(".");
    gen.add_messages_domain("messages");

    //One of these linses should be uncommented to allow switching locales
    std::locale::global(gen("de_DE.UTF-8"));
    //std::locale::global(gen(""));
    cout.imbue(locale());

    zoo_main();
    
    std::cout << translate("Client Starting");

    system("pause");

} // End main()