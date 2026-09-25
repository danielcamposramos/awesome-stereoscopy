# Awesome Stereoscopy [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Stereoscopic 3D: the formats, the standards, the software that speaks them, and the 190 years behind them.

Stereoscopy is older than the photograph. Charles Wheatstone described the stereoscope in 1838, the year *before* photography was announced publicly, and every 3D format since has been one more way of getting a different picture to each eye. This list collects what that history produced and what still works: the encodings, the specifications that define them, the tools that read and write them, and the communities keeping the material alive.
*AI was leveraged as a partner in the development of this work — [more information here](PROVENANCE.md).*

## Contents

- [History](#history)
- [How stereo is stored](#how-stereo-is-stored)
- [Depth, and making the second view](#depth-and-making-the-second-view)
- [Capture](#capture)
- [Who can see it, and who cannot](#who-can-see-it-and-who-cannot)
- [Standards and specifications](#standards-and-specifications)
- [Tools](#tools)
- [Players and viewers](#players-and-viewers)
- [Servers and delivery](#servers-and-delivery)
- [Displays decide the format](#displays-decide-the-format)
- [Displays and devices](#displays-and-devices)
- [Headsets and worn displays](#headsets-and-worn-displays)
- [Beyond the eyes](#beyond-the-eyes)
- [Communities and archives](#communities-and-archives)
- [Preservation](#preservation)
- [Adjacent fields](#adjacent-fields)
- [In fiction](#in-fiction)
- [Related lists](#related-lists)
- [Known gaps](#known-gaps)

## History

Two centuries in five movements. The formats in the next section only make sense in this order.

### Prehistory: knowing about two eyes

The stereoscope is Victorian. Understanding that two eyes see different images, and that this is what depth is made of, is far older and not European in origin.

- [Mozi](https://en.wikipedia.org/wiki/Mozi) - The earliest known description of the [camera obscura](https://en.wikipedia.org/wiki/Camera_obscura) is in the Mohist writings, China, around the 4th century BC: the beginning of understanding how an image forms at all.
- [Euclid's Optics](https://en.wikipedia.org/wiki/Euclid%27s_Optics) - Around 300 BC, notes that the two eyes see different amounts of a sphere. The geometry of binocular disparity, written down two millennia before anyone built a viewer for it.
- [Ibn al-Haytham](https://en.wikipedia.org/wiki/Ibn_al-Haytham) - His [Book of Optics](https://en.wikipedia.org/wiki/Book_of_Optics), completed around 1021 in Cairo, studies [binocular vision](https://en.wikipedia.org/wiki/Binocular_vision) and the fusion of two images experimentally, and is the foundation the European work later built on.
- [Sushruta Samhita](https://en.wikipedia.org/wiki/Sushruta_Samhita) - The ancient Indian surgical compendium attributed to [Sushruta](https://en.wikipedia.org/wiki/Sushruta), which treats the eye as an organ to be studied and operated on, including the couching technique that stands at the head of [cataract surgery](https://en.wikipedia.org/wiki/Cataract_surgery).
- [Nyaya](https://en.wikipedia.org/wiki/Nyaya) and [Vaisheshika](https://en.wikipedia.org/wiki/Vaisheshika) - Indian schools that argued in detail about how [perception](https://en.wikipedia.org/wiki/Visual_perception) works, what the senses contribute and what the mind adds: the same question stereoscopy answers mechanically.
- [Leonardo da Vinci](https://en.wikipedia.org/wiki/Leonardo_da_Vinci) - Identified the problem that defines this entire list: a painting cannot reproduce depth as the eyes see it, because each eye receives a different view and a flat surface can only give one.
- [Giambattista della Porta](https://en.wikipedia.org/wiki/Giambattista_della_Porta) - Wrote on binocular vision in the sixteenth century, in the same generation that drawings later argued to be stereo pairs were made, such as those attributed to [Jacopo da Empoli](https://en.wikipedia.org/wiki/Jacopo_da_Empoli). The attribution is disputed, which is itself worth knowing before repeating it.

### Origins, 1838 onwards

- [Stereoscopy](https://en.wikipedia.org/wiki/Stereoscopy) - The medium itself, and the best single starting point.
- [Charles Wheatstone](https://en.wikipedia.org/wiki/Charles_Wheatstone) - Described the stereoscope in 1838, using drawings, because photography did not yet exist publicly.
- [David Brewster](https://en.wikipedia.org/wiki/David_Brewster) - His lens-based box stereoscope of 1849 turned the effect into a product, shown at the 1851 Great Exhibition.
- [Stereoscope](https://en.wikipedia.org/wiki/Stereoscope) - The viewers themselves and the side-by-side stereo cards they were built for. The 1861 Holmes design is the handheld one everyone recognises, and it is the direct ancestor of a phone in a cardboard holder.
- [Oliver Wendell Holmes Sr.](https://en.wikipedia.org/wiki/Oliver_Wendell_Holmes_Sr.) - Designed that viewer and deliberately never patented it, which is why it became universal.
- [Louis Arthur Ducos du Hauron](https://en.wikipedia.org/wiki/Louis_Arthur_Ducos_du_Hauron) - Patented the anaglyph in 1891, the format that still works on any colour display.

### Stereo photography as a mass medium

- [London Stereoscopic and Photographic Company](https://en.wikipedia.org/wiki/London_Stereoscopic_and_Photographic_Company) - The 1854 London firm whose name became synonymous with the Victorian stereo card.
- [Kilburn Brothers](https://en.wikipedia.org/wiki/Kilburn_Brothers) - The Littleton, New Hampshire firm that mass-produced stereoviews for the American market through the late nineteenth century.
- [Underwood & Underwood](https://en.wikipedia.org/wiki/Underwood_%26_Underwood) - At its peak the largest publisher of stereographs in the world, producing ten million views a year. The title did not stay put: [Keystone View Company](https://en.wikipedia.org/wiki/Keystone_View_Company) is described as the world's largest stereographic company by 1905, and between 1915 and 1921 it bought the negatives of nearly all its competitors, which is how one firm ended up holding the era's output.
- [Keystone View Company](https://en.wikipedia.org/wiki/Keystone_View_Company) - Outlasted its rivals and supplied schools, keeping stereo cards in print into the twentieth century.
- [View-Master](https://en.wikipedia.org/wiki/View-Master) - From 1939, the reels that carried stereo photography through every boom and bust since.
- [Stereo Realist](https://en.wikipedia.org/wiki/Stereo_Realist) - The 1947 camera that made 35 mm stereo slides the ordinary format of the 1950s boom, and whose "Realist format" mount outlived the camera.

### The continental trade

Paris was selling stereo views before London had its famous firm: Duboscq's stereo daguerreotypes and Ferrier's glass views were both on offer by 1852, two years before the London Stereoscopic Company was founded. The continental trade then ran alongside the British and American one for the rest of the century.

- [Jules Duboscq](https://en.wikipedia.org/wiki/Jules_Duboscq) - The Paris instrument maker, trained under Jean-Baptiste Soleil, who built and marketed Brewster's lens stereoscope. His stereoscope was on show at the Great Exhibition of 1851, and his 1852 catalogue already offered stereo daguerreotypes of nearly forty subjects, as the stereo historian Denis Pellerin [sets out](https://stereoscopy.blog/2024/06/21/early-stereo-daguerreotypes-and-lithographs-published-by-jules-duboscq/).
- [Claude-Marie Ferrier](https://en.wikipedia.org/wiki/Claude-Marie_Ferrier) - Credited with the first glass stereoviews for the Brewster stereoscope, in 1852. From 1859 the firm traded with his son and [Charles Soulier](https://fr.wikipedia.org/wiki/Charles_Soulier), who has an article only in French, and in 1863 the business was sold to Léon & Lévy.
- [Léon & Lévy](https://en.wikipedia.org/wiki/L%C3%A9on_%26_L%C3%A9vy) - The successor to Ferrier and Soulier, founded in 1864, which published stereoscopic views of Europe, Asia, Africa and the Americas and became one of the most important postcard publishers in France.
- [Furne & Tournier](https://imagestereoscopiques.com/stereopedia/les-editeurs/furne-tournier/) - The cousins Charles-Paul Furne and Henri-Alexis-Omer Tournier made nearly forty series and some seven thousand stereo photographs between 1857 and 1864: journeys through Brittany, the Pyrenees, Provence and Switzerland, and staged fictions such as *Un mariage sous Louis XV* (1859) and *Une maison à Paris* (1860), told a card at a time. The fullest account is Le Stéréopôle's Stéréopédia, in French.
- [Hippolyte Jouvin](https://en.wikipedia.org/wiki/Hippolyte_Jouvin) - His *Vues instantanées de Paris* (1863), more than two hundred stereographs, used exposures short enough to catch people moving in the streets. Stereo here records the city in motion rather than its empty monuments.
- [Diableries](https://en.wikipedia.org/wiki/Diableries) - Paris, 1860s: sculpted clay scenes of daily life in Hell, satirising the Second Empire, published as stereo "tissue views". Each print was hand-coloured on the reverse and backed with tissue, and the skeletons' eyes were pierced and dabbed with coloured gelatin so that, held to the light, they glow red. The series was begun by François Benjamin Lamiche and expanded to 72 scenes by [Adolphe Block](https://fr.wikipedia.org/wiki/Adolphe_Block), who has an article only in French.
- [Adolphe Braun](https://en.wikipedia.org/wiki/Adolphe_Braun) - From his studio at Dornach in Alsace, produced thousands of stereoscopic views of the Alps in France, Germany, Switzerland and Italy.
- [Lachenal, Favre et Cie](https://gallica.bnf.fr/ark:/12148/btv1b525055719.image) - Glass-stereoview publishers at 72 Boulevard de Sébastopol, Paris, whose *Catalogue général des vues stéréoscopiques sur verre* of 1871, digitised by the Bibliothèque nationale de France, shows what a single firm's list actually held: Paris and Versailles, Italy, Switzerland, Egypt, Hindustan, the Cape and Madagascar, Spain and Portugal, Prussia, Austria, Constantinople, and Russia from Saint Petersburg to Kiev and Kraków, with a section titled "Paris en 1871" printed that same year. The back cover also sells views and photomicrographs for magic-lantern projection, and "stereoscopes of every kind, holding up to 250 views".
- [Carlo Ponti](https://en.wikipedia.org/wiki/Carlo_Ponti_(photographer)) - The Venice optician who published stereographs of the city on an industrial scale. Worth knowing for a contrast as well: his megalethoscope, awarded the Grand Prix in London in 1862, gave an illusion of depth from a *single* photograph under one wide lens, which is [depth without two views](#depth-without-two-views-head-tracking-and-parallax) a century and a half early.
- [Jean Laurent](https://en.wikipedia.org/wiki/Jean_Laurent_(photographer)) - Working from Madrid, made roughly 1,400 stereoscopic photographs, the largest body of stereo views produced in nineteenth-century Spain and about a fifth of his whole output. His English article does not mention them at all; they are documented in [a study of Laurent's stereoscopic photography](http://eprints.rclis.org/43417/).
- [Kaiserpanorama](https://en.wikipedia.org/wiki/Kaiserpanorama) - Stereo as a shared show: around 25 wooden viewing stations, each with a pair of lenses, and a rotating mechanism inside that carried backlit glass stereoviews past them. [August Fuhrmann](https://de.wikipedia.org/wiki/August_Fuhrmann), who has an article only in German, opened the first in Breslau in 1880 and moved it to Berlin's Kaiser-Passage in 1883, and by about 1907 his panoramas ran in some 247 cities. It is counted among the precursors of film.
- [Neue Photographische Gesellschaft](https://de.wikipedia.org/wiki/Neue_Photographische_Gesellschaft) - Founded in Berlin-Schöneberg in 1894 by Arthur Schwarz, one of the largest German producers of postcards, photographs and stereo photographs, and a supplier of views to the Kaiserpanoramas. It has an article only in German.

### Beyond Europe and North America

The stereo view travelled with photography itself. Outside Europe and North America it was made by local studios and court photographers as well as by visitors, and much of that record is documented only in the language of the country that made it:

- [Revert Henrique Klumb](https://ims.com.br/titular-colecao/revert-henrique-klumb/) - Settled in Rio de Janeiro in 1852 and was already making stereoscopic views of the imperial capital by 1855, one of the photographers who brought stereoscopy to Brazil. The account is the Instituto Moreira Salles', in Portuguese.
- [Coleção D. Thereza Christina Maria](https://www.gov.br/bn/pt-br/atuacao/pesquisa-e-editoracao/programa-nacional-de-apoio-a-pesquisa/pnap-2019/a-fotografia-estereoscopica-no-brasil-do-seculo-xix-e-a-colecao-d-thereza-christina-maria) - Emperor Pedro II's own photograph collection, in Brazil's National Library, which includes the stereoscopic views of the photographers of the Imperial House. The library has funded research on it as a record of stereo in nineteenth-century Brazil; in Portuguese.
- [Pioneer Iranian stereo-photographers at the Persian court](https://revistas.ulusofona.pt/index.php/stereo/article/view/6631) - Qajar Iran, 1858–1905: Aqa Reza, made Naser al-Din Shah's chief photographer in 1863, left several hundred stereographs from 1858 to 1865, and Mozaffar al-Din Shah was making stereographs himself on his second journey to Europe in 1903. The peer-reviewed study is candid that the early work shows "a stereo desire that was not paired with proper technological skill".
- [Maison Bonfils](https://heritage.bnf.fr/bibliothequesorient/en/felix-bonfils-1831-1885) - The Beirut studio Félix Bonfils founded in 1867, the first opened there by a Frenchman. By the early 1870s its catalogue listed some fifteen thousand prints and nine thousand stereoscopic views, from negatives made in Egypt, Palestine, Syria and Greece. Neither English Wikipedia article on the studio or its founder mentions the stereo work; this account is the Bibliothèque nationale de France's.
- [T. Enami](https://en.wikipedia.org/wiki/T._Enami) - A Meiji-era Japanese photographer whose hand-coloured stereoviews of Japan were distributed internationally, the Japanese side of the same pre-1900 card boom.
- [Marc Ferrez](https://ims.com.br/por-dentro-acervo/a-fotografia-amadora-e-a-estereoscopia-na-passagem-do-seculo-xix-para-o-xx/) - The Rio de Janeiro photographer who, with his sons Júlio and Luciano, left a large body of black-and-white and colour stereo images. He introduced the Lumière Autochrome to Brazil and used it largely for stereo, mainly with Richard Vérascope cameras. In Portuguese, from the Instituto Moreira Salles.

### Stereo as an instrument

Most of this list is stereo as entertainment. It has also, since before cinema, been a working instrument — a way of seeing small things, mapped ground, distant planets and the Sun itself in depth, where the stereo pair is doing a job rather than telling a story.

- [Stereo microscope](https://en.wikipedia.org/wiki/Stereo_microscope) - The first practical design, by the American zoologist Horatio Saltonstall Greenough in 1892 and made by Zeiss from 1896, gives a binocular, magnified, three-dimensional view of a small object. It is still in everyday use in surgery, electronics and biology, where depth is the point of the tool. The two-eyes-one-object path is the same one Wheatstone described, aimed down at a specimen instead of out at a view.
- [Stereoplotter](https://en.wikipedia.org/wiki/Stereoplotter) - The instrument that turned overlapping [aerial photographs](https://en.wikipedia.org/wiki/Aerial_photography) into surveyed maps, by fusing the pair into a stereo model of the terrain. Stereo aerial photography, flown for reconnaissance and cartography through two world wars, is the reason much of the twentieth century's ground was measured in stereo before it was measured any other way; the software descendants of that measurement sit under [From depth to objects](#from-depth-to-objects).
- [Curiosity rover](https://en.wikipedia.org/wiki/Curiosity_(rover)) - Drives on stereo: its black-and-white Navcam and Hazcam cameras are stereo pairs that see the ground in 3D. Its colour Mastcams are not a matched pair (34 mm and 100 mm lenses), so NASA's Mastcam 3D views are often made by shooting again after the rover has moved sideways. Perseverance's [Mastcam-Z](https://en.wikipedia.org/wiki/Mastcam-Z) is a true stereoscopic pair of zoom cameras. NASA publishes the results in its [anaglyph gallery](https://science.nasa.gov/photojournal/galleries/pj-anaglyphs/), one of the few places the general public still meets red-blue stereo today.
- [STEREO](https://en.wikipedia.org/wiki/STEREO) - NASA's Solar Terrestrial Relations Observatory: two nearly identical spacecraft launched in 2006 into solar orbits that carry one ahead of Earth and the other behind, a stereo baseline that grew to hundreds of millions of kilometres, aimed at the Sun. In April 2007 NASA published [the first three-dimensional images of the Sun taken from a real stereo baseline](https://science.nasa.gov/photojournal/full-disk-image-of-the-sun-march-26-2007-anaglyph/), as anaglyphs. Solar features had been reconstructed in 3D before, from one instrument and the Sun's own rotation, which is parallax borrowed from time rather than from two positions at once. NASA [explained the STEREO pair](https://science.nasa.gov/earth/earth-observatory/first-3-d-vews-of-the-sun-7618/) exactly as this list would: "just as our two eyes give us a three-dimensional view of the world", the two spacecraft give one of the Sun. Its SECCHI instruments were built to follow coronal mass ejections in 3D from the Sun's surface to their impact at Earth, where they can disrupt satellites, communications and power grids. On 6 February 2011 the pair were exactly 180° apart and the entire Sun was seen at once for the first time; contact with STEREO-B was lost in 2014.

### Cinema and Hollywood

- [3D film](https://en.wikipedia.org/wiki/3D_film) - The whole cycle of revivals, and the best overview of why each one ended.
- [The Power of Love](https://en.wikipedia.org/wiki/The_Power_of_Love_(film)) - The 1922 feature generally credited as the first shown to a paying audience in stereo.
- [Bwana Devil](https://en.wikipedia.org/wiki/Bwana_Devil) - The 1952 film that started Hollywood's golden era of 3D.
- [House of Wax](https://en.wikipedia.org/wiki/House_of_Wax_(1953_film)) - 1953, the first colour 3D feature from a major studio, and the era's biggest hit.
- [Creature from the Black Lagoon](https://en.wikipedia.org/wiki/Creature_from_the_Black_Lagoon) - 1954, the era's most enduring title.
- [Dial M for Murder](https://en.wikipedia.org/wiki/Dial_M_for_Murder) - Hitchcock shot it in 3D in 1954, then it was mostly shown flat: the era's ending in one film.
- [Jaws 3-D](https://en.wikipedia.org/wiki/Jaws_3-D) and [Friday the 13th Part III](https://en.wikipedia.org/wiki/Friday_the_13th_Part_III) - The early-1980s revival, remembered mostly for things thrown at the camera, which is a large part of why the format kept having to earn its reputation back.
- [Captain EO](https://en.wikipedia.org/wiki/Captain_EO) ([Japanese article](https://ja.wikipedia.org/wiki/%E3%82%AD%E3%83%A3%E3%83%97%E3%83%86%E3%83%B3EO)) - 1986, seventeen minutes, 70mm 3-D: directed by Francis Ford Coppola, executive-produced by George Lucas, starring Michael Jackson, built by Disney as a park attraction, a gathering of those four names that never happened again, and at an officially unreleased cost — estimates run $17–30 million for seventeen minutes, $23.7 million being the usual quote, some $70 million in 2025 dollars — the most expensive film ever made per minute when it premiered; the later holder of that record is T2-3D a park generation on (its entry and the per-minute math are below). The gathering itself was Jackson's doing: he insisted the era's top names join, Spielberg or Lucas — Spielberg was committed, Lucas agreed and brought Coppola. The money was Disney's all-in parks budget plus a Kodak share after a Frank Wells renegotiation, fought over by Lucas and Katzenberg as it roughly doubled — no production history has Jackson paying; what he paid was attention: the scarier Supreme Leader and the finale kept apart from the plot were his calls over Coppola's, and with Coppola already on Peggy Sue Got Married, Jackson and Rusty Lemorande did the reshooting and recutting themselves. It ran at the Disney parks from 1986, returned in 2010 after fan campaigns following Jackson's death, and played for the last time anywhere at Epcot on 6 December 2015. The best argument on record that stereo 3D was never only a gimmick, with [sourced production notes](https://github.com/danielcamposramos/sony-bravia-linux/blob/main/docs/judging-by-the-cover.md) for the chaos behind it; its park chapter is [below](#theme-parks-where-3d-never-stopped).
- [4D film](https://en.wikipedia.org/wiki/4D_film) - Stereo projection plus effects in the room: motion seats, water, air, scent. The venue format that outlived every consumer 3D wave, because the experience cannot be taken home. The "5D" and "6D" booths in shopping centres are the same thing with a larger number on the sign, and the count has no technical meaning.
- [IMAX](https://en.wikipedia.org/wiki/IMAX) - Where large-format stereo projection was kept working continuously between the revivals.
- [Terminator 2 in 3D](https://variety.com/2017/artisans/production/james-cameron-terminator-3d-1202535947/) - The 2017 conversion of James Cameron's 1991 film. Its colours were [re-timed from scratch](https://whatculture.com/film/terminator-2-3d-review-6-ups-3-downs?page=2): the image was brightened to make up for the light the glasses absorb, and the trailers' grade leaned visibly cyan. Converted 3D is a colour problem as much as a depth problem.

### World stereo cinema

Hollywood's golden era is the loudest chapter, not the only one — these cinemas ran in parallel, and together they answer the idea that stereo film is a single-nation story:

- [Semyon Pavlovich Ivanov](https://ru.wikipedia.org/wiki/%D0%98%D0%B2%D0%B0%D0%BD%D0%BE%D0%B2,_%D0%A1%D0%B5%D0%BC%D1%91%D0%BD_%D0%9F%D0%B0%D0%B2%D0%BB%D0%BE%D0%B2%D0%B8%D1%87_%28%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B5%D1%82%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%29) - Russian, 1906-1972, who invented the Soviet glasses-free stereoscopic cinema system in 1935: a radial raster screen that let an audience see stereo with no glasses at all, a decade before Hollywood's golden era began. Moscow had a cinema running on it from 1941. His article is in Russian and there is none in English, where the same name returns a Soviet general instead, which is the Anglo-centrism of this subject in one example. See also [autostereoscopy in Russian](https://ru.wikipedia.org/wiki/%D0%90%D0%B2%D1%82%D0%BE%D1%81%D1%82%D0%B5%D1%80%D0%B5%D0%BE%D1%81%D0%BA%D0%BE%D0%BF%D0%B8%D1%8F), which describes his raster.
- [Robinson Crusoe](https://en.wikipedia.org/wiki/Robinson_Crusoe_(1947_film)) - The 1947 Soviet 3D feature shown on that system, glasses-free, and the most visible surviving artefact of a stereo-cinema programme that ran in parallel with Hollywood's.
- [The Soviet stereokino programme](https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D0%B5%D1%80%D0%B5%D0%BE%D0%BA%D0%B8%D0%BD%D0%B5%D0%BC%D0%B0%D1%82%D0%BE%D0%B3%D1%80%D0%B0%D1%84) - Not one film but a state cinema that ran for decades: after Robinson Crusoe the system matured into **Стерео-70** (1963), which won an Academy Award for technical achievement and shot more than thirty films, including puppet animation. The fullest account is the Russian Wikipedia article on stereocinematography, which has no English equivalent.
- [Toho Toovision](https://eiga.com/extra/oguchi/7/2/) - Japan's first 3D fiction films: two anaglyph shorts, *Watashi wa nerawarete iru* (私は狙われている) and *Tobidashita nichiyōbi* (飛び出した日曜日), which opened at the Nichigeki in Tokyo on 22 April 1953. The camera system had been developed from 1941 by the Toho engineer Kiichi Iwabuchi, at the studio unit that made training films for naval aviation. Shochiku answered on 12 May with *Kettō* (決闘), shot on its own "Shochiku Natural Vision" system, and then both studios announced they would stop making 3D films to concentrate on widescreen, TohoScope and Shochiku GrandScope: [the format war](#the-format-war-that-decided-the-frame), fought again in Japan. The history is by the stereo-film researcher Takayuki Ōguchi, in Japanese; see also [the Japanese Wikipedia article on 3D film](https://ja.wikipedia.org/wiki/%E7%AB%8B%E4%BD%93%E6%98%A0%E7%94%BB).
- [El Corazón y la Espada](https://cinema.wisc.edu/2025/03/06/sword-of-granada-a-golden-age-3-d-rarity/) - *Sword of Granada*, 1953: shot by Estudios Tepeyac on a dual-camera 3D rig from the Howard Anderson Optical Company, and shown in dual-strip polarised 3D. It is usually billed as the first 3D feature shot in Mexico, a claim the UW–Madison Cinematheque note linked here calls contentious, since Rosa Elena Cabiedes' 54-minute *El Reportero TD* may predate it by about a year. Restored by the 3D Film Archive and screened again in 2025.
- [Buenos Aires en relieve](https://www.archivorta.com.ar/buenos-aires-en-relieve-la-primera-pelicula-argentina-en-3d-1954/) - Argentina's first 3D film, a medium-length picture directed by Don Napy with Jorge A. Duclout as technical director for the relief and the colour. It premiered on 10 March 1954 at the first Mar del Plata International Film Festival, with President Perón present, on the same programme as André de Toth's *House of Wax*, and was billed as made "entirely by Argentine technicians and systems". It has no Wikipedia article; the account is from the historical archive of Radio y Televisión Argentina, in Spanish.
- [The Magician's Adventure](https://zh.wikipedia.org/wiki/%E9%AD%94%E6%9C%AF%E5%B8%88%E7%9A%84%E5%A5%87%E9%81%87) - 魔术师的奇遇, 1962: the People's Republic of China's first widescreen colour film and its first 3D film, directed by Sang Hu for the Tianma studio and watched through red-green glasses. It ran in cinemas continuously for four years. The article is in Chinese only.
- [A Man of Great Strength, Im Ggyeok-jeong](https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE10738593) - 천하장사 임꺽정, 1968: identified in Korean film scholarship as the first Korean 3D film. It has no English Wikipedia article; the source is a Korean film-studies paper, in Korean.
- [My Dear Kuttichathan](https://en.wikipedia.org/wiki/My_Dear_Kuttichathan) - India's first 3D film, a 1984 Malayalam children's feature released alongside Tamil, Telugu and Hindi dubs. Hindi cinema followed with [Shiva Ka Insaaf](https://en.wikipedia.org/wiki/Shiva_Ka_Insaaf_(1985_film)) (1985), termed the first Hindi film shot in 3D, and the digital wave reached it with [Haunted – 3D](https://en.wikipedia.org/wiki/Haunted_%E2%80%93_3D) (2011), the first Indian stereoscopic 3D horror film.
- [Brasil Animado](https://en.wikipedia.org/wiki/Brasil_Animado) - A 2011 feature by Mariana Caltabiano that mixes live action and animation, described as the first Brazilian film produced entirely in 3D.
- [Legend of the Naga Pearls](https://en.wikipedia.org/wiki/Legend_of_the_Naga_Pearls) - A 2017 Chinese 3D fantasy film, one of the post-*Avatar* wave of Chinese-language 3D productions.

### The format war that decided the frame

The stereo formats below did not choose their shape in a vacuum. They inherited a century-long fight over the shape of the frame itself, and over how much of it a home screen is allowed to show. Two threads of that fight reach stereo directly, and [Slidebean](https://www.youtube.com/c/Slidebean)'s [*Why Do Movies Have Black Bars?*](https://www.youtube.com/watch?v=Pq8YoHpmlKs) tells the whole war in one sitting, and its longer successor [*The brilliant scam of cinematic "black bars"*](https://www.youtube.com/watch?v=JYg0rBfAz6U) follows the same fight through the anamorphic lens, the pan-and-scan VHS era in which buyers were sold cropped films without being told, and the 16:9 compromise every modern set inherited.

**The aspect-ratio war.** Silent film settled on a near-square 1.33:1. The arrival of sound in the late 1920s, and the [Academy ratio](https://en.wikipedia.org/wiki/Academy_ratio) of 1.37:1 that followed it, left the frame at 1.37 — so close to television's 1.33:1 that the two media were almost, and never quite, the same shape. When television filled living rooms in the 1950s, Hollywood answered by making films that could not fit a TV: [Cinerama](https://en.wikipedia.org/wiki/Cinerama) (three cameras, three projectors), [VistaVision](https://en.wikipedia.org/wiki/VistaVision) (35mm run sideways for double the negative), 65mm [Super Panavision 70](https://en.wikipedia.org/wiki/Super_Panavision_70), and the anamorphic squeeze of [CinemaScope](https://en.wikipedia.org/wiki/CinemaScope). The war produced the catalogue of ratios — 1.33, 1.37, 1.66, 1.78, 1.85, 2.20, 2.35, 2.39, 2.76 — that still decides how much of a screen goes black.

**The 16:9 truce.** The one ratio that was not a weapon was 16:9 (1.78:1). It was proposed at SMPTE in 1984 by Kerns H. Powers as the [geometric mean](https://en.wikipedia.org/wiki/Geometric_mean) of the extremes, 4:3 and 2.35:1 — a single shape inside which every existing ratio fits with the least waste. It is the only format here chosen for compatibility rather than spectacle, which is why the modern television is 16:9.

**The anamorphic squeeze, the trick half-SBS inherited.** CinemaScope ran on the [Hypergonar](https://en.wikipedia.org/wiki/Henri_Chr%C3%A9tien), an anamorphic lens by Henri Chrétien whose lineage runs back to the wide-view periscopes of First World War tanks. A 2× horizontal squeeze records a wide picture on ordinary 35mm film; a matching lens at the projector unsqueezes it. This is the same squeeze-and-unsqueeze that side-by-side relies on, and the same failure: if nothing unsqueezes it, it stays stretched. Half-SBS is CinemaScope with the second lens missing.

### Theme parks: where 3D never stopped

Consumer 3D came and went twice. In parks it simply ran, for decades, because the venue can charge for what a living room cannot reproduce.

- [Magic Journeys](https://en.wikipedia.org/wiki/Magic_Journeys) - 1982, Disney's first 3D film, and the start of the park lineage.
- [Captain EO](https://en.wikipedia.org/wiki/Captain_EO) - 1986, the park chapter of [the cinema-era entry above](#cinema-and-hollywood), and the one whose credits gather the people who kept pursuing the dream of bringing this tech to the masses: Francis Ford Coppola directed, George Lucas executive-produced, Michael Jackson starred, Disney built it — a gathering that never repeated. The two directors with the deepest personal stakes in stereo each left their mark in this park lineage: Lucas, here in 1986 and again with the 3D Star Wars re-release of 2012, and James Cameron, with T2-3D in 1996 (the entry below) and then Avatar. Of the 2010 tribute revival, Tokyo Disneyland was the first park to close its run, on 30 June 2014 (announced the previous December, to make way for Stitch Encounter), and Epcot the last, on 6 December 2015, the final showing anywhere. And Tokyo's theatre carries this section's thesis in one building: Captain EO from 1987 to 1996, then Honey, I Shrunk the Audience! (the entry below, which Tokyo was also the last park in the world to close), then the Captain EO tribute from 2010 to 2014 — a 3D show running in that room, essentially unbroken, for twenty-seven years, longer than any park in the USA managed. Part of that longevity is human: in the United States Jackson's star dimmed after [the 1993 accusations](https://en.wikipedia.org/wiki/1993_Michael_Jackson_sexual_abuse_allegations), while in Japan he never stopped being an idol — MTV Japan gave him its Legend Award at the [2006 Video Music Awards Japan](https://en.wikipedia.org/wiki/2006_MTV_Video_Music_Awards_Japan), before eight thousand people in Tokyo — and Tokyo's audiences never stopped adoring his stereo film. Put the numbers together and one more title lands: no 3D film was ever on show more often — four parks across two runs add up to over fifty venue-years of daily showings between 1986 and 2015, and the 2010 tribute exists because fan campaigns demanded it, the only 3D film audiences ever brought back from retirement. Honours honestly shared: T2-3D later out-spent it per minute, and Muppet*Vision holds the longest single-venue run, thirty-three years in one theatre; nobody else had the comeback.
- [Muppet*Vision 3D](https://en.wikipedia.org/wiki/Muppet*Vision_3D) - 1991, Jim Henson's last completed project, and a masterclass in using stereo for comic timing rather than for objects flying at the audience.
- [Honey, I Shrunk the Audience!](https://en.wikipedia.org/wiki/Honey,_I_Shrunk_the_Audience!) - 1994, which took over Captain EO's theatre and held it until Captain EO came back; when the revival evicted it, Tokyo Disneyland was the last park in the world to let it go, on 10 May 2010.
- [T2-3D: Battle Across Time](https://en.wikipedia.org/wiki/T2-3D:_Battle_Across_Time) - 1996, directed by James Cameron for the Universal parks: 70mm 3D intercut with live actors on stage, and the holder of the per-minute budget record Captain EO set a decade earlier. The record deserves the same math the EO entry gets: roughly $60 million for twelve minutes is $5 million a minute, and matched for the economy of each year (US CPI 1986→1996 ≈ ×1.43) Captain EO's high estimate of $30 million works out near $2.5 million a minute in 1996 money — Cameron's commission still nearly doubles it. The money's origin is the contrast worth keeping: T2-3D was a clean studio-park commission, and EO's record budget had been Disney going all-in on a park attraction its star had personally dreamed up.
- [It's Tough to Be a Bug!](https://en.wikipedia.org/wiki/It%27s_Tough_to_Be_a_Bug!) - 1998, in-theatre effects married to stereo.
- [Shrek 4-D](https://en.wikipedia.org/wiki/Shrek_4-D) - 2003, the format's most widely cloned example.
- [Pirates 4-D](https://en.wikipedia.org/wiki/Pirates_4-D) - 1999, the same formula outside the big two.
- [Back to the Future: The Ride](https://en.wikipedia.org/wiki/Back_to_the_Future:_The_Ride) - 1991. Included as the honest contrast: a motion simulator with 70mm dome projection, *not* stereoscopic, which is exactly the line "4D" marketing tends to blur.
- [Digital 3D](https://en.wikipedia.org/wiki/Digital_3D) - The projection technology behind the 2000s revival.
- [RealD 3D](https://en.wikipedia.org/wiki/RealD_3D) - Circular-polarised projection, the system most cinema 3D actually runs on.
- [Dolby 3D](https://en.wikipedia.org/wiki/Dolby_3D) - The wavelength-multiplexing alternative, with expensive glasses and no silver screen.
- [Avatar](https://en.wikipedia.org/wiki/Avatar_(2009_film)) - 2009, the film that made studios, broadcasters and television manufacturers commit at once.
- [Hugo](https://en.wikipedia.org/wiki/Hugo_(film)) - 2011, the counter-example usually cited for 3D as a language rather than an effect.

### Television and home video

The asymmetry here is the part worth noticing. Cinema 3D continued while consumer 3D was withdrawn, and the withdrawal has dates. The broadcasters went first: DirecTV stopped its 3D programming in 2012, ESPN in 2013, and the BBC ended its 3D shows the same year, citing a "lack of public appetite". Then the manufacturers: Vizio stopped making 3D sets in 2014, Samsung in March 2016, Panasonic after it, and in January 2017 the last two holdouts, Sony and LG, [dropped 3D support entirely](https://www.smh.com.au/technology/its-official-3d-tv-is-dead-20170127-gtznpi.html) — the report at the time concluding that "the cinema will soon, once again, be the only place for 3D films". It was right, and 3D screenings are still routine in multiplexes today. The explanation usually given is commercial rather than technical, since a cinema ticket, an IMAX screen or a theme-park attraction can carry a surcharge and a living room cannot. That incentive is on the record: [Regal lists a 3D surcharge](https://www.regmovies.com/help/tickets-and-cancellations), while [IMAX tells investors](https://www.sec.gov/Archives/edgar/data/921582/000092158225000037/imax_10kx932691xars24.pdf) that exhibitors charge premium prices and that the resulting incremental box office benefits exhibitors and studios. Worth noting too, from [The Verge at CES 2013](https://www.theverge.com/2013/1/7/3848856/sony-ces-2013-4k-oled-prototypes-to-flagship-xperia-phones), that Sony had tried to own every link of the chain for 3D — content creation, distribution and playback — before running exactly the same play for 4K, which is the one that stuck. Whatever the reason, the effect on owners was the same: hardware that kept its panel and lost its ecosystem, which is why several entries in this list are about recovering formats rather than buying them.

- [3D television](https://en.wikipedia.org/wiki/3D_television) - The 2010-2013 consumer wave, the ramp-up after *Avatar*, and the withdrawal that followed.
- Multiview Video Coding - The MVC extension that carried Blu-ray 3D, and the reason a 3D disc is not simply two files.
- [3D television broadcasting in Japan](https://ja.wikipedia.org/wiki/%E7%AB%8B%E4%BD%93%E3%83%86%E3%83%AC%E3%83%93%E6%94%BE%E9%80%81) - A national 3D broadcast era from start to finish, documented in Japanese Wikipedia with no English equivalent. BS11 began regular 3D broadcasting in December 2007, in the "MT" format developed by NHK Media Technology, and BS-TBS followed, two years before the post-*Avatar* sets. Sky PerfecTV! started HD 3D on 19 June 2010, BS11 carried Japan's first live 3D broadcast, from the Sanja Festival, the same year, and WOWOW ran a paid 3D slot from April 2012 to March 2015. The end is dated too: when BS11's short programme *3D Kikō* finished on 30 September 2015, regular 3D disappeared from free commercial television.
- [Integral 3D television](https://ja.wikipedia.org/wiki/%E3%82%A4%E3%83%B3%E3%83%86%E3%82%B0%E3%83%A9%E3%83%AB%E7%AB%8B%E4%BD%93%E3%83%86%E3%83%AC%E3%83%93) - The glasses-free line of NHK's Science & Technology Research Laboratories: a lens array of tiny lenses used for both capture and display, developed as an application of 8K Super Hi-Vision, with the first prototype shown at the laboratories' 1999 open house. A [2007 visit report](https://gijutsu.jbmia.or.jp/rep_res/2007/07kengaku-NHK.pdf) records it as joint research with JVC, commissioned by NICT. It is documented in Japanese only; the English article on the laboratories does not mention it.

### PC gaming and the driver era

A rendered game is already a stereo source, which is why this era happened at all. The engine holds the scene as geometry and a camera looking at it, so a second view costs one more camera, offset by the distance between two eyes. Nvidia's own description of the mechanism is plain about it: the driver performs "automatic stereoscopic conversion by using the 3D models submitted by the application and rendering two stereoscopic views instead of the standard mono view". Nothing is estimated and no depth is guessed. That is the difference between this and the 2D-to-3D conversion further up the list, and it is why a driver could deliver real parallax in games written years earlier by people who had never thought about stereo. Perspective projection, which computer graphics inherited from the Renaissance, was always an attempt to put depth on a flat surface; binocular disparity is the one depth cue it cannot fake, and rendering twice is the whole of the fix.

- [VMD “stereo in a window”](https://www.ks.uiuc.edu/Research/vmd/vmd-1.5/ug/node104.html) - The missing pre-consumer lineage. VMD's CrystalEyes mode on SGI RealityEngine2 let one display window run in stereo while the other desktop windows remained normal. VMD was publicly released in 1995, and this contemporary documentation calls the arrangement “new-style stereo”: windowed stereoscopy was real workstation software years before iZ3D, not a later consumer-driver invention.
- [StereoGraphics on HP windowed OpenGL stereo](https://www.schneider-digital.com/wp-content/downloadcenter/3D-Stereo/How_To_implement_QuadBuffer_Stereo/older_instructions/how_to_implement_stereo.pdf) - A 1998 programming guide separating the old whole-screen Starbase path from windowed OpenGL stereo buffering on HP Visualize FX hardware. It describes the four-buffer contract directly: front-left, front-right, back-left and back-right.
- [Nvidia Quadro windowed stereo](https://developer.download.nvidia.cn/GPU_Programming_Guide/GPU_Programming_Guide.pdf) - Nvidia's GPU Programming Guide records that OpenGL quad-buffered stereo works in windowed mode; the chapter entered the guide in July 2004. The matching [Quadro workstation guide](https://download.nvidia.com/Windows/61.76/61.76_Quadro_Release_60_Graphics_Display_Property_Users_Guide..pdf) says its stereo pixel formats organize memory so stereoscopic and monoscopic applications can run simultaneously. Nvidia's 2003 consumer game driver was still fullscreen-only, so workstation OpenGL and consumer injection were distinct branches.
- [DirectDraw stereo surface pairs](https://learn.microsoft.com/en-us/windows/win32/api/ddraw/ns-ddraw-ddscaps2) - Microsoft's `DDSCAPS2_STEREOSURFACELEFT` flag paired a left-eye surface with every right-eye surface in a primary flip chain. It is the Windows-era API evidence for applications submitting two synchronized views before automatic game wrappers became the familiar model.
- [Nvidia 3D Vision](https://en.wikipedia.org/wiki/Nvidia_3D_Vision) - Active-shutter kit and driver that rendered existing games in stereo. Its 3DTV Play half sent that stereo to a 3D television over [HDMI 1.4](https://en.wikipedia.org/wiki/HDMI) as frame packing — the same frame packing the set auto-detects — so a GeForce card drove the TV straight from the PC using the set's own glasses. Discontinued in 2019.
- [iZ3D](https://en.wikipedia.org/wiki/IZ3D) - The vendor-neutral alternative: a dual-LCD monitor with passive glasses and a driver that worked on AMD and Nvidia alike, at a time when stereo was being locked to one GPU vendor. Contemporary reviews describe what that actually meant to use: [Ubergizmo](https://www.ubergizmo.com/2008/03/iz3d-22-lcd-monitor-review/) on the bulk of two stacked panels and the setup, [Digital Reviews Network](https://www.digitalreviews.net/reviews/reviews-archives/iz3d-gaming-monitor-reviewed/) on the polarization, the washed-out 2D mode and imperfect eye separation. The company folded around 2012, and then did the opposite of what this era's software usually does: the original developers released the driver's source code under the MIT licence, kept at [bo3b/iZ3D](https://github.com/bo3b/iZ3D) — "generously provided to us by Vadim and crew", as that repository puts it, with the stated goal of replacing 3D Vision with something non-proprietary.
- [TriDef 3D](https://roadtovr.com/ddd-release-beta-tridef-3d-drivers-with-experiemental-oculus-rift-support/) - The third driver of the era, from **DDD Group** ("Dynamic Digital Depth", the "DDD" mark). TriDef Ignition injected stereo into DirectX games the same way iZ3D did, powered AMD's HD3D, shipped in Acer, Lenovo and Samsung notebooks, and reached the VR wave with experimental Oculus Rift support. A dead product now documented by its [archived site](https://web.archive.org/web/20171001060410/https://www.tridef.com/), a community [game-profile library](https://github.com/drowhunter/TridefProfiles), and a [PCGamingWiki glossary entry](https://www.pcgamingwiki.com/wiki/Glossary:TriDef_3D).
- [Nvidia 3D Vision Vs. AMD HD3D: 18 Games, Evaluated](https://www.tomshardware.com/reviews/tridef-stereoscopic-3d-gaming,3019.html) - Tom's Hardware, 2011, twenty-two pages: the era's most thorough test of whether these drivers actually delivered, title by title, with the verdicts buyers had no other way to obtain — which games were excellent, which were "not recommended", and which broke under DirectX 11. It also states the buying reality plainly: an AMD user needed "a TriDef or iZ3D 3D middleware game driver (or both)", because the stereo layer was middleware you bought separately. The live copy now sits behind a membership wall, and its [first page had never been archived by anyone](https://web.archive.org/web/20260919071832/https://www.tomshardware.com/reviews/tridef-stereoscopic-3d-gaming,3019-1.html) until September 2026.
- [wiz3D](https://github.com/effcol/wiz3D) - "We See 3D", the living continuation of that source: a universal stereo wrapper for DirectX 7-11 and OpenGL, LGPL-2.1, under active development in 2026. It replaces iZ3D's kernel-level hooks with a proxy DLL, needs no proprietary driver or kernel component, outputs side-by-side, top-and-bottom and anaglyph, and re-enables the stereo paths already sitting unused inside games that shipped with AMD HD3D or 3D Vision support. The vendor-neutral idea outliving both vendors' own implementations.
- [VR Stereo Spectator](https://github.com/danielcamposramos/sony-bravia-linux/tree/main/tools/vr-stereo-spectator) - The other route to the same goal, 2026: a replacement `sourcevr.so` for Half-Life 2 that implements Valve's own VR interface for a 3D television instead of a headset. The game's VR mode already renders both eyes, so the module supplies off-axis eyes sharing one window at the screen plane, packs them side by side or top and bottom, puts the HUD, crosshair and menus on a 2D layer at zero parallax, and lets the game's view replace head tracking; shadows, lighting and effects come out right in each eye because the engine draws each eye itself, where a wrapper must reconstruct them. On Linux it runs through [DXVK](https://github.com/doitsujin/dxvk), the Vulkan implementation of Direct3D 9 that Half-Life 2 uses with `-vulkan` (its OpenGL path crashed in VR mode), and it played through saves and level transitions on two Sony 3D sets in September 2026. For screens with no 3D mode, a [gamescope effect](https://github.com/danielcamposramos/sony-bravia-linux/tree/main/tools/vr-stereo-spectator/anaglyph) turns its side-by-side output into red/cyan anaglyph, with one matrix for CRT phosphors and one for modern LCD panels. Its [formula](https://github.com/danielcamposramos/sony-bravia-linux/blob/main/tools/vr-stereo-spectator/FORMULA.md) lists what any VR engine needs to change to drive a 3D display: the counterpart for VR games of what wiz3D does for games that never had a VR mode.
- [Multiple buffering](https://en.wikipedia.org/wiki/Multiple_buffering) - Quad buffering, the API-level mechanism stereo rendering depends on.

### Consoles

- [Sega 3-D Glasses](https://en.wikipedia.org/wiki/Sega_3-D_Glasses) - SegaScope, 1987: active-shutter glasses for the Master System, plugged into the card slot, with eight games including *Space Harrier 3-D*, *Zaxxon 3-D* and *OutRun 3-D*. The Master System II dropped the card slot, and the 3D with it.
- [Famicom 3D System](https://en.wikipedia.org/wiki/Famicom_3D_System) - Nintendo's answer the same year, Japan only, ¥6,000: shutter glasses on the expansion port, games running flat until a button press switched them to stereo. Both of these chose shutters over anaglyph twenty-three years before the console 3D wave, and both failed.
- [PlayStation 3](https://en.wikipedia.org/wiki/PlayStation_3) - The console that made home stereo ordinary. System software [3.30](https://blog.playstation.com/2010/04/21/ps3-3-30-system-software-update/) (April 2010) added stereoscopic *gaming* console-wide, and said why: "in time for the launch of Sony's 3D BRAVIA TVs". [3.50](https://blog.playstation.com/archive/2010/09/21/ps3-system-software-update-ver-3-50) (September 2010) added Blu-ray 3D films, needing only "a 3D compatible television that complies with the 3D standard and a high-speed HDMI cable". Sony's [own running list](https://blog.playstation.com/2011/07/01/stereoscopic-3d-on-ps3-updated-list-of-all-3d-games-and-movies/) reached 58 3D games and films by July 2011, *WipEout HD*, *Gran Turismo 5*, *Killzone 3*, *Uncharted 3* and *Batman: Arkham City* among them.
- [PlayStation 3D Display](https://sonyinteractive.com/en/press-releases/2011/sony-computer-entertainment-announces-3d-display-to-further-expand-the-world-of-3d-on-playstation3-hitting-worldwide-market-in-fall-2011/) - The 24-inch set Sony built for it (CECH-ZED1, November 2011, $499.99), notable for using the glasses for something other than depth: in **SimulView** two players each saw a *different full-screen image* instead of a split screen, one eye's channel per player. [Sony's FAQ](https://blog.playstation.com/2011/10/19/3d-display-arrives-in-november-read-the-faq/) names the launch titles: *MotorStorm Apocalypse*, *Gran Turismo 5*, *Killzone 3* and *Super Stardust HD*. It has no Wikipedia article.
- [Xbox 360](https://en.wikipedia.org/wiki/Xbox_360) - The other side of that generation: stereo games shipped as half-resolution side-by-side inside an ordinary 720p frame, until a 2011 update adopted the same oversized-buffer trick for full 720p per eye ([The Register](https://www.theregister.com/2011/05/24/microsoft_xbox_goes_3d/)).

**The PS3 did frame packing by hand.** Its HDMI output is 1.3a, a version that predates 3D, so the console emulates two of the HDMI 1.4 3D modes and renders stereo games into an oversized 1280×1470 buffer: two 720p eyes with thirty blank rows between them, which is frame packing built by the application rather than the port. Movies used the other mode, 1080p at 24Hz. Developers could drop to narrower buffers for performance, and the eye pair travelled together in one frame either way — the same arrangement the television has to be told about, a decade before the same argument had to be had with media players.

**Then the television stopped being the 3D display.** [PlayStation 4](https://en.wikipedia.org/wiki/PlayStation_4) and Xbox One both added Blu-ray 3D *playback* in 2014, but neither offered console-wide stereo game output the way the PS3 had, and the ninth generation dropped the discs too: the [PlayStation 5](https://en.wikipedia.org/wiki/PlayStation_5) drive reads Ultra HD Blu-ray, Blu-ray and DVD, and neither CDs nor Blu-ray 3D. Stereo did not disappear, it moved indoors: [PlayStation VR](https://en.wikipedia.org/wiki/PlayStation_VR) (2016) and [PlayStation VR2](https://blog.playstation.com/2022/11/02/playstation-vr2-launches-in-february-at-549-99/) (2023) put the two views back where only the wearer can see them. Blu-ray 3D was never a streaming format, so those discs and an ageing player are the whole of that archive.

### Games and handhelds

- [Virtual Boy](https://en.wikipedia.org/wiki/Virtual_Boy) - Nintendo's 1995 worn stereo display: a commercial failure, and a genuine mirror-scanned stereoscope.
- [Stereoscopic video game](https://en.wikipedia.org/wiki/Stereoscopic_video_game) - How games have rendered two eyes, from the 1980s onward, on consoles, handhelds and headsets alike.
**The 2011 phones had game libraries too.** The LG Optimus 3D shipped Gameloft titles rendered natively in 3D (N.O.V.A., Asphalt 6, Let's Golf 2), and a [**3D Game Converter**](https://techcrunch.com/2011/08/29/lg-bolsters-optimus-3d-app-library-with-3d-game-converter/) arrived later that year in a maintenance release, lifting a whitelist of around fifty OpenGL games into stereo in real time. The converter is the mobile counterpart to the [PC driver era](#pc-gaming-and-the-driver-era) — Nvidia 3D Vision and iZ3D's trick, moved into a phone — and it ended the same way, abandonware when the platform died. The HTC Evo 3D had no converter and leaned on a preloaded Gameloft storefront instead, shipping a *Spider-Man: Total Mayhem* 3D demo out of the box with *Assassin's Creed: Altair's Chronicles* and *GT Racing* on sale at launch. Both phones are described under [glasses-free phones, handhelds and cameras](#glasses-free-phones-handhelds-and-cameras).

- [Sharp AQUOS PHONE](https://en.wikipedia.org/wiki/Sharp_Aquos_Phone) - The Japanese wave's answer to the converter: the SH80F claimed to be the first Android phone to convert 2D to 3D in real time, and shipped EA's *Need for Speed Shift* playable in 3D.

### Perception and curiosities

- [Pulfrich effect](https://en.wikipedia.org/wiki/Pulfrich_effect) - Depth from a delay in one eye, which produced a whole genre of cheap 3D broadcasts.
- [Autostereogram](https://en.wikipedia.org/wiki/Autostereogram) - The *Magic Eye* branch: stereo with no device at all.
- [Wiggle stereoscopy](https://en.wikipedia.org/wiki/Wiggle_stereoscopy) - Animation as a stereo display, needing neither glasses nor a special screen.

## How stereo is stored

Every stereoscopic file answers one question: where is the second eye? The answers, in rough order of age:

- [Anaglyph 3D](https://en.wikipedia.org/wiki/Anaglyph_3D) - Both eyes multiplexed into colour channels, 1853 onwards. Lossy and universal: it plays on anything, including paper, and it survives being printed, photocopied or posted anywhere. The autostereogram above survives the same treatment, and needs no filters to do it; anaglyph's advantage is that it works on any image rather than only on images built for the trick.

### Anaglyph colour codes

The glasses decide the encoding, and they are not interchangeable. Which pair a file was made for is part of the file's meaning, and getting it wrong is why so much archived anaglyph looks broken:

**Red / cyan.** The default, and what almost everything in circulation assumes. Left eye red, right eye cyan. Cyan covers green and blue, which is why the right eye keeps most of the colour information and the left eye keeps almost none.

**Red / green** and **red / blue.** The older pairs, common in print and comics. Nearly no colour survives, but the separation is strong and the filters are cheap.

**Green / magenta.** Marketed as Trioscopics. Splits the luminance more evenly between the eyes than red/cyan, so it holds colour noticeably better.

**Amber / dark blue.** [ColorCode 3-D](https://en.wikipedia.org/wiki/ColorCode_3-D), designed so the image is nearly watchable without glasses, at the cost of heavy eye asymmetry.

**Dubois anaglyph.** Not another colour pair but the right way to compute one: a least-squares optimisation of the channel mix for a given filter pair, which reduces the ghosting and retinal rivalry that plain channel-copying produces. Stock FFmpeg implements it as `arcd`, `agmd` and `aybd`.

**Making your own pair.** The filters are two rectangles of coloured plastic, which is why this is the one stereo method nobody can withdraw from you. What matters is that each filter blocks the *other* eye's band hard, and the measurements are published: Woods and Rourke's [*Ghosting in Anaglyphic Stereoscopic Images*](http://cmst.curtin.edu.au/wp-content/uploads/sites/4/2016/05/2004-08.pdf) (Curtin University, 2004) found a tenfold spread in crosstalk across twenty-seven real pairs of glasses, and Woods and Harris' [*Comparing levels of crosstalk with red/cyan, blue/yellow, and green/magenta anaglyph 3D glasses*](http://cmst.curtin.edu.au/wp-content/uploads/sites/4/2016/05/2010-11.pdf) (2010) measured the asymmetry that ruins home-made pairs: their better cyan gel filters averaged 2.2% crosstalk against 13.5% for red. **Reds leak.** The same paper's blunt advice, from the worst performer they measured, is "don't use inkjet printed anaglyph filters", so printing your own onto transparency is the one method to skip.

For filters that behave, theatrical lighting gel is the portable answer, because the swatch numbers are identical worldwide: practitioners report [Lee 106 Primary Red with Lee 116 Medium Blue-Green](https://forum.vvvv.org/t/what-lee-filters-for-building-custom-3d-glasses-anaglyph-effect/7793) — "some ghosts appear, but that's quite fine" — and Rosco's [own equivalence table](https://us.rosco.com/en/lee-rosco-equivalents) gives the same two as Roscolux 26 and Roscolux 95. Gel sample books are cheap or free from stage-lighting suppliers, and one book makes many pairs.

Without gel, the materials people actually use, each from a source that tried them: coloured [acetate, which a Brazilian university guide rates above cellophane outright](https://ole.uff.br/wp-content/uploads/sites/392/2018/07/Guia_para_constru%C3%A7%C3%A3o_do_anaglifo.pdf) (*resultado melhor*); [permanent marker on any transparent sheet](https://science.nasa.gov/resource/build-your-own-3d-glasses/), which NASA suggests for its Mars anaglyphs; cellophane from sweet wrappers, [doubled on the cyan side because one layer is too weak](https://www.haworth-village.org.uk/3d/3d-glasses.asp); and in Indonesia, [*mika* sheets from photocopy and print shops](http://faisalicang.blogspot.com/2015/04/cara-membuat-kacamata-3d-anaglyph.html), stacked until the wrong-eye image disappears from a test picture. Photocopy shops exist nearly everywhere, which makes that the most portable sourcing tip found.

Ready-made frames and instructions: [NASA's STEREO mission classroom page](https://stereo-ssc.nascom.nasa.gov/classroom/glasses.shtml), [Hanover College](https://isle.hanover.edu/Preface/P01AnaglyphGlasses.html), which is honest that red/blue substitutes "work but do not completely match" red/cyan, and the [University of Arizona's optical sciences outreach](https://wp.optics.arizona.edu/oscoutreach/3d-stereoscopic). No openly licensed frame template was found, which is a gap this list would rather fill than link around.

One honest correction to the assumption that DIY is always the cheap path: in India, ready-made paper anaglyph glasses [sell for about ₹20 each](https://www.tronicsindia.in/anaglyph-red-cyan-3d-glasses.html), roughly a quarter of a US dollar, while Lee gel is stocked mainly in trade quantities. Where glasses are that cheap, building your own is about access and immediacy rather than money — and about being able to equip a classroom tonight.

[Infitec](https://en.wikipedia.org/wiki/Infitec) - The professional descendant of the idea: narrow interference filters splitting each primary rather than whole channels, used by Dolby 3D. Full colour, expensive glasses.

[Complementary colours](https://en.wikipedia.org/wiki/Complementary_colors) - Why any of it works, and why the pairs are always opposites.

One practical note, because it costs people their archives: anaglyph made for CRT phosphors ghosts on a modern LED panel, since the filters were chosen against a different spectrum. The fix is a per-panel correction on top of Dubois, not a different file.
[Vectograph](https://en.wikipedia.org/wiki/Vectograph) - A polarised 3D print: the two views are printed as differently-polarised images on a single sheet and read through polarised glasses. Conceived by Joseph Mahler, who developed it into a practical process with [Edwin Land](https://en.wikipedia.org/wiki/Edwin_Land) at Polaroid. The print counterpart to a polarised cinema: in the Second World War, stereo aerial reconnaissance was printed as vectographs, both for troops in the field and as transparencies projected for group viewing.

**Side-by-side and over-under**, "frame compatible" - Two half-resolution views inside one ordinary frame. The broadcast era's compromise, and still the most common layout in the wild.

**Frame packing.** Both views at full resolution in one coded frame, as HDMI 1.4 and Blu-ray 3D carry them.

**Row and column interleaving.** Alternate lines or columns per eye, matching passive polarised and parallax-barrier panels directly.

[Multiview Video Coding](https://en.wikipedia.org/wiki/Multiview_Video_Coding) - The MVC extension used by Blu-ray 3D: a second view coded as a prediction of the first.

[Stereoscopic video coding](https://en.wikipedia.org/wiki/Stereoscopic_video_coding) - The general survey of how stereo is packed into video streams.

**MPO.** Two JPEGs in one file with an index, the format 3D cameras wrote. Standardised by CIPA as DC-007.

[2D-plus-depth](https://en.wikipedia.org/wiki/2D-plus-depth) - One view plus a greyscale depth map, standardised as MPEG-C Part 3. The display synthesises the other eye, which is how a single file can serve 2D screens and autostereoscopic ones at once.

**MV-HEVC.** The multiview extension of HEVC, and the encoding behind Apple's "spatial video": two views in one modern codec, which is the same idea as MVC a decade later. See [High Efficiency Video Coding](https://en.wikipedia.org/wiki/High_Efficiency_Video_Coding).

**VR180.** Google's 180° stereo photo and video format, the headset-era counterpart to the frame-compatible and full-resolution packings above. Its [specification](https://github.com/google/spatial-media/blob/master/docs/vr180.md) requires a mesh projection rather than the equirectangular mapping used for 360 video, so the camera's fisheye frames are carried as shot and warped at playback instead of being reprojected first. See [VR photography](https://en.wikipedia.org/wiki/VR_photography).

**JPS and PNS.** A side-by-side pair in a JPEG or PNG, by community convention rather than by standard. A `.jps` is a valid JPEG that most software refuses purely because of its extension.

And separately from the pixels, **how the file says what it is**: a container tag (Matroska's `StereoMode`) or an in-stream message (H.264's `frame_packing_arrangement` SEI). Hardware 3D displays generally act on the second and ignore the first, which is why correctly authored files so often play flat.

## Depth, and making the second view

3D means depth, and depth is what two eyes are for. Stereo needs two views; when only one exists, depth is how the other gets made. That single idea connects a games console accessory, a phone's front camera, the current monocular depth models, and, at the far end, scanners and printers that turn depth back into objects.

### Measuring depth

- [Depth map](https://en.wikipedia.org/wiki/Depth_map) - The intermediate representation everything here produces or consumes.
- [Kinect](https://en.wikipedia.org/wiki/Kinect) - Microsoft's depth camera made real-time depth cheap and ordinary in 2010, and was promptly used for everything except the games it shipped with: scanning, reconstruction, research.
- [Structured light](https://en.wikipedia.org/wiki/Structured_light) and [time-of-flight camera](https://en.wikipedia.org/wiki/Time-of-flight_camera) - The two ways a consumer device measures depth actively; the first Kinect used one, the second used the other.
- [Lidar](https://en.wikipedia.org/wiki/Lidar) - The same principle at longer range, now sitting in phones and tablets.
- [Face ID](https://en.wikipedia.org/wiki/Face_ID) - Apple's structured-light dot projector, the reason tens of millions of pockets contain a depth camera whose maps feed portrait effects and spatial stills.
- [Photogrammetry](https://en.wikipedia.org/wiki/Photogrammetry) and [3D reconstruction](https://en.wikipedia.org/wiki/3D_reconstruction) - Recovering geometry from ordinary photographs, the software route to the same result.
- [Light field](https://en.wikipedia.org/wiki/Light_field) - Capturing rays rather than pixels, which makes any view synthesisable after the fact.

### Estimating depth from a single image

- [Depth Anything V2](https://github.com/DepthAnything/Depth-Anything-V2) and [Depth Anything 3](https://github.com/ByteDance-Seed/Depth-Anything-3) - Current monocular depth foundation models, and the most practical way today to derive a depth map from an ordinary photograph or frame.
- [MiDaS](https://github.com/isl-org/MiDaS) - The robust monocular depth estimator that established the approach.

These matter to this list for one reason: a view plus a depth map can be warped into a stereo pair. That is what 2D-to-3D conversion has always been, whether done by hand in a post house, in real time by a television's "simulated 3D" mode, or by a model on a laptop. It is also the honest route for recovering colour from anaglyph, where the usable stereo information is thin and the geometry has to come from somewhere.

### Generated views and generated worlds

If a model can produce the geometry, the second view costs nothing: a stereo pair is simply two camera positions in the same scene. That makes this the newest answer to the oldest problem in the list, which is where the other eye comes from.

- [View synthesis](https://en.wikipedia.org/wiki/View_synthesis) - Rendering viewpoints that were never photographed, the general problem.
- [Neural radiance field](https://en.wikipedia.org/wiki/Neural_radiance_field) - NeRF: a scene encoded as a function of position and direction, renderable from anywhere.
- [Gaussian splatting](https://en.wikipedia.org/wiki/Gaussian_splatting) - The faster successor now used in practice; the [reference implementation](https://github.com/graphdeco-inria/gaussian-splatting) and [Nerfstudio](https://github.com/nerfstudio-project/nerfstudio) for the whole pipeline.
- [Sora](https://en.wikipedia.org/wiki/Sora_(text-to-video_model)) and [generative AI](https://en.wikipedia.org/wiki/Generative_AI) - Generated video, and the point at which a "world model" that stays geometrically consistent between frames becomes a renderer rather than a slideshow.
- [awesome-world-models-video-games-3d](https://github.com/gxchris95/awesome-world-models-video-games-3d) - A companion list for that branch specifically.

**Generated frames**, the in-between ones that were never filmed:

- [Motion interpolation](https://en.wikipedia.org/wiki/Motion_interpolation) - Drawing the frames between two real ones, which is what lifts a 24 fps film toward 60 fps.
- [FILM](https://github.com/google-research/frame-interpolation) and [RIFE](https://github.com/hzwer/ECCV2022-RIFE) - Two current frame-interpolation models: FILM for large motion, RIFE for real time.

This is view synthesis turned sideways — applied to *time* instead of *space* — and it is the direct answer to the temporal-stereo problem the high-refresh note describes: a 24 fps film gives each eye only 24 frames a second, so motion stutters ("still shots are good but motion's a little rough"). Generate the in-between frames and each eye gets a smooth 48 or 60. The open question is doing it twice — once per eye — and keeping the two streams consistent, so the depth does not break.

**Text to 3D and image to 3D**, which produce geometry directly and therefore produce stereo for free:

- [Shap-E](https://github.com/openai/shap-e) and [Point-E](https://github.com/openai/point-e) - Text and image to 3D, the models that made the category ordinary.
- [threestudio](https://github.com/threestudio-project/threestudio) - Unified framework covering most text-to-3D methods in one place.
- [stable-dreamfusion](https://github.com/ashawkey/stable-dreamfusion) - Open implementation of the DreamFusion approach.
- [TripoSR](https://github.com/VAST-AI-Research/TripoSR) and [InstantMesh](https://github.com/TencentARC/InstantMesh) - One image to a mesh, in seconds.
- [Hunyuan3D 2](https://github.com/Tencent-Hunyuan/Hunyuan3D-2) - Current large open model for 3D generation.

The honest caveat for this list: generated depth is invented depth. It is excellent for making something watchable and it is not a recovery of what was actually in front of the lens, which matters when the goal is restoring an archive rather than producing an effect.

### From depth to objects

Depth is the common denominator. Measure it and you can synthesise a view, or you can build the thing itself. The same scans, point clouds and meshes feed both a stereo pair and a printer, which is why "3D" means all of this at once and why the word has never split.

- [3D scanning](https://en.wikipedia.org/wiki/3D_scanning) - Capturing an object's geometry, by the same structured-light, time-of-flight and photogrammetric methods used above.
- [Point cloud](https://en.wikipedia.org/wiki/Point_cloud) and [polygon mesh](https://en.wikipedia.org/wiki/Polygon_mesh) - What a depth measurement becomes once it is more than a picture.
- [3D printing](https://en.wikipedia.org/wiki/3D_printing) and [stereolithography](https://en.wikipedia.org/wiki/Stereolithography) - The output end: geometry returned to the physical world, where it needs no glasses at all. Note the name: *stereo*lithography, from the same root, for the same reason.
- [Meshroom](https://github.com/alicevision/Meshroom) - Free photogrammetry pipeline built on AliceVision: photographs in, textured mesh out.
- [COLMAP](https://github.com/colmap/colmap) - Structure-from-motion and multi-view stereo, the reference implementation most pipelines lean on.
- [openMVG](https://github.com/openMVG/openMVG) - Multiple-view geometry library, the maths underneath.
- [Volumetric display](https://en.wikipedia.org/wiki/Volumetric_display) and [holography](https://en.wikipedia.org/wiki/Holography) - The end of the road this list keeps walking towards: depth that is actually there, rather than depth delivered one eye at a time.

### Depth without two views: head tracking and parallax

- [Johnny Lee](https://en.wikipedia.org/wiki/Johnny_Lee_(computer_scientist)) - His 2007 [Wii Remote](https://en.wikipedia.org/wiki/Wii_Remote) head-tracking demo produced convincing depth on an ordinary flat screen with no glasses, by moving the rendered viewpoint with the viewer's head.
- [Parallax](https://en.wikipedia.org/wiki/Parallax) - The cue it exploits; motion parallax is a depth signal on its own, which is why the New Nintendo 3DS added head tracking to keep the sweet spot.
- [Depth perception](https://en.wikipedia.org/wiki/Depth_perception) - The full set of cues the brain actually uses, of which binocular disparity is only one.

### Depth drawn rather than computed

Before real-time 3D was affordable, games still had to put space on a screen, and the answer was a fixed camera held above the scene at an angle. It is the flat era's complete answer to the problem this whole list is about, and it is worth understanding as an engineering choice rather than a limitation.

- [Isometric video game graphics](https://en.wikipedia.org/wiki/Isometric_video_game_graphics) - The convention, used by [X-COM](https://en.wikipedia.org/wiki/UFO:_Enemy_Unknown) (1994), [Diablo](https://en.wikipedia.org/wiki/Diablo_(video_game)) (1996) and most of the strategy and role-playing games of that decade. Usually not true isometric but dimetric, with two of the three axis angles equal and a 2:1 pixel ratio.
- [Axonometric projection](https://en.wikipedia.org/wiki/Axonometric_projection) - The family it belongs to. These are **parallel** projections, so an object does not shrink as it moves away, and the reason is economy: the machine never scales a sprite and never computes a perspective divide. A 386 could draw a large map quickly because it refused to do the one thing that makes distance look like distance.

What replaces perspective is the rest of the monocular stack: occlusion, height on the screen, and a scale the player can trust because it never changes. It reads as space, and it reads as space for everyone, including the roughly one viewer in twenty who cannot fuse a stereo pair at all.

Layers moving at different speeds are the other half of the flat era's answer, and this one is not a convention at all: it is a real depth cue, the same motion parallax the New Nintendo 3DS later used head tracking to preserve.

- [Parallax scrolling](https://en.wikipedia.org/wiki/Parallax_scrolling) - "Background images move past the camera more slowly than foreground images, creating an illusion of depth in a 2D scene". Some appeared in [Jump Bug](https://en.wikipedia.org/wiki/Jump_Bug) (1981), and [Moon Patrol](https://en.wikipedia.org/wiki/Moon_Patrol) (1982) is usually credited with popularising it with three background layers at three speeds. The 16-bit generation made it the house style, [Sonic the Hedgehog](https://en.wikipedia.org/wiki/Sonic_the_Hedgehog_(1991_video_game)) and *Street Fighter II* among them.
- [Colour cycling](https://en.wikipedia.org/wiki/Color_cycling) - The companion trick, and the reason those backgrounds look deeper than the hardware should allow. Rewriting the palette animates a whole screen at no cost and "gives the illusion of another layer", which is how a console with a fixed number of background planes appeared to have one more, and how skies got their gradients.

Then the floor tilted. [Wolfenstein 3D](https://en.wikipedia.org/wiki/Wolfenstein_3D) (1992) and [Doom](https://en.wikipedia.org/wiki/Doom_(1993_video_game)) (1993) drew convincing first-person space without a true three-dimensional world behind it: no room above another room, no looking properly up or down. [Descent](https://en.wikipedia.org/wiki/Descent_(video_game)) (1995) was the break, described as the first first-person shooter with entirely true-3D graphics and holding a Guinness record for it, with six degrees of freedom and a fully textured 3D environment. [3dfx](https://en.wikipedia.org/wiki/3dfx_Interactive)'s Voodoo cards and the Glide, [OpenGL](https://en.wikipedia.org/wiki/OpenGL) and Direct3D APIs then made that geometry the normal way to build a game rather than a feat.

**Which is what made the driver era above possible.** Once a game keeps its world as geometry and hands it to a standard API, something outside the game can ask for the same scene from a second viewpoint. A raycaster cannot be asked that question, because there is no scene to re-render, only a wall distance per screen column. The stereo drivers arrived when they did because that is when there was finally something to render twice.

And the loop closes, because someone went back and gave those games the dimension they never had.

- [3dSen](https://geodstudio.net/) - Geod Studio's NES emulator, ten years in the making and out of Steam Early Access in 2025, which plays the flat library as 3D voxel dioramas you can move a camera around, with lighting and cast shadows in worlds that never had either. [3dSen PC](https://store.steampowered.com/app/1147940/3dSen_PC/) and a VR edition, the latter with a mixed-reality mode on Quest. Over a hundred titles, plus community-made profiles.

The method is the interesting part, and the developer is honest about it. The emulator samples the PPU's output and divides it into 8x8 tiles automatically, but what turns those tiles into volume is a per-game profile: static rules saying "this tile is a wall, that tile is a backdrop, this sprite is a cylinder", plus runtime scripts for the cases the rules cannot cover. Every supported game is, in his words, painstakingly handmade, a few days for a simple one and weeks or months for *Super Mario Bros. 3*.

So this is not depth estimation and it is not reconstruction. It is a person reading a game's own internal logic and writing down the spatial intent that was always encoded in it, because a designer who places a wall tile means a wall. The flat era compressed a three-dimensional idea into two dimensions using the techniques above, and this decompresses it by hand. Once that volume exists, stereo is free, which is why a VR edition exists at all and why this belongs in a list about depth rather than in one about emulation.

The convention outlived its own justification. Modern games in the genre render in 3D and keep the camera exactly where it was, because an elevated fixed vantage turned out to be the right way to command a dozen units and read a floor plan, quite apart from what the hardware could afford. It is the one place in this list where a depth technique survived on ergonomics after the technical reason for it disappeared.

### Emulators that can output stereo

This is here as preservation rather than as a survey of emulation, which is its own
argument and not this list's. The point is narrower: a good deal of stereoscopic work
was published on hardware that is now dead, scarce or degrading, and for some of it
these are the only surviving ways to see it in stereo at all. The Virtual Boy is the
clearest case, an entire library that is stereoscopic by design and unviewable without
either a working 1995 unit or one of the tools below.

Two different things get called the same name here, though, and the difference is the
one this whole section turns on: whether the stereo already exists or has to be made.

**Where the console really had stereo, the emulator is preserving it.** The data is in
the ROM because the original hardware drove two eyes, so the only question is how to
get it back out to a modern display.

- [Mednafen / Beetle VB](https://mednafen.github.io/documentation/vb.html) - The Virtual Boy emulator, also the standard libretro core. Seven output modes: anaglyph in six colour pairings, CyberScope, side by side, vertical and horizontal line interlaced, and either eye alone. Side by side is described exactly as you would hope: "the left-eye image is displayed on the left, and the right-eye image is displayed on the right". Feed that to a 3D television and a console built as a visor for one face becomes something a room can watch, which the hardware never allowed.
- [Azahar](https://github.com/azahar-emu/azahar) - The 3DS emulator that absorbed Lime3DS after Citra's shutdown. Its [3D rendering option](https://github.com/azahar-emu/azahar/pull/2339) offers side by side, full side by side, anaglyph, interlaced, reverse interlaced and Cardboard, with an intensity factor, for games that used the console's own depth slider.
- [Dega](https://github.com/Plombo/dega) - A Master System emulator that turns the [SegaScope 3-D Glasses](https://en.wikipedia.org/wiki/Sega_3D_Glasses) signal into anaglyph: it "will take the original flickering glasses effect used on some games and merge the images into a Red/Blue image". Worth knowing that this was done once, in 2004, and the rest of the Master System emulators never copied it.
- [MAME](https://github.com/mamedev/mame) - Reproduces the SegaScope glasses at driver level, with a binocular hack that can emit either lens or both. A community layout that would present it as half side-by-side for a 3D television has been [open and unmerged since 2018](https://github.com/mamedev/mame/issues/3492).
- [RPCS3](https://github.com/RPCS3/rpcs3) - Reproduces the PlayStation 3's own stereoscopic mode, [added in 2020](https://github.com/RPCS3/rpcs3/pull/7657) as anaglyph, with [side-by-side following in 2023](https://github.com/RPCS3/rpcs3/issues/13059) after a request for output to 3D televisions.

**Where the console never had stereo, the emulator is making it**, and it can only do that because the game is a 3D scene. This is the driver era again, aimed at a console.

- [Dolphin](https://github.com/dolphin-emu/dolphin) - Produces both eyes for the GameCube and Wii, neither of which shipped any stereo capability, and its implementation is the clearest worked example in this list. A geometry shader amplifies every primitive into a two-layer array in a single pass rather than drawing the scene twice, then shifts each eye horizontally in clip space by an amount proportional to depth, `f.pos.x += hoffset * (f.pos.w - convergence)`, a formula its source credits to Nvidia's 3D Vision Automatic guide. The two controls are exactly the two that matter anywhere: depth, described in the program as "the separation distance between the virtual cameras", and convergence, "the distance at which virtual objects will appear to be in front of the screen". Output as side by side, top and bottom, anaglyph with a Dubois matrix, scanline-interleaved for passive displays, or quad-buffered. Worth knowing that the geometry shader is a hard requirement, so the macOS Metal backend cannot do stereo at all, and that quad-buffer output is in practice OpenGL only.
- [PPSSPP VR](https://github.com/hrydgard/ppsspp/pull/15901) - The same move for the PSP, re-rendering its geometry from two viewpoints with head tracking, in a fork rather than the mainline build.

**Why some consoles can have this and others cannot** is a hardware question, not a
question of effort, and it is worth stating because the same feature request keeps
being made and refused without the reason surviving anywhere findable.

The GameCube has a fixed-function transform unit with addressable matrix-load commands
in its graphics command stream, so an emulator can see the projection before anything
is drawn and perturb it. That is why Dolphin can offer stereo as a checkbox that works
across the whole library.

The PlayStation 2 cannot be treated that way. Its Graphics Synthesizer is a rasterizer
that receives vertices already transformed, perspective-divided and clipped: PCSX2's
own vertex structure carries no matrix and its position field is raw screen-space fixed
point. The projection happens earlier, in VU1 microcode, which is *the game's own
program*, executed by the emulator as a general vector coprocessor with no knowledge of
what any of it means. There is no camera for an emulator to find, because by the time
the emulator is involved the camera has already been applied by code it cannot
interpret.

So on a PS2 emulator the routes are per-game reverse engineering of each title's own
vector memory, in the spirit of the per-game widescreen patches such projects already
carry, or shader injection from outside the emulator entirely. Both were tried; neither
is a general feature. One scene and two cameras remains the right description of stereo
rendering, and it needs a camera to exist in a place the renderer can reach.

**The gaps are worth recording too**, and the reasons given for them are not what you might expect. The Famicom 3D System, Nintendo's own shutter-glasses accessory, appears to be emulated nowhere; the [Nestopia request](https://github.com/0ldsk00l/nestopia/issues/155) was closed in 2016, and when it resurfaced the maintainer explained that doing it properly "would require a Vulkan renderer with multi-viewport capability", which is a rendering-architecture problem rather than a display one. Genesis Plus GX does not implement SegaScope and halves the frame rate instead. The long-running [PCSX2 request](https://github.com/pcsx2/pcsx2/issues/1461) ran from 2016 to 2022 and turned largely on what the stereo driver of the day required, including that Direct3D 11 titles could not be made to work in windowed mode at all.

One practical note for anyone trying this on a 3D television: every mode above produces correctly packed stereo and none of them tells the set what it is sending. The television will show a side-by-side pair as two flat images until 3D is switched on by hand, because over HDMI the layout is announced in an InfoFrame that emulators do not emit and desktop operating systems do not expose. The pixels are right and the signalling is missing, which is the same shape as the frame-packing problem described further up this list.

## Capture

A stereo pair is shot before it is stored or shown. The hardware falls into two kinds: a twin-lens body that does both eyes at once, built as a still camera or as a camcorder, and two ordinary cameras fixed together in a rig.

### Still cameras

Twin-lens compacts that write MPO straight out of the box. The [Fujifilm FinePix Real 3D](https://en.wikipedia.org/wiki/Fujifilm_FinePix_Real_3D) W1 and W3 (2009–2010) are the ones that made the format ordinary, and they sit with the glasses-free phones under [Glasses-free phones, handhelds and cameras](#glasses-free-phones-handhelds-and-cameras), because that 2011 generation both shot and displayed the pair. The category also includes:

- [Panasonic Lumix DMC-3D1](https://en.wikipedia.org/wiki/Panasonic_Lumix_DMC-3D1) - A twin-lens compact of the same wave: MPO stills and 3D video from a pocket body.

### Camcorders

The same twin lenses aimed at motion. Every maker claimed a "world's first" with a different qualifier, which is its own small lesson in how crowded that one year was:

- [Sony HDR-TD10](https://www.sony.jp/products/overseas/contents/pickup/english/110324_promotion/TD10_Web/index.html) - "Double Full HD 3D" (2011): twin G Lenses, two Exmor R sensors and two BIONZ processors recording full resolution per eye.
- [Panasonic HDC-SDT750](https://www.prnewswire.com/news-releases/panasonic-unveils-the-worlds-first-3d-consumer-camcorder-complete-with-a-3d-conversion-lens1-99433594.html) - The first 3D consumer camcorder (2010), via a detachable 3D conversion lens on a 3MOS body.
- [JVC GS-TD1](https://manual3.jvckenwood.com/c1dw/lyt2327-002en/index.html) - Twin-lens Full HD 3D (2011) on the FALCONBRID engine, recording a full-resolution "LR Independent" format and side-by-side for AVCHD 3D compatibility.

The **Sony Bloggie 3D (MHS-FS3)** belongs here too, the pocket end of the same wave, recording 1080p 3D side-by-side; no stable manufacturer page survives to link to. The line between stills and motion never really held either: the still Fujifilm W3 also shot 720p 3D video, and every camcorder here shot 2D stills.

### Two identical cameras in a rig

The oldest method needs no 3D hardware at all: two identical ordinary cameras, synchronized, each becoming one eye. The two files are combined into side-by-side or top-bottom in post — the same frame-compatible packing the displays section describes.

**Side-by-side bar rig.** Two cameras bolted to a plate about an [interpupillary distance](https://en.wikipedia.org/wiki/Interpupillary_distance) apart (roughly 63 mm). Camera body width forces the lenses a little wider than the eyes, so hand-held bar rigs lean toward mild **hyperstereo** — exaggerated depth that suits landscapes and hates close-ups.

**Over-under rig.** Two cameras stacked with one inverted, the lenses brought near-coaxial; one stream is flipped in post. The compact answer when the pair has to stay narrow.

**Beam-splitter rig.** A semi-silvered [beam splitter](https://en.wikipedia.org/wiki/Beam_splitter) at 45°, one camera shooting through it and the other the reflection, which is how 3D films bring the lenses down to near-zero spacing for close work.

**Sync is the hard part.** Genlock or a sync cable where the cameras have one; otherwise a clapper or an audio spike to align the streams in post. Mismatched exposure, focus or rolling shutter between the two eyes ruins a rig shot far more than the spacing does.

## Who can see it, and who cannot

The medium assumes two working eyes that cooperate, and for a significant minority they do not. This is not a footnote to stereoscopy; it is a boundary condition on the whole subject, and it explains part of why every consumer 3D wave met resistance that surprised the people selling it.

- [Stereopsis](https://en.wikipedia.org/wiki/Stereopsis) and [binocular vision](https://en.wikipedia.org/wiki/Binocular_vision) - The faculty being exploited, and how the two images fuse.
- [Stereoblindness](https://en.wikipedia.org/wiki/Stereoblindness) - The inability to perceive depth from binocular disparity. Estimates vary by definition and test, but a meaningful percentage of people are affected, and many discover it only when a 3D film does nothing for them.
- [Amblyopia](https://en.wikipedia.org/wiki/Amblyopia) and [strabismus](https://en.wikipedia.org/wiki/Strabismus) - The common causes: one eye suppressed in childhood, or eyes that do not align, so the brain never learns to fuse.
- [Monocular vision](https://en.wikipedia.org/wiki/Monocular_vision) - Living with one eye. Depth does not vanish, because the other cues remain, but judging distance, catching, pouring and driving all get measurably harder. It is the clearest everyday demonstration of what the second view is actually worth.
- [Binocular summation](https://en.wikipedia.org/wiki/Binocular_summation) - The other half of the benefit: two eyes also see fainter, finer detail than one.

### Stereo as treatment, not only entertainment

The same apparatus that shows a film can rebuild the faculty itself, which is the most underrated fact in this entire list:

- [Vision therapy](https://en.wikipedia.org/wiki/Vision_therapy) - Including dichoptic training, where each eye is shown a different image so the weaker one must contribute. Modern versions use exactly the hardware in this list: stereoscopic displays, anaglyph glasses, headsets.
- [Stereopsis recovery](https://en.wikipedia.org/wiki/Stereopsis_recovery) - Evidence that adults can gain stereo vision long after the supposed critical period closed.
- [Susan R. Barry](https://en.wikipedia.org/wiki/Susan_R._Barry) - The neurobiologist who acquired stereopsis in her late forties and wrote about what it was like to see depth for the first time. Her case, reported by [Oliver Sacks](https://en.wikipedia.org/wiki/Oliver_Sacks) as "Stereo Sue", is the single best argument that this medium is about perception rather than gimmickry.

**The design consequence**, for anyone building with the formats in this list: never let stereo be the only channel carrying meaning. Keep the image readable flat, because some of your audience will always see it that way — and, as the entries above show, some of them may be using your work to change that.

## Standards and specifications

- [Stereoscopy standards index](standards.md) - Pinned official editions and primary-source links for video, container and display signalling, with the frame-packing persistence rules separated from encoder cadence and hardware observations.
- [ITU-T H.264](https://www.itu.int/rec/T-REC-H.264) - Annex D defines the `frame_packing_arrangement` SEI, including the type codes for checkerboard, column-interleaved, row-interleaved, side-by-side, top-bottom and temporal interleaving.
- [Matroska element specification](https://www.matroska.org/technical/elements.html) - Defines `StereoMode`, the container-level 3D flag and its value table.
- [CIPA standards](https://www.cipa.jp/e/std/std-sec.html) - Publishes DC-007, the Multi-Picture Format that defines MPO.
- [DVB specifications](https://dvb.org/specifications/) - The frame-compatible and service-compatible 3DTV specifications used by broadcasters.
- [MPEG](https://en.wikipedia.org/wiki/Moving_Picture_Experts_Group) - The video-coding body behind 2D-plus-depth (MPEG-C Part 3). Multiview Video Coding (MVC) and MV-HEVC were joint work with ITU-T's VCEG, through the JVT and JCT-3V teams.
- [Blu-ray 3D](https://en.wikipedia.org/wiki/Blu-ray_3D) - The Blu-ray Disc Association's delivery spec for the 3D disc era. In a [2009 announcement](https://us.blu-raydisc.com/wp-content/uploads/sites/2/2019/09/20090904-IFA-BDA-Press-Release.pdf) the Association said its specification would require 1080p for each eye and called Blu-ray the ideal packaged-media platform for 3D home entertainment. Its successor then severed that path: the Association's own [Ultra HD Blu-ray FAQ](https://us.blu-raydisc.com/blog/fandq/ultra-hd-blu-rays-available-3d/) says simply that the 4K format does not support 3D content. Owners had to choose the old 1080p 3D edition or the new 4K 2D edition; the home format never offered both advances together.
- [HDMI Forum](https://en.wikipedia.org/wiki/HDMI_Forum) - Custodian of the HDMI specification from 1.4b onward, founded in 2011. The 3D signalling that tells a set which packing is coming down the cable is older: HDMI 1.4 (2009) and 1.4a (2010) were issued by HDMI Licensing for the founding companies, before the Forum existed.
- [SMPTE](https://en.wikipedia.org/wiki/SMPTE) - The cinema and broadcast engineering body behind the professional 3D standards.
- [3D Consortium](https://www.nttdata.com/global/ja/news/release/2003/030400/) - Founded in March 2003 by Itochu, NTT Data, Sanyo, Sharp and Sony, with some seventy member organisations at launch, to develop and spread 3D display hardware and widen the distribution of 3D content: the Japanese industry organising around stereo six years before *Avatar*. The founding announcement is in Japanese.

### Every HDMI 1.4 stereo structure

HDMI does not define “3D mode” as one packing. Its Vendor-Specific InfoFrame assigns a four-bit `3D_Structure` code to eight layouts. The [Linux HDMI definitions](https://github.com/torvalds/linux/blob/master/include/linux/hdmi.h) preserve the complete wire-level list, and the [DRM mode API](https://github.com/torvalds/linux/blob/master/include/drm/drm_modes.h) describes their framebuffer meaning:

| HDMI code | structure | what crosses the link |
|---:|---|---|
| 0 | frame packing | two complete eye frames with the format-defined blanking space between them |
| 1 | field alternative | left and right views in alternating fields |
| 2 | line alternative | left and right views on alternating lines |
| 3 | side-by-side full | two complete eye frames horizontally adjacent |
| 4 | L + depth | one conventional image plus a depth map from which another view can be synthesized |
| 5 | L + depth + graphics + graphics-depth | image and depth plus a separately depth-positioned graphics layer |
| 6 | top-and-bottom | both views split across the upper and lower parts of one frame |
| 8 | side-by-side half | both views split across the left and right parts, with defined horizontal subsampling |

Code 7 and codes 9–15 are reserved. “Full” and “half” describe spatial sampling, not frame rate: a 60 Hz half-SBS frame still contains sixty synchronized eye pairs per second.

HDMI 1.4a also defines a baseline set every 3D implementation can recognize. The [mainline Linux EDID parser](https://github.com/torvalds/linux/blob/master/drivers/gpu/drm/drm_edid.c) carries that mandatory table directly:

| base timing | mandatory stereo packing |
|---|---|
| 1920×1080p at 23.976/24 Hz | frame packing; top-and-bottom |
| 1920×1080i at 50 Hz | side-by-side half |
| 1920×1080i at 59.94/60 Hz | side-by-side half |
| 1280×720p at 50 Hz | frame packing; top-and-bottom |
| 1280×720p at 59.94/60 Hz | frame packing; top-and-bottom |

That table is the interoperability floor, not the ceiling. A sink's HDMI Vendor-Specific Data Block can attach structures to additional video timings, which is why real sets may advertise combinations such as 1080p60 SBS-half, 1080p30 frame packing or 720p24 frame packing. There is therefore no honest universal list of every resolution/layout pair: the complete answer is the eight structures above, the mandatory baseline, and then the per-display EDID. HDMI Licensing's [1.4a announcement](https://www.hdmi.org/announce/detail/84) confirms that the revision added mandatory broadcast formats and top-and-bottom, while the public [HDMI 1.4 feature archive](https://www.hdmi.org/download/savefile?bucket=hdmi-web-public&fileKey=Specifications%2F1dot4_feature_archive.pdf) describes dual-stream 1080p and warns that manufacturers need not implement every optional feature.

There is also a Linux gap hiding in that distinction. Mainline defines and can serialize all eight structures into the HDMI InfoFrame, but its EDID mode-creation paths currently instantiate only frame packing, top-and-bottom and side-by-side half. Field alternative, line alternative, full-SBS and both depth structures are represented in the API yet ignored when parsing the sink's optional 3D structure map. That deserves a separate compatibility audit rather than assuming an absent DRM mode means an incapable television.

### Do the newer HDMI specs still carry 3D?

Frozen, not removed. The stereoscopic framework lives in HDMI 1.4/1.4a (2009/2010) and its last public home is the [HDMI 1.4b 3D document](https://hdmi.org/docs/hdmi14bspecs). HDMI 2.0 (2013) kept that entire structure set and added small 3D conveniences such as OSD disparity signalling, but defined no new stereo packing for 4K: no frame-packed 2160p timing was ever standardized, which is why 4K-era 3D sets fell back to half-resolution SBS/TaB or 1080p24 frame packing. HDMI 2.1 (2017) dropped the topic from its feature list entirely; the [Forum's own release](https://hdmiforum.org/hdmi-forum-releases-version-2-1-hdmi-specification/) names higher resolutions, Dynamic HDR, eARC, VRR, QMS, QFT and ALLM, and HDMI Licensing's [feature-marketing guidance](https://hdmi.org/blog/detail/139) makes every 2.1 feature optional, with 3D not even on the menu. HDMI 2.2 (2025) continues the pattern with bandwidth, not stereo.

The capability itself never left the wire. Later specifications [continue to reference and rely on HDMI 1.4b](https://hdmiforum.org/about/faq/), and the CTA-861 family still defines the Vendor-Specific InfoFrame 3D structure codes, so a modern sink could legally advertise 1.4-style 3D formats in its EDID tomorrow. What ended around 2016-2017 is the implementation in consumer panels, not the standard that carries it. That asymmetry is this list's argument in one sentence: the pipe was never sealed; the industry simply stopped sending water through it.

The Linux lineage is equally short and recoverable. Mainline's HDMI stereoscopy came from Alastair Bridgewater's 2017 nouveau series ([patch 5/6 and discussion](https://lists.freedesktop.org/archives/dri-devel/2017-January/130144.html), [v2 cover letter](https://lists.freedesktop.org/archives/dri-devel/2017-March/137040.html)): his attempt to delete the mandatory-stereo table was dropped after Damien Lespiau cited the HDMI 1.4a "shall support" language, the frame-packing failures were traced to nouveau's own timing, and the merged series fixed them with the `CRTC_STEREO_DOUBLE` transform in `drm_mode_set_crtcinfo()`. That 2017 work is why stock nouveau drives a 2011 BRAVIA in full-resolution frame packing today, and its missing counterpart inside amdgpu DC is the open port.

## Tools

- [FFmpeg `stereo3d` filter](https://ffmpeg.org/ffmpeg-filters.html) - Converts between side-by-side, over-under, interleaved, checkerboard and anaglyph, including Dubois anaglyph, in one filter.
- [x264](https://www.videolan.org/developers/x264.html) - Writes the frame-packing SEI with `--frame-packing`.
- [HandBrake](https://handbrake.fr) - Cross-platform encoder; writes the frame-packing SEI on H.264 output.
- [MKVToolNix](https://mkvtoolnix.download) - Sets and inspects the Matroska `StereoMode` flag without re-encoding.
- [StereoPhoto Maker](https://stereo.jpn.org/eng/stphmkr/) - The stereo-photography community's standard editor: alignment, conversion between every still format, batch processing. Its author, Masuji Suto, received the Royal Photographic Society's Saxby Award, for achievement in three-dimensional imaging, in 2015.
- [StereoMovie Maker](https://stereo.jpn.org/eng/stvmkr/) - The companion to StereoPhoto Maker for moving pictures: the same alignment and format conversion, applied to video pairs.
- [StereoscoPy](https://github.com/2sh/StereoscoPy) - Python tool and library that builds anaglyph, side-by-side and cross-eye images from a pair.
- [a2sbs.py](https://gist.github.com/JackDesBwa/f86eb3fcdf3a0be1734bcdb4f535a52a) - Recovers a side-by-side pair from an anaglyph. The conversion is necessarily approximate, because the anaglyph threw information away, but it goes past a plain greyscale split: it can rebuild chroma with an anisotropic blur, or from the optical flow where both views agree, and it can undo the anti-ghosting some creators burn into the image before applying the anaglyph matrix.
- [mpo2sbs.py](https://gist.github.com/JackDesBwa/317ef94cc8c67c02c78c7e4b1e038b1a) - Turns an MPO camera file into a parallel side-by-side image, which is the conversion most tools assume you have already done.
- [OBS SBS scripts](https://github.com/JackDesBwa/OBS_SBS_scripts) - Lua scripts for handling side-by-side sources inside OBS, for anyone streaming or recording in stereo.
- [ExifTool](https://exiftool.org) - Reads and writes the MPO structure, and is the practical way to check whether a file is really a stereo pair.
- [sony-bravia-linux tools](https://github.com/danielcamposramos/sony-bravia-linux/tree/main/tools) - Losslessly injects the frame-packing SEI into existing H.264 files, converts anaglyph back to side-by-side, writes MPO, and indexes a library by stereo format.
- [HDMI 1.4 3D driver patches](https://github.com/danielcamposramos/sony-bravia-linux/blob/main/docs/upstream/community-hdmi-3d-patches.md) - Hardware-verified kernel patches that un-prune the stereo modes a 3D TV already declares in its own EDID: a six-line `stereo_allowed` opt-in installable on NVIDIA's kernel-open 615.71.09, and an amdgpu backport pair (VSIF emission plus frame-packing scanout) for 7.0-era trees. Written to be applied today, in parallel with the upstream series rather than instead of it; nouveau needs no patch and serves as the control.

## Players and viewers

**Our pick: mpv.** It detects the 3D layout signalled in the stream in its own upstream code ([PR #18490](https://github.com/mpv-player/mpv/pull/18490), merged 23 September 2026), so no patched fork is needed; until the next release (the latest, v0.41.0, predates it), that means a development build from that date on. Our VLC fork below is for people who rely on VLC. mpv is also the maintainer's personal choice.

- [mpv](https://mpv.io) - Scriptable player with `stereo3d` filtering. Since September 2026 its development branch also detects the layout signalled in the stream itself, the H.264/HEVC frame-packing SEI or the MP4 `st3d` box ([PR #18490](https://github.com/mpv-player/mpv/pull/18490)).
- [VLC with the 3D fix](https://github.com/danielcamposramos/vlc) - Fork of VLC, which describes itself as "focused on playing everything". Upstream VLC has discarded the H.264 frame-packing SEI since 2017 (commit 89347c3e2d), so video that signals its 3D layout the standard way plays and converts as flat 2D. This fork detects the SEI and keeps it through transcoding; tested [builds](https://github.com/danielcamposramos/vlc/releases/tag/3.0.24-3d1) for Windows and Debian.
- [Kodi](https://github.com/xbmc/xbmc) - Media centre with stereoscopic display modes; derives the stereo mode from the stream's own metadata.
- [Bino](https://bino3d.org) - Dedicated 3D video player, strong on multi-display and projection setups.
- [sView](https://www.sview.ru/en/) - Stereoscopic image and video viewer for desktop and mobile, with many output modes.
- [Stereoscopic Player](https://www.3dtv.at) - Long-standing Windows player covering most stereo layouts.
- [StereoWebViewer](https://github.com/JackDesBwa/StereoWebViewer) - Renders one side-by-side image into parallel, cross, anaglyph or interleaved output in a browser. Its author has since abandoned it in favour of threejs-StereoscopicEffects below, so read it as a compact reference rather than a maintained tool.
- [threejs-StereoscopicEffects](https://github.com/JackDesBwa/threejs-StereoscopicEffects) - A broader set of stereoscopic effects for three.js, and the maintained successor to the viewer above. Stereopix uses it, which is how its interleaved modes came to be exercised in the field.
- [PhereoRoll3D](https://github.com/JackDesBwa/PhereoRoll3D) - Qt client for the Phereo stereo-photo community, and a readable reference implementation of Dubois anaglyph.
- [PhotoRoll3D](https://github.com/JackDesBwa/PhotoRoll3D) - A rewrite of that viewer intended to reach more online sources. Its author reports it frozen, with no plan to resume, so treat it as an architecture sketch rather than something to build on.

## Servers and delivery

- [Serviio](https://serviio.org) - DLNA server with per-renderer profiles, able to serve or transcode per device.
- [Jellyfin](https://jellyfin.org) - Free software media server, with 3D handling under active development.
- [Gerbera](https://gerbera.io) - Lightweight UPnP server with transcoding profiles.
- [Universal Media Server](https://www.universalmediaserver.com) - DLNA server with an extensive renderer-configuration collection.
- [ReadyMedia (MiniDLNA)](https://sourceforge.net/projects/minidlna/) - Minimal DLNA server that serves files untouched, which is often exactly what a 3D file needs.

## Displays decide the format

This is the join between the two halves of this list, and the thing most explanations skip: **a display can only show the packing its optics are built for.** Side-by-side versus over-under, full versus half, interleaved versus frame-sequential — none of those were arbitrary decisions. Each one exists because some screen needed the two views arranged that way.

| Display                                                                                                                                       | How it separates the eyes                                                                             | What it wants                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [CRT](https://en.wikipedia.org/wiki/Cathode_ray_tube) with shutter glasses                                                                    | alternating fields in time, at high [refresh rate](https://en.wikipedia.org/wiki/Refresh_rate)        | frame-sequential; the original PC stereo, and why [interlaced video](https://en.wikipedia.org/wiki/Interlaced_video) and 120 Hz mattered so much          |
| Active shutter LCD/[plasma](https://en.wikipedia.org/wiki/Plasma_display)/[OLED](https://en.wikipedia.org/wiki/OLED)                          | alternating whole frames, glasses synced                                                              | full-frame per eye: frame packing, or a half-width/half-height frame the set unsqueezes                                                                   |
| Passive polarised (FPR) panels                                                                                                                | [circular polarisation](https://en.wikipedia.org/wiki/Circular_polarization), alternate rows filtered | **row-interleaved at the panel**: each eye gets half the vertical resolution, always                                                                      |
| Parallax barrier / lenticular                                                                                                                 | alternate columns sent to each eye                                                                    | **column-interleaved**, which is why glasses-free devices are the odd ones out                                                                            |
| [DLP](https://en.wikipedia.org/wiki/Digital_light_processing) [rear-projection](https://en.wikipedia.org/wiki/Rear-projection_television) TVs | micromirrors, eyes split in a chequer pattern                                                         | **checkerboard**, which is exactly why `frame_packing_arrangement_type` 0 exists in H.264                                                                 |
| Cinema, single projector                                                                                                                      | RealD circular polarisation switched per frame                                                        | frame-sequential, and a [silver screen](https://en.wikipedia.org/wiki/Silver_screen) — an ordinary white screen depolarises the light and the effect dies |
| Cinema, Dolby 3D                                                                                                                              | Infitec wavelength splitting                                                                          | full colour on a normal screen, expensive glasses                                                                                                         |
| IMAX                                                                                                                                          | historically two projectors, one per eye                                                              | two full-resolution streams, the highest-fidelity arrangement there is                                                                                    |

So the format questions answer themselves.

**Side-by-side or over-under?** Side-by-side halves horizontal resolution; over-under halves vertical. On a passive panel that is already throwing away half the rows, over-under costs you less that you had not already lost. On an active-shutter set both are unsqueezed identically, so the choice is mostly about what your broadcaster or ripper picked.

**Full or half?** "Frame compatible" (half) exists so a 3D picture fits down a pipe built for 2D: same bitrate, same infrastructure, half the resolution per eye. Full frame packing needs a link that knows about 3D, which is what HDMI 1.4 added and what Blu-ray 3D uses with MVC.

**Does side-by-side halve the frame rate?** No. A 1920×1080 half-SBS output at 60 Hz carries sixty complete left/right pairs each second, so both eyes can receive sixty new temporal samples; each view instead loses half its horizontal pixels and is stretched from 960×1080. Technical full-SBS would carry two full 1920×1080 views in a 3840×1080 frame and needs a sink and link that advertise enough bandwidth. For HDMI 1.4-era televisions the useful gaming trade is often 1280×720 frame packing at 60 pairs per second, which preserves every 720p pixel in both eyes, while 1920×1080 frame packing at 24 pairs per second preserves cinema resolution and cadence but feels visibly slower in an interactive application. Linux names these as different DRM stereo layouts rather than treating “3D” as one mode.

**What if a display only offers 24p stereo?** Then 24 eye pairs per second is its limit. That is useful for film and visibly poor for a responsive game or tracked application; software cannot compose sixty genuinely new presentations through a sink mode that accepts twenty-four. A useful compatibility list should therefore print both the per-eye resolution and stereo-pair rate instead of awarding one vague “3D capable” badge. The owner can then choose the available compromise with an explanation of why that particular display feels slow.

**Why is my half-width file stretched?** Because half-SBS is [anamorphic](https://en.wikipedia.org/wiki/Anamorphic_format): the display is expected to know it must stretch each half back to full width. If nothing tells it — the exact failure this list keeps returning to — you get two squashed pictures side by side instead of one 3D image.

**Why does interleaved content look wrong on the wrong screen?** Row-interleaved assumes the panel filters alternate rows. Send it to an active-shutter set and it is just a striped 2D picture.

**Is interlaced 3D worth chasing?** Not for any display made since HDMI 1.4. The [mandatory table](#every-hdmi-14-stereo-structure) does include 1080i side-by-side, the broadcast format, but that obligation falls on the display, and every 3D display must also accept progressive frame packing, so nothing that shows 1080i 3D is limited to it. Sources are not obliged to send interlaced at all, and the PC drivers no longer do: NVIDIA's [modesetting code](https://github.com/NVIDIA/open-gpu-kernel-modules/blob/main/src/nvidia-modeset/src/nvkms-modepool.c) rejects every interlaced mode, nouveau [switched it off from Volta onward](https://github.com/torvalds/linux/commit/8ba9249396bef37cb68be9e8dee7847f1737db9d) after the display hardware refused it, and amdgpu's display core [never allows it](https://github.com/torvalds/linux/blob/master/drivers/gpu/drm/amd/display/amdgpu_dm/amdgpu_dm.c) on any connector. Interlace also stops at 1080 lines: none of the 4K or 8K formats in CTA-861 is interlaced, and [Rec. 2020](https://en.wikipedia.org/wiki/Rec._2020) allows progressive frame rates only. The devices that truly needed interlaced 3D are the analog ones, CRT televisions with field-sequential shutter kits, where the set itself is plain 2D and each eye rides in its own field.

**Can field-sequential 3D be saved?** Yes, as content. A field-sequential recording converts with stock FFmpeg: [`separatefields`](https://ffmpeg.org/ffmpeg-filters.html#separatefields) splits each frame into its fields in the stream's own order, and [`stereo3d`](https://ffmpeg.org/ffmpeg-filters.html#stereo3d) with input `al` (left eye in the first field, or `ar` when it is the second) pairs them. Top-and-bottom is the natural packing, because each field is already one eye at full width; side-by-side works too but halves the width again. Each eye keeps half the lines, and fifty or sixty fields become twenty-five or thirty stereo pairs a second, but both views come from the same instant and nothing is invented. Encode with x264's `frame-packing` option and the SEI that lets a 3D television switch itself is written too. The chain is [checked frame by frame](https://github.com/danielcamposramos/sony-bravia-linux/blob/main/tools/fieldseq-3d/verify-fieldseq-to-sbs.sh) on synthetic clips of both field orders, and on a real field-sequential DVD it [switched a 2011 Sony BRAVIA into 3D by itself](https://github.com/danielcamposramos/sony-bravia-linux/blob/main/docs/legacy-3d-formats.md#why-field-sequential-needs-the-high-refresh), with the depth the right way round.

**Why does 3D need a high refresh rate?** Cinema locked itself to [24 frames per second](https://en.wikipedia.org/wiki/24p) when sync sound arrived, because 24 was the slowest speed that still carried an acceptable optical soundtrack, and slower film cost less. But the eye sees [flicker](https://en.wikipedia.org/wiki/Flicker_fusion_threshold) below roughly 50–60 Hz, so a projector flashes each frame two or three times (48 or 72 Hz) to keep 24 fps from strobing. Stereo doubles the demand: two eyes each need their 24 frames, an alternation of only 48 flashes per second — right on the flicker threshold. That is why active-shutter 3D televisions run at 120 Hz or higher, lighting each eye 60 times a second, and why a 24 fps 3D film is the most flicker-prone thing a display can be asked to show. The one frame rate cinema chose to sit on its floor is the one frame rate stereo tolerates least. The real-world symptom is described best by [Linus Tech Tips](https://www.youtube.com/watch?v=_4Sz6J49jho): active-shutter glasses gave his wife a headache, and a mis-synced dual-projector pair juddered in motion while still shots stayed clean. Passive methods carry no such clock, and the contemporary reports say so: a 2008 review of the passive-polarised [iZ3D monitor](https://www.gameindustry.com/reviews/game-review/iz3d-is-a-ok/) records six straight hours of *World of Warcraft* in 3D followed by two of *BioShock* with no discomfort at all. Comfort is a property of the method, not of 3D, which is worth remembering whenever "3D gives people headaches" is offered as though it described every kind.

## Displays and devices

- [3D display](https://en.wikipedia.org/wiki/3D_display) - The survey of every approach to getting two images to two eyes.
- [Active shutter 3D system](https://en.wikipedia.org/wiki/Active_shutter_3D_system) - Alternating frames and synchronised glasses, used by most 3D televisions.
- [Polarized 3D system](https://en.wikipedia.org/wiki/Polarized_3D_system) - Passive glasses, cinema projection and film-patterned retarder panels, which are row-interleaved at the panel.
- [Autostereoscopy](https://en.wikipedia.org/wiki/Autostereoscopy) - Stereo with no glasses at all.
- [Parallax barrier](https://en.wikipedia.org/wiki/Parallax_barrier) - The glasses-free method used by the Nintendo 3DS and the 3D phones.
- [Lenticular printing](https://en.wikipedia.org/wiki/Lenticular_printing) - The same idea on paper, and the oldest glasses-free medium still in production.
- [Toshiba REGZA](https://en.wikipedia.org/wiki/Toshiba_Regza) - The Japanese end of the 3D television wave: the GL1 (2010) was shown as the first glasses-free 3D television, and the 55X3 (2011) shipped a glasses-free 3D display in the first 4K set.

**A passive 3D theater at home, 2024.** Linus Tech Tips built the cinema method in a basement, and the video works as a parts list. Two image sources, one per eye, each behind its own polarising filter: two used 4K projectors at about 500 US dollars each, because the laser projector already in the room [could not be polarised](https://www.youtube.com/watch?v=_4Sz6J49jho&t=162s) with circular or linear filters. Glass circular polarisers (clockwise and counter-clockwise) and glasses from [American Polarizers](https://www.apioptics.com/), [over 1,500 US dollars](https://www.youtube.com/watch?v=_4Sz6J49jho&t=242s) together; cheap plastic ones were cloudy, and [linear filters](https://www.youtube.com/watch?v=_4Sz6J49jho&t=531s) swap the eyes when you tilt your head. A screen that keeps the polarisation, a [Stewart](https://www.stewartfilmscreen.com/) Silver 5D at [about 6,000 dollars](https://www.youtube.com/watch?v=_4Sz6J49jho&t=356s), since a screen sold as "3D" usually means active 3D only. Blu-ray 3D ripped, remuxed with [BD3D2MK3D](https://forum.makemkv.com/forum/viewtopic.php?t=23561) and split to the two projectors with Stereoscopic Player. The verdict was "theater grade" with very little crosstalk, but [motion looked rough](https://www.youtube.com/watch?v=_4Sz6J49jho&t=910s), "like it's alternating which frame": two projectors that are not frame-locked show the eyes at slightly different moments.

### Glasses-free phones, handhelds and cameras

The 2011 wave is why stereo files exist in ordinary people's archives: these devices both *shot* stereo pairs and *displayed* them, with no glasses and no extra hardware. Most of the MPO and JPS files in circulation came from here.

- [Nintendo 3DS](https://en.wikipedia.org/wiki/Nintendo_3DS) - Parallax-barrier handheld that shot and displayed MPO stereo photographs; the [New Nintendo 3DS](https://en.wikipedia.org/wiki/New_Nintendo_3DS) added head tracking to hold the sweet spot.
- [LG Optimus 3D](https://en.wikipedia.org/wiki/LG_Optimus_3D) - Glasses-free phone with a dual-camera stereo pair, 2011, and one of the few that recorded 3D video as well as stills. Its software also converted 2D games into 3D — see [Games and handhelds](#games-and-handhelds).
- [HTC Evo 3D](https://en.wikipedia.org/wiki/HTC_Evo_3D) - Its direct contemporary: same parallax barrier, same twin cameras, same brief window.
- [Fujitsu F-09C](https://ja.wikipedia.org/wiki/F-09C) - The Japanese half of the same 2011 wave: an NTT docomo flip phone with a glasses-free 3D display that shipped a 3D block-breaking game among its preloaded 3D apps. It has an article in Japanese and none in English, which is the Japanese gap this list admits to, in one phone.
- [LG Optimus Pad](https://en.wikipedia.org/wiki/LG_Optimus_Pad) - The tablet of the same generation, shooting stereo video while showing it in 2D.
- [Red Hydrogen One](https://en.wikipedia.org/wiki/Red_Hydrogen_One) - The 2018 attempt at reviving glasses-free 3D on a phone, with a four-view light-field display.
- Fujifilm FinePix Real 3D - The twin-lens consumer cameras, with a glasses-free display on the back, that made MPO a format people actually had files in.
- [Stereo camera](https://en.wikipedia.org/wiki/Stereo_camera) - The general form, from the Victorian twin-lens cameras onward.
- [Budget glasses-free tablets](https://github.com/danielcamposramos/sony-bravia-linux/blob/main/docs/legacy-3d-formats.md) - Parallax-barrier Android tablets such as the Gadmei T883-3D sold in volume outside the brand-name market between roughly 2011 and 2013, and are now close to undocumented: no manufacturer site, no archive, firmware passed around in forums. One is catalogued in the sony-bravia-linux legacy-formats notes as a preserved example.

### Current

Glasses-free 3D came back to the living room as prototypes and first production in 2026, this time built mostly on light-field (plenoptic) panels instead of the lenticular sheets of 2010, so there is no narrow sweet spot and several people can watch side by side. Projectors that take 3D Blu-ray with active glasses never went away.

- [Glasses-free 3D TVs at CES 2026](https://www.techradar.com/televisions/i-saw-2-next-gen-3d-tvs-without-glasses-that-use-a-new-tech-that-changes-everything-heres-how-it-works) - TechRadar, January 2026, on the two sets shown: Visual Semiconductor's GF3D, a 65-inch 8K set, and a TCL prototype, both light-field (plenoptic) panels. GF3D converts any 2D programme into an emulated light field, which is how it expects to have content at all, since nobody films with plenoptic cameras.
- [Samsung Odyssey 3D](https://news.samsung.com/global/samsung-electronics-unveils-groundbreaking-glasses-free-odyssey-3d-gaming-monitor-at-gamescom-2024) - Glasses-free gaming monitors, lenticular with eye tracking: the 27-inch 4K model shown at Gamescom 2024, and a [32-inch 6K model](https://www.techradar.com/computing/monitors/glasses-free-3d-displays-are-making-an-unlikely-comeback-as-samsung-reveals-worlds-first-6k-monitor-with-real-time-eye-tracking) that follows the viewer's eyes to steer each view.
- [Looking Glass](https://lookingglassfactory.com/) - Light-field displays, the commercial descendant of the glasses-free line; its old looking-glass.com domain now belongs to an unrelated company.
- [Leia](https://www.leiainc.com) - Light-field displays and the conversion tooling around them, now operating under the name Immersity.
- [Top 3D projectors](https://www.projectorcentral.com/top-3d-projectors.htm) - ProjectorCentral's list of 3D projectors on sale, updated September 2026: ten models from BenQ, XGIMI, Optoma, Epson, JVC, Hisense and Valerion, from about 500 to 17,000 US dollars, all working with 3D glasses. The cheapest way to 3D Blu-ray at cinema size today.

## Headsets and worn displays

A headset is a stereoscope you wear. The line from Wheatstone's mirrors through Brewster's lenses, the View-Master, the Virtual Boy and Google Cardboard to today's head-mounted displays is one continuous idea: two images, two eyes, held at the right distance. The optics and the tracking changed; the stereo pair did not.

- [The Sword of Damocles](https://en.wikipedia.org/wiki/The_Sword_of_Damocles_(virtual_reality)) - Ivan Sutherland's 1968 head-mounted display, built with Bob Sproull, Quintin Foster and Danny Cohen, which showed the output of a computer program stereoscopically. It matters here for who built it: Sutherland had already written [Sketchpad](https://en.wikipedia.org/wiki/Sketchpad) and is called the father of computer graphics, and the first thing he pointed a computer-generated image at was two eyes. Computer graphics and stereoscopic display do not meet later; they start together.
- [Head-mounted display](https://en.wikipedia.org/wiki/Head-mounted_display) - The general form, from military optics to consumer headsets.
- [Virtual reality headset](https://en.wikipedia.org/wiki/Virtual_reality_headset) - The modern category and how its stereo rendering works.
- [Google Cardboard](https://en.wikipedia.org/wiki/Google_Cardboard) - A phone in a folded holder with two lenses. It is Brewster's 1849 box stereoscope and Holmes's 1861 handheld viewer, rebuilt around a screen, and it shows the same side-by-side pair the Victorians printed on cards.
- [Oculus Rift](https://en.wikipedia.org/wiki/Oculus_Rift) - The 2012 development kit that restarted the category.
- [HTC Vive](https://en.wikipedia.org/wiki/HTC_Vive) and [Valve Index](https://en.wikipedia.org/wiki/Valve_Index) - Room-scale PC headsets built around SteamVR.
- [Steam Frame](https://en.wikipedia.org/wiki/Steam_Frame) - Valve's standalone headset.
- [Meta Quest](https://en.wikipedia.org/wiki/Meta_Quest) and [Meta Quest 3](https://en.wikipedia.org/wiki/Meta_Quest_3) - The standalone line that made headsets a mass product.
- [Samsung Galaxy XR](https://en.wikipedia.org/wiki/Samsung_Galaxy_XR) - The first [Android XR](https://en.wikipedia.org/wiki/Android_XR) headset, October 2025.
- [Apple Vision Pro](https://en.wikipedia.org/wiki/Apple_Vision_Pro) - Notable here for making stereoscopic capture ordinary again: its "spatial video" is an MV-HEVC stereo pair shot on a phone.
- [Augmented reality](https://en.wikipedia.org/wiki/Augmented_reality) - The same stereo optics aimed at the world instead of a virtual scene; "mixed reality" redirects here.

### Open software for headsets

- [OpenXR](https://en.wikipedia.org/wiki/OpenXR) - The Khronos standard that replaced one vendor API per headset; [SDK and specification sources](https://github.com/KhronosGroup/OpenXR-SDK).
- [Monado](https://gitlab.freedesktop.org/monado/monado) - Free and open-source OpenXR runtime, the reference implementation on Linux.
- [OpenVR](https://github.com/ValveSoftware/openvr) - Valve's API and SDK behind SteamVR.
- [OpenHMD](https://github.com/OpenHMD/OpenHMD) - Free driver library covering a wide range of older and current headsets.
- [ALVR](https://github.com/alvr-org/ALVR) - Streams PC VR to standalone headsets over the network.
- [WiVRn](https://github.com/WiVRn/WiVRn) - OpenXR streaming to standalone headsets, built on Monado.
- [WebXR](https://en.wikipedia.org/wiki/WebXR) - Stereo rendering in the browser; [immersiveweb.dev](https://immersiveweb.dev) and the [samples](https://github.com/immersive-web/webxr-samples).
- [Godot XR Tools](https://github.com/GodotVR/godot-xr-tools) - XR toolkit for the Godot engine.
- [ARCore SDK](https://github.com/google-ar/arcore-android-sdk) - Google's AR framework for Android.

**From headset eye images back to a 3D television.** An XR runtime and an HDMI 3D display want the same two finished eye images but package them differently. The missing bridge is an output stage that scales those images into the two halves of a side-by-side or top-and-bottom frame, then requests the matching HDMI stereo mode. This is already a known composition operation: [wiz3D's open SideBySideOutput](https://github.com/effcol/wiz3D/tree/main/OutputMethods/SideBySideOutput) reads separate left and right Direct3D backbuffers and copies them into horizontal or vertical output rectangles. On Linux, a [gamescope](https://github.com/ValveSoftware/gamescope) or Monado output target could perform the same operation (gamescope already carries an OpenVR backend that outputs its session as a VR overlay, cursor included: the reverse direction); full frame packing additionally needs a 1920×2205 two-eye scanout and driver support for doubled HDMI timing. The [sony-bravia-linux implementation note](https://github.com/danielcamposramos/sony-bravia-linux/blob/main/docs/dual-surface-hdmi-3d.md) traces that path from compositor surfaces through DRM to the television: SBS/TaB works through the patched AMD path, full 1080p24 frame packing is proven through stock nouveau, and amdgpu's frame-packing timing translation remains the driver boundary.

**Proven on a VR engine, 2026.** The bridge above now exists for one game. Half-Life 2 has had a VR mode since 2013; a [replacement for its VR module](https://github.com/danielcamposramos/sony-bravia-linux/tree/main/tools/vr-stereo-spectator/sourcevr) points the two eyes at a 3D television instead of a headset, and in September 2026 it played through level transitions on two Sony 3D sets on Linux, with the HUD, crosshair and menus moved onto the screen plane. What any VR engine needs for the same is written up as a [formula](https://github.com/danielcamposramos/sony-bravia-linux/blob/main/tools/vr-stereo-spectator/FORMULA.md), and the idea, a stereo spectator for the room while one person wears the headset or a player with no headset at all, has its own section in [awesome-vr](https://github.com/danielcamposramos/awesome-vr#vr-on-3d-displays-the-stereo-spectator). Valve was asked the same day for the pieces only it can change: [Source-1-Games #8297](https://github.com/ValveSoftware/Source-1-Games/issues/8297) for the game, [SteamVR-for-Linux #961](https://github.com/ValveSoftware/SteamVR-for-Linux/issues/961) for the runtime. It also answered a request that had waited since 2013, [#1013](https://github.com/ValveSoftware/Source-1-Games/issues/1013): "Pretty much all 3D ready DLP projectors support SBS".

**One stereo window is enough.** HDMI 3D applies to the whole output, but every window does not need two different views. A compositor can keep left-eye and right-eye desktop canvases, duplicate ordinary windows and UI into both at screen depth, and place a stereo application's two buffers at the same logical window rectangle, one per canvas. It then packs the two completed canvases once for the television. The same contract serves a game or XR runtime supplying two rendered eye surfaces and a video player whose decoder found H.264/H.265 frame-packing SEI or container stereo metadata. The Linux work is a way to pair two buffers as one stereo surface, a persistent stereo-intent signal, and the HDMI output backend.

### The cheapest working path

A phone the reader already owns, a pair of lenses, and a PC doing the rendering is the least expensive route to real stereo in full colour today, and every part of it is still available.

- [Cardboard SDK](https://github.com/googlevr/cardboard) - What Google did on the way out. [Daydream](https://en.wikipedia.org/wiki/Google_Daydream) was discontinued in October 2019 with the explanation that "there hasn't been the broad consumer or developer adoption we had hoped", and the Google Store stopped selling Cardboard viewers in March 2021, but the SDK was open-sourced under Apache 2.0 rather than withdrawn. It is still released, v1.35.0 in August 2026, which makes it one of the rare vendor exits in this list that left the format usable. The one part of the viewer that cannot be improvised is the lens pair, specified at a 45 mm focal length because the eye cannot focus on a screen a few centimetres away. Bare biconvex pairs sell for [under a dollar](https://www.crcibernetica.com/lens-for-google-cardboard-25mm-45mm-focal-length-1-pair/), and complete viewers for about [599 rupees in India](https://www.irusu.co.in/product/irusu-google-cardboard/).
- [ReShade](https://reshade.me/) - Open-source (BSD 3-clause) post-processing injector for Direct3D, OpenGL and Vulkan games, and the host that modern stereo injection runs inside.
- [Depth3D](https://github.com/BlueSkyDefender/Depth3D) - Builds the second eye from a game's depth buffer, the technique iZ3D, 3D Vision and TriDef once sold as drivers, now running as a shader inside ReShade. It outputs side-by-side, top-and-bottom, line and column interlaced, checkerboard and anaglyph, and has a Theater mode aimed at phone viewers. Actively maintained, and free for personal use, but its README is explicit that it "is not open source and it is not free to ship inside a product".
- [Sunshine](https://github.com/LizardByte/Sunshine) and [Moonlight](https://github.com/moonlight-stream/moonlight-qt) - Open-source (GPL-3.0) game streaming, a PC host and a client for phones, televisions and other computers. Neither knows anything about stereo, which is exactly why they work here: they carry whatever frame the PC renders, so a side-by-side frame from Depth3D reaches the phone intact.

**What this path does not solve.** The phone still needs a player that sends each half of a side-by-side frame to one eye, and no open-source Android player that does this and is clearly maintained was found. VLC [renders side-by-side sources as anaglyph](https://wiki.videolan.org/3D) on the desktop rather than splitting them for a viewer. A current buying guide dismisses phone viewers as "a neat demo a decade ago" and recommends a [Meta Quest 3S at $349, or a used Quest 2 at around $150](https://vr.org/best-budget-vr-headset), which is sound advice for anyone who can afford it. For anyone who cannot, the phone already in their pocket and a few rupees of plastic and glass remain the only full-colour stereo within reach, since the television makers stopped building 3D sets with their 2017 ranges.

## Beyond the eyes

**Scope note, stated plainly: none of this is stereoscopy.** A haptic vest puts no image in either eye. It is here because the stereo image is the first component of presence and never the only one, and because the question "what would full immersion actually take" leads straight out of the display and into the body. Treat this section as the neighbours, clearly labelled, not as the subject.

- [Haptic technology](https://en.wikipedia.org/wiki/Haptic_technology) - Touch as an output device, and the general field the rest of this section sits in. "Force feedback" redirects here, and the idea is worth stating in this list's own terms: it is **depth you feel instead of see**. A wheel that fights back, a trigger that resists, a seat that moves — the same substitution a 4D cinema makes when it adds motion and air to a stereo image.
- [Rumble Pak](https://en.wikipedia.org/wiki/Rumble_Pak) - 1997, where force feedback became something ordinary people owned.
- [Motion simulator](https://en.wikipedia.org/wiki/Motion_simulator) - Moving the body to sell the image, from flight trainers to the motion seats in 4D theatres and the Back to the Future ride above.
- [Proprioception](https://en.wikipedia.org/wiki/Proprioception) - The sense these devices actually address: where your body believes it is. Contradict it and you get [simulator sickness](https://en.wikipedia.org/wiki/Simulator_sickness), which is the single biggest limit on all of it.
- [Haptic suit](https://en.wikipedia.org/wiki/Haptic_suit) - Worn feedback across the torso and limbs, the wearable half of "full body".
- [bHaptics](https://www.bhaptics.com) - The vests, sleeves and face haptics that actually shipped to consumers.
- [HaptX](https://haptx.com) - Force-feedback gloves aimed at industrial and research use, where the hand resists as well as buzzes.
- [Teslasuit](https://teslasuit.io) - Full-body suit combining electro-muscular stimulation, motion capture and biometrics.
- [Wired glove](https://en.wikipedia.org/wiki/Wired_glove) - The lineage, from the Power Glove and DataGlove onward: the first serious attempt to get the hand into the scene.
- [OpenGloves](https://github.com/LucidVR/opengloves-driver) - Open driver for do-it-yourself haptic gloves, the community answer to gloves costing more than the headset.
- [SlimeVR](https://slimevr.dev) - Open-source full-body tracking: [firmware](https://github.com/SlimeVR/SlimeVR-Tracker-ESP), [server](https://github.com/SlimeVR/SlimeVR-Server) and an [OpenVR driver](https://github.com/SlimeVR/SlimeVR-OpenVR-Driver) for cheap IMU trackers. The clearest example in this section of a proprietary capability being rebuilt as something people can own and repair.
- [Motion capture](https://en.wikipedia.org/wiki/Motion_capture) and [finger tracking](https://en.wikipedia.org/wiki/Finger_tracking) - Getting the body into the scene at all, which is the other half of full-body VR.

### Omnidirectional controllers

Locomotion is the oldest unsolved problem in the category: the scene is infinite and the room is not.

- [Omnidirectional treadmill](https://en.wikipedia.org/wiki/Omnidirectional_treadmill) and [Virtuix Omni](https://en.wikipedia.org/wiki/Virtuix_Omni) - Walking without leaving the room, the approach most attempts have taken.
- [KAT VR](https://www.kat-vr.com) - Current locomotion platforms of that kind.
- [Disney HoloTile](https://xchange.avixa.org/posts/disney-advances-vr-treadmill-technology-with-holotile) - An omnidirectional floor of small rotating tiles that lets several people walk anywhere, in any direction, without moving from the spot, invented by [Lanny Smoot](https://en.wikipedia.org/wiki/Lanny_Smoot) at [Walt Disney Imagineering](https://en.wikipedia.org/wiki/Walt_Disney_Imagineering), with more from [Disney Research](https://la.disneyresearch.com). The same company that built Captain EO in 1986 is still inventing immersion hardware forty years later, which says something about where this medium has always been funded.
- [Galvanic vestibular stimulation](https://en.wikipedia.org/wiki/Galvanic_vestibular_stimulation) - Driving the [vestibular system](https://en.wikipedia.org/wiki/Vestibular_system) directly, the research edge where motion is felt rather than shown, and the most direct attack on motion sickness.
- [Brain-computer interface](https://en.wikipedia.org/wiki/Brain%E2%80%93computer_interface) - The far end of the same road, where the display disappears entirely.

### Light beyond the frame

The cheapest immersion trick of all: extend the picture past the edges of the screen into the room, so [peripheral vision](https://en.wikipedia.org/wiki/Peripheral_vision) stops reporting that the image ends. No stereo involved, and the effect on presence is real.

- [Ambilight](https://en.wikipedia.org/wiki/Ambilight) - Philips' built-in version, lighting the wall with colours sampled from the edges of the frame. Often misremembered as an LG feature; it is Philips', through [TP Vision](https://en.wikipedia.org/wiki/TP_Vision).
- [Hyperion](https://github.com/hyperion-project/hyperion.ng) - The open-source implementation, which does the same for any screen and any LED strip, including televisions whose manufacturer never offered it.
- [WLED](https://github.com/Aircoookie/WLED) - The firmware most of those strips end up running.
- [Lightpack / Prismatik](https://github.com/psieg/Lightpack) and [Adalight](https://github.com/dmadison/Adalight-FastLED) - The earlier open hardware and sketch that started the do-it-yourself lineage.
- [Philips Hue](https://en.wikipedia.org/wiki/Philips_Hue) - The commercial route, via its HDMI sync hardware.
- [Field of view](https://en.wikipedia.org/wiki/Field_of_view) - Why any of it works, and the quantity every immersion technology in this section is ultimately buying.

## Communities and archives

- [Stereopix](https://stereopix.net) - Active stereo-photo sharing platform, handling MPO and JPS with browser-side viewing in every common mode.
- [photo-3d group](https://photo-3d.groups.io/g/main) - One of the oldest continuously running stereo-photography mailing lists.
- [MTBS3D](https://www.mtbs3d.com) - Meant to be Seen: forums and reporting that covered the PC and consumer 3D era closely.
- [International Stereoscopic Union](https://www.isu3d.org) - The international body for stereo photography, with congresses and a journal.
- [The Stereoscopic Society](https://www.stereoscopicsociety.org.uk/) - Founded in London in 1893, the oldest stereoscopic society in the world and still meeting.
- [STEREO CLUB Tokyo](http://www.stereoclub.jp/) - The Tokyo stereo-photography club, founded in 1996 and still holding seasonal meetings. It hosted the International Stereoscopic Union's 24th world congress at Tsukuba in 2023, the first held in Japan, and its [chronology of stereo photography in Japan](https://isu2023.stereoclub.jp/index_stereojapan_j.html), in Japanese, records a far older society: the Japan Binocular Photography Society (日本双眼寫眞會), founded in 1923 at the urging of Hayao Yoshikawa and Shūsuke Satō.
- [Stereo World](https://www.stereoworld.org) - The National Stereoscopic Association's magazine, continuous since 1974.
- [Phereo](https://phereo.com) - Stereo-photo community whose archive is historically important, still holding more than 200,000 images. It lost the images published between roughly January 2019 and October 2022; the loss has since stopped, but some functions such as search no longer work, so treat it as an archive rather than a live service.
**Reddit stereo communities.** [r/CrossView](https://www.reddit.com/r/CrossView/), [r/ParallelView](https://www.reddit.com/r/ParallelView/), [r/Anaglyph](https://www.reddit.com/r/Anaglyph/) and [r/wigglegrams](https://www.reddit.com/r/wigglegrams/) are the most active day-to-day stereo photography communities on the web, each with a fixed convention for the pair it displays.

## Preservation

- [sony-bravia-linux](https://github.com/danielcamposramos/sony-bravia-linux) - The project this list grew out of. It documents why correctly authored 3D files play flat on hardware that supports them: the in-stream frame-packing SEI that displays act on and almost nothing wrote. Measurements on real sets, fixes taken upstream across the whole encode, remux, serve and play chain, tools that repair existing files losslessly, and the same research published in eleven languages so owners can find it in their own.
- [Consumer Rights Wiki: Sony BRAVIA pre-Android Linux TVs](https://consumerrights.wiki/index.php?title=Sony_BRAVIA_pre-Android_Linux_TVs_(2011-2012)) - A worked example of documenting what happens to a 3D product line after its services are switched off, sourced to the manufacturer's own notices.

### Services that were switched off

The hardware outlived the services. These are the 3D channels and content platforms that launched, ran, and closed, with what their operators said on the way out. Japan's own run, [documented above](#television-and-home-video), lasted longest of all: Star Channel kept a monthly 3D film slot until 23 January 2020, six years after the English-language channels had gone.

- [ESPN 3D](https://www.sportsvideo.org/2013/06/12/breaking-news-espn-to-discontinue-3d-network/) - Launched June 2010 with the World Cup, closed 30 September 2013. The stated reason was demand, not technology: "Due to limited viewer adoption of 3D services to the home, ESPN is discontinuing ESPN 3D."
- [3net](https://en.wikipedia.org/wiki/3net) - Sony, Discovery and IMAX's joint 24-hour 3D channel, February 2011 to August 2014. Its programmes kept airing afterwards on a sister channel, in 2D. No announcement to subscribers has been found.
- [Sky 3D](https://vodzilla.co/blog/vod-news/sky-scraps-3d-channel/) - The UK linear channel closed 9 June 2015 and became on-demand only, framed as an improvement: the films would be "ready and waiting for our customers to view whenever it suits them".
- [Sky 3D Germany](https://en.wikipedia.org/wiki/Sky_3D_(German_TV_channel)) - The same brand in another market outlived the British one by two years, closing 1 July 2017 over low ratings.
- [BBC's 3D trial](https://www.hdtvtest.co.uk/news/bbc-axes-3d-201307083167) - Suspended indefinitely in July 2013 after two years, with the clearest audience verdict anyone published: 3D viewing was "quite hassly", and in 3D-equipped homes the audience fell from about half for the 2012 Olympic opening ceremony to roughly a twentieth for Christmas Day programming.
- [DirecTV n3D](https://www.nexttv.com/news/directv-downgrades-its-3d-channel-part-time-status-377565) - Billed as the first 24-hour 3D channel (2010), cut to part-time in June 2012. Sources disagree on when it stopped entirely, which is its own kind of answer.

**Four manufacturers' 3D portals were one company, and it went bankrupt.** [LG launched "3D World"](https://www.lg.com/global/newsroom/news/media-entertainment-solution/lg-announces-global-launch-of-3d-world-next-generation-premium-3d-content-service-2/) in April 2012 to CINEMA 3D owners in some seventy countries, describing it as "a critical part of LG's long-term strategy which includes controlling more of the 3D ecosystem". [Panasonic's VIERA sets got the same kind of service in May 2014](https://www.hdtvsolutions.com/flatscreen_news_story_651.htm), and Samsung and Vizio followed. Underneath the different brand names sat one supplier's platform, [SENSIO Technologies](https://en.wikipedia.org/wiki/SENSIO_Technologies) and its 3DGO! service, and when SENSIO was deemed to have filed an assignment in bankruptcy on 22 April 2016, the 3D storefront inside all of those televisions went with it. [LG's own support notice](https://www.lg.com/ca_en/support/product-support/troubleshoot/help-library/cs-CT20098005-20150136152117/) is exact about it: "the 3DGO! 3D content streaming service will be permanently discontinued from the LG Smart Television flat panel display panels", on 16 April 2016 — four years to the day after the launch. The notice promises refunds for *subscriptions* and says nothing about films already bought.

**Some removals were never announced at all.** [YouTube's help page still documents uploading stereoscopic 3D](https://support.google.com/youtube/answer/7278886) with its `st3d` metadata, while the player's own 3D viewing modes — anaglyph, side-by-side, interleaved, the ones that let any screen show a stereo video — are simply gone from the ordinary player, with no changelog entry, blog post or date that could be found. The format still uploads. The audience just cannot choose to see it. [Where those videos are, and how to find them](stereo-video-on-youtube.md): viewer playlists, the old `yt3d` tags as a search key, and one creator's 3D run from 2010-2011.

### The format that retired but did not die

Consumer 3D was withdrawn, not abandoned by the people who had it. The gap between those two things is where this whole list lives, and it shows up publicly whenever somebody well equipped tries to use the hardware they already own:

- I built a 3D theater in my basement - Linus Tech Tips, 2024. Worth watching for one admission at [10:20](https://www.youtube.com/watch?v=_4Sz6J49jho&t=620s): getting the *files* to play took "more tinkering behind the scenes than anything else we've done so far" — ripping discs and remuxing by hand, on a channel with a full engineering team behind it. He also notes in the same video that dozens of 3D titles still ship on Blu-ray every year, which is the point: the content exists, and the playback chain is what broke.
**Phereo**, filed under communities above, is relevant here too: an archive of community stereo photography whose backend has become unreliable, which is how a format's material disappears in practice. Not with an announcement, just with timeouts.

## Adjacent fields

Same word, and in one case the same root, for a different problem.

### Depth from two views

"Stereo" in computer vision means recovering depth from two views, rather than presenting two views to two eyes. The perceptual basis is the one described under who can see it, and who cannot.

- [SimpleStereo](https://github.com/decadenza/SimpleStereo) - Calibration and depth estimation, for when the goal is a depth map rather than a stereo pair.

### Two ears, two eyes

Stereo sound is not a pun on this list's subject. It is the same idea in another sense organ, from the same Greek word: *stereoscopy* is στερεός (stereós, "firm, solid") with σκοπέω, "to look"; *stereophonic* is that same στερεός with φωνή, "sound". Both were named for making something solid out of two flat signals, and both work the same way — two receptors, and a brain reading the difference between them.

- [Stereophonic sound](https://en.wikipedia.org/wiki/Stereophonic_sound) - Invented by Alan Blumlein at EMI in 1931 to fix a problem in a cinema. In the early talkies the actor could be on one side of the screen while his voice came from a single speaker somewhere else, and Blumlein told his wife he had found a way to "make the sound follow the actor across the screen". His patent, applied for that December and accepted in 1933 as UK 394,325, covered stereo records, stereo films and surround sound. Stereo pictures and stereo sound both began as cinema problems.
- [Alan Blumlein](https://en.wikipedia.org/wiki/Alan_Blumlein) - The engineer behind that patent and 127 others, who died in 1942 testing airborne radar, and whose two-microphone technique is still standard practice.
- [Binaural recording](https://en.wikipedia.org/wiki/Binaural_recording) - Two microphones in the ears of a dummy head: a two-camera rig built for ears. Because the head is really there, the head shadow and the timing and level differences between the ears are recorded rather than simulated, which is exactly the argument for shooting a stereo pair instead of synthesising one.
- [Sound localization](https://en.wikipedia.org/wiki/Sound_localization) - Interaural time and level differences, computed in the brainstem: the ears' counterpart to binocular disparity. The two senses divide the work, since the eyes cover a fraction of the world and fail in darkness, while localisation works in every direction at once.
- [Head-related transfer function](https://en.wikipedia.org/wiki/Head-related_transfer_function) - How one particular head and pair of ears filter the sound arriving at them. It differs from person to person, which is why binaural audio suits some listeners better than others — the audio counterpart of interpupillary distance, and of the fact that some viewers cannot fuse a stereo pair at all.

## In fiction

Stories about depth, and what they got right. The fuller fiction threads live in [awesome-vr](https://github.com/danielcamposramos/awesome-vr#in-fiction) and [awesome-ar](https://github.com/danielcamposramos/awesome-ar#in-fiction).

- [Pygmalion's Spectacles](https://www.gutenberg.org/ebooks/22893) - Stanley G. Weinbaum's 1935 story of spectacles that put the wearer inside a film. A stereoscope that tells a story you stand in is what a headset became.
- [Back to the Future Part II](https://en.wikipedia.org/wiki/Back_to_the_Future_Part_II) - The 1989 film's "Jaws 19" shark, a joke on the real 1983 [Jaws 3-D](#cinema-and-hollywood). Depth that leaves the screen is exactly what a stereo pair fakes, for one seat at a time.
- [Star Wars](https://en.wikipedia.org/wiki/Holography_in_fiction) - Leia's 1977 message, depth visible from every side with no glasses. The real routes to that are holography and light fields (see [Related lists](#related-lists)), not two views.

## Related lists

- [awesome-vr](https://github.com/danielcamposramos/awesome-vr) - Virtual reality as its own subject: headsets, the open runtimes that keep them working, standards, comfort and accessibility, and the platforms that were switched off. A headset is a stereoscope you wear, and this is where that thread continues.
- [awesome-ar](https://github.com/danielcamposramos/awesome-ar) - Augmented reality: see-through optics, the SLAM and visual-inertial tracking that decide where the room is, the SDKs and the standards.
- [awesome-linux-hdr](https://github.com/danielcamposramos/awesome-linux-hdr) - HDR and deep colour on Linux, from specification to photons. The EDID and InfoFrame machinery that signals 3D also signals colour depth and HDR, and both share one HDMI link budget.
- [From one bit to HDR](https://github.com/danielcamposramos/awesome-linux-hdr/blob/main/colour-depth-explained.md) - Colour depth explained, from 2 colours to 281 trillion: why each step happened, the caveats, and how HDR differs from simply more bits.
- [awesome-webxr](https://github.com/msub2/awesome-webxr) - The browser side of both, maintained separately.
- [awesome-computer-vision](https://github.com/jbhuang0604/awesome-computer-vision) - Where the other meaning of "stereo" lives: matching, calibration and depth from two views as a research field.
- [awesome-3D-gaussian-splatting](https://github.com/MrNeRF/awesome-3D-gaussian-splatting) - The current literature on splatting and view synthesis, which is where the second eye increasingly comes from.
- [awesome-holography](https://github.com/bchao1/awesome-holography) - Holographic displays, the end of the road this list keeps walking towards.
- [awesome-OpenSourcePhotography](https://github.com/ibaaj/awesome-OpenSourcePhotography) - Open-source photography tooling generally, for the parts of a stereo workflow that are simply photography.
- [awesome-ffmpeg](https://github.com/transitive-bullshit/awesome-ffmpeg) - Tooling around the one program most of this list's conversions actually run on.
- [awesome-NeRF](https://github.com/awesome-NeRF/awesome-NeRF) - Neural radiance field papers, the other main route to synthesizing a second view.
- [awesome-light-fields](https://github.com/JoanCharmant/awesome-light-fields) - Light field capture, rendering and displays, the step beyond two views; dormant since 2016, kept for its history.
- [awesome-volumetric-filmmaking](https://github.com/SimileSystems/awesome-volumetric-filmmaking) - Volumetric video capture and playback; dormant since 2018, still a useful map of the field.
- [awesome-digital-preservation](https://github.com/digipres/awesome-digital-preservation) - Digital preservation practice and tools, for keeping discontinued platforms, formats and their content usable.

## Known gaps

Stated openly, because a curated list that hides its blind spots is worse than one that names them. These are the places this list is weakest, and the contributions most wanted:

**The record is still Western-leaning, though less than it was.** [World stereo cinema](#world-stereo-cinema) now runs from the Soviet Union and Japan through Mexico, Argentina, China, Korea, India and Brazil, and [Beyond Europe and North America](#beyond-europe-and-north-america) carries stereo photography in Brazil, Iran, Lebanon and Japan. Still missing: anything citable from Southeast Asia or sub-Saharan Africa, the Chinese 3D wave of the 1980s (so far documented only on sites that cannot be cited), and nineteenth-century stereo photography by Indian practitioners. Contributions in any language are wanted; cite what you can.

**Mexico's first 3D film** is an open question. Rosa Elena Cabiedes' *El Reportero TD* (1953) may predate *El Corazón y la Espada*, but it is known here only through a citation of the FIAF *Journal of Film Preservation*; nothing else about the film or its director was found online.

**Japanese coverage** now reaches the stereo societies, the broadcast era and 1950s cinema. Two holes remain: no NHK network 3D broadcast trial, as distinct from its laboratory research, has been found with a source, and the 1923 society is known only through a later chronology.

**Sanskrit sources.** Whether older Sanskrit texts discuss binocular depth directly is still open. Nothing citable was found, and a claim that cannot be sourced does not belong here, so the space is left open rather than filled.

**Pre-1900 publishing** now has a [continental section](#the-continental-trade) covering France, Germany, Italy and Spain alongside the British, American and Japanese firms. No publisher from Austria, Switzerland, Belgium, the Netherlands, Scandinavia or the Russian Empire has yet been found with a citable source, and the thousands of smaller firms that shipped cards are still unrepresented.

Several entries describe things that are defunct or unreliable. That is deliberate, but it means some links will rot; reports are welcome.

## Contributing

Contributions are welcome. Read the [contribution guidelines](contributing.md) first.
