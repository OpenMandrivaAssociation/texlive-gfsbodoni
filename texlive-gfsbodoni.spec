Name:		texlive-gfsbodoni
Version:	28484
Release:	1
Summary:	A Greek and Latin font based on Bodoni
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/greek/gfs/gfsbodoni
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsbodoni.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsbodoni.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Bodoni's Greek fonts in the 18th century broke, for the first
time, with the Byzantine cursive tradition of Greek fonts. GFS
Bodoni resurrects his work for general use. The font family
supports both Greek and Latin letters. LaTeX support of the
fonts is provided, offering OT1, T1 and LGR encodings. The
fonts themselves are provided in Adobe Type 1 and OpenType
formats.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/gfsbodoni/GFSBodoni-Bold.afm
%{_texmfdistdir}/fonts/afm/public/gfsbodoni/GFSBodoni-BoldItalic.afm
%{_texmfdistdir}/fonts/afm/public/gfsbodoni/GFSBodoni-Italic.afm
%{_texmfdistdir}/fonts/afm/public/gfsbodoni/GFSBodoni-Regular.afm
%{_texmfdistdir}/fonts/enc/dvips/gfsbodoni/bodoni.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsbodoni/bodonidenomnums.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsbodoni/bodoniec.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsbodoni/bodoniecsc.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsbodoni/bodoniel.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsbodoni/bodonielsc.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsbodoni/bodoninumnums.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsbodoni/bodonisc.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsbodoni/bodonitabnums.enc
%{_texmfdistdir}/fonts/map/dvips/gfsbodoni/gfsbodoni.map
%{_texmfdistdir}/fonts/opentype/public/gfsbodoni/GFSBodoni.otf
%{_texmfdistdir}/fonts/opentype/public/gfsbodoni/GFSBodoniBold.otf
%{_texmfdistdir}/fonts/opentype/public/gfsbodoni/GFSBodoniBoldIt.otf
%{_texmfdistdir}/fonts/opentype/public/gfsbodoni/GFSBodoniIt.otf
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonib8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonib8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonib9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonib9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonibi8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonibi8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonibi9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonibi9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonibo8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonibo8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonibo9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonibo9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonidenomnums8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonidenomnums8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonii8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonii8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonii9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonii9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodoninumnums8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodoninumnums8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonio8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonio8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonio9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonio9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonirg8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonirg8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonirg9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonirg9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonisc8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonisc8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonisc9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonisc9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonisco8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonisco8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonisco9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonisco9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonitabnums8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonitabnums8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonib6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonib6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonibi6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonibi6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonibo6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonibo6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonii6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonii6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonio6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonio6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonio9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonirg6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonirg6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonisc6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonisc6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonisco6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonisco6r.tfm
%{_texmfdistdir}/fonts/type1/public/gfsbodoni/GFSBodoni-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/gfsbodoni/GFSBodoni-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/public/gfsbodoni/GFSBodoni-Italic.pfb
%{_texmfdistdir}/fonts/type1/public/gfsbodoni/GFSBodoni-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonib8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonib9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonibi8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonibi9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonibo8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonibo9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonidenomnums8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonii8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonii9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodoninumnums8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonio8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonio9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonirg8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonirg9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonisc8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonisc9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonisco8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonisco9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonitabnums8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/gbodonib6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/gbodonibi6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/gbodonibo6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/gbodonii6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/gbodonio6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/gbodonio9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/gbodonirg6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/gbodonisc6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/gbodonisco6a.vf
%{_texmfdistdir}/tex/latex/gfsbodoni/gfsbodoni.sty
%{_texmfdistdir}/tex/latex/gfsbodoni/lgrbodoni.fd
%{_texmfdistdir}/tex/latex/gfsbodoni/ot1bodoni.fd
%{_texmfdistdir}/tex/latex/gfsbodoni/t1bodoni.fd
%{_texmfdistdir}/tex/latex/gfsbodoni/ubodoninums.fd
%doc %{_texmfdistdir}/doc/fonts/gfsbodoni/OFL-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/gfsbodoni/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/gfsbodoni/README
%doc %{_texmfdistdir}/doc/fonts/gfsbodoni/README.TEXLIVE
%doc %{_texmfdistdir}/doc/fonts/gfsbodoni/gfsbodoni.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
