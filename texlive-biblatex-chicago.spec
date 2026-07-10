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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a BibLaTeX style that implements the Chicago 'author-date' and
'notes with bibliography' style specifications given in the Chicago
Manual of Style, 17th edition (with continuing support for the 16th
edition, too). The style implements entry types for citing audio-visual
materials, among many others. The package was previously known as
biblatex-chicago-notes-df.

