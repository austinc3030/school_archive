#pragma once
#include "AppFeaturesOpsExports.h"

namespace Application
{
	class Block;
	class PartFile;
	class BlockBuilder;
	class Hole;
	class HoleBuilder;
}


APPLIBRARY_API Application::BlockBuilder* Journaling_FeatureCollection_CreateBlockBuilder(Application::PartFile *part, Application::Block* block);
APPLIBRARY_API Application::HoleBuilder* Journaling_FeatureCollection_CreateHoleBuilder(Application::PartFile* part, Application::Hole* hole);