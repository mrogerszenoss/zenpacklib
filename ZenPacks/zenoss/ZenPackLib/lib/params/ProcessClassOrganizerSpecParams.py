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
from .ProcessClassSpecParams import ProcessClassSpecParams
from ..spec.ProcessClassOrganizerSpec import ProcessClassOrganizerSpec


class ProcessClassOrganizerSpecParams(SpecParams, ProcessClassOrganizerSpec):
    def __init__(self, zenpack_spec, path, description='', process_classes=None, remove=False, **kwargs):
        SpecParams.__init__(self, **kwargs)
        self.path = path
        self.description = description
        self.remove = remove
        self.process_classes = self.specs_from_param(
            ProcessClassSpecParams, 'process_classes', process_classes)

    @classmethod
    def fromObject(cls, processclass):
        self = super(ProcessClassOrganizerSpecParams, cls).fromObject(processclass)

        processclass = aq_base(processclass)
        self.process_classes = {x.id: ProcessClassSpecParams.fromObject(x) for x in processclass.osProcessClasses()}

        return self

    @classmethod
    def new(cls, processclass, description='', remove=False):
        self = object.__new__(cls)
        SpecParams.__init__(self)
        self.path = processclass
        self.description = description
        self.remove = remove
        return self
