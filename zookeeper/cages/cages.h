// ----------------------------------------------------------------------------
// Name: cages.h
// Abstract: This is the bear dll
// ----------------------------------------------------------------------------
#pragma once

#ifdef CAGES_EXPORTS
#define CAGES_API __declspec(dllexport)
#else
#define CAGES_API __declspec(dllimport)
#endif

extern "C" CAGES_API void feed_animals();