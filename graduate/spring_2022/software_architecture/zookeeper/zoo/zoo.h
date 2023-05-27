#pragma once

#ifdef ZOO_EXPORTS
#define ZOO_API __declspec(dllexport)
#else
#define ZOO_API __declspec(dllimport)
#endif

extern "C" ZOO_API void zoo_main();