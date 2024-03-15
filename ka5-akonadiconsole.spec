#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.5
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		akonadiconsole
Summary:	Akonadi Console
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	cadf3ecdc5374b3e2eb187098a631bcc
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= 5.15.2
BuildRequires:	Qt5DBus-devel >= 5.15.2
BuildRequires:	Qt5Gui-devel >= 5.15.2
BuildRequires:	Qt5Sql-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel >= 5.15.2
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	gpgme-qt5-devel
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
BuildRequires:	kf5-extra-cmake-modules >= 5.91.0
BuildRequires:	kf5-kauth-devel >= 5.93.0
BuildRequires:	kf5-kcalendarcore-devel >= 5.91.0
BuildRequires:	kf5-kcodecs-devel >= 5.93.0
BuildRequires:	kf5-kcompletion-devel >= 5.93.0
BuildRequires:	kf5-kconfig-devel >= 5.93.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.93.0
BuildRequires:	kf5-kcontacts-devel >= 5.91.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.93.0
BuildRequires:	kf5-kcrash-devel >= 5.91.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.91.0
BuildRequires:	kf5-kdoctools-devel >= 5.91.0
BuildRequires:	kf5-ki18n-devel >= 5.93.0
BuildRequires:	kf5-kio-devel >= 5.91.0
BuildRequires:	kf5-kitemmodels-devel >= 5.91.0
BuildRequires:	kf5-kitemviews-devel >= 5.93.0
BuildRequires:	kf5-kjobwidgets-devel >= 5.93.0
BuildRequires:	kf5-kservice-devel >= 5.91.0
BuildRequires:	kf5-ktextwidgets-devel >= 5.91.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.93.0
BuildRequires:	kf5-kxmlgui-devel >= 5.91.0
BuildRequires:	kf5-solid-devel >= 5.93.0
BuildRequires:	kf5-sonnet-devel >= 5.93.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xapian-core-devel
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/akonadiconsole
%ghost %{_libdir}/libakonadiconsole.so.5
%attr(755,root,root) %{_libdir}/libakonadiconsole.so.*.*.*
%{_desktopdir}/org.kde.akonadiconsole.desktop
%{_iconsdir}/hicolor/128x128/apps/akonadiconsole.png
%{_iconsdir}/hicolor/16x16/apps/akonadiconsole.png
%{_iconsdir}/hicolor/22x22/apps/akonadiconsole.png
%{_iconsdir}/hicolor/256x256/apps/akonadiconsole.png
%{_iconsdir}/hicolor/32x32/apps/akonadiconsole.png
%{_iconsdir}/hicolor/48x48/apps/akonadiconsole.png
%{_iconsdir}/hicolor/64x64/apps/akonadiconsole.png
%{_datadir}/qlogging-categories5/akonadiconsole.categories
%{_datadir}/qlogging-categories5/akonadiconsole.renamecategories
