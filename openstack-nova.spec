%global prj nova
%global with_doc 0
%global os_release essex

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

Name:             openstack-nova
Version:          2012.1.2
Release:          5
Epoch:            1
Summary:          OpenStack Compute (nova)

Group:            Development/Languages
License:          ASL 2.0
Vendor:           Grid Dynamics Consulting Services, Inc.
URL:              http://openstack.org/projects/compute/
Source0:          %{name}-%{version}.tar.gz

BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}

BuildArch:        noarch
BuildRequires:    python-devel
BuildRequires:    python-setuptools
BuildRequires:    intltool

Requires(post):   chkconfig
Requires(postun): initscripts
Requires(preun):  chkconfig
Requires(pre):    shadow-utils
Requires:         python-%{prj} = %{epoch}:%{version}-%{release}
Requires:         start-stop-daemon

Obsoletes:        %{name}-essex

Requires:         python-%{prj} = %{epoch}:%{version}-%{release}

%description
Nova is a cloud computing fabric controller (the main part of an IaaS system)
built to match the popular AWS EC2 and S3 APIs. It is written in Python, using
the Tornado and Twisted frameworks, and relies on the standard AMQP messaging
protocol, and the Redis KVS.

Nova is intended to be easy to extend, and adapt. For example, it currently
uses an LDAP server for users and groups, but also includes a fake LDAP server,
that stores data in Redis. It has extensive test coverage, and uses the Sphinx
toolkit (the same as Python itself) for code and user documentation.


%package          node-full
Summary:          OpenStack Nova full node installation
Group:            Applications/System

Requires:   %{name} = %{epoch}:%{version}-%{release}
Requires:   %{name}-api = %{epoch}:%{version}-%{release}
Requires:   %{name}-compute = %{epoch}:%{version}-%{release}
Requires:   %{name}-network = %{epoch}:%{version}-%{release}
Requires:   %{name}-objectstore = %{epoch}:%{version}-%{release}
Requires:   %{name}-scheduler = %{epoch}:%{version}-%{release}
Requires:   %{name}-volume = %{epoch}:%{version}-%{release}

Obsoletes:        %{name}-essex-node-full

%description      node-full
This package installs full set of OpenStack Nova packages and Cloud Controller
configuration.


%package          node-compute
Summary:          OpenStack Nova compute node installation
Group:            Applications/System

Requires:   %{name} = %{epoch}:%{version}-%{release}
Requires:   %{name}-compute = %{epoch}:%{version}-%{release}
Requires:   %{name}-network = %{epoch}:%{version}-%{release}
Requires:         MySQL-python

Obsoletes:        %{name}-essex-node-compute

%description      node-compute
This package installs compute set of OpenStack Nova packages and Compute node
configuration.


%package common
Summary:          Components common to all OpenStack services
Group:            Applications/System

Requires:         openstack-utils
Requires:         python-nova = %{epoch}:%{version}-%{release}

Requires(post):   chkconfig
Requires(postun): initscripts
Requires(preun):  chkconfig
Requires(pre):    shadow-utils

Requires:         python-setuptools

Obsoletes:        %{name}-essex-common

%description common
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains scripts, config and dependencies shared
between all the OpenStack nova services.

%package compute
Summary:          OpenStack Nova Virtual Machine control service
Group:            Applications/System

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}
Requires:         curl
Requires:         iscsi-initiator-utils
Requires:         iptables iptables-ipv6
Requires:         vconfig
# tunctl is needed where `ip tuntap` is not available
Requires:         tunctl
Requires:         libguestfs-mount >= 1.7.17
# The fuse dependency should be added to libguestfs-mount
Requires:         fuse
Requires:         libvirt >= 0.8.7
Requires:         libvirt-python
Requires(pre):    qemu-kvm

Obsoletes:        %{name}-essex-compute

%description compute
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova service for controlling Virtual Machines.


%package network
Summary:          OpenStack Nova Network control service
Group:            Applications/System

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}
Requires:         vconfig
Requires:         radvd
Requires:         bridge-utils
#TODO: Enable when available in RHEL 6.3
#Requires:         dnsmasq-utils
# tunctl is needed where `ip tuntap` is not available
Requires:         tunctl

