#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	File
%define		pnam	chmod
Summary:	File::chmod - Implements symbolic and ls chmod modes
Summary(pl.UTF-8):	File::chmod - implementacja uprawnień symbolicznych i ls funkcji chmod
Name:		perl-File-chmod
Version:	0.42
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b94807f4bef13506ee529a214524f9de
URL:		https://metacpan.org/release/File-chmod
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::chmod is a utility that allows you to bypass system calls or bit
processing of a file's permissions. It overloads the chmod() function
with its own that gets an octal mode, a symbolic mode or an "ls" mode.
If you wish not to overload chmod(), you can export symchmod() and
lschmod(), which take, respectively, a symbolic mode and an "ls" mode.

%description -l pl.UTF-8
File::chmod to narzędzie pozwalające na pominięcie wywołań systemowych
lub przetwarzania bitów uprawnień plików. Przeciąża funkcję chmod()
własną, która przyjmuje uprawnienia w postaci ósemkowej, symbolicznej
i "ls". Modułu można użyć też bez przeciążania chmod(), eksportując
funkcje symchmod() i lschmod, które przyjmują uprawnienia w postaci
odpowiednio symbolicznej i "ls".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/File/chmod.pm
%{_mandir}/man3/File::chmod.3pm*
