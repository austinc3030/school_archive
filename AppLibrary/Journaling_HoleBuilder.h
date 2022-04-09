#pragma once

#include "AppFeaturesOpsExports.h"
#include "..\AppLibrary\HoleBuilder.h"



APPLIBRARY_API bool Journaling_HoleBuilder_SetDepth(int intDepth);

APPLIBRARY_API bool Journaling_HoleBuilder_SetDiameter(int intDiameter);

APPLIBRARY_API void Journaling_HoleBuilder_SetType(Application::HoleBuilder* holeBuilder, JournalHoleBuilderTypes autType);

APPLIBRARY_API JournalHoleBuilderTypes Journaling_HoleBuilder_GetType(Application::HoleBuilder* HoleBuilder);