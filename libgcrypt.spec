Summary:	Cryptographic library based on the code from GnuPG
Summary(es):	Libgcrypt es una biblioteca general de desarrole embasada em GnuPG
Summary(pl):	Biblioteka kryptograficzna oparta na kodzie GnuPG
Summary(pt_BR):	libgcrypt � uma biblioteca de criptografia de uso geral baseada no GnuPG
Name:		libgcrypt
Version:	1.1.9
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/libgcrypt/%{name}-%{version}.tar.gz
Patch0:		%{name}-no_libnsl.patch
Patch1:		%{name}-info.patch
URL:		http://www.gnu.org/gnulist/production/libgcrypt.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a general purpose cryptographic library based on the code from
GnuPG. It provides functions for all cryptograhic building blocks:
symmetric ciphers (AES, DES, Blowfish, CAST5, Twofish, Arcfour), hash
algorithms (MD5, RIPE-MD160, SHA-1, TIGER-192), MACs (HMAC for all
hash algorithms), public key algorithms (RSA, ElGamal, DSA), large
integer functions, random numbers and a lot of supporting functions.

%description -l pl
Ten pakiet zawiera bibliotek� kryptograficzn� og�lnego przeznaczenia,
opart� na kodzie GnuPG. Biblioteka ta dostarcza funkcje do wszystkich
podstawowych blok�w kryptografii: szyfr�w symetrycznych (AES, DES,
Blowfish, CAST5, Twofish, Acrfour), algorytm�w mieszaj�cych (MD5,
RIPE-MD160, SHA-1, RIGER-192), MAC-�w (HMAC dla wszystkich algorytm�w
mieszaj�cych), algorytm�w klucza publicznego (RSA, ElGamal, DSA),
funkcji du�ych liczb ca�kowitych, liczb losowych i wiele funkcji
pomocniczych.

%description -l pt_BR
Libgcrypt � uma biblioteca de criptografia de uso geral baseada no
GnuPG.

%package devel
Summary:	Header files etc to develop libgcrypt applications
Summary(es):	Archivos de desarrollo de libgcrypt
Summary(pl):	Pliki nag��wkowe i inne do libgcrypt
Summary(pt_BR):	Arquivos de desenvolvimento da libgcrypt
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files etc to develop libgcrypt applications.

%description devel -l pl
Pliki nag��wkowe i inne do libgcrypt.

%description devel -l pt_BR
Bibliotecas de desenvolvimento para libgcrypt.

%package static
Summary:	Static libgcrypt library
Summary(es):	Archivos de desarrollo de libgcrypt - estatico
Summary(pl):	Biblioteka statyczna libgcrypt
Summary(pt_BR):	Arquivos de desenvolvimento da libgcrypt - biblioteca est�tica
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libgcrypt library.

%description static -l pl
Biblioteka statyczna libgcrypt.

%description static -l pt_BR
Bibliotecas de desenvolvimento para libgcrypt - est�tico.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f misssing
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libgcrypt-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_infodir}/*info*
%{_includedir}/*.h
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
