#include "Journaling_FeatureCollection.h"
#include "Block.h";
#include "BlockBuilder.h";
#include "..\AppPartOps\PartOps.h"
#include "..\Journaling\Journaling.h"
#include "..\Journaling\JournalHelpers.h"
#include "Hole.h"
#include "HoleBuilder.h"

Application::BlockBuilder* Journaling_FeatureCollection_CreateBlockBuilder(Application::PartFile *part, Application::Block* block)
{
	//If Journaling write the thing things
	if (IsJournaling())
	{
		JournalStartCall("CreateBlockBuilder", part);
		JournalInClassParam( block, "AutomationAPI::Block", "block");
	}
	Application::BlockBuilder* retVal = nullptr;
	// TODO
	// Obtain next available guid
	static int guid = 8888;
	guid++;
	retVal = new Application::BlockBuilder(block, guid);

	if (IsJournaling())
	{
		JournalReturnClass(retVal, "AutomationAPI::Blockbuilder", "Blockbuilder");
		JournalEndCall();
	}

	return retVal;
}



Application::HoleBuilder* Journaling_FeatureCollection_CreateHoleBuilder(Application::PartFile* part, Application::Hole* hole)
{

	if (IsJournaling())
	{

		JournalStartCall("CreateHoleBuilder", part);
		JournalInClassParam(hole, "AutomationAPI::Hole", "hole");

	}

	Application::HoleBuilder* holeBuilder = nullptr;

	if (IsJournaling())
	{
		JournalReturnClass(holeBuilder, "AutomationAPI::HoleBuilder", "HoleBuilder");
		JournalEndCall();
	}

	return holeBuilder;

}