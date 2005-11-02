# TODO
# - kde control panel applet doesn't get found
# - where to place the .theme?
Summary:	A GTK+ theme engine that uses Qt for drawing
Summary(pl):	Silnik graficzny wykorzystuj�cy Qt do rysowania kontrolek GTK+
Name:		gtk2-theme-engine-qt
Version:	0.6
Release:	0.6
License:	GPL
Group:		Themes/GTK+
Source0:	http://www.freedesktop.org/~davidsansome/gtk-qt-engine-%{version}.tar.bz2
# Source0-md5:	9c02c95a6e8d304b1f2801429759e1c0
Patch0:		%{name}-black-menus.patch
URL:		http://www.freedesktop.org/Software/gtk-qt
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	kdelibs-devel
BuildRequires:	pkgconfig
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This GTK+ theme engine uses the currently selected Qt style to do it's
drawing. Basically, it makes your GTK+ apps look like Qt ones.

%description -l pl
Ten silnik graficzny do rysowania kontrolek GTK+ u�ywa aktualnie
wybranego stylu Qt. Inaczej m�wi�c - sprawia, �e aplikacje GTK+
wygl�daj� jak aplikacje Qt.

%prep
%setup -q -n gtk-qt-engine-%{version}
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.4.*/engines/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/gtk-2.0/2.4.*/engines/*.so
%{_datadir}/themes/Qt
%{_libdir}/kde3/kcm_kcmgtk.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kcmgtk.so
%{_desktopdir}/kcmgtk-xdg.desktop
