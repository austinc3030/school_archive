// ----------------------------------------------------------------------------
// Name: games.cpp
// Abstract: This is the games dll
// ----------------------------------------------------------------------------
#include "pch.h"
#include "games.h"
#include <iostream>
#include "lion.h"
#include "bear.h"
#include "tiger.h"
#include <boost/locale.hpp>


// ----------------------------------------------------------------------------
// Name: play_games
// Abstract: The main method for the games dll
// ----------------------------------------------------------------------------
void play_games()
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
	std::cout << translate("Let's play some games!!!");

	Bear* bear = get_bear();
	play_hide_and_go_seek(bear);

	Lion* lion = get_lion();
	play_marco_polo(lion);

	Tiger* tiger = get_tiger();
	play_tag(tiger);

} // End play_games()