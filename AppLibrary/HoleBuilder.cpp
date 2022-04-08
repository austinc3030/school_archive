#include "HoleBuilder.h"
#include <iostream>

Application::HoleBuilder::HoleBuilder(Application::Hole* hole, int guid) : GuidObject(guid), m_hole(hole)
{

	if (m_hole == nullptr)
	{
	
		std::cout << "Hole is creation mode" << std::endl;
	
	}
	else
	{
	
		std::cout << "Hole is edit/query mode" << std::endl;
	
	}

}



JournalHoleBuilderTypes Application::HoleBuilder::GetType()
{

	return m_journalHoleBuilderTypes;

}



void Application::HoleBuilder::SetType(JournalHoleBuilderTypes type)
{

	m_journalHoleBuilderTypes = type;

}



bool Application::HoleBuilder::SetDepth(int intDepth)
{

	if (intDepth > 0) {
	
		return true;
	
	}
	
	return false;

}



bool Application::HoleBuilder::SetDiameter(int intDiameter)
{

	if (intDiameter > 0) {

		return true;
	
	}
	
	return false;

}