Obsoletes:        %{name}-essex-network

%description network
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova service for controlling networking.


%package volume
Summary:          OpenStack Nova storage volume control service
Group:            Applications/System

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}
Requires:         lvm2
Requires:         scsi-target-utils

Obsoletes:        %{name}-essex-volume

%description volume
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova service for controlling storage volumes.


%package scheduler
Summary:          OpenStack Nova VM distribution service
Group:            Applications/System

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}

Obsoletes:        %{name}-essex-scheduler

%description scheduler
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the service for scheduling where
to run Virtual Machines in the cloud.


%package cert
Summary:          OpenStack Nova certificate management service
Group:            Applications/System

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}

Obsoletes:        %{name}-essex-cert

%description cert
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova service for managing certificates.


%package api
Summary:          OpenStack Nova API services
Group:            Applications/System

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}

Obsoletes:        %{name}-essex-api

%description api
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova services providing programmatic access.


%package objectstore
Summary:          OpenStack Nova simple object store service
Group:            Applications/System

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}

Obsoletes:        %{name}-essex-objectstore

%description objectstore
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova service providing a simple object store.


%package console
Summary:          OpenStack Nova console access services
Group:            Applications/System

Requires:         openstack-nova-common = %{epoch}:%{version}-%{release}

Obsoletes:        %{name}-essex-console

%description console
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova services providing
console access services to Virtual Machines.


%package -n       python-nova
Summary:          Nova Python libraries
Group:            Applications/System

Requires:         openssl
Requires:         sudo

Requires:         MySQL-python

Requires:         python-crypto
Requires:         python-paramiko

Requires:         python-qpid
Requires:         python-kombu
Requires:         python-amqplib


Requires:         python-sqlalchemy>=0.7.3
Requires:         python-cheetah==2.4.4
Requires:         python-amqplib==0.6.1
Requires:         python-anyjson==0.2.4
Requires:         python-boto==2.1.1
Requires:         python-carrot==0.10.5
Requires:         python-eventlet
Requires:         python-kombu==1.0.4
Requires:         python-lockfile==0.8
Requires:         python-lxml==2.3
Requires:         python-daemon==1.5.5
Requires:         python-gflags==1.3
Requires:         python-novaclient
Requires:         python-routes==1.12.3
Requires:         python-webob==1.0.8
Requires:         python-greenlet>=0.3.1
Requires:         python-paste-deploy==1.5.0
Requires:         python-paste
Requires:         python-migrate>=0.7.2
Requires:         python-netaddr
Requires:         python-glance>=2011.3.1
Requires:         python-suds==0.4
Requires:         python-paramiko
Requires:         python-feedparser
Requires:         python-pycrypto
Requires:         python-iso8601>=0.1.4


Obsoletes:        python-nova-essex

%description -n   python-nova
Nova is a cloud computing fabric controller (the main part of an IaaS system)
built to match the popular AWS EC2 and S3 APIs. It is written in Python, using
the Tornado and Twisted frameworks, and relies on the standard AMQP messaging
protocol, and the Redis KVS.

This package contains the %{name} Python library.

%if 0%{?with_doc}

%package doc
Summary:          Documentation for %{name}
Group:            Documentation

BuildRequires:    python-sphinx

%description      doc
Nova is a cloud computing fabric controller (the main part of an IaaS system)
built to match the popular AWS EC2 and S3 APIs. It is written in Python, using
the Tornado and Twisted frameworks, and relies on the standard AMQP messaging
protocol, and the Redis KVS.

This package contains documentation files for %{name}.
%endif

%prep
%setup -q

install redhat/openstack-nova-README.rhel6 README.rhel6

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%if 0%{?with_doc}
export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html source build/html
popd

# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo
%endif

# Give stack, instance-usage-audit and clear_rabbit_queues a reasonable prefix
mv %{buildroot}%{_bindir}/stack %{buildroot}%{_bindir}/nova-stack
mv %{buildroot}%{_bindir}/instance-usage-audit %{buildroot}%{_bindir}/nova-instance-usage-audit
mv %{buildroot}%{_bindir}/clear_rabbit_queues %{buildroot}%{_bindir}/nova-clear-rabbit-queues

