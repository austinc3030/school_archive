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
	using namespace boost::locale;
	std::cout << translate("Let's go to the zoo!!!");

	feed_animals();
	play_games();

} // End zoo_main() 