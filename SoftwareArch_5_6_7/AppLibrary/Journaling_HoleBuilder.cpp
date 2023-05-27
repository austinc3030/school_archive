
#include "Journaling_HoleBuilder.h"
#include "..\Journaling\Journaling.h"
#include "..\Journaling\JournalHelpers.h"



bool Journaling_HoleBuilder_SetDepth(int intDepth)
{

	if (intDepth > 0) {

		return true;

	}

	return false;

}



bool Journaling_HoleBuilder_SetDiameter(int intDiameter)
{

	if (intDiameter > 0) {

		return true;

	}

	return false;

}



void Journaling_HoleBuilder_SetType(Application::HoleBuilder* holeBuilder, JournalHoleBuilderTypes autType)
{

	holeBuilder->SetType(autType);

}



JournalHoleBuilderTypes Journaling_HoleBuilder_GetType(Application::HoleBuilder* holeBuilder)
{

	auto type = holeBuilder->GetType();

	return type;

}