# Setup directories
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/buckets
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/images
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/instances
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/keys
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/networks
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/tmp
install -d -m 755 %{buildroot}%{_localstatedir}/log/nova

# Setup ghost CA cert
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/CA
install -p -m 755 nova/CA/*.sh %{buildroot}%{_sharedstatedir}/nova/CA
install -p -m 644 nova/CA/openssl.cnf.tmpl %{buildroot}%{_sharedstatedir}/nova/CA
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/CA/{certs,crl,newcerts,projects,reqs}
touch %{buildroot}%{_sharedstatedir}/nova/CA/{cacert.pem,crl.pem,index.txt,openssl.cnf,serial}
install -d -m 750 %{buildroot}%{_sharedstatedir}/nova/CA/private
touch %{buildroot}%{_sharedstatedir}/nova/CA/private/cakey.pem

# Install config files
install -d -m 755 %{buildroot}%{_sysconfdir}/nova
install -p -D -m 640 etc/nova/api-paste.ini %{buildroot}%{_sysconfdir}/nova/api-paste.ini
install -p -D -m 640 etc/nova/policy.json %{buildroot}%{_sysconfdir}/nova/policy.json

install -p -D -m 640 redhat/nova.conf %{buildroot}%{_sysconfdir}/nova/nova.conf

# Install initscripts for Nova services
INIT_SCRIPTS="
    nova-compute nova-direct-api nova-objectstore nova-volume nova-api
    nova-cert nova-consoleauth nova-network
    nova-scheduler nova-xvpvncproxy"
for i in $INIT_SCRIPTS; do
    install -p -D -m 755 "redhat/${i}.init" %{buildroot}%{_initrddir}/$i
done

# Install sudoers
install -p -D -m 440 redhat/nova-sudoers %{buildroot}%{_sysconfdir}/sudoers.d/nova

# Install logrotate
install -p -D -m 644 redhat/openstack-nova.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Install pid directory
install -d -m 755 %{buildroot}%{_localstatedir}/run/nova

# Install template files
install -p -D -m 644 nova/auth/novarc.template %{buildroot}%{_datarootdir}/nova/novarc.template
install -p -D -m 644 nova/cloudpipe/client.ovpn.template %{buildroot}%{_datarootdir}/nova/client.ovpn.template
install -p -D -m 644 nova/virt/libvirt.xml.template %{buildroot}%{_datarootdir}/nova/libvirt.xml.template
install -p -D -m 644 nova/virt/interfaces.template %{buildroot}%{_datarootdir}/nova/interfaces.template

# Network configuration templates for injection engine
install -d -m 755 %{buildroot}%{_datarootdir}/nova/interfaces
#install -p -D -m 644 nova/virt/interfaces.template %{buildroot}%{_datarootdir}/nova/interfaces/interfaces.ubuntu.template
install -p -D -m 644 redhat/openstack-nova-rhel-ifc-template %{buildroot}%{_datarootdir}/nova/interfaces.template

# Clean CA directory
find %{buildroot}%{_sharedstatedir}/nova/CA -name .gitignore -delete
find %{buildroot}%{_sharedstatedir}/nova/CA -name .placeholder -delete

install -d -m 755 %{buildroot}%{_sysconfdir}/polkit-1/localauthority/50-local.d
install -p -D -m 644 redhat/openstack-nova-polkit.pkla %{buildroot}%{_sysconfdir}/polkit-1/localauthority/50-local.d/50-nova.pkla

# Remove unneeded in production stuff
rm -f %{buildroot}%{_bindir}/nova-debug
rm -fr %{buildroot}%{python_sitelib}/nova/tests/
rm -fr %{buildroot}%{python_sitelib}/run_tests.*
rm -f %{buildroot}%{_bindir}/nova-combined
rm -f %{buildroot}/usr/share/doc/nova/README*

%clean
rm -rf %{buildroot}

%post
if %{_sbindir}/selinuxenabled; then
    echo -e "\033[47m\033[1;31m***************************************************\033[0m"
    echo -e "\033[47m\033[1;31m*\033[0m \033[40m\033[1;31m                                                \033[47m\033[1;31m*\033[0m"
    echo -e "\033[47m\033[1;31m*\033[0m \033[40m\033[1;31m >> \033[5mYou have SELinux enabled on your host !\033[25m <<  \033[47m\033[1;31m*\033[0m"
    echo -e "\033[47m\033[1;31m*\033[0m \033[40m\033[1;31m                                                \033[47m\033[1;31m*\033[0m"
    echo -e "\033[47m\033[1;31m*\033[0m \033[40m\033[1;31mPlease disable it by setting \`SELINUX=disabled' \033[47m\033[1;31m*\033[0m"
    echo -e "\033[47m\033[1;31m*\033[0m \033[40m\033[1;31min /etc/sysconfig/selinux and don't forget      \033[47m\033[1;31m*\033[0m"
    echo -e "\033[47m\033[1;31m*\033[0m \033[40m\033[1;31mto reboot your host to apply that change!       \033[47m\033[1;31m*\033[0m"
    echo -e "\033[47m\033[1;31m*\033[0m \033[40m\033[1;31m                                                \033[47m\033[1;31m*\033[0m"
    echo -e "\033[47m\033[1;31m***************************************************\033[0m"
fi

%pre common
getent group nova >/dev/null || groupadd -r nova --gid 162
if ! getent passwd nova >/dev/null; then
  useradd -u 162 -r -g nova -G nova,nobody -d %{_sharedstatedir}/nova -s /sbin/nologin -c "OpenStack Nova Daemons" nova
fi
exit 0

%pre compute
usermod -a -G qemu nova
# Add nova to the fuse group (if present) to support guestmount
if getent group fuse >/dev/null; then
  usermod -a -G fuse nova
fi
exit 0

%post compute
/sbin/chkconfig --add openstack-nova-compute
%post network
/sbin/chkconfig --add openstack-nova-network
%post volume
/sbin/chkconfig --add openstack-nova-volume
%post scheduler
/sbin/chkconfig --add openstack-nova-scheduler
%post cert
/sbin/chkconfig --add openstack-nova-cert
%post api
for svc in api direct-api metadata-api; do
    /sbin/chkconfig --add openstack-nova-$svc
done
%post objectstore
/sbin/chkconfig --add openstack-nova-objectstore
%post console
for svc in console consoleauth xvpvncproxy; do
    /sbin/chkconfig --add openstack-nova-$svc
done

%preun compute
if [ $1 -eq 0 ] ; then
    for svc in compute; do
        /sbin/service openstack-nova-${svc} stop >/dev/null 2>&1
        /sbin/chkconfig --del openstack-nova-${svc}
    done
fi
%preun network
if [ $1 -eq 0 ] ; then
    for svc in network; do
        /sbin/service openstack-nova-${svc} stop >/dev/null 2>&1
        /sbin/chkconfig --del openstack-nova-${svc}
    done
fi
%preun volume
if [ $1 -eq 0 ] ; then
    for svc in volume; do
        /sbin/service openstack-nova-${svc} stop >/dev/null 2>&1
        /sbin/chkconfig --del openstack-nova-${svc}
    done
fi
%preun scheduler
if [ $1 -eq 0 ] ; then
    for svc in scheduler; do
        /sbin/service openstack-nova-${svc} stop >/dev/null 2>&1
        /sbin/chkconfig --del openstack-nova-${svc}
    done
fi
%preun cert
if [ $1 -eq 0 ] ; then
    for svc in cert; do
        /sbin/service openstack-nova-${svc} stop >/dev/null 2>&1
        /sbin/chkconfig --del openstack-nova-${svc}
    done
fi
%preun api
if [ $1 -eq 0 ] ; then
    for svc in api direct-api metadata-api; do
        /sbin/service openstack-nova-${svc} stop >/dev/null 2>&1
        /sbin/chkconfig --del openstack-nova-${svc}
    done
fi
%preun objectstore
if [ $1 -eq 0 ] ; then
    for svc in objectstore; do
        /sbin/service openstack-nova-${svc} stop >/dev/null 2>&1
        /sbin/chkconfig --del openstack-nova-${svc}
    done
fi
%preun console
if [ $1 -eq 0 ] ; then
    for svc in console consoleauth xvpvncproxy; do
        /sbin/service openstack-nova-${svc} stop >/dev/null 2>&1
        /sbin/chkconfig --del openstack-nova-${svc}
    done
fi

%postun compute
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in compute; do
        /sbin/service openstack-nova-${svc} condrestart > /dev/null 2>&1 || :
    done
fi
%postun network
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in network; do
        /sbin/service openstack-nova-${svc} condrestart > /dev/null 2>&1 || :
    done
fi
%postun volume
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in volume; do
        /sbin/service openstack-nova-${svc} condrestart > /dev/null 2>&1 || :
    done
fi
%postun scheduler
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in scheduler; do
        /sbin/service openstack-nova-${svc} condrestart > /dev/null 2>&1 || :
    done
fi
%postun cert
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in cert; do
        /sbin/service openstack-nova-${svc} condrestart > /dev/null 2>&1 || :
    done
fi
%postun api
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in api direct-api metadata-api; do
        /sbin/service openstack-nova-${svc} condrestart > /dev/null 2>&1 || :
    done
fi
%postun objectstore
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in objectstore; do
        /sbin/service openstack-nova-${svc} condrestart > /dev/null 2>&1 || :
    done
fi
%postun console
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in console consoleauth xvpvncproxy; do
        /sbin/service openstack-nova-${svc} condrestart > /dev/null 2>&1 || :
    done
fi

%files
%doc LICENSE
%{_bindir}/nova-all

%files common
%doc LICENSE
%dir %{_sysconfdir}/nova
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/nova.conf
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/api-paste.ini
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/policy.json
%config(noreplace) %{_sysconfdir}/logrotate.d/openstack-nova
%config(noreplace) %{_sysconfdir}/sudoers.d/nova
%config(noreplace) %{_sysconfdir}/polkit-1/localauthority/50-local.d/50-nova.pkla

%dir %attr(0755, nova, root) %{_localstatedir}/log/nova
%dir %attr(0755, nova, root) %{_localstatedir}/run/nova

%{_bindir}/nova-stack
%{_bindir}/nova-clear-rabbit-queues
%{_bindir}/nova-manage
%{_bindir}/nova-rootwrap

%{_datarootdir}/nova
#%{_mandir}/man1/nova*.1.gz

%defattr(-, nova, nova, -)
%dir %{_sharedstatedir}/nova
%dir %{_sharedstatedir}/nova/buckets
%dir %{_sharedstatedir}/nova/images
%dir %{_sharedstatedir}/nova/instances
%dir %{_sharedstatedir}/nova/keys
%dir %{_sharedstatedir}/nova/networks
%dir %{_sharedstatedir}/nova/tmp

%files compute
%{_bindir}/nova-compute
%{_bindir}/nova-instance-usage-audit
%{_initrddir}/nova-compute
%{python_sitelib}/nova/rootwrap/compute.py*

%files network
%{_bindir}/nova-network
%{_bindir}/nova-dhcpbridge
%{_initrddir}/nova-network
%{python_sitelib}/nova/rootwrap/network.py*

%files volume
%{_bindir}/nova-volume
%{_initrddir}/nova-volume
%{python_sitelib}/nova/rootwrap/volume.py*

%files scheduler
%{_bindir}/nova-scheduler
%{_initrddir}/nova-scheduler

%files cert
%{_bindir}/nova-cert
%{_initrddir}/nova-cert
%defattr(-, nova, nova, -)
%dir %{_sharedstatedir}/nova/CA/
%dir %{_sharedstatedir}/nova/CA/certs
%dir %{_sharedstatedir}/nova/CA/crl
%dir %{_sharedstatedir}/nova/CA/newcerts
%dir %{_sharedstatedir}/nova/CA/projects
%dir %{_sharedstatedir}/nova/CA/reqs
%{_sharedstatedir}/nova/CA/*.sh
%{_sharedstatedir}/nova/CA/openssl.cnf.tmpl
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/cacert.pem
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/crl.pem
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/index.txt
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/openssl.cnf
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/serial
%dir %attr(0750, -, -) %{_sharedstatedir}/nova/CA/private
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/private/cakey.pem

%files api
%{_bindir}/nova-api*
%{_bindir}/nova-direct-api
%{_initrddir}/nova-*api

%files objectstore
%{_bindir}/nova-objectstore
%{_initrddir}/nova-objectstore

%files console
%{_bindir}/nova-console*
%{_bindir}/nova-xvpvncproxy
%{_initrddir}/nova-console*
%{_initrddir}/nova-xvpvncproxy

%files -n python-nova
%defattr(-,root,root,-)
%exclude %{python_sitelib}/nova/rootwrap/compute.py*
%exclude %{python_sitelib}/nova/rootwrap/network.py*
%exclude %{python_sitelib}/nova/rootwrap/volume.py*
%doc LICENSE
%{python_sitelib}/nova
%{python_sitelib}/nova-%{version}-*.egg-info

%if 0%{?with_doc}
%files doc
%doc LICENSE doc/build/html
%endif

%files node-full

%files node-compute

%changelog
* Fri Dec 20 2011 Boris Filippov <bfilippov@griddynamics.com> - 2011.3
- Obsolete nova-cc-config
- Add nova.conf to compute package 

* Fri Dec 16 2011 Boris Filippov <bfilippov@griddynamics.com> - 2011.3
- Make init scripts LSB conformant
- Rename init scripts
- Disable services autorun
- Disable db sync during install

* Tue Aug 29 2011 Alessio Ababilov <aababilov@griddynamics.com> - 2011.3
- Drop openstack-noVNC dependency

* Fri Aug 26 2011 Alessio Ababilov <aababilov@griddynamics.com> - 2011.3-0.20110826.1448
- Fixed openstack-nova-scsi-target-utils-support.patch

* Mon Aug 22 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.3-0.20110822.1819
- Added nova-api-{ec2,os}

* Thu Aug 18 2011 Alessio Ababilov <aababilov@griddynamics.com> - 2011.4-0.20110818.1721
- Return type of server's IP patch

* Thu Aug 11 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.4-0.20110810.1412
- Removed /usr/bin/nova-import-canonical-imagestore
  https://bugs.launchpad.net/nova/+bug/820062

* Fri Aug 05 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.3-0.20110804.1364
- Removed openstack-nova-instancemonitor

* Mon Jul 25 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.3-0.20110724.1308
- Added MySQL-python as dep for openstack-nova-node-compute
- Added nova-network for compute-only nodes due recent changes in network HA code
  https://code.launchpad.net/~vishvananda/nova/ha-net/+merge/67078
- Fixed db upgrade in postscript, changed postscript to /bin/bash
- Removed duplicate entry for /usr/bin/instance-usage-audit

* Tue Jul 12 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.3-0.20110711.1265
- Removed lots of meaningless changelog entries from Jenkins
- Added dependency on dmidecode to openstack-nova-compute because it's missing
  in libvirt package
- Changed versioning for better upgrade experience

* Tue May 03 2011 Mr. Jenkins GD <openstack@griddynamics.net> - 2011.3-0.36.bzr1052
- Added support for scsi-target-utils

* Wed Apr 27 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.3-0.23.bzr1032
- created separate package for noVNC due licensing issue

* Tue Apr 26 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.3-0.21.bzr1031
- Updated patch6

* Mon Apr 25 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.3-0.19.bzr1030
- Floating IPs merged to trunk

* Tue Apr 19 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.3-0.11.bzr1000
- Updated dependency on python-routes with version 1.12.3

* Tue Apr 19 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.3-0.10.bzr1000
- Updated floating IP patch, kudos to Ilya Alekseyev

* Fri Apr 15 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.3-0.1.bzr990
- Diablo versioning

* Thu Apr 14 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.111.bzr988
- Uncommented initial db sync on fresh install
- Added banner with link to instructions

* Thu Apr 14 2011 Ilya Alekseyev <ialekseev@griddynamics.com> - 2011.2-0.110.bzr988
- Patch for auto assigning floating ips (AWS EC2 behaviour emulation) added

* Thu Apr 14 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.108.bzr987
- Fixed an odd typo

* Tue Apr 12 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.101.bzr980
- Added initscript for vncproxy

* Mon Apr 11 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.97.bzr975
- Removed openssl.cnf patch (included in upstream)

* Mon Apr 11 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.94.bzr973
- Removed temp patch

* Mon Apr 11 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.93.bzr973
- Added dependency libvirt >= 0.8.2 for openstack-nova-compute package, see
  https://bugs.launchpad.net/nova/+bug/757283

* Mon Apr 11 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.91.bzr972
- Added temp patch for bug LP755666

* Sun Apr 10 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.89.bzr971
- Added quick fix for s3server.py which restoring euca-upload-bundle

* Fri Apr 08 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.84.bzr967
- Fixed initscript for objectstore

* Fri Apr 08 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.82.bzr965
- Added noVNC tarball

* Wed Apr 06 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.65.bzr946
- Update to bzr946
- Migrated openssl.cnf patch
- Relocated CA directory
- Disabled manual api-paste.ini installation
- Moved ajaxterm to /usr/share/nova

* Wed Apr 06 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.65.bzr942
- Updated network injection patch wich bugfix

* Tue Apr 05 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.64.bzr942
- Updated network injection patch (Ilya Alekseyev)

* Mon Apr 04 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.55.bzr932
- Removed patch for euca-get-ajax-console due it's inclution in upstream

* Fri Apr 01 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.52.bzr930
- Changed location of ajaxterm.py
- Patched netcat binary name s/netcat/nc/

* Fri Apr 01 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.51.bzr930
- Added dependency on our version of euca2ools

* Thu Mar 31 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.47.bzr926
- s/config-cc/cc-config/

* Thu Mar 31 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.46.bzr926
- Added empty files sections for meta packages to enable RPM generation

* Thu Mar 31 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.45.bzr926
- Added SELinux banner

* Thu Mar 31 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.43.bzr925
- Added openstack-nova-node-full, openstack-nova-node-compute meta packages

* Wed Mar 30 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.33.bzr913
- Added nova-vncproxy

* Wed Mar 30 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.28.bzr908
- Migrated guestfs patch

* Tue Mar 29 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.23.bzr905
- Enabled doc build 

* Fri Mar 25 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.20.bzr890
- Migrated guestfs patch

* Fri Mar 25 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.17.bzr886
- Added dependency on python-suds

* Fri Mar 25 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.15.bzr885
- Added dependency on python-novaclient

* Thu Mar 17 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.9.bzr815
- Update to bzr815
- Removed libvirt-xml-cpus.patch

* Tue Mar 15 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.8.bzr807
- Update to bzr807

* Tue Mar 15 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.7.bzr806
- Update to bzr806

* Tue Mar 15 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.6.bzr805
- Added database migration
- Temporary disabled documentation build until release

* Tue Mar 15 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.5.bzr805
- Update to bzr805

* Tue Mar 15 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.4.bzr802
- Added openstack-nova-libvirt-xml-cpus.patch to prevent error with nova-compute startup

* Tue Mar 15 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.3.bzr802
- sudo configuration updated

* Tue Mar 15 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.2-0.2.bzr802
- Update to bzr802

* Mon Mar 14 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> 2011.2-0.1.bzr795
- Cactus pre-release build
- Changed release to better comply packaging policy
  https://fedoraproject.org/wiki/Packaging:NamingGuidelines
- /etc/nova/nova-api.conf -> /etc/nova/api-paste.ini
- guestfs patch migrated
- rhel config paths patch - added handling of api-paste.ini

* Wed Mar 02 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> 2011.1.1-5
- Changed logrotate script - it should not rotate empty logs

* Wed Mar 02 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> 2011.1.1-4
- Updated logrotate script with nova-ajax-console-proxy and nova-direct-api
  logfiles

* Wed Mar 02 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> 2011.1.1-3
- Added initscript for nova-ajax-console-proxy

* Wed Mar 02 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> 2011.1.1-2
- Added initscript for nova-direct-api

* Wed Mar 02 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> 2011.1.1-1
- Bugfix release 2011.1.1
- Added python-distutils-extra to BuildReqs

* Fri Feb 25 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> 2011.1-5
- Merged updated guestfs patch from Ilya Alekseyev
- Refactored guestfs patch - now it creates directory only if it does not exist

* Fri Feb 18 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> 2011.1-4
- Added patch with network interface template for RHEL guest OS
  (kudos to Ilya Alekseyev)

* Fri Feb 18 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> 2011.1-3
- Disabled SELinux for KVM images in libvirt.xml.template
- Added patch for image injection (kudos to Ilya Alekseyev).
- Updated dependencies

* Mon Feb 07 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> 2011.1-1
- Bexar release

* Wed Feb 02 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> 2011.1-bzr642
- Deleted patch from bzr638 rev because it was merged to trunk
- Updated dependencies
- Updated sudo configuration for nova user

* Mon Jan 31 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> 2011.1-bzr640
- Updated to bzr640

* Mon Jan 31 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> 2011.1-bzr639
- Added condrestart target to initscripts
- Added condrestart on package upgrade

* Mon Jan 31 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> 2011.1-bzr638
- Added patch openstack-nova-logging.py - re-routing unhandled exceptions to logs

* Thu Jan 27 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> 2011.1-bzr629
- Update to bzr629
- Refactored initscripts with start-stop-daemon since standard RHEL initscripts
  does not support creation of pidfiles
- Removed dependency on upstart
- All daemons are once again running under user nova instead of root

* Wed Jan 26 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> 2011.1-bzr621
- Updated to bzr621

* Mon Jan 24 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> 2011.1-bzr604
- Update to bzr604
- Added dependency on python-sqlalchemy-migrate

* Fri Jan 21 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> 2011.1-bzr598
- Updated to bzr598
- Updated patch for rhel paths

* Fri Jan 21 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> 2011.1-bzr597
- Added dependency for python-glance

* Tue Jan 18 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.1-bzr572
- Added /etc/nova/nova-api.conf
- Reworked openstack-nova-rhel-paths.patch
- Added dependencies for openstack-nova-api for paste & paste-deploy modules

* Mon Jan 17 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.1-bzr569
- Temporary commented logrotate script

* Fri Jan 14 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.1-bzr565
- Added build and runtime dep on python-netaddr

* Wed Jan 12 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.1-bzr553
- Added dep on python-cheetah from standard RHEL distro
- Temporary disabled build of -doc package to speed up testing env

* Wed Jan 12 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.1-bzr552
- Fixed bug with upstart configs

* Wed Jan 12 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.1-bzr551
- Moved initscripts to upstart

* Sat Jan 01 2011 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.1-bzr509
- Updated config patch
- Removed templates

* Tue Dec 14 2010 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.1-bzr464
- Changed dependency for python-daemon to = 1.5.5

* Tue Dec 14 2010 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.1-bzr460
- Added vconfig as a dep for python-nova

* Thu Dec 09 2010 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.1-bzr454
- Added postscript to openstac-nova package to add inclution of files to
  /etc/sudoers

* Thu Dec 09 2010 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.1-bzr453
- Added dependency >= 10.1.0 for twisted-core and twisted-web - 8.2.0 from RHEL6
  is not ok for use with nova-objectstore

* Wed Dec 01 2010 Andrey Brindeyev <abrindeyev@griddynamics.com> - 2011.1-bzr435
- Moved config files to separate package openstack-nova-cc-config for easy
  package-based deployment

* Thu Nov 04 2010 Silas Sewell <silas@sewell.ch> - 2010.1-2
- Fix various issues (init, permissions, config, etc..)

* Thu Oct 21 2010 Silas Sewell <silas@sewell.ch> - 2010.1-1
- Initial build
