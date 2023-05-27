// ----------------------------------------------------------------------------
// Name: ui.h
// Abstract: This is the ui dll
// ----------------------------------------------------------------------------
#pragma once

#ifdef UI_EXPORTS
#define UI_API __declspec(dllexport)
#else
#define UI_API __declspec(dllimport)
#endif

extern "C" UI_API void ui_main();