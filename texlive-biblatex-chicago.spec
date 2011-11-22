# revision 24608
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-chicago
# catalog-date 2011-11-15 19:32:33 +0100
# catalog-license lppl1.3
# catalog-version 0.9.8d
Name:		texlive-biblatex-chicago
Version:	0.9.8d
Release:	1
Summary:	Chicago style files for biblatex
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-chicago
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-chicago.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-chicago.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is a biblatex style that implements the Chicago 'author-
date' and 'notes with bibliography' style specifications given
in the Chicago Manual of Style, 15th edition. The style
implements entry types for citing audio-visual materials. The
package was previously known as biblatex-chicago-notes-df.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-chicago/biblatex-chicago.sty
%{_texmfdistdir}/tex/latex/biblatex-chicago/chicago-authordate.bbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/chicago-authordate.cbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/chicago-notes.bbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/chicago-notes.cbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/cms-american.lbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/cms-french.lbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/cms-german.lbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/cms-ngerman.lbx
%doc %{_texmfdistdir}/doc/latex/biblatex-chicago/README
%doc %{_texmfdistdir}/doc/latex/biblatex-chicago/RELEASE
%doc %{_texmfdistdir}/doc/latex/biblatex-chicago/biblatex-chicago.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-chicago/biblatex-chicago.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-chicago/cms-dates-sample.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-chicago/cms-dates-sample.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-chicago/cms-notes-sample.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-chicago/cms-notes-sample.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-chicago/dates-test.bib
%doc %{_texmfdistdir}/doc/latex/biblatex-chicago/notes-test.bib
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
