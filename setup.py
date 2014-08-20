from distutils.core import setup

setup(name='openvswitch-plugin-collectd',
      version='0.1.1',
      description='OpenVSwitch plugin for Collectd',
      author='Luiz Ozaki',
      author_email='luiz.ozaki@locaweb.com.br',
      url='https://github.com/LuizOz/openvswitch-collectd-plugin',
      data_files=[('/etc/collectd/collectd.conf.d/', ['openvswitch.conf']),
                  ('/etc/collectd/', ['openvswitch.db']),
                  ('/usr/lib/collectd/', ['openvswitch.py'])]
     )
