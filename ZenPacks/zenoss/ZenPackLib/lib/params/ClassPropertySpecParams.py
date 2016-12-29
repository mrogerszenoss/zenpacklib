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
from ..spec.ClassPropertySpec import ClassPropertySpec


class ClassPropertySpecParams(SpecParams, ClassPropertySpec):
    """ClassPropertySpecParams"""

    def __init__(self, class_spec, name, **kwargs):
        SpecParams.__init__(self, **kwargs)
        self.name = name

    @classmethod
    def fromObject(cls, id, ob):
        """Generate SpecParams from example object and list of properties"""
        print 'getting property {} ({})'.format(ob.id, id)
        self = object.__new__(cls)
        SpecParams.__init__(self)

        ob = aq_base(ob)

        self.name = id

        proto = ob.__class__(ob.id)

        self.default = getattr(proto, id, None)

        entry = next((p for p in proto._properties if p['id'] == id), None)

        if entry:
            self.type_ = entry.get('type', 'string')
            self.label = entry.get('label')

        return self
