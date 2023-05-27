// ----------------------------------------------------------------------------
// Name: ui.cpp
// Abstract: This is the ui dll
// ----------------------------------------------------------------------------
#include "pch.h"
#include "zoo.h"
#include <iostream>
#include "ui.h"
#include <boost/locale.hpp>


// ----------------------------------------------------------------------------
// Name: ui_main()
// Abstract: The main method of the ui dll
// ----------------------------------------------------------------------------
void ui_main()
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
	std::cout << translate("The zoo LOOKS so cool!!!");

	zoo_main();

} // End ui_main()