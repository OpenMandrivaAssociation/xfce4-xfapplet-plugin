%define oname xfce4-xfapplet-plugin

Summary:	XfApplet is a plugin for the Xfce panel
Name:		xfce-xfapplet-plugin
Version:	0.1.0
Release:	%mkrel 6
License:	GPL
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-xfapplet-plugin
Source0:	http://goodies.xfce.org/_media/projects/panel-plugins/%{oname}-%{version}.tar.bz2
Requires:	xfce-panel >= 4..3
BuildRequires:	xfce-panel-devel >= 4.3
BuildRequires:	gnome-panel-devel >= 2.0.0
BuildRequires:	libxfcegui4-devel >= 4.3
BuildRoot:	%{_tmppath}/%{name}-%{version}-builfroot

%description
XfApplet is a plugin for the Xfce panel. The plugin itself has no special
functionallity, its only purpose is to enable one to use Gnome applets inside
the Xfce 4 panel just as they are used inside the Gnome panel.

%prep
%setup -qn %{oname}-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std 
 
%find_lang %{oname}

%clean
rm -rf %{buildroot}

%files -f %{oname}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%dir %{_datadir}/%{oname}
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/pixmaps/*.svg
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_datadir}/xfce4-xfapplet-plugin/ui/XFCE_Panel_Popup.xml
