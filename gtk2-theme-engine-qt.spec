Summary:	A GTK+ theme engine that uses Qt for drawing
Summary(pl.UTF-8):	Silnik graficzny wykorzystujący Qt do rysowania kontrolek GTK+
Name:		gtk2-theme-engine-qt
Version:	0.8
Release:	1
License:	GPL
Group:		Themes/GTK+
Source0:	http://gtk-qt.ecs.soton.ac.uk/files/0.8/gtk-qt-engine-%{version}.tar.bz2
# Source0-md5:	9fe75b7765b6a5b49901fcd6f4f4aa4b
URL:		http://gtk-qt.ecs.soton.ac.uk/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cmake
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

%build
cmake \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    .
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# proper category
sed -i 's/Categories=.*/Categories=X-KDE-settings-looknfeel;/' \
	$RPM_BUILD_ROOT%{_desktopdir}/kcmgtk.desktop

rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/engines/*.la

%find_lang gtkqtengine --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gtkqtengine.lang
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/gtk-2.0/*/engines/*.so
%{_datadir}/themes/Qt
%{_desktopdir}/kcmgtk.desktop
%{_libdir}/kde3/kcm_kcmgtk.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kcmgtk.so
