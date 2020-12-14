#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : virt-manager
Version  : 2.2.1
Release  : 29
URL      : https://virt-manager.org/download/sources/virt-manager/virt-manager-2.2.1.tar.gz
Source0  : https://virt-manager.org/download/sources/virt-manager/virt-manager-2.2.1.tar.gz
Summary  : Desktop tool for managing virtual machines via libvirt
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: virt-manager-bin = %{version}-%{release}
Requires: virt-manager-data = %{version}-%{release}
Requires: virt-manager-license = %{version}-%{release}
Requires: virt-manager-locales = %{version}-%{release}
Requires: virt-manager-man = %{version}-%{release}
Requires: ipaddr-python
Requires: libcdio
Requires: libosinfo
Requires: libvirt-glib
Requires: libvirt-python
Requires: libxml2-python
Requires: osinfo-db-tools
Requires: pygobject-python
Requires: requests
BuildRequires : buildreq-distutils3
BuildRequires : glib-bin
BuildRequires : intltool
BuildRequires : ipaddr-python
BuildRequires : libcdio
BuildRequires : libosinfo
BuildRequires : libvirt-glib
BuildRequires : libvirt-python
BuildRequires : libxml2-python
BuildRequires : osinfo-db-tools
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pygobject
BuildRequires : requests

%description
Virtual Machine Manager provides a graphical tool for administering virtual
machines for KVM, Xen, and LXC. Start, stop, add or remove virtual devices,
connect to a graphical or serial console, and see resource usage statistics
for existing VMs on local or remote machines. Uses libvirt as the backend
management API.

%package bin
Summary: bin components for the virt-manager package.
Group: Binaries
Requires: virt-manager-data = %{version}-%{release}
Requires: virt-manager-license = %{version}-%{release}

%description bin
bin components for the virt-manager package.


%package data
Summary: data components for the virt-manager package.
Group: Data

%description data
data components for the virt-manager package.


%package license
Summary: license components for the virt-manager package.
Group: Default

%description license
license components for the virt-manager package.


%package locales
Summary: locales components for the virt-manager package.
Group: Default

%description locales
locales components for the virt-manager package.


%package man
Summary: man components for the virt-manager package.
Group: Default

%description man
man components for the virt-manager package.


