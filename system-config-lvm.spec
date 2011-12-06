# -*- RPM-SPEC -*-
Summary: A utility for graphically configuring Logical Volumes
Name: system-config-lvm
Version: 1.1.12
Release: 7%{?dist}
URL: http://git.fedorahosted.org/git/?p=system-config-lvm.git 
Source0: %{name}-%{version}.tar.gz
License: GPLv2
Group: Applications/System
BuildArch: noarch
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires: usermode-gtk, /sbin/chkconfig
Requires: gnome-python2, pygtk2, pygtk2-libglade, gnome-python2-canvas 
Requires: gnome-python2-bonobo, gnome-python2-gnome
Requires: urw-fonts
Requires: lvm2 >= 2.00.20
Requires: python >= 2.3
BuildRequires: perl(XML::Parser) gettext intltool
BuildRequires: desktop-file-utils

Patch0: scl-adjustement.patch
Patch1: scl-correct_localization.patch
Patch2: scl-duplicate_entry_fstab.patch
Patch3: scl-localization_update.patch
Patch4: scl-volume_change_fails.patch
Patch5: scl-volume_change_fails2.patch
Patch6: scl-unable_to_add_new_entry_to_fstab.patch

%description
system-config-lvm is a utility for graphically configuring Logical Volumes

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

desktop-file-install --vendor system --delete-original		\
  --dir %{buildroot}%{_datadir}/applications			\
  --remove-category Application					\
 --remove-category SystemSetup					\
  --remove-category X-Red-Hat-Base				\
  --add-category Settings					\
  --add-category System						\
  %{buildroot}%{_datadir}/applications/system-config-lvm.desktop

%find_lang %name

%clean
rm -rf %{buildroot}

#Replace the files line with the one commented out when translations are done
%files -f %{name}.lang
#%files

%defattr(-,root,root)
%doc COPYING
#%doc docs/ReleaseNotes
#%doc docs/html/*
%{_sbindir}/*
%{_bindir}/*
%{_datadir}/applications/system-config-lvm.desktop
%{_datadir}/system-config-lvm
%config(noreplace) %{_sysconfdir}/pam.d/system-config-lvm
%config(noreplace) %{_sysconfdir}/security/console.apps/system-config-lvm

%changelog
* Wed Jul 28 2010 Marek Grac <mgrac@redhat.com> - 1.1.12-7
- Unable to add new entry to /etc/fstab 
- Resolves: rhbz#619040

* Fri Jun 18 2010 Marek Grac <mgrac@redhat.com> - 1.1.12-6
- system-config-lvm spec file cleanups
- Modification of volume size fails
- Resolves: rhbz#604174 rhbz#603770

* Fri May 07 2010 Marek Grac <mgrac@redhat.com> - 1.1.12-5
- Modification of volume size fails
- Update localization for supported languages
- Resolves: rhbz#585845 rhbz#584985

* Wed May 05 2010 Marek Grac <mgrac@redhat.com> - 1.1.12-4
- Localization problem at startup
- Extending LV creates a duplicate entry in /etc/fstab
- Cannot start due to missing module gnome 
- Resolves: rhbz#579055 rhbz#586554 rhbz#585501

* Wed Feb 24 2010 Marek Grac <mgrac@redhat.com> - 1.1.12-3
- Remove dependency on rhpl as it is not used anymore
- Resolves: rhbz#557593

* Mon Feb 15 2010 Marek Grac <mgrac@redhat.com> - 1.1.12-2
- Deprecation warning when run from terminal
- Resolves: rhbz#565489 

* Fri Jan 22 2010 Marek Grac <mgrac@redhat.com> - 1.1.12-1
- New version from Fedora 12

* Wed Jan 13 2010 Marek Grac <mgrac@redhat.com> - 1.1.11-1
- New version from Fedora 12
