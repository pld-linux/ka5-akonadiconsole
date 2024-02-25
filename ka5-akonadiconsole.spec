#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.01.95
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		akonadiconsole
Summary:	Akonadi Console
Name:		ka5-%{kaname}
Version:	24.01.95
Release:	0.1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/unstable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	f6dd46243334b3d598fbc53cfe29cc10
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= 5.15.2
BuildRequires:	Qt6DBus-devel >= 5.15.2
BuildRequires:	Qt6Gui-devel >= 5.15.2
BuildRequires:	Qt6Sql-devel
BuildRequires:	Qt6Test-devel
BuildRequires:	Qt6Widgets-devel >= 5.15.2
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	gpgme-qt6-devel
BuildRequires:	ka5-akonadi-calendar-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-contacts-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-search-devel >= %{kdeappsver}
BuildRequires:	ka5-calendarsupport-devel >= %{kdeappsver}
BuildRequires:	ka5-kidentitymanagement-devel >= %{kdeappsver}
BuildRequires:	ka5-kmime-devel >= %{kdeappsver}
BuildRequires:	ka5-kpimtextedit-devel >= %{kdeappsver}
BuildRequires:	ka5-libkdepim-devel >= %{kdeappsver}
BuildRequires:	ka5-messagelib-devel >= %{kdeappsver}
BuildRequires:	ka5-pimcommon-devel >= %{kdeappsver}
BuildRequires:	kf6-extra-cmake-modules >= 5.91.0
BuildRequires:	kf6-kauth-devel >= 5.93.0
BuildRequires:	kf6-kcalendarcore-devel >= 5.91.0
BuildRequires:	kf6-kcodecs-devel >= 5.93.0
BuildRequires:	kf6-kcompletion-devel >= 5.93.0
BuildRequires:	kf6-kconfig-devel >= 5.93.0
BuildRequires:	kf6-kconfigwidgets-devel >= 5.93.0
BuildRequires:	kf6-kcontacts-devel >= 5.91.0
BuildRequires:	kf6-kcoreaddons-devel >= 5.93.0
BuildRequires:	kf6-kcrash-devel >= 5.91.0
BuildRequires:	kf6-kdbusaddons-devel >= 5.91.0
BuildRequires:	kf6-kdoctools-devel >= 5.91.0
BuildRequires:	kf6-ki18n-devel >= 5.93.0
BuildRequires:	kf6-kio-devel >= 5.91.0
BuildRequires:	kf6-kitemmodels-devel >= 5.91.0
BuildRequires:	kf6-kitemviews-devel >= 5.93.0
BuildRequires:	kf6-kjobwidgets-devel >= 5.93.0
BuildRequires:	kf6-kservice-devel >= 5.91.0
BuildRequires:	kf6-ktextwidgets-devel >= 5.91.0
BuildRequires:	kf6-kwidgetsaddons-devel >= 5.93.0
BuildRequires:	kf6-kxmlgui-devel >= 5.91.0
BuildRequires:	kf6-solid-devel >= 5.93.0
BuildRequires:	kf6-sonnet-devel >= 5.93.0
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xapian-core-devel
BuildRequires:	xz
ExcludeArch:	x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Akonadi console.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/akonadiconsole
%ghost %{_libdir}/libakonadiconsole.so.6
%attr(755,root,root) %{_libdir}/libakonadiconsole.so.*.*
%{_desktopdir}/org.kde.akonadiconsole.desktop
%{_iconsdir}/hicolor/*x*/apps/akonadiconsole.png
%{_datadir}/qlogging-categories6/akonadiconsole.categories
%{_datadir}/qlogging-categories6/akonadiconsole.renamecategories
