// ----------------------------------------------------------------------------
// Name: bear.h
// Abstract: This is the bear dll
// ----------------------------------------------------------------------------
#pragma once

#ifdef BEAR_EXPORTS
#define BEAR_API __declspec(dllexport)
#else
#define BEAR_API __declspec(dllimport)
#endif

class Bear
{

public:
    void feed_bear();
    void play_hide_and_go_seek();
};

extern "C" BEAR_API Bear * get_bear();

extern "C" BEAR_API void feed_bear(Bear * bear);

extern "C" BEAR_API void play_hide_and_go_seek(Bear * bear);