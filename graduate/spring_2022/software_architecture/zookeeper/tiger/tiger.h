// ----------------------------------------------------------------------------
// Name: tiger.h
// Abstract: This is the tiger dll
// ----------------------------------------------------------------------------
#pragma once

#ifdef TIGER_EXPORTS
#define TIGER_API __declspec(dllexport)
#else
#define TIGER_API __declspec(dllimport)
#endif

class Tiger
{

public:
    void feed_tiger();
    void play_tag();
};

extern "C" TIGER_API Tiger * get_tiger();

extern "C" TIGER_API void feed_tiger(Tiger * tiger);

extern "C" TIGER_API void play_tag(Tiger * tiger);
