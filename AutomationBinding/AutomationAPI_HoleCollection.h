#pragma once

#include "AutomationBindingExports.h"



namespace AutomationAPI
{

	class Hole;
	class HoleBuilder;



	class AUTOMATIONBINDING_API HoleCollection
	{

	public:

		HoleCollection(int guid);

		virtual ~HoleCollection();

		HoleBuilder* CreateHoleBuilder(Hole* hole);

	private:

		int m_guid;

	};

}