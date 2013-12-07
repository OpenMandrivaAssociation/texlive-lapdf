# revision 23806
# category Package
# catalog-ctan /macros/latex/contrib/lapdf
# catalog-date 2011-09-04 01:09:50 +0200
# catalog-license gpl
# catalog-version 1.1
Name:		texlive-lapdf
Version:	1.1
Release:	4
Summary:	PDF drawing directly in TeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lapdf
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lapdf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lapdf.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the means to use PDF drawing primitives to
produce high quality, colored graphics. It - uses Bezier curves
(integral and rational) from degree one to seven, - allows TeX
typesetting in the graphic, - offers most of the standard math
functions, - allows plotting normal, parametric and polar
functions. The package has linear, logx, logy, logxy and polar
grids with many specs; - it can rotate, clip and do many nice
things easily - it has two looping commands for programming and
many instructive example files. The package requires pdfTeX but
otherwise only depends on the calc package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lapdf/lapdf.sty
%doc %{_texmfdistdir}/doc/latex/lapdf/README
%doc %{_texmfdistdir}/doc/latex/lapdf/arcs.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/arcs.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/bezier.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/bezier.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/bezinfo.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/bezinfo.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/buttrfly.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/buttrfly.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/cfamily.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/cfamily.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/chrysant.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/chrysant.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/circle.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/circle.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/colors.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/colors.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/conic.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/conic.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/curve.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/curve.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/curveto.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/curveto.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/cycloid.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/cycloid.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/drawing.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/drawing.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/ellipse.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/ellipse.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/fplot.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/fplot.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/geometry.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/geometry.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/grids.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/grids.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/hippo.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/hippo.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/lapdf.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/lapdf.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/licence.txt
%doc %{_texmfdistdir}/doc/latex/lapdf/line.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/line.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/polygon.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/polygon.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/polynom.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/polynom.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/pplot.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/pplot.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/preamble.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/pythagor.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/pythagor.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/qcircle.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/qcircle.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/quartic.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/quartic.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/rational.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/rational.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/rcircle.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/rcircle.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/rcurve.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/rcurve.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/recttria.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/recttria.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/roundtri.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/roundtri.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/rparams.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/rparams.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/superell.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/superell.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/tplot.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/tplot.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/trochoid.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/trochoid.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/turtle.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/turtle.tex
%doc %{_texmfdistdir}/doc/latex/lapdf/vector.pdf
%doc %{_texmfdistdir}/doc/latex/lapdf/vector.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 753125
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 718804
- texlive-lapdf
- texlive-lapdf
- texlive-lapdf
- texlive-lapdf

