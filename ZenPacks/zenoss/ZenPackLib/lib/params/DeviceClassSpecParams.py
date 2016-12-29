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
from .RRDTemplateSpecParams import RRDTemplateSpecParams
from .ZPropertySpecParams import ZPropertySpecParams

from ..spec.DeviceClassSpec import DeviceClassSpec


class DeviceClassSpecParams(SpecParams, DeviceClassSpec):
    def __init__(self, zenpack_spec, path, zProperties=None, templates=None, **kwargs):
        SpecParams.__init__(self, **kwargs)
        self.path = path
        self.zProperties = zProperties
        self.templates = self.specs_from_param(
            RRDTemplateSpecParams, 'templates', templates, zplog=self.LOG)

    @classmethod
    def fromObject(cls, deviceclass):
        self = super(DeviceClassSpecParams, cls).fromObject(deviceclass)

        deviceclass = aq_base(deviceclass)

        zprops = [x for x in deviceclass.zenPropertyIds(all=False) if deviceclass.isLocal(x)]

        self.zProperties = {x: ZPropertySpecParams.fromObject(x, deviceclass) for x in zprops}

        self.templates = {x.id: RRDTemplateSpecParams.fromObject(x) for x in deviceclass.rrdTemplates()}

        return self
