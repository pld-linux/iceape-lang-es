%define	_lang	es
%define	_reg	ES
%define	_lare	%{_lang}-%{_reg}
Summary:	Spanish resources for Iceape
Summary(ca.UTF-8):	Recursos espanyols per a Iceape
Summary(es.UTF-8):	Recursos españoles para Iceape
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Iceape
Name:		iceape-lang-es
Version:	1.1.13
Release:	1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/contrib-localized//seamonkey-%{version}.%{_lare}.langpack.xpi
# Source0-md5:	aa789a6abf2120717e9de8ccce6b66cd
Source1:	http://www.mozilla-enigmail.org/download/release/0.95/enigmail-%{_lare}-0.95.xpi
# Source1-md5:	b4600f86bce0ab816bb2896a936eecaa
Source2:	gen-installed-chrome.sh
URL:		http://www.seamonkey-project.org/
BuildRequires:	unzip
Requires(post,postun):	iceape >= %{version}
Requires(post,postun):	textutils
Requires:	iceape >= %{version}
Obsoletes:	mozilla-lang-es
Obsoletes:	seamonkey-lang-es
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_chromedir	%{_datadir}/iceape/chrome

%description
Spanish resources for Iceape.

%description -l ca.UTF-8
Recursos espanyols per a Iceape.

%description -l es.UTF-8
Recursos españoles para Iceape.

%description -l pl.UTF-8
Hiszpańskie pliki językowe dla Iceape.

%prep
%setup -q -c
%{__unzip} -o -qq %{SOURCE1}
install %{SOURCE2} .
./gen-installed-chrome.sh locale \
	chrome/{%{_lare},%{_lang}-unix,enigmail-%{_lare}}.jar \
		> lang-%{_lang}-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install chrome/{%{_lare},%{_lang}-unix,enigmail-%{_lare}}.jar \
	$RPM_BUILD_ROOT%{_chromedir}
install lang-%{_lang}-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}

# rebrand locale for iceape
cd $RPM_BUILD_ROOT%{_chromedir}
unzip %{_lare}.jar locale/%{_lare}/branding/brand.dtd locale/%{_lare}/branding/brand.properties
sed -i -e 's/SeaMonkey/Iceape/g;' locale/%{_lare}/branding/brand.dtd \
	locale/%{_lare}/branding/brand.properties
zip -0 %{_lare}.jar locale/%{_lare}/branding/brand.dtd locale/%{_lare}/branding/brand.properties
rm -f locale/%{_lare}/branding/brand.dtd locale/%{_lare}/branding/brand.properties

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/iceape-chrome+xpcom-generate

%postun
%{_sbindir}/iceape-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_lare}.jar
%{_chromedir}/%{_lang}-unix.jar
%{_chromedir}/enigmail-%{_lare}.jar
%{_chromedir}/lang-%{_lang}-installed-chrome.txt
