#pragma once
#include "AutomationBindingExports.h"



namespace AutomationAPI
{

	class BlockBuilder;
	class Block;
	class HoleBuilder;
	class Hole;
	
	
	
	class AUTOMATIONBINDING_API FeatureCollection
	{
	
	public:
	
		FeatureCollection(int guid);

		virtual ~FeatureCollection();

		BlockBuilder* CreateBlockBuilder(Block* block);

		HoleBuilder* CreateHoleBuilder(Hole* hole);


	private:
		int m_guid;
	};
}