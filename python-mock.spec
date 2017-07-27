# centos/sclo spec file for python-mock, from:
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

%{?scl:          %scl_package        python-mock}
%{!?scl:         %global pkg_name    %{name}}

%global mod_name mock

Name:           %{?sub_prefix}python-mock
Version:        1.0.1
Release:        10%{?dist}
Summary:        A Python Mocking and Patching Library for Testing

License:        BSD
URL:            http://www.voidspace.org.uk/python/%{mod_name}/
Source0:        http://pypi.python.org/packages/source/m/%{mod_name}/%{mod_name}-%{version}.tar.gz
Source1:        LICENSE.txt

BuildArch:      noarch
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools
# For tests
%if 0%{?with_python3} 
BuildRequires:  %{?scl_prefix}python-unittest2
%endif

Requires:    %{?scl_prefix}python

%if 0%{?scl:1}
Provides: %{?scl_prefix}python-%{mod_name} = %{version}-%{release}
%if %{?with_python3}
Provides: %{?scl_prefix}python3-%{mod_name} = %{version}-%{release}
%else
Provides: %{?scl_prefix}python2-%{mod_name} = %{version}-%{release}
%endif
%endif

%description
Mock is a Python module that provides a core mock class. It removes the need
to create a host of stubs throughout your test suite. After performing an
action, you can make assertions about which methods / attributes were used and
arguments they were called with. You can also specify return values and set
needed attributes in the normal way.

%prep
%setup -q -n %{mod_name}-%{version}
cp -p %{SOURCE1} .


%build
%{?scl:scl enable %{scl} - << \EOF}
%{__python} setup.py build
rm -rvf %{buildroot}/%{python_sitelib}/__pycache__
%{?scl:EOF}

%if 0%{?with_python3} 
%check
%{?scl:scl enable %{scl} - << \EOF}
%{__python} setup.py test ||:
rm -rvf %{buildroot}/%{python_sitelib}/__pycache__
%{?scl:EOF}
%endif

%install
%{?scl:scl enable %{scl} - << \EOF}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
rm -rvf %{buildroot}/%{python_sitelib}/__pycache__
%{?scl:EOF}
 
%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%doc docs/* README.txt PKG-INFO
%{python_sitelib}/*.egg-info
%{python_sitelib}/%{mod_name}.py*

%changelog
* Thu Jul 27 2017 Jaroslaw Polok <jaroslaw.polok@cern.ch>
- SCLo build.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 6 2016 Orion Poplawski <orion@cora.nwra.com> - 1.0.1-9
- Modernize spec
- Run python2 tests, python3 failing

* Thu Nov 12 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Nov 02 2015 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1.0.1-7
- Fix #1276771

* Wed Sep 23 2015 Robert Kuska <rkuska@redhat.com> - 1.0.1-6
- Rebuilt for Python3.5 rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 09 2014 Dennis Gilmore <dennis@ausil.us> - 1.0.1-3
- rebuild for python 3.4
- disable test suite deps missing

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Luke Macken <lmacken@redhat.com> - 1.0.1-1
- Update to 1.0.1
- Run the test suite
- Add python-unittest2 as a build requirement

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 0.8.0-4
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Ralph Bean <rbean@redhat.com> - 0.8.0-2
- Python3 support

* Thu Mar 22 2012 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.8.0-1
- Updated to new version

* Fri Jul 22 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.7.2-1
- Initial RPM release
