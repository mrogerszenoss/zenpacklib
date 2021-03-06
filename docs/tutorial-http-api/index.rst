.. _tutorial-http-api-5:

######################
Monitoring an HTTP API
######################

This tutorial will describe an efficient approach to monitoring data via a HTTP
API. We'll start by using `zenpack.yaml` to extend the Zenoss object model. Then
we'll use a Python modeler plugin to fill out the object model. Then we'll use
PythonCollector to monitor for events, datapoints and even to update the model.

For purposes of this guide we'll be building a ZenPack that monitors the weather
using The Weather Channel's Weather Underground API.

.. note::

    This tutorial assumes your system is already setup as described in
    :ref:`development-environment-5` and :ref:`getting-started-5`.

.. toctree::
    :maxdepth: 2

    wunderground-api
    create-zenpack-5
    modeler-plugin-5
    add-device-class-5
    datasource-plugin-events-5
    datasource-plugin-datapoints-5
    datasource-plugin-model-5
