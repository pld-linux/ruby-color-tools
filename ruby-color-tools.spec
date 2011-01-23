Summary:	Color manipulation library for Ruby
Summary(pl.UTF-8):	Biblioteka manipulacji kolorami dla języka Ruby
Name:		ruby-color-tools
Version:	1.3.0
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/5478/color-tools-%{version}.tar.gz
# Source0-md5:	7459f0ca6214d2f340a2f260de56c68c
URL:		http://ruby-pdf.rubyforge.org/pdf-writer/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
#BuildRequires:	setup.rb = 3.3.1
Requires:	ruby-color-tools
Requires:	ruby-transaction-simple
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ruby-color-tools is a Ruby library to provide RGB, CMYK, and other
colourspace support to applications that require it. It offers 152
named RGB colours (184 with spelling variations) that are commonly
supported and used in HTML, SVG, and X11 applications. A technique for
generating a monochromatic contrasting palette is also included.

%description -l pl.UTF-8
ruby-color-tools jest biblioteką języka Ruby dostarczającą wsparcie
przestrzeni kolorów RGB, CMYK i innych dla aplikacji, które tego
wymagają. Oferuje 152 nazwane kolory RGB (184 licząc z różnymi
wymowami), które są powszechnie wspierane i używane w HTML, SVG i
aplikacjach dla X11. Zawiera również technikę generacji kontrastowej
palety monochromatycznej.

%prep
%setup -q -n color-tools-%{version}
#cp %{_datadir}/setup.rb .

%build
rm pre-setup.rb
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/*
%{ruby_ridir}/*
