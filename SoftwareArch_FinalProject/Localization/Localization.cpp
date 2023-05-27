#include "Localization.h"
#include <boost/locale.hpp>


Localization::Localization() { }

Localization::~Localization() { }



bool Localization::InstantiateLocalization()
{

	Localization* objLocalizationinstance = Localization::GetInstance();

	if (objLocalizationinstance->blnLocalizationReady) {
		return false;
	}

	objLocalizationinstance->g_objGenerator.add_messages_path("C:\\Users\\user\\Desktop\\software_arch\\SoftwareArch_FinalProject\\Localization");
	objLocalizationinstance->g_objGenerator.add_messages_domain("Localization");

	objLocalizationinstance->blnLocalizationReady = true;

	return true;

}



bool Localization::DestroyLocalization()
{

	Localization* objLocalizationinstance = Localization::GetInstance();

	if (!objLocalizationinstance->blnLocalizationReady) {
	
		return false;
	
	}

	objLocalizationinstance->g_strLocale = "";
	objLocalizationinstance->blnLocalizationReady = false;

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
