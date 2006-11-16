# TODO
# - kde control panel applet doesn't get found
Summary:	A GTK+ theme engine that uses Qt for drawing
Summary(pl):	Silnik graficzny wykorzystuj±cy Qt do rysowania kontrolek GTK+
Name:		gtk2-theme-engine-qt
Version:	0.6
Release:	2
License:	GPL
Group:		Themes/GTK+
Source0:	http://www.freedesktop.org/~davidsansome/gtk-qt-engine-%{version}.tar.bz2
# Source0-md5:	9c02c95a6e8d304b1f2801429759e1c0
Patch0:		%{name}-black-menus.patch
Patch1:		%{name}-kcm-fixinstallationdir.patch
# don't dup GTK-QT in kde menu(s)
Patch2:		%{name}-dt.patch
# segfault in libqtengine.so drawing notebook
# https://bugs.freedesktop.org/show_bug.cgi?id=3919
Patch3:		%{name}-notebook.patch
Patch4:		kde-ac260-lt.patch
Patch5:		kde-ac260.patch
Patch6:		kde-am110.patch
URL:		http://www.freedesktop.org/Software/gtk-qt
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	kdelibs-devel
BuildRequires:	libbonoboui-devel
BuildRequires:	pkgconfig
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This GTK+ theme engine uses the currently selected Qt style to do it's
drawing. Basically, it makes your GTK+ apps look like Qt ones.

%description -l pl
Ten silnik graficzny do rysowania kontrolek GTK+ u¿ywa aktualnie
wybranego stylu Qt. Inaczej mówi±c - sprawia, ¿e aplikacje GTK+
wygl±daj± jak aplikacje Qt.

%prep
%setup -q -n gtk-qt-engine-%{version}
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%{__make} -f admin/Makefile.common cvs

%build
export QTLIB=%{_libdir}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# proper category
sed -i 's/Categories=.*/Categories=X-KDE-settings-looknfeel;/' \
	$RPM_BUILD_ROOT%{_desktopdir}/kcmgtk-xdg.desktop

rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/engines/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/gtk-2.0/*/engines/*.so
%{_datadir}/themes/Qt
%{_datadir}/gtk-qt-engine/
%{_desktopdir}/*.desktop
%{_libdir}/kde3/kcm_kcmgtk.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kcmgtk.so
