// ----------------------------------------------------------------------------
// Name: lion.cpp
// Abstract: This is the lion dll
// ----------------------------------------------------------------------------
#include "pch.h"
#include <iostream>
#include "lion.h"
#include <boost/locale.hpp>


// ----------------------------------------------------------------------------
// Name: Lion::feed_lion()
// Abstract: Member method to feed the lion
// ----------------------------------------------------------------------------
void Lion::feed_lion()
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
    std::cout << translate("eat", "Feeding Lion\n");

} // End Lion::feed_lion()



// ----------------------------------------------------------------------------
// Name: Lion::play_marco_polo()
// Abstract: Member method to play marco polo
// ----------------------------------------------------------------------------
void Lion::play_marco_polo()
{

    std::cout << "Playing marco polo!\n";

}



// ----------------------------------------------------------------------------
// Name: get_lion()
// Abstract: Return a new instance of a lion
// ----------------------------------------------------------------------------
LION_API Lion* get_lion()
{

    return new Lion();

} // End get_lion()



// ----------------------------------------------------------------------------
// Name: feed_lion()
// Abstract: Non-member method to Feed the lion
// ----------------------------------------------------------------------------
LION_API void feed_lion(Lion* lion)
{

    lion->feed_lion();

} // End feed_lion()



// ----------------------------------------------------------------------------
// Name: play_marco_polo
// Abstract: Non-member method to play marco polo
// ----------------------------------------------------------------------------
LION_API void play_marco_polo(Lion* lion)
{

    lion->play_marco_polo();

} // End play_marco_polo()
