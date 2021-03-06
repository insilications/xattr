#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xattr
Version  : 0.9.8
Release  : 402
URL      : file:///aot/build/clearlinux/packages/xattr/xattr-v0.9.8.tar.gz
Source0  : file:///aot/build/clearlinux/packages/xattr/xattr-v0.9.8.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: xattr-bin = %{version}-%{release}
Requires: xattr-python = %{version}-%{release}
Requires: xattr-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : setuptools-python

%description
xattr
-----
.. image:: https://travis-ci.org/xattr/xattr.svg?branch=master
:target: https://travis-ci.org/xattr/xattr

%package bin
Summary: bin components for the xattr package.
Group: Binaries

%description bin
bin components for the xattr package.


%package python
Summary: python components for the xattr package.
Group: Default
Requires: xattr-python3 = %{version}-%{release}

%description python
python components for the xattr package.


%package python3
Summary: python3 components for the xattr package.
Group: Default
Requires: python3-core

%description python3
python3 components for the xattr package.


%prep
%setup -q -n xattr
cd %{_builddir}/xattr

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639122805
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=16 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=16 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=16 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=16 "
export MAKEFLAGS=%{?_smp_mflags}
if [ ! -f setup.py ]; then
printf "#!/usr/bin/env python\nfrom setuptools import setup\nsetup()" > setup.py
chmod +x setup.py
python3 setup.py build -j 16
else
python3 setup.py build -j 16
fi

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build -j 16 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xattr

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
