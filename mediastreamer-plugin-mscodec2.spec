Summary:	Codec2 audio codec for mediastreamer
Summary(pl.UTF-8):	Kodek dźwięku Codec2 dla mediastreamera
Name:		mediastreamer-plugin-mscodec2
Version:	1.0
Release:	3
License:	GPL v2+
Group:		Libraries
#Source0Download: https://gitlab.linphone.org/BC/public/mscodec2/-/tags
Source0:	https://gitlab.linphone.org/BC/public/mscodec2/-/archive/%{version}/mscodec2-%{version}.tar.bz2
# Source0-md5:	1b926337bda6cfaa899dbf5edfe9bb09
URL:		https://www.linphone.org/technical-corner/mediastreamer2/overview
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	codec2-devel
BuildRequires:	mediastreamer-devel >= 2.11.2
BuildRequires:	ortp-devel >= 0.24.2
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
Requires:	ortp >= 0.24.2
Requires:	mediastreamer >= 2.11.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package supplies the mediastreamer plugin for the Codec2 audio
codec.

%description -l pl.UTF-8
Ten pakiet udostępnia wtyczkę mediastreamera do kodeka dźwięku Codec2.

%prep
%setup -q -n mscodec2-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/mediastreamer/plugins/libmscodec2.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/mediastreamer/plugins/libmscodec2.so*
