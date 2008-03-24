%include	/usr/lib/rpm/macros.mono
Summary:	Plugins for gnome-do
Name:		gnome-do-plugins
Version:	0.4.0
Release:	2
License:	GPL v3
Group:		X11/Applications
Source0:	https://launchpad.net/do/trunk/0.4/+download/do-plugins-%{version}.tar.gz
# Source0-md5:	0e3901a07e45ec6ebd26ce76fcea76a6
URL:		http://do.davebsd.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-evolution-sharp-devel
BuildRequires:	dotnet-gnome-sharp-devel
BuildRequires:	dotnet-gtk-sharp2-devel
BuildRequires:	dotnet-ndesk-dbus-glib-sharp-devel
BuildRequires:	dotnet-ndesk-dbus-sharp-devel
BuildRequires:	gnome-do-devel
BuildRequires:	mono-csharp >= 1.1.13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugins for gnome-do.

%prep
%setup -q -n do-plugins-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS
%{_datadir}/gnome-do/plugins/Amarok.dll
%{_datadir}/gnome-do/plugins/AppendTextAction.dll
%{_datadir}/gnome-do/plugins/Banshee.dll
%{_datadir}/gnome-do/plugins/Epiphany.dll
%{_datadir}/gnome-do/plugins/Evolution.dll
%{_datadir}/gnome-do/plugins/EyeOfGNOMEPlaySlideshowAction.dll
%{_datadir}/gnome-do/plugins/File.dll
%{_datadir}/gnome-do/plugins/GNOME-Session.dll
%{_datadir}/gnome-do/plugins/GoogleCalculatorAction.dll
%{_datadir}/gnome-do/plugins/GoogleMapAction.dll
%{_datadir}/gnome-do/plugins/Launchpad.dll
%{_datadir}/gnome-do/plugins/LocateFiles.dll
%{_datadir}/gnome-do/plugins/OpenSearch.dll
%{_datadir}/gnome-do/plugins/Pastebin.dll
%{_datadir}/gnome-do/plugins/Pidgin.dll
%{_datadir}/gnome-do/plugins/Rhythmbox.dll
%{_datadir}/gnome-do/plugins/SSH.dll
%{_datadir}/gnome-do/plugins/StockQuoteAction.dll
%{_datadir}/gnome-do/plugins/Thunderbird.dll
