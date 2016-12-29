##############################################################################
#
# Copyright (C) Zenoss, Inc. 2016, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################
from Acquisition import aq_base
from .SpecParams import SpecParams
from ..spec.ClassRelationshipSpec import ClassRelationshipSpec


class ClassRelationshipSpecParams(SpecParams, ClassRelationshipSpec):
    def __init__(self, class_spec, name, **kwargs):
        SpecParams.__init__(self, **kwargs)
        self.name = name

    @classmethod
    def fromObject(cls, rel, ob):
        """Generate SpecParams from example object and list of properties"""
        print 'getting relationship {} ({})'.format(ob.id, rel)
        self = object.__new__(cls)
        SpecParams.__init__(self)

        ob = aq_base(ob)

        self.name = rel[0]
        return self
