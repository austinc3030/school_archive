// ----------------------------------------------------------------------------
// Name: zoo.cpp
// Abstract: This is the zoo dll
// ----------------------------------------------------------------------------
#include "pch.h"
#include "zoo.h"
#include <iostream>
#include "cages.h"
#include "games.h"
#include <boost/locale.hpp>



// ----------------------------------------------------------------------------
// Name: zoo_main
// Abstract: The main method of the zoo dll
// ----------------------------------------------------------------------------
void zoo_main()
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
	std::cout << translate("Let's go to the zoo!!!");

	feed_animals();
	play_games();

} // End zoo_main() 