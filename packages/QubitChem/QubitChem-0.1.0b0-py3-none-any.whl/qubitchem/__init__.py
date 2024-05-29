#
# @ 2023. Triad National Security, LLC. All rights reserved.
#
# This program was produced under U.S. Government contract 89233218CNA000001
# for Los Alamos National Laboratory (LANL), which is operated by Triad
# National Security, LLC for the U.S. Department of Energy/National Nuclear
# Security Administration. All rights in the program are reserved by Triad
# National Security, LLC, and the U.S. Department of Energy/National Nuclear
# Security Administration. The Government is granted for itself and others acting
# on its behalf a nonexclusive, paid-up, irrevocable worldwide license in this
# material to reproduce, prepare derivative works, distribute copies to the
# public, perform publicly and display publicly, and to permit others to do so.
#
# Author: Yu Zhang <zhy@lanl.gov>
#


import os
import sys
import textwrap

# TODO: extract it from __version__.py
__version__ = "0.1.0.beta"

__author__ = "Yu Zhang (zhy@lanl.gov)"
__copyright__ = f"""
{" " * 3}
{" " * 3} @ 2023. Triad National Security, LLC. All rights reserved.
{" " * 3}
{" " * 3}This program was produced under U.S. Government contract 89233218CNA000001
{" " * 3} for Los Alamos National Laboratory (LANL), which is operated by Triad
{" " * 3}National Security, LLC for the U.S. Department of Energy/National Nuclear
{" " * 3}Security Administration. All rights in the program are reserved by Triad
{" " * 3}National Security, LLC, and the U.S. Department of Energy/National Nuclear
{" " * 3}Security Administration. The Government is granted for itself and others acting
{" " * 3}on its behalf a nonexclusive, paid-up, irrevocable worldwide license in this
{" " * 3}material to reproduce, prepare derivative works, distribute copies to the
{" " * 3}
{" " * 3}Authors: Yu Zhang <zhy@lanl.gov>
"""

__logo__ = f"""
TBA
{__copyright__}
Version: {__version__}
"""

