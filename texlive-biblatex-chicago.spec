%global tl_name biblatex-chicago
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.3b
Release:	%{tl_revision}.1
Summary:	Chicago style files for BibLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-chicago
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-chicago.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-chicago.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a BibLaTeX style that implements the Chicago 'author-date' and
'notes with bibliography' style specifications given in the Chicago
Manual of Style, 17th edition (with continuing support for the 16th
edition, too). The style implements entry types for citing audio-visual
materials, among many others. The package was previously known as
biblatex-chicago-notes-df.

%prep
%setup -q -c -a1
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
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-chicago
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-chicago
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chicago/README
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chicago/RELEASE
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chicago/biblatex-chicago.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chicago/biblatex-chicago.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chicago/cms-dates-intro.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chicago/cms-dates-intro.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chicago/cms-dates-sample.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chicago/cms-dates-sample.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chicago/cms-legal-sample.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chicago/cms-legal-sample.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chicago/cms-noteref-demo.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chicago/cms-noteref-demo.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chicago/cms-notes-intro.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chicago/cms-notes-intro.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chicago/cms-notes-sample.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chicago/cms-notes-sample.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chicago/cms-trad-appendix.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chicago/cms-trad-appendix.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chicago/cms-trad-sample.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chicago/cms-trad-sample.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chicago/dates-test.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chicago/legal-test.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-chicago/notes-test.bib
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/biblatex-chicago.sty
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/chicago-authordate-trad.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/chicago-authordate-trad.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/chicago-authordate-trad16.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/chicago-authordate-trad16.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/chicago-authordate.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/chicago-authordate.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/chicago-authordate16.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/chicago-authordate16.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/chicago-dates-common.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/chicago-dates-common16.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/chicago-notes.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/chicago-notes.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/chicago-notes16.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/chicago-notes16.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/cms-american.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/cms-brazilian.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/cms-british.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/cms-dutch.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/cms-finnish.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/cms-french.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/cms-german.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/cms-icelandic.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/cms-ngerman.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/cms-norsk.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/cms-norwegian.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/cms-nynorsk.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/cms-romanian.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/cms-spanish.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/cms-swedish.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/cms.dbx
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/cmsdocs.sty
%{_datadir}/texmf-dist/tex/latex/biblatex-chicago/cmsendnotes.sty
