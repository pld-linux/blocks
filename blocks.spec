%define	githash	a50575b
%define	rel		1
Summary:	Conversion tools to enable bcache or LVM on existing block devices
Summary(pl.UTF-8):	Narzędzia do konwersji pozwalające na włączenie bcache lub LVM na istniejących urządzeniach
Name:		blocks
Version:	0.1.4
Release:	0.%{githash}.%{rel}
License:	GPL v3
Group:		Applications/System
Source0:	https://github.com/g2p/blocks/archive/%{githash}/%{name}-%{version}-%{githash}.tar.gz
# Source0-md5:	06d0033af5a3d4f138698cccf0fa4a6b
Patch0:		egg-deps.patch
URL:		https://github.com/g2p/blocks
BuildRequires:	python3-distribute
BuildRequires:	python3-modules >= 3.3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python3-augeas >= 0.4.1-2
Requires:	python3-distribute
Requires:	python3-parted >= 3.10
Suggests:	maintboot
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Conversion tools for block devices.

Convert between raw partitions, logical volumes, and bcache devices
without moving data. blocks shuffles blocks and sprouts superblocks.

%description -l pl.UTF-8
Narzędzia do konwersji dla urządzeń blokowych.

Pozwalają na konwersję między surowymi partycjami, wolumenami
logicznymi oraz urządzeniami bcache bez potrzeby przenoszenia danych.
blocks przestawia bloki i tworzy nowe superbloki.

%prep
%setup -qc
mv blocks-*/* .
%patch0 -p1

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

install -d $RPM_BUILD_ROOT%{_sbindir}
# admin tool. move to sbin
mv $RPM_BUILD_ROOT{%{_bindir},%{_sbindir}}/blocks

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_sbindir}/blocks
%dir %{py3_sitescriptdir}/blocks
%{py3_sitescriptdir}/blocks/*.py
%{py3_sitescriptdir}/blocks/augeas
%{py3_sitescriptdir}/blocks/maintboot.init
%{py3_sitescriptdir}/blocks/__pycache__
%{py3_sitescriptdir}/blocks-%{version}-py*.egg-info
