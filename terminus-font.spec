Summary:	A clean fixed width font
Name:		terminus-font
Version:	4.39
Release:	1
License:	GPL
Group:		Fonts
Source0:	http://downloads.sourceforge.net/project/terminus-font/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1ec1bee67a1c017f349bc8558b2d4fa6
URL:		http://sourceforge.net/projects/terminus-font/
BuildRequires:	perl-base
BuildRequires:	xorg-app-bdftopcf
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Terminus Font is designed for long (8 and more hours per day) work
with computers. Version 4.09 contains 594 characters, covering code
pages ISO8859-1/2/5/9/13/15/16, Windows-1250/1251/1252/1254/1257,
IBM-437/852/855/866, KOI8-R/U/E/F, Bulgarian-MIK,
Paratype-PT154/PT254, Macintosh-Ukrainian and Esperanto, and also the
vt100 and xterm pseudographic characters.

The sizes present are 8x14, 8x16, 10x20, 12x24, 14x28 and 16x32. The
styles are normal and bold, plus EGA/VGA-bold for 8x14 and 8x16.

This package contains Terminus Font for Linux console.

%package X11
Summary:	A clean fixed width font
Group:		Fonts
Requires(post,postun): fontpostinst

%description X11
Terminus Font is designed for long (8 and more hours per day) work
with computers. Version 4.09 contains 594 characters, covering code
pages ISO8859-1/2/5/9/13/15/16, Windows-1250/1251/1252/1254/1257,
IBM-437/852/855/866, KOI8-R/U/E/F, Bulgarian-MIK,
Paratype-PT154/PT254, Macintosh-Ukrainian and Esperanto, and also the
vt100 and xterm pseudographic characters.

%prep
%setup -q

%build
chmod +x ./configure
%configure \
	--psfdir=%{_datadir}/kbd/consolefonts	\
	--x11dir=%{_fontsdir}/misc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail
install -d $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# fontconfig configuration
install 75-yes-terminus.conf \
	$RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail
ln -s %{_datadir}/fontconfig/conf.avail/75-yes-terminus.conf \
	$RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d

%clean
rm -rf $RPM_BUILD_ROOT

%post X11
fontpostinst misc

%postun X11
fontpostinst misc

%files
%defattr(644,root,root,755)
%doc README
%{_datadir}/kbd/consolefonts/*

%files X11
%defattr(644,root,root,755)
%doc README
%{_fontsdir}/misc/*
%{_datadir}/fontconfig/conf.avail/75-yes-terminus.conf
%{_sysconfdir}/fonts/conf.d/75-yes-terminus.conf

