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



// ----------------------------------------------------------------------------
// Name: play_games
// Abstract: The main method for the games dll
// ----------------------------------------------------------------------------
void play_games()
{

	std::cout << "\n\nLet's play some games!!!\n\n";

	Bear* bear = get_bear();
	play_hide_and_go_seek(bear);

	Lion* lion = get_lion();
	play_marco_polo(lion);

	Tiger* tiger = get_tiger();
	play_tag(tiger);

} // End play_games()