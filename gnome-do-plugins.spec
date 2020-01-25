Summary:	Plugins for gnome-do
Name:		gnome-do-plugins
Version:	0.8.2.1
Release:	2
License:	GPL v3
Group:		X11/Applications
Source0:	http://edge.launchpad.net/do-plugins/0.8/0.8.2.1/+download/%{name}-%{version}.tar.gz
# Source0-md5:	32b88c062209e5b107602ccc5df285e7
Patch0:		%{name}-banshee_indexer.patch
Patch1:		%{name}-no-protected-struct.patch
Patch2:		%{name}-cs0834.patch
Patch3:		%{name}-firefox_iceweasel_rename.patch
Patch4:		%{name}-sqlite.patch
Patch5:		%{name}-pidgin.patch
Patch6:		%{name}-gcontacts.patch
URL:		http://do.davebsd.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-evolution-sharp-devel
BuildRequires:	dotnet-flickrnet
BuildRequires:	dotnet-gdata-sharp-devel
BuildRequires:	dotnet-gnome-desktop-sharp-devel
BuildRequires:	dotnet-gnome-keyring-sharp-devel
BuildRequires:	dotnet-gnome-sharp-devel
BuildRequires:	dotnet-gtk-sharp2-devel
BuildRequires:	dotnet-ndesk-dbus-glib-sharp-devel
BuildRequires:	dotnet-ndesk-dbus-sharp-devel
BuildRequires:	dotnet-notify-sharp-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel
BuildRequires:	gnome-do-devel >= 0.8.2-3
BuildRequires:	intltool
BuildRequires:	mono-addins-devel
BuildRequires:	mono-csharp >= 1.1.13
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugins for gnome-do.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%{__aclocal} -I m4/shamrock
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%defattr(644,root,root,755)
%doc AUTHORS
%dir %{_libdir}/gnome-do/plugins
%{_libdir}/gnome-do/plugins/*.dll
%{_libdir}/gnome-do/plugins/*.mdb
