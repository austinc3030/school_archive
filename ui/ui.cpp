// ----------------------------------------------------------------------------
// Name: ui.cpp
// Abstract: This is the ui dll
// ----------------------------------------------------------------------------
#include "pch.h"
#include "zoo.h"
#include <iostream>
#include "ui.h"



// ----------------------------------------------------------------------------
// Name: ui_main()
// Abstract: The main method of the ui dll
// ----------------------------------------------------------------------------
void ui_main()
{

	std::cout << translate("\n\nThe zoo LOOKS so cool!!!\n\n");

	zoo_main();

} // End ui_main()