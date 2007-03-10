Summary:	Color manipulation library for Ruby
Name:		ruby-color-tools
Version:	1.3.0
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/5478/color-tools-%{version}.tar.gz
# Source0-md5:	7459f0ca6214d2f340a2f260de56c68c
#Patch0: %{name}-nogems.patch
URL:		http://ruby-pdf.rubyforge.org/pdf-writer/
BuildRequires:	rake
BuildRequires:	rpmbuild(macros) >= 1.277
#BuildRequires:	setup.rb = 3.3.1
Requires:	ruby-color-tools
Requires:	ruby-transaction-simple
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Color manipulation library for Ruby.

%prep
%setup -q -n color-tools-%{version}
#%patch0 -p1
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
