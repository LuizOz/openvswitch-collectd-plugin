# openvswitch-collectd-plugin
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; only version 2 
# of the License is applicable.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
import collectd
import re

from subprocess import Popen, PIPE

def ovs_fetch():
    data = {}
    try:
        p = Popen(["/usr/bin/ovs-dpctl", "show"], stdout=PIPE, close_fds=True)
        output = p.stdout.readlines()
        for i, line in enumerate(output):
            if line.find("@") != -1:
                bridge = line.strip().replace(":", "")
                data[bridge] = output[i+1].strip()
        return struct_info(data)
    except OSError:
        collectd.error("Failed to run ovs-dpctl")
        return None

def struct_info(lines):
    struct = {}
    for line in lines:
        struct[line] = {}
        for d in re.split(":? ", lines[line], 3):
            if d.find(":") != -1:
                stats = d.split(":")
                struct[line][stats[0]] = float(stats[1])
    return struct

def dispatch_all_value(info):
    keys = ["hit", "missed", "lost"]
    for val in info:
        values = []
        cc = collectd.Values(plugin="openvswitch")
        cc.type = "openvswitch"
        cc.type_instance = val
        for key in keys:
            if (info[val].get(key) is not None):
                values.append(info[val][key])
            else:
                values.append(0.00)
        cc.values = values
        cc.dispatch()

def read_callback():
    data = ovs_fetch()

    if not data:
        collectd.error("Failed to fetch OVS data")
        return None

    dispatch_all_value(data)

collectd.register_read(read_callback)
