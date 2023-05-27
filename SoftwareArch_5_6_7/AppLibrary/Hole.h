#pragma once
#include "AppFeaturesOpsExports.h"
#include "Feature.h"

#include <iostream>
#include <fstream>
#include "..\Core\GuidObject.h"



namespace Application
{

	class APPLIBRARY_API IHole : public GuidObject
	{

	public:

		virtual std::string GetVersion() = 0;
		IHole(int guid) : GuidObject(guid)
		{

		}

		IHole() = delete;

	};


	class APPLIBRARY_API Hole : public Application::Feature, public IHole
	{

	public:

		Hole() = delete;
		Hole(int guid) : IHole(guid)
		{

		}
		std::string GetVersion() override
		{

			return "1";

		}

	};

}