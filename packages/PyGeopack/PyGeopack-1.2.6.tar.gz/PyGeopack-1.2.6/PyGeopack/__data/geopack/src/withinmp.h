#ifndef __WITHINMP_H__
#define __WITHINMP_H__
#include <stdio.h>
#include <stdlib.h>
#include "math.h"

extern "C" {
	bool WithinMP(double x, double y, double z, double Bz, double Pdyn);
}

#endif