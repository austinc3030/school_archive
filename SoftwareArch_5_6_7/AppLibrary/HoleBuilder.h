#pragma once
#include "AppFeaturesOpsExports.h"
#include "..\Core\GuidObject.h"
#include "Extrude.h"
#include "Block.h"

enum JournalHoleBuilderTypes
{

	HoleJournalTypesRadii,		/**Represents the radii of the hole's ends. */
	HoleJournalTypesChamfers,	/**Represents the chamfers of the hole's ends*/
	HoleJournalTypesTapers		/**Represents the tapers of the hole. */

};



namespace Application
{

	class Block;
	class Wire;
	class Hole;

	class APPLIBRARY_API HoleBuilder : public GuidObject
	{

	public:
		
		HoleBuilder() = delete;
		HoleBuilder(Application::Hole* hole, int guid);
		JournalHoleBuilderTypes GetType();
		void SetType(JournalHoleBuilderTypes type);
		bool SetDepth(int intDepth);
		bool SetDiameter(int intDiameter);

	private:

		Hole* m_hole;
		JournalHoleBuilderTypes m_journalHoleBuilderTypes;

	};

}