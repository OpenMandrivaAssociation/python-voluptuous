%define module	voluptuous

Summary:	Python data validation library
Name:		python-%{module}
Version:	0.15.2
Release:	1
Source0:	https://github.com/alecthomas/voluptuous/archive/%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://github.com/alecthomas/voluptuous/
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
find %{buildroot} -type d -exec chmod 755 {} \;
find %{buildroot} -type f -exec chmod 644 {} \;

%files -f FILE_LIST
%defattr(-,root,root)
