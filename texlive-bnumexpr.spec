Name:		texlive-bnumexpr
Version:	59244
Release:	2
Summary:	Extends eTeX's \numexpr...\relax construct to big integers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bnumexpr
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bnumexpr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bnumexpr.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bnumexpr.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package extends e-TeX \numexpr...\relax operation to allow
big integers, powers, factorials, truncated division and its
associated modulo. By default, bnumexpr loads package xintcore
(part of the xint bundle) and uses its arithmetic macros.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/bnumexpr
%{_texmfdistdir}/tex/latex/bnumexpr
%doc %{_texmfdistdir}/doc/latex/bnumexpr

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
