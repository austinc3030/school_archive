// ----------------------------------------------------------------------------
// Name: zoo.cpp
// Abstract: This is the zoo dll
// ----------------------------------------------------------------------------
#include "pch.h"
#include "zoo.h"
#include <iostream>
#include "cages.h"
#include "games.h"



// ----------------------------------------------------------------------------
// Name: zoo_main
// Abstract: The main method of the zoo dll
// ----------------------------------------------------------------------------
void zoo_main()
{

	std::cout << translate("\n\nLet's go to the zoo!!!\n\n");

	feed_animals();
	play_games();

} // End zoo_main() 