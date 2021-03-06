.. _tutorial-snmp-device-5:

#########################
Monitoring an SNMP Device
#########################

The following sections will describe a common approach to monitoring an SNMP-
enabled device. We'll start with the basics that can be done without writing a
line of code, and then move on to more sophisticated capabilities.

For purposes of this guide we'll be building a ZenPack to support a NetBotz
environmental sensor device. This device has a variety of sensors that monitor
temperature, humidity, dew point, audio levels and air flow.

.. note::

    This tutorial assumes your system is already setup as described in
    :ref:`development-environment-5` and :ref:`getting-started-5`.

.. toctree::
    :maxdepth: 2

    snmp-tools-5
    device-monitoring-5
    device-modeling-5
    component-modeling-5
    component-monitoring-5
    snmp-traps-5
