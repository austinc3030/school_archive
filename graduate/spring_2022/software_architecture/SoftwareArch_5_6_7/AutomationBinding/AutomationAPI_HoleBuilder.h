#pragma once

#include "AutomationBindingExports.h"
#include "AutomationAPI_IBuilder.h"



namespace AutomationAPI
{

	class CADObject;
	class BlockBuilder;
	class BlockBuilderImpl;


	class AUTOMATIONBINDING_API HoleBuilder : public IBuilder
	{

	public:

		enum JournalHoleBuilderTypes
		{

			HoleJournalTypesRadii,		/**Represents the radii of the hole's ends. */
			HoleJournalTypesChamfers,	/**Represents the chamfers of the hole's ends*/
			HoleJournalTypesTapers		/**Represents the tapers of the hole. */

		};

		void SetType(HoleJournalTypes type);
		HoleJournalTypes GetType();

		bool SetDepth(int intDepth);
		bool SetDiameter(int intDiameter);


		CADObject* Commit() override;

		static HoleBuilder* CreateHoleBuilder(int guid);
		virtual ~HoleBuilder();
		HoleBuilder() = delete;

	private:

		HoleBuilder(int guid);

	};

}