Summary:	A GTK theme engine that uses QT for drawing
Summary(pl):	Silnik graficzny wykorzystuj±cy QT do rysowania kontrolek GTK
Name:		gtk2-theme-engine-qt
Version:	0.3
Release:	3
License:	GPL
Group:		Themes/Gtk
Source0:	http://www.freedesktop.org/Software/gtk-qt/gtk-qt-engine-%{version}.tar.bz2
# Source0-md5:	0685783bec472b682366f213134a6b3c
Patch0:		%{name}-qtdir.patch
URL:		http://www.freedesktop.org/Software/gtk-qt
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This GTK theme engine uses the currently selected QT style to do it's
drawing. Basically, it makes your GTK apps look like QT ones.

%description -l pl
Ten silnik graficzny do rysowania kontrolek GTK u¿ywa aktualnie
wybranego stylu QT. Inaczej mówi±c - sprawia, ¿e aplikacje GTK
wygl±daj± jak aplikacje QT.

%prep
%setup -q -n gtk-qt-engine-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
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
