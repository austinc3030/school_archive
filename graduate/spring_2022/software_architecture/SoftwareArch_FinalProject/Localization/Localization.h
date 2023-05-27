#pragma once

#include <iostream>
#include "LocalizationExports.h"
#include <boost/locale.hpp>


class LOCALIZATION_API Localization
{

public:

	Localization(Localization const&) = delete;
	void operator=(Localization const&) = delete;

	~Localization();

	static Localization* GetInstance();

	static bool InstantiateLocalization();

	static bool DestroyLocalization();

	bool SetLocale(std::string strLocale);

	std::string GetLocale();

private:
	
	Localization();
	std::string g_strLocale;
	bool blnLocalizationReady;
	boost::locale::generator g_objGenerator;

};