%prep
%setup -q -n virt-manager-2.2.1
cd %{_builddir}/virt-manager-2.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1580932093
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python3 setup.py test || true
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/virt-manager
cp %{_builddir}/virt-manager-2.2.1/COPYING %{buildroot}/usr/share/package-licenses/virt-manager/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
%find_lang virt-manager
## Remove excluded files
rm -f %{buildroot}/usr/share/icons/hicolor/icon-theme.cache
rm -f %{buildroot}/usr/share/glib-2.0/schemas/gschemas.compiled

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
/usr/share/appdata/virt-manager.appdata.xml
/usr/share/applications/virt-manager.desktop
/usr/share/bash-completion/completions/virt-clone
/usr/share/bash-completion/completions/virt-convert
/usr/share/bash-completion/completions/virt-install
/usr/share/bash-completion/completions/virt-xml
/usr/share/glib-2.0/schemas/org.virt-manager.virt-manager.gschema.xml
/usr/share/icons/hicolor/16x16/apps/virt-manager.png
/usr/share/icons/hicolor/22x22/apps/virt-manager.png
/usr/share/icons/hicolor/24x24/apps/virt-manager.png
/usr/share/icons/hicolor/256x256/apps/virt-manager.png
/usr/share/icons/hicolor/32x32/apps/virt-manager.png
/usr/share/icons/hicolor/48x48/apps/virt-manager.png
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
/usr/share/virt-manager/ui/clone.ui
/usr/share/virt-manager/ui/connectauth.ui
/usr/share/virt-manager/ui/createconn.ui
/usr/share/virt-manager/ui/createnet.ui
/usr/share/virt-manager/ui/createpool.ui
/usr/share/virt-manager/ui/createvm.ui
/usr/share/virt-manager/ui/createvol.ui
/usr/share/virt-manager/ui/delete.ui
/usr/share/virt-manager/ui/details.ui
/usr/share/virt-manager/ui/fsdetails.ui
/usr/share/virt-manager/ui/gfxdetails.ui
/usr/share/virt-manager/ui/host.ui
/usr/share/virt-manager/ui/hostnets.ui
/usr/share/virt-manager/ui/hoststorage.ui
/usr/share/virt-manager/ui/manager.ui
/usr/share/virt-manager/ui/migrate.ui
/usr/share/virt-manager/ui/netlist.ui
/usr/share/virt-manager/ui/oslist.ui
/usr/share/virt-manager/ui/preferences.ui
/usr/share/virt-manager/ui/snapshots.ui
/usr/share/virt-manager/ui/snapshotsnew.ui
/usr/share/virt-manager/ui/storagebrowse.ui
/usr/share/virt-manager/ui/vmwindow.ui
/usr/share/virt-manager/ui/vsockdetails.ui
/usr/share/virt-manager/ui/xmleditor.ui
/usr/share/virt-manager/virt-clone
/usr/share/virt-manager/virt-convert
/usr/share/virt-manager/virt-install
/usr/share/virt-manager/virt-manager
/usr/share/virt-manager/virt-xml
/usr/share/virt-manager/virtManager/__init__.py
/usr/share/virt-manager/virtManager/about.py
/usr/share/virt-manager/virtManager/addhardware.py
/usr/share/virt-manager/virtManager/asyncjob.py
/usr/share/virt-manager/virtManager/baseclass.py
/usr/share/virt-manager/virtManager/clone.py
/usr/share/virt-manager/virtManager/config.py
/usr/share/virt-manager/virtManager/connection.py
/usr/share/virt-manager/virtManager/connmanager.py
/usr/share/virt-manager/virtManager/createconn.py
/usr/share/virt-manager/virtManager/createnet.py
/usr/share/virt-manager/virtManager/createpool.py
/usr/share/virt-manager/virtManager/createvm.py
/usr/share/virt-manager/virtManager/createvol.py
/usr/share/virt-manager/virtManager/delete.py
/usr/share/virt-manager/virtManager/details/__init__.py
/usr/share/virt-manager/virtManager/details/console.py
/usr/share/virt-manager/virtManager/details/details.py
/usr/share/virt-manager/virtManager/details/serialcon.py
/usr/share/virt-manager/virtManager/details/snapshots.py
/usr/share/virt-manager/virtManager/details/sshtunnels.py
/usr/share/virt-manager/virtManager/details/viewers.py
/usr/share/virt-manager/virtManager/device/__init__.py
/usr/share/virt-manager/virtManager/device/addstorage.py
/usr/share/virt-manager/virtManager/device/fsdetails.py
/usr/share/virt-manager/virtManager/device/gfxdetails.py
/usr/share/virt-manager/virtManager/device/mediacombo.py
/usr/share/virt-manager/virtManager/device/netlist.py
/usr/share/virt-manager/virtManager/device/vsockdetails.py
/usr/share/virt-manager/virtManager/engine.py
/usr/share/virt-manager/virtManager/error.py
/usr/share/virt-manager/virtManager/host.py
/usr/share/virt-manager/virtManager/hostnets.py
/usr/share/virt-manager/virtManager/hoststorage.py
/usr/share/virt-manager/virtManager/lib/__init__.py
/usr/share/virt-manager/virtManager/lib/connectauth.py
/usr/share/virt-manager/virtManager/lib/graphwidgets.py
/usr/share/virt-manager/virtManager/lib/inspection.py
/usr/share/virt-manager/virtManager/lib/keyring.py
/usr/share/virt-manager/virtManager/lib/libvirtenummap.py
/usr/share/virt-manager/virtManager/lib/module_trace.py
/usr/share/virt-manager/virtManager/lib/statsmanager.py
/usr/share/virt-manager/virtManager/lib/uiutil.py
/usr/share/virt-manager/virtManager/manager.py
/usr/share/virt-manager/virtManager/migrate.py
/usr/share/virt-manager/virtManager/object/__init__.py
/usr/share/virt-manager/virtManager/object/domain.py
/usr/share/virt-manager/virtManager/object/interface.py
/usr/share/virt-manager/virtManager/object/libvirtobject.py
/usr/share/virt-manager/virtManager/object/network.py
/usr/share/virt-manager/virtManager/object/nodedev.py
/usr/share/virt-manager/virtManager/object/storagepool.py
/usr/share/virt-manager/virtManager/oslist.py
/usr/share/virt-manager/virtManager/preferences.py
/usr/share/virt-manager/virtManager/storagebrowse.py
/usr/share/virt-manager/virtManager/systray.py
/usr/share/virt-manager/virtManager/vmmenu.py
/usr/share/virt-manager/virtManager/vmwindow.py
/usr/share/virt-manager/virtManager/xmleditor.py
/usr/share/virt-manager/virtconv/__init__.py
/usr/share/virt-manager/virtconv/formats.py
/usr/share/virt-manager/virtconv/ovf.py
/usr/share/virt-manager/virtconv/vmx.py
/usr/share/virt-manager/virtinst/__init__.py
/usr/share/virt-manager/virtinst/buildconfig.py
/usr/share/virt-manager/virtinst/capabilities.py
/usr/share/virt-manager/virtinst/cli.py
/usr/share/virt-manager/virtinst/cloner.py
/usr/share/virt-manager/virtinst/connection.py
/usr/share/virt-manager/virtinst/devices/__init__.py
/usr/share/virt-manager/virtinst/devices/char.py
/usr/share/virt-manager/virtinst/devices/controller.py
/usr/share/virt-manager/virtinst/devices/device.py
/usr/share/virt-manager/virtinst/devices/disk.py
/usr/share/virt-manager/virtinst/devices/filesystem.py
/usr/share/virt-manager/virtinst/devices/graphics.py
/usr/share/virt-manager/virtinst/devices/hostdev.py
/usr/share/virt-manager/virtinst/devices/input.py
/usr/share/virt-manager/virtinst/devices/interface.py
/usr/share/virt-manager/virtinst/devices/memballoon.py
/usr/share/virt-manager/virtinst/devices/memory.py
/usr/share/virt-manager/virtinst/devices/panic.py
/usr/share/virt-manager/virtinst/devices/redirdev.py
/usr/share/virt-manager/virtinst/devices/rng.py
/usr/share/virt-manager/virtinst/devices/smartcard.py
/usr/share/virt-manager/virtinst/devices/sound.py
/usr/share/virt-manager/virtinst/devices/tpm.py
/usr/share/virt-manager/virtinst/devices/video.py
/usr/share/virt-manager/virtinst/devices/vsock.py
/usr/share/virt-manager/virtinst/devices/watchdog.py
/usr/share/virt-manager/virtinst/diskbackend.py
/usr/share/virt-manager/virtinst/domain/__init__.py
/usr/share/virt-manager/virtinst/domain/blkiotune.py
/usr/share/virt-manager/virtinst/domain/clock.py
/usr/share/virt-manager/virtinst/domain/cpu.py
/usr/share/virt-manager/virtinst/domain/cputune.py
/usr/share/virt-manager/virtinst/domain/features.py
/usr/share/virt-manager/virtinst/domain/idmap.py
/usr/share/virt-manager/virtinst/domain/launch_security.py
/usr/share/virt-manager/virtinst/domain/memorybacking.py
/usr/share/virt-manager/virtinst/domain/memtune.py
/usr/share/virt-manager/virtinst/domain/metadata.py
/usr/share/virt-manager/virtinst/domain/numatune.py
/usr/share/virt-manager/virtinst/domain/os.py
/usr/share/virt-manager/virtinst/domain/pm.py
/usr/share/virt-manager/virtinst/domain/resource.py
/usr/share/virt-manager/virtinst/domain/seclabel.py
/usr/share/virt-manager/virtinst/domain/sysinfo.py
/usr/share/virt-manager/virtinst/domain/vcpus.py
/usr/share/virt-manager/virtinst/domain/xmlnsqemu.py
/usr/share/virt-manager/virtinst/domcapabilities.py
/usr/share/virt-manager/virtinst/generatename.py
/usr/share/virt-manager/virtinst/guest.py
/usr/share/virt-manager/virtinst/hostkeymap.py
/usr/share/virt-manager/virtinst/install/__init__.py
/usr/share/virt-manager/virtinst/install/installer.py
/usr/share/virt-manager/virtinst/install/installerinject.py
/usr/share/virt-manager/virtinst/install/installertreemedia.py
/usr/share/virt-manager/virtinst/install/kernelupload.py
/usr/share/virt-manager/virtinst/install/unattended.py
/usr/share/virt-manager/virtinst/install/urldetect.py
/usr/share/virt-manager/virtinst/install/urlfetcher.py
/usr/share/virt-manager/virtinst/interface.py
/usr/share/virt-manager/virtinst/logger.py
/usr/share/virt-manager/virtinst/network.py
/usr/share/virt-manager/virtinst/nodedev.py
/usr/share/virt-manager/virtinst/osdict.py
/usr/share/virt-manager/virtinst/pollhelpers.py
/usr/share/virt-manager/virtinst/progress.py
/usr/share/virt-manager/virtinst/snapshot.py
/usr/share/virt-manager/virtinst/storage.py
/usr/share/virt-manager/virtinst/support.py
/usr/share/virt-manager/virtinst/uri.py
/usr/share/virt-manager/virtinst/xmlapi.py
/usr/share/virt-manager/virtinst/xmlbuilder.py
/usr/share/virt-manager/virtinst/xmlutil.py

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/virt-manager/06877624ea5c77efe3b7e39b0f909eda6e25a4ec

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/virt-clone.1
/usr/share/man/man1/virt-convert.1
/usr/share/man/man1/virt-install.1
/usr/share/man/man1/virt-manager.1
/usr/share/man/man1/virt-xml.1

%files locales -f virt-manager.lang
%defattr(-,root,root,-)

