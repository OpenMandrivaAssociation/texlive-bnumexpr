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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the command \bnumeval, which extends LaTeX's
\inteval with support for arbitrarily big integers, // for floored
division, /: for the associated remainder, ^ and ** for powers, ! for
factorials, 0b, 0o and ', 0x and ", as prefixes for binary, octal, or
hexadecimal inputs. With the optional argument [h] (or [o] or [b]) the
output is converted to hexadecimal (or octal, or binary).

