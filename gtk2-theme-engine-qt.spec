# TODO
# - kde control panel applet doesn't get found
#   (recheck - probably caused by old -dt patch which added NotShowIn=KDE instead of OnlyShowIn)
Summary:	A GTK+ theme engine that uses Qt for drawing
Summary(pl.UTF-8):	Silnik graficzny wykorzystujący Qt do rysowania kontrolek GTK+
Name:		gtk2-theme-engine-qt
Version:	0.7
Release:	1
License:	GPL
Group:		Themes/GTK+
Source0:	http://people.freedesktop.org/~davidsansome/gtk-qt-engine-%{version}.tar.bz2
# Source0-md5:	27ca211621f38c45b1c4c9e9ef1f84b0
Patch0:		kde-ac260-lt.patch
Patch1:		kde-ac260.patch
Patch2:		kde-am110.patch
URL:		http://gtk-qt.ecs.soton.ac.uk/
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

%description -l pl.UTF-8
Ten silnik graficzny do rysowania kontrolek GTK+ używa aktualnie
wybranego stylu Qt. Inaczej mówiąc - sprawia, że aplikacje GTK+
wyglądają jak aplikacje Qt.

%prep
%setup -q -n gtk-qt-engine
%patch0 -p1
%patch1 -p1
%patch2 -p1

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
%{_datadir}/gtk-qt-engine
%{_desktopdir}/*.desktop
%{_libdir}/kde3/kcm_kcmgtk.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kcmgtk.so
