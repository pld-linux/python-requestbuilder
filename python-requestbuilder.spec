#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	requestbuilder
Summary:	Command line-driven HTTP request builder
Summary(pl.UTF-8):	Budowanie żądań HTTP w oparciu o linię poleceń
Name:		python-%{module}
Version:	0.2.3
Release:	10
License:	ISC
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/r/requestbuilder/%{module}-%{version}.tar.gz
# Source0-md5:	3d9793e3a3b3dad23a8475e0480581db
URL:		https://github.com/boto/requestbuilder
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools > 1:7.0
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools > 1:7.0
%endif
Requires:	python-requests >= 1
Requires:	python-six
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Command line-driven HTTP request builder.

%description -l pl.UTF-8
Budowanie żądań HTTP w oparciu o linię poleceń.

%package -n python3-%{module}
Summary:	Command line-driven HTTP request builder
Summary(pl.UTF-8):	Budowanie żądań HTTP w oparciu o linię poleceń
Group:		Libraries/Python
Requires:	python-requests >= 1
Requires:	python-six

%description -n python3-%{module}
Command line-driven HTTP request builder.

%description -n python3-%{module} -l pl.UTF-8
Budowanie żądań HTTP w oparciu o linię poleceń.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
