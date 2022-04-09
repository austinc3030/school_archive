#include "AutomationAPI_HoleCollection.h"
#include "AutomationAPI_Hole.h"
#include <iostream>

class Hole;



AutomationAPI::HoleCollection::HoleCollection(int guid) : m_guid(guid)
{

}



AutomationAPI::HoleCollection::~HoleCollection()
{

}



AutomationAPI::HoleCollection* CreateHoleBuilder(Hole* hole)
{

	return nullptr;

}