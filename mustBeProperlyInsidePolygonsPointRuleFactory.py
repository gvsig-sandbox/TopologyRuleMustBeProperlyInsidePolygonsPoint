# encoding: utf-8

import gvsig
import sys

from gvsig import uselib
uselib.use_plugin("org.gvsig.topology.app.mainplugin")

from org.gvsig.fmap.geom import Geometry
from org.gvsig.tools.util import ListBuilder
from org.gvsig.topology.lib.api import TopologyLocator
from org.gvsig.topology.lib.spi import AbstractTopologyRuleFactory

from mustBeProperlyInsidePolygonsPointRule import MustBeProperlyInsidePolygonsPointRule

class MustBeProperlyInsidePolygonsPointRuleFactory(AbstractTopologyRuleFactory):
      
    def __init__(self):
        AbstractTopologyRuleFactory.__init__(
            self,
            "MustBeProperlyInsidePolygonsPoint",
            "Must Be Properly Inside Polygons Point Rule",
            "This rule requires that the points must fall within the area, not on the boundary. So points errors are created on the points that are not inside the polygon.",
            ListBuilder().add(Geometry.TYPES.POINT).add(Geometry.TYPES.MULTIPOINT).asList(),
            ListBuilder().add(Geometry.TYPES.SURFACE).add(Geometry.TYPES.MULTISURFACE).asList()
        )
    
    def createRule(self, plan, dataSet1, dataSet2, tolerance):
        rule = MustBeProperlyInsidePolygonsPointRule(plan, self, tolerance, dataSet1, dataSet2)
        return rule

def selfRegister():
    try:
        manager = TopologyLocator.getTopologyManager()
        manager.addRuleFactories(MustBeProperlyInsidePolygonsPointRuleFactory())
    except:
        ex = sys.exc_info()[1]
        gvsig.logger("Can't register rule. Class Name: " + ex.__class__.__name__ + ". Exception: " + str(ex), gvsig.LOGGER_ERROR)

def main(*args):
    pass
