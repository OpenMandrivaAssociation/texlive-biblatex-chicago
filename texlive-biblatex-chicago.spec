# revision 27254
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-chicago
# catalog-date 2012-07-05 15:34:29 +0200
# catalog-license lppl1.3
# catalog-version 0.9.9
Name:		texlive-biblatex-chicago
Version:	0.9.9
Release:	2
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

%description
This is a biblatex style that implements the Chicago 'author-
date' and 'notes with bibliography' style specifications given
in the Chicago Manual of Style, 15th edition. The style
implements entry types for citing audio-visual materials. The
package was previously known as biblatex-chicago-notes-df.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-chicago/biblatex-chicago.sty
%{_texmfdistdir}/tex/latex/biblatex-chicago/chicago-authordate.bbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/chicago-authordate.cbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/chicago-authordate15.bbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/chicago-authordate15.cbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/chicago-notes.bbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/chicago-notes.cbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/chicago-notes15.bbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/chicago-notes15.cbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/cms-american.lbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/cms-french.lbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/cms-german.lbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/cms-ngerman.lbx
%doc %{_texmfdistdir}/doc/latex/biblatex-chicago/README
%doc %{_texmfdistdir}/doc/latex/biblatex-chicago/RELEASE
%doc %{_texmfdistdir}/doc/latex/biblatex-chicago/biblatex-chicago.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-chicago/biblatex-chicago.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-chicago/biblatex-chicago15.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-chicago/biblatex-chicago15.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-chicago/cms-dates-sample.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-chicago/cms-dates-sample.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-chicago/cms-notes-sample.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-chicago/cms-notes-sample.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-chicago/cms15-dates-sample.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-chicago/cms15-dates-sample.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-chicago/cms15-notes-sample.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-chicago/cms15-notes-sample.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-chicago/dates-test.bib
%doc %{_texmfdistdir}/doc/latex/biblatex-chicago/notes-test.bib

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
