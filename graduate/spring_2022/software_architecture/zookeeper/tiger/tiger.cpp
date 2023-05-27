// ----------------------------------------------------------------------------
// Name: tiger.cpp
// Abstract: This is the tiger dll
// ----------------------------------------------------------------------------
#include "pch.h"
#include <iostream>
#include "tiger.h"
#include <boost/locale.hpp>


// ----------------------------------------------------------------------------
// Name: Tiger::feed_tiger()
// Abstract: Member method to feed the tiger
// ----------------------------------------------------------------------------
void Tiger::feed_tiger()
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
    std::cout << translate("eat", "Feeding Tiger");

} // End Tiger::feed_tiger()



// ----------------------------------------------------------------------------
// Name: Tiger::play_tag()
// Abstract: Member method to play tag
// ----------------------------------------------------------------------------
void Tiger::play_tag()
{

    std::cout << "Playing tag!\n";

} // End play_tag



// ----------------------------------------------------------------------------
// Name: get_tiger()
// Abstract: Return a new instance of a tiger
// ----------------------------------------------------------------------------
TIGER_API Tiger* get_tiger()
{

    return new Tiger();

} // End get_tiger()



// ----------------------------------------------------------------------------
// Name: feed_tiger()
// Abstract: Non-member method to Feed the tiger
// ----------------------------------------------------------------------------
TIGER_API void feed_tiger(Tiger* tiger)
{

    tiger->feed_tiger();

} // End feed_tiger()



// ----------------------------------------------------------------------------
// Name: play_tag()
// Abstract: Non-member method to play tag
// ----------------------------------------------------------------------------
TIGER_API void play_tag(Tiger* tiger)
{

    tiger->play_tag();

} // End play_tag()
