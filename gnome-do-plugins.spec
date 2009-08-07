%include	/usr/lib/rpm/macros.mono
Summary:	Plugins for gnome-do
Name:		gnome-do-plugins
Version:	0.8.2
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0: http://edge.launchpad.net/do-plugins/0.8/0.8.2/+download/%{name}-%{version}.tar.gz
# Source0-md5:	6e79a666619aae1b1e2916f0fe364d94
URL:		http://do.davebsd.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-evolution-sharp-devel
BuildRequires:	dotnet-gnome-sharp-devel
BuildRequires:	dotnet-gtk-sharp2-devel
BuildRequires:	dotnet-ndesk-dbus-glib-sharp-devel
BuildRequires:	dotnet-ndesk-dbus-sharp-devel
BuildRequires:	dotnet-flickrnet
BuildRequires:	gnome-do-devel
BuildRequires:	mono-addins-devel
BuildRequires:	mono-csharp >= 1.1.13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugins for gnome-do.

%prep
%setup -q

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
