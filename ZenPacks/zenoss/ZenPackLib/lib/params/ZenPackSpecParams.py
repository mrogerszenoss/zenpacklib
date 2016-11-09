##############################################################################
#
# Copyright (C) Zenoss, Inc. 2016, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################
from .SpecParams import SpecParams
from .ZPropertySpecParams import ZPropertySpecParams
from .ClassSpecParams import ClassSpecParams
from .DeviceClassSpecParams import DeviceClassSpecParams
from .EventClassSpecParams import EventClassSpecParams
from .ProcessClassOrganizerSpecParams import ProcessClassOrganizerSpecParams
from ..spec.RelationshipSchemaSpec import RelationshipSchemaSpec
from ..spec.ZenPackSpec import ZenPackSpec


class ZenPackSpecParams(SpecParams, ZenPackSpec):
    def __init__(self,
                 name,
                 zProperties=None,
                 class_relationships=None,
                 classes=None,
                 device_classes=None,
                 event_classes=None,
                 process_class_organizers=None,
                 **kwargs):
        SpecParams.__init__(self, **kwargs)
        self.name = name

        self.zProperties = self.specs_from_param(
            ZPropertySpecParams, 'zProperties', zProperties, leave_defaults=True, zplog=self.LOG)

        self.class_relationships = []
        if class_relationships:
            if not isinstance(class_relationships, list):
                raise ValueError("class_relationships must be a list, not a %s" % type(class_relationships))

            for rel in class_relationships:
                rel['zplog'] = self.LOG
                self.class_relationships.append(RelationshipSchemaSpec(self, **rel))

        self.classes = self.specs_from_param(
            ClassSpecParams, 'classes', classes, leave_defaults=True, zplog=self.LOG)

        self.device_classes = self.specs_from_param(
            DeviceClassSpecParams, 'device_classes', device_classes, leave_defaults=True, zplog=self.LOG)

        self.event_classes = self.specs_from_param(
            EventClassSpecParams, 'event_classes', event_classes, leave_defaults=True, zplog=self.LOG)

        self.process_class_organizers = self.specs_from_param(
            ProcessClassOrganizerSpecParams, 'process_class_organizers', process_class_organizers, leave_defaults=True, zplog=self.LOG)