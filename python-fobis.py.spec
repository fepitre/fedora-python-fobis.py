# Based on spec created by pyp2rpm-3.3.7
%global pypi_name fobis.py
%global pypi_version 3.0.5
%global desc FoBiS.py, a Fortran Building System for poor men, is a KISS tool for automatic building modern Fortran projects, it being able to automatically resolve inter-modules dependancy hierarchy.

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        a Fortran Building System for poor men

License:        GPLv3
URL:            https://github.com/szaghi/FoBiS
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/FoBiS.py-%{pypi_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-ford
Requires:       python3-graphviz
Requires:       python3-preform.py
Requires:       python3-setuptools
%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -n FoBiS.py-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# prevent trying to automatically add python3-configparser
sed -i 's|, "configparser"||' setup.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.gpl3.md
%doc README.md
%{_bindir}/FoBiS.py
%{python3_sitelib}/fobis
%{python3_sitelib}/FoBiS.py-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Dec 14 2021 Frédéric Pierret (fepitre) <frederic@invisiblethingslab.com> - 3.0.5-1
- Initial package.
