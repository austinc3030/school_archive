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
	using namespace boost::locale;
	std::cout << translate("The zoo LOOKS so cool!!!");

	zoo_main();

} // End ui_main()