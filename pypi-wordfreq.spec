#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-wordfreq
Version  : 3.0.1
Release  : 3
URL      : https://files.pythonhosted.org/packages/b6/cb/1ec9f38dd8ba501cae663b25272e7f20ebaa7f59dd02097b10e4db17c6dc/wordfreq-3.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/b6/cb/1ec9f38dd8ba501cae663b25272e7f20ebaa7f59dd02097b10e4db17c6dc/wordfreq-3.0.1.tar.gz
Summary  : Look up the frequencies of words in many languages, based on many sources of data.
Group    : Development/Tools
License  : MIT
Requires: pypi-wordfreq-python = %{version}-%{release}
Requires: pypi-wordfreq-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)

%description
wordfreq is a Python library for looking up the frequencies of words in many
languages, based on many sources of data.

%package python
Summary: python components for the pypi-wordfreq package.
Group: Default
Requires: pypi-wordfreq-python3 = %{version}-%{release}

%description python
python components for the pypi-wordfreq package.


%package python3
Summary: python3 components for the pypi-wordfreq package.
Group: Default
Requires: python3-core
Provides: pypi(wordfreq)
Requires: pypi(ftfy)
Requires: pypi(langcodes)
Requires: pypi(msgpack)
Requires: pypi(regex)

%description python3
python3 components for the pypi-wordfreq package.


%prep
%setup -q -n wordfreq-3.0.1
cd %{_builddir}/wordfreq-3.0.1
pushd ..
cp -a wordfreq-3.0.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656361400
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
