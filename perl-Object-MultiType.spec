#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Object
%define		pnam	MultiType
Summary:	Object::MultiType - Perl objects as hash, array, scalar, code and glob at the same time
Summary(pl):	Object::MultiType - obiekty perlowe jako hasze, tablice, skalary, kod i globy jednocze�nie
Name:		perl-Object-MultiType
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	171ed010dab19fb8b94f22a5fca97814
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module returns an object that works like a Hash, Array, Scalar,
Code and Glob object at the same time.

The usual way is to call it from your module at new().

%description -l pl
Ten modu� zwraca obiekt dzia�aj�cy jako hasz, tablica, skalar, kod i
glob jednocze�nie. Zwykle wywo�uje si� go przy new().

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
%doc Changes README
%{perl_vendorlib}/Object/MultiType.pm
%{_mandir}/man3/*
