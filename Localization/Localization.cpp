#include "Localization.h"



Localization::Localization() { }

Localization::~Localization() { }



bool Localization::InstantiateLocalization()
{

	Localization* objLocalizationinstance = Localization::GetInstance();

	if (objLocalizationinstance->initialized) {
		return false;
	}

	objLocalizationinstance->blnLocalizationReady = true;

	return true;

}



bool Localization::DestroyLocalization()
{

	Localization* instance = Localization::GetInstance();

	if (!instance->initialized) {
	
		return false;
	
	}

	// Teardown anything set up during instantiation

	instance->initialized = false;

	return true;

}



Localization* Localization::GetInstance()
{

	static Localization objLocalizationinstance;

	return &objLocalizationinstance;

}



bool Localization::SetLocale(std::string strLocale)
{

	g_strLocale = strLocale;

	// Set the locale. Do anything required by boost to set the locale

	return false;

}



std::string Localization::GetLocale()
{

	return g_strLocale;

}
