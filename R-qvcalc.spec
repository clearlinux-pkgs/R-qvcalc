#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-qvcalc
Version  : 1.0.2
Release  : 40
URL      : https://cran.r-project.org/src/contrib/qvcalc_1.0.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/qvcalc_1.0.2.tar.gz
Summary  : Quasi Variances for Factor Effects in Statistical Models
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
BuildRequires : R-psychotools
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n qvcalc
cd %{_builddir}/qvcalc

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641084805

%install
export SOURCE_DATE_EPOCH=1641084805
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library qvcalc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library qvcalc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library qvcalc
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc qvcalc || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/qvcalc/DESCRIPTION
/usr/lib64/R/library/qvcalc/INDEX
/usr/lib64/R/library/qvcalc/Meta/Rd.rds
/usr/lib64/R/library/qvcalc/Meta/features.rds
/usr/lib64/R/library/qvcalc/Meta/hsearch.rds
/usr/lib64/R/library/qvcalc/Meta/links.rds
/usr/lib64/R/library/qvcalc/Meta/nsInfo.rds
/usr/lib64/R/library/qvcalc/Meta/package.rds
/usr/lib64/R/library/qvcalc/NAMESPACE
/usr/lib64/R/library/qvcalc/NEWS.md
/usr/lib64/R/library/qvcalc/R/qvcalc
/usr/lib64/R/library/qvcalc/R/qvcalc.rdb
/usr/lib64/R/library/qvcalc/R/qvcalc.rdx
/usr/lib64/R/library/qvcalc/help/AnIndex
/usr/lib64/R/library/qvcalc/help/aliases.rds
/usr/lib64/R/library/qvcalc/help/paths.rds
/usr/lib64/R/library/qvcalc/help/qvcalc.rdb
/usr/lib64/R/library/qvcalc/help/qvcalc.rdx
/usr/lib64/R/library/qvcalc/html/00Index.html
/usr/lib64/R/library/qvcalc/html/R.css
