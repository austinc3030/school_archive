// ----------------------------------------------------------------------------
// Name: games.h
// Abstract: This is the games dll
// ----------------------------------------------------------------------------
#pragma once

#ifdef GAMES_EXPORTS
#define GAMES_API __declspec(dllexport)
#else
#define GAMES_API __declspec(dllimport)
#endif

extern "C" GAMES_API void play_games();