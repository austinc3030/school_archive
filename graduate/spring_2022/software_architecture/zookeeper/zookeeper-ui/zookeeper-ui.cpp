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
    ui_main();
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

   
    std::cout << translate("UI Started");

    system("pause");

} // End main()