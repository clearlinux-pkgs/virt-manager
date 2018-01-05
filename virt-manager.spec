#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : virt-manager
Version  : 1.4.3
Release  : 4
URL      : https://virt-manager.org/download/sources/virt-manager/virt-manager-1.4.3.tar.gz
Source0  : https://virt-manager.org/download/sources/virt-manager/virt-manager-1.4.3.tar.gz
Summary  : Desktop tool for managing virtual machines via libvirt
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: virt-manager-bin
Requires: virt-manager-data
Requires: virt-manager-locales
Requires: virt-manager-doc
Requires: ipaddr-python
Requires: libosinfo
Requires: libvirt-python
BuildRequires : glib-bin
BuildRequires : intltool
BuildRequires : ipaddr-python
BuildRequires : libosinfo
BuildRequires : libvirt-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Virtual Machine Manager provides a graphical tool for administering virtual
machines for KVM, Xen, and LXC. Start, stop, add or remove virtual devices,
connect to a graphical or serial console, and see resource usage statistics
for existing VMs on local or remote machines. Uses libvirt as the backend
management API.

%package bin
Summary: bin components for the virt-manager package.
Group: Binaries
Requires: virt-manager-data

%description bin
bin components for the virt-manager package.


%package data
Summary: data components for the virt-manager package.
Group: Data

%description data
data components for the virt-manager package.


%package doc
Summary: doc components for the virt-manager package.
Group: Documentation

%description doc
doc components for the virt-manager package.


%package locales
Summary: locales components for the virt-manager package.
Group: Default

%description locales
locales components for the virt-manager package.


%prep
%setup -q -n virt-manager-1.4.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1515168051
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
%find_lang virt-manager

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/virt-clone
/usr/bin/virt-convert
/usr/bin/virt-install
/usr/bin/virt-manager
/usr/bin/virt-xml

