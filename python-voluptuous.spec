%define module	voluptuous
%define name	python-%{module}
%define version	0.4
%define release %mkrel 1

Summary:	Python data validation library
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://github.com/alecthomas/voluptuous/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	python-devel

%description
Voluptuous, despite the name, is a Python data validation library. It
is primarily intended for validating data coming into Python as JSON,
YAML, etc. It has three goals:

1. Simplicity.
2. Support for complex data structures.
3. Provide useful error messages.

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
chmod 644 *.rst
find %{buildroot} -type d -exec chmod 755 {} \;
find %{buildroot} -type f -exec chmod 644 {} \;

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc README.rst tests.rst


%changelog
* Thu Nov 17 2011 Lev Givon <lev@mandriva.org> 0.4-1mdv2011.0
+ Revision: 731410
- Update to 0.4.

* Mon Sep 05 2011 Lev Givon <lev@mandriva.org> 0.3.3-2
+ Revision: 698373
- Fix permissions.

* Tue Aug 30 2011 Lev Givon <lev@mandriva.org> 0.3.3-1
+ Revision: 697507
- import python-voluptuous

