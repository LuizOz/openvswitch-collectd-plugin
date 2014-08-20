openvswitch-collectd-plugin
===========================

OpenVSwitch plugin for Collectd

Simplistic OpenVSwitch plugin made in Python for Collectd.

Collects the hit, miss and lost stats from the OpenVSwitch DataPath.

Install
-------
1. Copy openvswitch.py to the Collectd plugins folder (/usr/lib/collectd/)
2. Copy openvswitch.conf to the collectd.conf.d folder (/etc/collectd/collectd.conf.d/)
3. Copy openvswitch.db to the /etc/collectd folder. If you place in another folder, make sure to change the .conf file for the correct db paths 

It's using a [custom TypesDB](https://collectd.org/documentation/manpages/types.db.5.shtml#custom_types) to save these metrics.
If you don't specify the default TypesDB + the plugin TypesDB file, its not going to work.

You can either edit the default TypesDB file and add the openvswitch.db line or specify the openvswitch.db file directly.

OpenVSwitch compatibility
-------------------------
ovs-dpctl is used to facilitate the compatibility for all OVS versions.

Should work on all OVS versions.
