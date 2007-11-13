#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	chmod
Summary:	File::chmod - Implements symbolic and ls chmod modes
Name:		perl-File-chmod
Version:	0.32
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0048eb67fffad544e1cc07e04c33b0b2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::chmod - Implements symbolic and ls chmod modes.

File::chmod is a utility that allows you to bypass system calls or bit
processing of a file's permissions. It overloads the chmod() function
with its own that gets an octal mode, a symbolic mode or an "ls" mode.
If you wish not to overload chmod(), you can export symchmod() and
lschmod(), which take, respectively, a symbolic mode and an "ls" mode.

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
%{_mandir}/man3/*
