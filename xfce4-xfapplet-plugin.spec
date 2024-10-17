Summary:	Plugin for the Xfce panel
Name:		xfce4-xfapplet-plugin
Version:	0.1.0
Release:	17
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-xfapplet-plugin
Source0:	http://goodies.xfce.org/_media/projects/panel-plugins/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	gnome-panel-devel >= 2.0.0
BuildRequires:	pkgconfig(libxfcegui4-1.0)
BuildRequires:  libORBit2-devel
BuildRequires:	libpanel-applet-2-devel

Obsoletes:	xfce-xfapplet-plugin

%description
XfApplet is a plugin for the Xfce panel. The plugin itself has no special
functionallity, its only purpose is to enable one to use Gnome applets inside
the Xfce 4 panel just as they are used inside the Gnome panel.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std 

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%dir %{_datadir}/%{name}
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/pixmaps/*.svg
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_datadir}/%{name}/ui/XFCE_Panel_Popup.xml
