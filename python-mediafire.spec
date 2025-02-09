Name:		python-mediafire
Version:	0.6.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/m/mediafire/mediafire-%{version}.tar.gz
Summary:	Python MediaFire client library
URL:		https://pypi.org/project/mediafire/
License:	BSD
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Python MediaFire client library

%files
%{py_sitedir}/mediafire
%{py_sitedir}/mediafire-*.*-info
