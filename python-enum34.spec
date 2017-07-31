# centos/sclo spec file for python-enum34, from:
#
# Fedora spec file
#

%if 0%{?scl:1}
 %if "%{scl}" == "rh-python34"
  %global sub_prefix sclo-python34-
  %global with_python3 1
 %else
  %if "%{scl}" == "rh-python35"
   %global sub_prefix sclo-python35-
   %global with_python3 1
  %else 
   %global sub_prefix sclo-%{scl_prefix}
   %global with_python3 0	
  %endif
 %endif
%endif

%{?scl:          %scl_package        python-enum34}
%{!?scl:         %global pkg_name    %{name}}

Name:           %{?sub_prefix}python-enum34
Version:        1.1.6
Release:        1%{?dist}
Group:          Development/Libraries
Summary:        Backport of Python 3.4 Enum
License:        BSD
BuildArch:      noarch
URL:            https://pypi.python.org/pypi/enum34
Source0:        https://files.pythonhosted.org/packages/source/e/enum34/enum34-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}python-devel %{?scl_prefix}python-setuptools

Requires:    %{?scl_prefix}python

%if 0%{?scl:1}
Provides: %{?scl_prefix}python-enum34 = %{version}-%{release}
%if %{?with_python3}
Provides: %{?scl_prefix}python3-enum34 = %{version}-%{release}
%else
Provides: %{?scl_prefix}python2-enum34 = %{version}-%{release}
%endif
%endif

%description
Python 3.4 introduced official support for enumerations.  This is a
backport of that feature to Python 3.3, 3.2, 3.1, 2.7, 2.5, 2.5, and 2.4.

An enumeration is a set of symbolic names (members) bound to unique,
constant values. Within an enumeration, the members can be compared by
identity, and the enumeration itself can be iterated over.

This module defines two enumeration classes that can be used to define
unique sets of names and values: Enum and IntEnum. It also defines one
decorator, unique, that ensures only unique member names are present
in an enumeration.


%prep
%setup -q -n enum34-%{version}


%build
%{?scl:scl enable %{scl} - << \EOF}
%{__python} setup.py build
%{?scl:EOF}

%check
%{?scl:scl enable %{scl} - << \EOF}
pushd %{buildroot}/%{python_sitelib}
PYTHONPATH=".:${PYTHONPATH}" %{__python} enum/test.py
popd
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - << \EOF}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
# remove docs from sitelib, we'll put them in doc dir instead
rm -rf %{buildroot}%{python_sitelib}/enum/{LICENSE,README,doc}
%{?scl:EOF}

%files
%doc PKG-INFO enum/LICENSE enum/README enum/doc/enum.rst
%{python_sitelib}/*

%changelog
* Fri Jul 28 2017 Jaroslaw Polok <jaroslaw.polok@cern.ch>
- SCLo build.

* Thu Jun 15 2017 Eric Smith <brouhaha@fedoraproject.org> 1.1.6-1
- New upstream version 1.1.6 (#1441428)
- Update upstream tarball dir
- Convert to newer build marcos
- Update tests to pass in new build
- These RPM spec changes were all provided by Greg Hellings.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 24 2016 Robert Kuska <rkuska@redhat.com> - 1.0.4-5
- Remove python3 subpackage, enum34 is now provided by python3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 08 2015 Eric Smith <brouhaha@fedoraproject.org> 1.0.4-1
- Updated to latest upstream.

* Mon Jul 21 2014 Matěj Cepl <mcepl@redhat.com> - 1.0-4
- No, we don’t have python3 in RHEL-7 :'(

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon May 26 2014 Eric Smith <brouhaha@fedoraproject.org> 1.0-1
- Updated to latest upstream.

* Mon Mar 17 2014 Eric Smith <brouhaha@fedoraproject.org> 0.9.23-1
- Updated to latest upstream.
- Spec updated per review comments (#1033975).

* Sun Nov 24 2013 Eric Smith <brouhaha@fedoraproject.org> 0.9.19-1
- Initial version.
