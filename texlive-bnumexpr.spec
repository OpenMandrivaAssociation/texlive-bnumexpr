%global tl_name bnumexpr
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.7b
Release:	%{tl_revision}.1
Summary:	Extends eTeXs \numexpr...\relax construct to big integers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bnumexpr
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bnumexpr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bnumexpr.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bnumexpr.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the command \bnumeval, which extends LaTeX's
\inteval with support for arbitrarily big integers, // for floored
division, /: for the associated remainder, ^ and ** for powers, ! for
factorials, 0b, 0o and ', 0x and ", as prefixes for binary, octal, or
hexadecimal inputs. With the optional argument [h] (or [o] or [b]) the
output is converted to hexadecimal (or octal, or binary).

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bnumexpr
%dir %{_datadir}/texmf-dist/source/latex/bnumexpr
%dir %{_datadir}/texmf-dist/tex/latex/bnumexpr
%doc %{_datadir}/texmf-dist/doc/latex/bnumexpr/README.md
%doc %{_datadir}/texmf-dist/doc/latex/bnumexpr/bnumexpr.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bnumexpr/bnumexpr.tex
%doc %{_datadir}/texmf-dist/doc/latex/bnumexpr/bnumexprchanges.tex
%doc %{_datadir}/texmf-dist/source/latex/bnumexpr/bnumexpr.dtx
%{_datadir}/texmf-dist/tex/latex/bnumexpr/bnumexpr.sty
