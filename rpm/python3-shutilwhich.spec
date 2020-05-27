Name: python3-shutilwhich
Summary: A copy & paste backport of Python 3.3's shutil.which function.
Version: 1.1.0
Release: 1
License: Python
URL: https://github.com/mbr/shutilwhich
Source0: %{name}-%{version}.tar.bz2
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
A copy & paste backport of Python 3.3's shutil.which function.

%prep
%autosetup -n  %{name}-%{version}/python-shutilwhich

%build
%py3_build

%install
rm -rf %{buildroot}
%py3_install

%files
%license LICENSE
%doc README.rst
%{python3_sitelib}/shutilwhich
%{python3_sitelib}/shutilwhich-*.egg-info/

