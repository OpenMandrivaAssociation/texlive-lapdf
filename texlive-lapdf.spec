%global tl_name lapdf
%global tl_revision 23806

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	PDF drawing directly in TeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lapdf
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lapdf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lapdf.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the means to use PDF drawing primitives to produce
high quality, colored graphics. It uses Bezier curves (integral and
rational) from degree one to seven, allows TeX typesetting in the
graphic, offers most of the standard math functions, allows plotting
normal, parametric and polar functions. The package has linear, logx,
logy, logxy and polar grids with many specs; it can rotate, clip and do
many nice things easily it has two looping commands for programming and
many instructive example files. The package requires pdfTeX but
otherwise only depends on the calc package.

