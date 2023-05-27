// ----------------------------------------------------------------------------
// Name: lion.h
// Abstract: This is the lion dll
// ----------------------------------------------------------------------------
#pragma once

#ifdef LION_EXPORTS
#define LION_API __declspec(dllexport)
#else
#define LION_API __declspec(dllimport)
#endif

class Lion
{

public:
    void feed_lion();
    void play_marco_polo();
};

extern "C" LION_API Lion * get_lion();

extern "C" LION_API void feed_lion(Lion * lion);

extern "C" LION_API void play_marco_polo(Lion * lion);