%files data
%defattr(-,root,root,-)
/usr/share/GConf/gsettings/org.virt-manager.virt-manager.convert
/usr/share/appdata/virt-manager.appdata.xml
/usr/share/applications/virt-manager.desktop
/usr/share/glib-2.0/schemas/gschemas.compiled
/usr/share/glib-2.0/schemas/org.virt-manager.virt-manager.gschema.xml
/usr/share/icons/hicolor/16x16/apps/virt-manager.png
/usr/share/icons/hicolor/22x22/apps/virt-manager.png
/usr/share/icons/hicolor/24x24/apps/virt-manager.png
/usr/share/icons/hicolor/256x256/apps/virt-manager.png
/usr/share/icons/hicolor/32x32/apps/virt-manager.png
/usr/share/icons/hicolor/48x48/apps/virt-manager.png
/usr/share/icons/hicolor/icon-theme.cache
/usr/share/virt-manager/icons/hicolor/16x16/actions/icon_console.png
/usr/share/virt-manager/icons/hicolor/16x16/actions/vm_new.png
/usr/share/virt-manager/icons/hicolor/22x22/actions/icon_console.png
/usr/share/virt-manager/icons/hicolor/22x22/actions/icon_details.png
/usr/share/virt-manager/icons/hicolor/22x22/actions/vm_new.png
/usr/share/virt-manager/icons/hicolor/22x22/devices/device_cpu.png
/usr/share/virt-manager/icons/hicolor/22x22/devices/device_mem.png
/usr/share/virt-manager/icons/hicolor/22x22/devices/device_pci.png
/usr/share/virt-manager/icons/hicolor/22x22/devices/device_serial.png
/usr/share/virt-manager/icons/hicolor/22x22/devices/device_usb.png
/usr/share/virt-manager/icons/hicolor/22x22/status/state_paused.png
/usr/share/virt-manager/icons/hicolor/22x22/status/state_running.png
/usr/share/virt-manager/icons/hicolor/22x22/status/state_shutoff.png
/usr/share/virt-manager/icons/hicolor/24x24/actions/icon_console.png
/usr/share/virt-manager/icons/hicolor/24x24/actions/vm_clone_wizard.png
/usr/share/virt-manager/icons/hicolor/24x24/actions/vm_new.png
/usr/share/virt-manager/icons/hicolor/32x32/actions/icon_console.png
/usr/share/virt-manager/icons/hicolor/32x32/actions/vm_new.png
/usr/share/virt-manager/icons/hicolor/32x32/status/state_paused.png
/usr/share/virt-manager/icons/hicolor/32x32/status/state_running.png
/usr/share/virt-manager/icons/hicolor/32x32/status/state_shutoff.png
/usr/share/virt-manager/icons/hicolor/48x48/actions/vm_clone_wizard.png
/usr/share/virt-manager/icons/hicolor/48x48/actions/vm_delete_wizard.png
/usr/share/virt-manager/icons/hicolor/48x48/actions/vm_import_wizard.png
/usr/share/virt-manager/icons/hicolor/48x48/actions/vm_new_wizard.png
/usr/share/virt-manager/ui/about.ui
/usr/share/virt-manager/ui/addhardware.ui
/usr/share/virt-manager/ui/addstorage.ui
/usr/share/virt-manager/ui/asyncjob.ui
/usr/share/virt-manager/ui/choosecd.ui
/usr/share/virt-manager/ui/clone.ui
/usr/share/virt-manager/ui/connect.ui
/usr/share/virt-manager/ui/create.ui
/usr/share/virt-manager/ui/createinterface.ui
/usr/share/virt-manager/ui/createnet.ui
/usr/share/virt-manager/ui/createpool.ui
/usr/share/virt-manager/ui/createvol.ui
/usr/share/virt-manager/ui/delete.ui
/usr/share/virt-manager/ui/details.ui
/usr/share/virt-manager/ui/fsdetails.ui
/usr/share/virt-manager/ui/gfxdetails.ui
/usr/share/virt-manager/ui/host.ui
/usr/share/virt-manager/ui/manager.ui
/usr/share/virt-manager/ui/migrate.ui
/usr/share/virt-manager/ui/netlist.ui
/usr/share/virt-manager/ui/preferences.ui
/usr/share/virt-manager/ui/snapshots.ui
/usr/share/virt-manager/ui/storagebrowse.ui
/usr/share/virt-manager/ui/storagelist.ui
/usr/share/virt-manager/virt-clone
/usr/share/virt-manager/virt-convert
/usr/share/virt-manager/virt-install
/usr/share/virt-manager/virt-manager
/usr/share/virt-manager/virt-xml
/usr/share/virt-manager/virtManager/__init__.py
/usr/share/virt-manager/virtManager/__init__.pyc
/usr/share/virt-manager/virtManager/about.py
/usr/share/virt-manager/virtManager/about.pyc
/usr/share/virt-manager/virtManager/addhardware.py
/usr/share/virt-manager/virtManager/addhardware.pyc
/usr/share/virt-manager/virtManager/addstorage.py
/usr/share/virt-manager/virtManager/addstorage.pyc
/usr/share/virt-manager/virtManager/asyncjob.py
/usr/share/virt-manager/virtManager/asyncjob.pyc
/usr/share/virt-manager/virtManager/baseclass.py
/usr/share/virt-manager/virtManager/baseclass.pyc
/usr/share/virt-manager/virtManager/choosecd.py
/usr/share/virt-manager/virtManager/choosecd.pyc
/usr/share/virt-manager/virtManager/clone.py
/usr/share/virt-manager/virtManager/clone.pyc
/usr/share/virt-manager/virtManager/config.py
/usr/share/virt-manager/virtManager/config.pyc
/usr/share/virt-manager/virtManager/connect.py
/usr/share/virt-manager/virtManager/connect.pyc
/usr/share/virt-manager/virtManager/connectauth.py
/usr/share/virt-manager/virtManager/connectauth.pyc
/usr/share/virt-manager/virtManager/connection.py
/usr/share/virt-manager/virtManager/connection.pyc
/usr/share/virt-manager/virtManager/console.py
/usr/share/virt-manager/virtManager/console.pyc
/usr/share/virt-manager/virtManager/create.py
/usr/share/virt-manager/virtManager/create.pyc
/usr/share/virt-manager/virtManager/createinterface.py
/usr/share/virt-manager/virtManager/createinterface.pyc
/usr/share/virt-manager/virtManager/createnet.py
/usr/share/virt-manager/virtManager/createnet.pyc
/usr/share/virt-manager/virtManager/createpool.py
/usr/share/virt-manager/virtManager/createpool.pyc
/usr/share/virt-manager/virtManager/createvol.py
/usr/share/virt-manager/virtManager/createvol.pyc
/usr/share/virt-manager/virtManager/delete.py
/usr/share/virt-manager/virtManager/delete.pyc
/usr/share/virt-manager/virtManager/details.py
/usr/share/virt-manager/virtManager/details.pyc
/usr/share/virt-manager/virtManager/domain.py
/usr/share/virt-manager/virtManager/domain.pyc
/usr/share/virt-manager/virtManager/engine.py
/usr/share/virt-manager/virtManager/engine.pyc
/usr/share/virt-manager/virtManager/error.py
/usr/share/virt-manager/virtManager/error.pyc
/usr/share/virt-manager/virtManager/fsdetails.py
/usr/share/virt-manager/virtManager/fsdetails.pyc
/usr/share/virt-manager/virtManager/gfxdetails.py
/usr/share/virt-manager/virtManager/gfxdetails.pyc
/usr/share/virt-manager/virtManager/graphwidgets.py
/usr/share/virt-manager/virtManager/graphwidgets.pyc
/usr/share/virt-manager/virtManager/host.py
/usr/share/virt-manager/virtManager/host.pyc
/usr/share/virt-manager/virtManager/inspection.py
/usr/share/virt-manager/virtManager/inspection.pyc
/usr/share/virt-manager/virtManager/interface.py
/usr/share/virt-manager/virtManager/interface.pyc
/usr/share/virt-manager/virtManager/keyring.py
/usr/share/virt-manager/virtManager/keyring.pyc
/usr/share/virt-manager/virtManager/libvirtobject.py
/usr/share/virt-manager/virtManager/libvirtobject.pyc
/usr/share/virt-manager/virtManager/manager.py
/usr/share/virt-manager/virtManager/manager.pyc
/usr/share/virt-manager/virtManager/mediacombo.py
/usr/share/virt-manager/virtManager/mediacombo.pyc
/usr/share/virt-manager/virtManager/migrate.py
/usr/share/virt-manager/virtManager/migrate.pyc
/usr/share/virt-manager/virtManager/module_trace.py
/usr/share/virt-manager/virtManager/module_trace.pyc
/usr/share/virt-manager/virtManager/netlist.py
/usr/share/virt-manager/virtManager/netlist.pyc
/usr/share/virt-manager/virtManager/network.py
/usr/share/virt-manager/virtManager/network.pyc
/usr/share/virt-manager/virtManager/nodedev.py
/usr/share/virt-manager/virtManager/nodedev.pyc
/usr/share/virt-manager/virtManager/packageutils.py
/usr/share/virt-manager/virtManager/packageutils.pyc
/usr/share/virt-manager/virtManager/preferences.py
/usr/share/virt-manager/virtManager/preferences.pyc
/usr/share/virt-manager/virtManager/serialcon.py
/usr/share/virt-manager/virtManager/serialcon.pyc
/usr/share/virt-manager/virtManager/snapshots.py
/usr/share/virt-manager/virtManager/snapshots.pyc
/usr/share/virt-manager/virtManager/sshtunnels.py
/usr/share/virt-manager/virtManager/sshtunnels.pyc
/usr/share/virt-manager/virtManager/storagebrowse.py
/usr/share/virt-manager/virtManager/storagebrowse.pyc
/usr/share/virt-manager/virtManager/storagelist.py
/usr/share/virt-manager/virtManager/storagelist.pyc
/usr/share/virt-manager/virtManager/storagepool.py
/usr/share/virt-manager/virtManager/storagepool.pyc
/usr/share/virt-manager/virtManager/systray.py
/usr/share/virt-manager/virtManager/systray.pyc
/usr/share/virt-manager/virtManager/uiutil.py
/usr/share/virt-manager/virtManager/uiutil.pyc
/usr/share/virt-manager/virtManager/viewers.py
/usr/share/virt-manager/virtManager/viewers.pyc
/usr/share/virt-manager/virtManager/vmmenu.py
/usr/share/virt-manager/virtManager/vmmenu.pyc
/usr/share/virt-manager/virtcli/__init__.py
/usr/share/virt-manager/virtcli/__init__.pyc
/usr/share/virt-manager/virtcli/cliconfig.py
/usr/share/virt-manager/virtcli/cliconfig.pyc
/usr/share/virt-manager/virtconv/__init__.py
/usr/share/virt-manager/virtconv/__init__.pyc
/usr/share/virt-manager/virtconv/formats.py
/usr/share/virt-manager/virtconv/formats.pyc
/usr/share/virt-manager/virtconv/ovf.py
/usr/share/virt-manager/virtconv/ovf.pyc
/usr/share/virt-manager/virtconv/vmx.py
/usr/share/virt-manager/virtconv/vmx.pyc
/usr/share/virt-manager/virtinst/__init__.py
/usr/share/virt-manager/virtinst/__init__.pyc
/usr/share/virt-manager/virtinst/capabilities.py
/usr/share/virt-manager/virtinst/capabilities.pyc
/usr/share/virt-manager/virtinst/cli.py
/usr/share/virt-manager/virtinst/cli.pyc
/usr/share/virt-manager/virtinst/clock.py
/usr/share/virt-manager/virtinst/clock.pyc
/usr/share/virt-manager/virtinst/cloner.py
/usr/share/virt-manager/virtinst/cloner.pyc
/usr/share/virt-manager/virtinst/connection.py
/usr/share/virt-manager/virtinst/connection.pyc
/usr/share/virt-manager/virtinst/cpu.py
/usr/share/virt-manager/virtinst/cpu.pyc
/usr/share/virt-manager/virtinst/device.py
/usr/share/virt-manager/virtinst/device.pyc
/usr/share/virt-manager/virtinst/deviceaudio.py
/usr/share/virt-manager/virtinst/deviceaudio.pyc
/usr/share/virt-manager/virtinst/devicechar.py
/usr/share/virt-manager/virtinst/devicechar.pyc
/usr/share/virt-manager/virtinst/devicecontroller.py
/usr/share/virt-manager/virtinst/devicecontroller.pyc
/usr/share/virt-manager/virtinst/devicedisk.py
/usr/share/virt-manager/virtinst/devicedisk.pyc
/usr/share/virt-manager/virtinst/devicefilesystem.py
/usr/share/virt-manager/virtinst/devicefilesystem.pyc
/usr/share/virt-manager/virtinst/devicegraphics.py
/usr/share/virt-manager/virtinst/devicegraphics.pyc
/usr/share/virt-manager/virtinst/devicehostdev.py
/usr/share/virt-manager/virtinst/devicehostdev.pyc
/usr/share/virt-manager/virtinst/deviceinput.py
/usr/share/virt-manager/virtinst/deviceinput.pyc
/usr/share/virt-manager/virtinst/deviceinterface.py
/usr/share/virt-manager/virtinst/deviceinterface.pyc
/usr/share/virt-manager/virtinst/devicememballoon.py
/usr/share/virt-manager/virtinst/devicememballoon.pyc
/usr/share/virt-manager/virtinst/devicememory.py
/usr/share/virt-manager/virtinst/devicememory.pyc
/usr/share/virt-manager/virtinst/devicepanic.py
/usr/share/virt-manager/virtinst/devicepanic.pyc
/usr/share/virt-manager/virtinst/deviceredirdev.py
/usr/share/virt-manager/virtinst/deviceredirdev.pyc
/usr/share/virt-manager/virtinst/devicerng.py
/usr/share/virt-manager/virtinst/devicerng.pyc
/usr/share/virt-manager/virtinst/devicesmartcard.py
/usr/share/virt-manager/virtinst/devicesmartcard.pyc
/usr/share/virt-manager/virtinst/devicetpm.py
/usr/share/virt-manager/virtinst/devicetpm.pyc
/usr/share/virt-manager/virtinst/devicevideo.py
/usr/share/virt-manager/virtinst/devicevideo.pyc
/usr/share/virt-manager/virtinst/devicewatchdog.py
/usr/share/virt-manager/virtinst/devicewatchdog.pyc
/usr/share/virt-manager/virtinst/diskbackend.py
/usr/share/virt-manager/virtinst/diskbackend.pyc
/usr/share/virt-manager/virtinst/distroinstaller.py
/usr/share/virt-manager/virtinst/distroinstaller.pyc
/usr/share/virt-manager/virtinst/domainblkiotune.py
/usr/share/virt-manager/virtinst/domainblkiotune.pyc
/usr/share/virt-manager/virtinst/domainfeatures.py
/usr/share/virt-manager/virtinst/domainfeatures.pyc
/usr/share/virt-manager/virtinst/domainmemorybacking.py
/usr/share/virt-manager/virtinst/domainmemorybacking.pyc
/usr/share/virt-manager/virtinst/domainmemorytune.py
/usr/share/virt-manager/virtinst/domainmemorytune.pyc
/usr/share/virt-manager/virtinst/domainnumatune.py
/usr/share/virt-manager/virtinst/domainnumatune.pyc
/usr/share/virt-manager/virtinst/domainresource.py
/usr/share/virt-manager/virtinst/domainresource.pyc
/usr/share/virt-manager/virtinst/domcapabilities.py
/usr/share/virt-manager/virtinst/domcapabilities.pyc
/usr/share/virt-manager/virtinst/guest.py
/usr/share/virt-manager/virtinst/guest.pyc
/usr/share/virt-manager/virtinst/hostkeymap.py
/usr/share/virt-manager/virtinst/hostkeymap.pyc
/usr/share/virt-manager/virtinst/idmap.py
/usr/share/virt-manager/virtinst/idmap.pyc
/usr/share/virt-manager/virtinst/initrdinject.py
/usr/share/virt-manager/virtinst/initrdinject.pyc
/usr/share/virt-manager/virtinst/installer.py
/usr/share/virt-manager/virtinst/installer.pyc
/usr/share/virt-manager/virtinst/interface.py
/usr/share/virt-manager/virtinst/interface.pyc
/usr/share/virt-manager/virtinst/kernelupload.py
/usr/share/virt-manager/virtinst/kernelupload.pyc
/usr/share/virt-manager/virtinst/network.py
/usr/share/virt-manager/virtinst/network.pyc
/usr/share/virt-manager/virtinst/nodedev.py
/usr/share/virt-manager/virtinst/nodedev.pyc
/usr/share/virt-manager/virtinst/osdict.py
/usr/share/virt-manager/virtinst/osdict.pyc
/usr/share/virt-manager/virtinst/osxml.py
/usr/share/virt-manager/virtinst/osxml.pyc
/usr/share/virt-manager/virtinst/pm.py
/usr/share/virt-manager/virtinst/pm.pyc
/usr/share/virt-manager/virtinst/pollhelpers.py
/usr/share/virt-manager/virtinst/pollhelpers.pyc
/usr/share/virt-manager/virtinst/progress.py
/usr/share/virt-manager/virtinst/progress.pyc
/usr/share/virt-manager/virtinst/seclabel.py
/usr/share/virt-manager/virtinst/seclabel.pyc
/usr/share/virt-manager/virtinst/snapshot.py
/usr/share/virt-manager/virtinst/snapshot.pyc
/usr/share/virt-manager/virtinst/storage.py
/usr/share/virt-manager/virtinst/storage.pyc
/usr/share/virt-manager/virtinst/support.py
/usr/share/virt-manager/virtinst/support.pyc
/usr/share/virt-manager/virtinst/sysinfo.py
/usr/share/virt-manager/virtinst/sysinfo.pyc
/usr/share/virt-manager/virtinst/uri.py
/usr/share/virt-manager/virtinst/uri.pyc
/usr/share/virt-manager/virtinst/urlfetcher.py
/usr/share/virt-manager/virtinst/urlfetcher.pyc
/usr/share/virt-manager/virtinst/util.py
/usr/share/virt-manager/virtinst/util.pyc
/usr/share/virt-manager/virtinst/xmlbuilder.py
/usr/share/virt-manager/virtinst/xmlbuilder.pyc
/usr/share/virt-manager/virtinst/xmlnsqemu.py
/usr/share/virt-manager/virtinst/xmlnsqemu.pyc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files locales -f virt-manager.lang
%defattr(-,root,root,-)

