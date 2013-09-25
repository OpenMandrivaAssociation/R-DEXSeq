%bcond_without bootstrap
%global packname  DEXSeq
%global rlibdir  %{_libdir}/R/library

%define debug_package %{nil}

Name:             R-%{packname}
Version:          1.6.0
Release:          1
Summary:          Inference of differential exon usage in RNA-Seq
Group:            Sciences/Mathematics
License:          GPL (>= 3)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/DEXSeq_1.6.0.tar.gz
Requires:         R-Biobase 
Requires:         R-hwriter R-methods R-stringr R-statmod 
Requires:         R-biomaRt
%if %{without bootstrap}
Requires:         R-pasilla 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-Biobase
BuildRequires:    R-hwriter R-methods R-stringr R-statmod 
%if %{without bootstrap}
BuildRequires:    R-pasilla 
%endif
BuildRequires:    R-biomaRt

%description
The package is focused on finding differential exon usage using RNA-seq
exon counts between samples with different experimental designs. It
provides functions that allows the user to make the necessary statistical
tests based on a model that uses the negative binomial distribution to
estimate the variance between biological replicates and generalized linear
models for testing. The package also provides functions for the
visualization and exploration of the results.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/python_scripts


%changelog
* Wed Feb 22 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-2
+ Revision: 778840
- Rebuild with proper dependencies

* Sat Feb 18 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-1
+ Revision: 776786
- Import R-DEXSeq
- Import R-DEXSeq



