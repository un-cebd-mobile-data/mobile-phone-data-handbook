from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "FINAL DRAFT (v1.4) MPD Design and Implementation Handbook - 26May26 [CLOSED FOR EDITS].docx.md"


FOOTNOTE_CITES = {
    "1": "[@unstats2019mpdhandbook]",
    "2": "[@blondel2015survey]",
    "3": "[@gsma2016mobileprivacy]",
    "4": "[@uncebd_information_society]",
    "5": "[@itu_sdg_case_study]",
    "6": "[@uncebd_dynamic_population; @deville2014dynamic_population; @ricciato2020present_population]",
    "7": "[@uncebd_migration_statistics]",
    "8": "[@uncebd_tourism_statistics; @ahas2008tourism]",
    "9": "[@caceres2007origin_destination; @calabrese2011od; @alexander2015od; @toole2015travel_demand]",
    "10": "[@blumenstock2015poverty; @steele2017poverty]",
    "11": "[@aiken2022machine_learning]",
    "12": "[@worldbank2021novissi]",
    "13": "[@gpsdd2025roadmap]",
    "14": "[@flowminder2023bias; @wesolowski2013biases; @ricciato2020present_population]",
    "16": "[@wesolowski2013biases; @cabrera_rowe2025bias]",
    "17": "[@flowminder2023standards]",
    "18": "[@ess2019qaf]",
    "19": "[@ascari2024quality]",
    "20": "[@itu_academy_data_governance; @flowgeek_data_governance]",
    "21": "[@gdpr_eu]",
    "22": "[@jansen2021publictrust; @un2014fundamental_principles]",
    "23": "[@locus_charter]",
    "24": "[@gsma2016mobileprivacy]",
}


INLINE_FOOTNOTES = {
    "15": "^[Substituting the identifier through pseudonymisation protects identity by stripping out easily identifiable data such as a telephone number. Maintaining a stable pseudonymised identifier can still enable longitudinal analysis where this is lawful, necessary, and appropriately governed.]",
}


SPLIT_FILES = {
    "Preface": "index.qmd",
    "Acknowledgements": "chapters/acknowledgements.qmd",
    "Glossary of Terms and Abbreviations": "chapters/glossary.qmd",
    "Chapter 1: Planning a Mobile Phone Data Initiative": "chapters/01-planning.qmd",
    "Chapter 2: Policy Applications for Mobile Phone Data": "chapters/02-policy-applications.qmd",
    "Chapter 3: Arranging Partnerships and Data Access": "chapters/03-partnerships-data-access.qmd",
    "Chapter 4: Data Processing and Data Pipelines for Mobile Phone Data Initiatives": "chapters/04-data-processing-pipelines.qmd",
    "Chapter 5: Data Quality and Characteristics": "chapters/05-data-quality-characteristics.qmd",
    "Chapter 6: Data Governance and Safeguards in MPD Initiatives": "chapters/06-data-governance-safeguards.qmd",
    "Chapter 7: Managing the Communications Aspects of Mobile Phone Data Initiatives": "chapters/07-communications.qmd",
    "Appendix 1: Further recommended resources": "chapters/appendix-resources.qmd",
}


FRONT_MATTER_SECTIONS = {
    "Preface",
    "Acknowledgements",
    "Glossary of Terms and Abbreviations",
}


TITLE_REPLACEMENTS = {
    "Chapter 5: Data quality and characteristics": "Chapter 5: Data Quality and Characteristics",
    "Chapter 6: Data Governance and Safeguards in MPD initiatives": "Chapter 6: Data Governance and Safeguards in MPD Initiatives",
}


INDEX_INTRO = ""


PROJECT_STATUS_CALLOUT = """

::: {.content-visible when-format="html"}
<div class="manual-cover-wrap">
  <img class="manual-cover" src="assets/manual-cover.png" alt="Cover of Design and Implementation of Mobile Phone Data Initiatives: A Practical Manual" />
</div>
:::

::: {.callout-note icon="false"}
## Project status

Publisher/imprint wording, licence, and DOI are TBC. The public website is configured for GitHub Pages at <https://un-cebd-mobile-data.github.io/mobile-phone-data-handbook/>.
:::

"""


AUTHORS_PREFACE = """

## Authors {.unnumbered}

Cathy Riley, Francisco Rowe, Esperanza Magpantay, Robert Eyre, Sophie Delaporte, James Harrison, Roland Hosner, Veronique Lefebvre, Thomas Smallwood, Luisa Chavez, Pablo Ruiz, Maria Henar Sales, Miguel Picornell, Egle Rüütli, Kaisa Vent, Siim Esko, Erki Saluveer, Ayumi Arai, Paul Blanchard, Sveta Milusheva, and Trevor Monroe.

"""


RECOMMENDED_CITATION = """

## Recommended citation {.unnumbered}

::: {.callout-note icon="false"}

Riley, C., Rowe, F., Magpantay, E., Eyre, R., Delaporte, S., Harrison, J., Hosner, R., Lefebvre, V., Smallwood, T., Chavez, L., Ruiz, P., Sales, M. H., Picornell, M., Rüütli, E., Vent, K., Esko, S., Saluveer, E., Arai, A., Blanchard, P., Milusheva, S., & Monroe, T. (2026). *Design and Implementation of Mobile Phone Data Initiatives: A Practical Manual*. Publisher/imprint TBC. Licence TBC. DOI TBC. <https://un-cebd-mobile-data.github.io/mobile-phone-data-handbook/>

:::
"""


REFERENCES_QMD = """# References {.unnumbered}

::: {#refs}
:::
"""


BIBTEX = r"""
@book{unstats2019mpdhandbook,
  title = {Handbook on the Use of Mobile Phone Data for Official Statistics},
  author = {{United Nations Statistics Division}},
  year = {2019},
  publisher = {United Nations},
  url = {https://unstats.un.org/bigdata/task-teams/mobile-phone/MPD%20Handbook%2020191004.pdf}
}

@article{blondel2015survey,
  title = {A survey of results on mobile phone datasets analysis},
  author = {Blondel, Vincent D. and Decuyper, Adeline and Krings, Gautier},
  journal = {EPJ Data Science},
  volume = {4},
  number = {10},
  year = {2015},
  doi = {10.1140/epjds/s13688-015-0046-0},
  url = {https://link.springer.com/article/10.1140/epjds/s13688-015-0046-0}
}

@article{gonzalez2008human_mobility,
  title = {Understanding individual human mobility patterns},
  author = {Gonzalez, Marta C. and Hidalgo, Cesar A. and Barabasi, Albert-Laszlo},
  journal = {Nature},
  volume = {453},
  number = {7196},
  pages = {779--782},
  year = {2008},
  doi = {10.1038/nature06958},
  url = {https://doi.org/10.1038/nature06958}
}

@article{song2010predictability,
  title = {Limits of predictability in human mobility},
  author = {Song, Chaoming and Qu, Zehui and Blumm, Nicholas and Barabasi, Albert-Laszlo},
  journal = {Science},
  volume = {327},
  number = {5968},
  pages = {1018--1021},
  year = {2010},
  doi = {10.1126/science.1177170},
  url = {https://doi.org/10.1126/science.1177170}
}

@article{deville2014dynamic_population,
  title = {Dynamic population mapping using mobile phone data},
  author = {Deville, Pierre and Linard, Catherine and Martin, Samuel and Gilbert, Marius and Stevens, Forrest R. and Gaughan, Andrea E. and Blondel, Vincent D. and Tatem, Andrew J.},
  journal = {Proceedings of the National Academy of Sciences},
  volume = {111},
  number = {45},
  pages = {15888--15893},
  year = {2014},
  doi = {10.1073/pnas.1408439111},
  url = {https://doi.org/10.1073/pnas.1408439111}
}

@article{lu2012haiti_displacement,
  title = {Predictability of population displacement after the 2010 Haiti earthquake},
  author = {Lu, Xin and Bengtsson, Linus and Holme, Petter},
  journal = {Proceedings of the National Academy of Sciences},
  volume = {109},
  number = {29},
  pages = {11576--11581},
  year = {2012},
  doi = {10.1073/pnas.1203882109},
  url = {https://doi.org/10.1073/pnas.1203882109}
}

@article{demontjoye2013unique,
  title = {Unique in the Crowd: The privacy bounds of human mobility},
  author = {de Montjoye, Yves-Alexandre and Hidalgo, Cesar A. and Verleysen, Michel and Blondel, Vincent D.},
  journal = {Scientific Reports},
  volume = {3},
  pages = {1376},
  year = {2013},
  doi = {10.1038/srep01376},
  url = {https://doi.org/10.1038/srep01376}
}

@article{demontjoye2018privacy,
  title = {On the privacy-conscientious use of mobile phone data},
  author = {de Montjoye, Yves-Alexandre and Gambs, Sebastien and Blondel, Vincent D. and others},
  journal = {Scientific Data},
  volume = {5},
  pages = {180286},
  year = {2018},
  doi = {10.1038/sdata.2018.286},
  url = {https://doi.org/10.1038/sdata.2018.286}
}

@misc{gsma2016mobileprivacy,
  title = {Mobile Privacy Principles},
  author = {{GSMA}},
  year = {2016},
  url = {https://www.gsma.com/solutions-and-impact/connectivity-for-good/public-policy/gsma_resources/mobile-privacy-principles/}
}

@misc{uncebd_information_society,
  title = {Methodological Guide on the Use of Mobile Phone Data: Measuring the Information Society},
  author = {{UN-CEBD Task Team on Mobile Phone Data}},
  year = {n.d.},
  publisher = {United Nations Statistics Division},
  url = {https://unstats.un.org/wiki/spaces/MPDMIS/overview}
}

@misc{uncebd_mobile_phone_task_team,
  title = {Task Team on Mobile Phone Data},
  author = {{United Nations Committee of Experts on Big Data and Data Science for Official Statistics}},
  year = {n.d.},
  url = {https://unstats.un.org/bigdata/task-teams/mobile-phone/}
}

@misc{itu_sdg_case_study,
  title = {Big Data for Measuring the Information Society},
  author = {{International Telecommunication Union}},
  year = {n.d.},
  url = {https://www.itu.int/en/ITU-D/Statistics/Documents/bigdata/ITU_SDG_case_study.pdf}
}

@misc{uncebd_dynamic_population,
  title = {Methodological Guide on the Use of Mobile Phone Data: Dynamic Population Mapping},
  author = {{UN-CEBD Task Team on Mobile Phone Data}},
  year = {n.d.},
  publisher = {United Nations Statistics Division},
  url = {https://unstats.un.org/wiki/spaces/MPDDPM/overview}
}

@misc{uncebd_disaster_statistics,
  title = {Methodological Guide on the Use of Mobile Phone Data: Displacement and Disaster Statistics},
  author = {{UN-CEBD Task Team on Mobile Phone Data}},
  year = {n.d.},
  publisher = {United Nations Statistics Division},
  url = {https://unstats.un.org/wiki/spaces/MPDDS/overview}
}

@misc{uncebd_migration_statistics,
  title = {Methodological Guide on the Use of Mobile Phone Data: Migration Statistics},
  author = {Rowe, F. and Magpantay, E. and Jalagonia, M. and Esko, S. and De Jesus, E. and Jansen, R. and Grum, F. and Blanchard, P. and Lumala, L.},
  year = {2022},
  publisher = {United Nations Statistics Division; UN-CEBD Task Team on Mobile Phone Data},
  url = {https://unstats.un.org/wiki/spaces/MPDMS/overview}
}

@misc{uncebd_tourism_statistics,
  title = {Methodological Guide on the Use of Mobile Phone Data: Tourism Statistics},
  author = {{UN-CEBD Task Team on Mobile Phone Data}},
  year = {n.d.},
  publisher = {United Nations Statistics Division},
  url = {https://unstats.un.org/wiki/display/MPDTS}
}

@article{caceres2007origin_destination,
  title = {Deriving origin-destination data from a mobile phone network},
  author = {Caceres, N. and Wideberg, J. P. and Benitez, F. G.},
  journal = {IET Intelligent Transport Systems},
  volume = {1},
  number = {1},
  pages = {15--26},
  year = {2007},
  doi = {10.1049/iet-its:20060020},
  url = {https://digital-library.theiet.org/doi/10.1049/iet-its%3A20060020}
}

@article{calabrese2011od,
  title = {Estimating origin-destination flows using mobile phone location data},
  author = {Calabrese, Francesco and Di Lorenzo, Giusy and Liu, Liang and Ratti, Carlo},
  journal = {IEEE Pervasive Computing},
  volume = {10},
  number = {4},
  pages = {36--44},
  year = {2011},
  doi = {10.1109/MPRV.2011.41},
  url = {https://doi.org/10.1109/MPRV.2011.41}
}

@article{alexander2015od,
  title = {Origin-destination trips by purpose and time of day inferred from mobile phone data},
  author = {Alexander, Lauren and Jiang, Shan and Murga, Mikel and Gonzalez, Marta C.},
  journal = {Transportation Research Part C: Emerging Technologies},
  volume = {58},
  pages = {240--250},
  year = {2015},
  doi = {10.1016/j.trc.2015.02.018},
  url = {https://doi.org/10.1016/j.trc.2015.02.018}
}

@article{toole2015travel_demand,
  title = {The path most traveled: Travel demand estimation using big data resources},
  author = {Toole, Jameson L. and Colak, Serdar and Sturt, Bradley and Alexander, Lauren P. and Evsukoff, Alexandre and Gonzalez, Marta C.},
  journal = {Transportation Research Part C: Emerging Technologies},
  volume = {58},
  pages = {162--177},
  year = {2015},
  doi = {10.1016/j.trc.2015.04.022},
  url = {https://doi.org/10.1016/j.trc.2015.04.022}
}

@article{ahas2008tourism,
  title = {Evaluating passive mobile positioning data for tourism surveys: An Estonian case study},
  author = {Ahas, Rein and Aasa, Anto and Roose, Antti and Mark, Ülar and Silm, Siiri},
  journal = {Tourism Management},
  volume = {29},
  number = {3},
  pages = {469--486},
  year = {2008},
  doi = {10.1016/j.tourman.2007.05.014},
  url = {https://doi.org/10.1016/j.tourman.2007.05.014}
}

@article{blumenstock2015poverty,
  title = {Predicting poverty and wealth from mobile phone metadata},
  author = {Blumenstock, Joshua and Cadamuro, Gabriel and On, Robert},
  journal = {Science},
  volume = {350},
  number = {6264},
  pages = {1073--1076},
  year = {2015},
  doi = {10.1126/science.aac4420},
  url = {https://www.science.org/doi/10.1126/science.aac4420}
}

@article{steele2017poverty,
  title = {Mapping poverty using mobile phone and satellite data},
  author = {Steele, Jessica E. and Sundsoy, Pal Roe and Pezzulo, Carla and Alegana, Victor A. and Bird, Tomas J. and Blumenstock, Joshua and Bjelland, Johannes and Engo-Monsen, Kenth and de Montjoye, Yves-Alexandre and Iqbal, Asif M. and Hadiuzzaman, Khandakar N. and Lu, Xin and Wetter, Erik and Tatem, Andrew J. and Bengtsson, Linus},
  journal = {Journal of the Royal Society Interface},
  volume = {14},
  number = {127},
  pages = {20160690},
  year = {2017},
  doi = {10.1098/rsif.2016.0690},
  url = {https://doi.org/10.1098/rsif.2016.0690}
}

@article{eagle2010network_diversity,
  title = {Network diversity and economic development},
  author = {Eagle, Nathan and Macy, Michael and Claxton, Rob},
  journal = {Science},
  volume = {328},
  number = {5981},
  pages = {1029--1031},
  year = {2010},
  doi = {10.1126/science.1186605},
  url = {https://doi.org/10.1126/science.1186605}
}

@article{aiken2022machine_learning,
  title = {Machine learning and phone data can improve targeting of humanitarian aid},
  author = {Aiken, Emily and Bedoya, Guadalupe and Blumenstock, Joshua and Coville, Aidan},
  journal = {Nature},
  volume = {603},
  pages = {864--870},
  year = {2022},
  doi = {10.1038/s41586-022-04484-9},
  url = {https://www.nature.com/articles/s41586-022-04484-9}
}

@misc{worldbank2021novissi,
  title = {Togo's Novissi Platform for Social Protection Uses Machine Learning, Mobile Money, and Satellite Data to Support the Most Vulnerable},
  author = {{World Bank}},
  year = {2021},
  url = {https://www.worldbank.org/en/results/2021/04/13/prioritizing-the-poorest-and-most-vulnerable-in-west-africa-togo-s-novissi-platform-for-social-protection-uses-machine-l}
}

@misc{gpsdd2025roadmap,
  title = {A Roadmap to Accessing Mobile Network Data for Statistics},
  author = {{Global Partnership for Sustainable Development Data} and {Positium}},
  year = {2025},
  url = {https://www.data4sdgs.org/roadmap-accessing-mobile-network-data-statistics}
}

@misc{gsma2019bigdata,
  title = {Big Data for Social Good: Mobile Network Operator Data Sharing},
  author = {{GSMA}},
  year = {2019},
  url = {https://www.gsma.com/solutions-and-impact/connectivity-for-good/external-affairs/wp-content/uploads/2019/09/Big-Data-AI-Ethics_web.pdf}
}

@misc{flowminder2023standards,
  title = {Flowminder standards in producing mobility and population estimates from call detail records in low- and middle-income countries},
  author = {{Flowminder Foundation}},
  year = {2023},
  url = {https://www.flowminder.org/resources/publications-reports/flowminder-standards-in-producing-mobility-and-population-estimates-from-call-details-records-in-low-and-middle-income-countries}
}

@misc{flowminder2023bias,
  title = {Correcting measurement biases in the detection of long and short stay locations in sparse Call Detail Records},
  author = {{Flowminder Foundation}},
  year = {2023},
  url = {https://www.flowminder.org/resources/publications-reports/correcting-measurement-biases-in-the-detection-of-long-and-short-stay-locations-in-sparse-call-detail-records-cdrs}
}

@article{wesolowski2013biases,
  title = {The impact of biases in mobile phone ownership on estimates of human mobility},
  author = {Wesolowski, Amy and Eagle, Nathan and Tatem, Andrew J. and Smith, David L. and Noor, Abdisalan M. and Snow, Robert W. and Buckee, Caroline O.},
  journal = {Journal of the Royal Society Interface},
  volume = {10},
  number = {81},
  pages = {20120986},
  year = {2013},
  doi = {10.1098/rsif.2012.0986}
}

@article{wesolowski2012malaria,
  title = {Quantifying the impact of human mobility on malaria},
  author = {Wesolowski, Amy and Eagle, Nathan and Tatem, Andrew J. and Smith, David L. and Noor, Abdisalan M. and Snow, Robert W. and Buckee, Caroline O.},
  journal = {Science},
  volume = {338},
  number = {6104},
  pages = {267--270},
  year = {2012},
  doi = {10.1126/science.1223467},
  url = {https://doi.org/10.1126/science.1223467}
}

@article{bengtsson2015cholera,
  title = {Using mobile phone data to predict the spatial spread of cholera},
  author = {Bengtsson, Linus and Gaudart, Jean and Lu, Xin and Moore, Sandra and Wetter, Erik and Sallah, Kankoe and Rebaudet, Stanislas and Piarroux, Renaud},
  journal = {Scientific Reports},
  volume = {5},
  pages = {8923},
  year = {2015},
  doi = {10.1038/srep08923},
  url = {https://www.nature.com/articles/srep08923}
}

@article{tizzoni2014epidemics,
  title = {On the Use of Human Mobility Proxies for Modeling Epidemics},
  author = {Tizzoni, Michele and Bajardi, Paolo and Decuyper, Adeline and Kon Kam King, Guillaume and Schneider, Christian M. and Blondel, Vincent D. and Smoreda, Zbigniew and Gonzalez, Marta C. and Colizza, Vittoria},
  journal = {PLOS Computational Biology},
  volume = {10},
  number = {7},
  pages = {e1003716},
  year = {2014},
  doi = {10.1371/journal.pcbi.1003716},
  url = {https://doi.org/10.1371/journal.pcbi.1003716}
}

@article{ricciato2020present_population,
  title = {Towards a methodological framework for estimating present population density from mobile network operator data},
  author = {Ricciato, Fabio and Lanzieri, Giampaolo and Wirthmann, Albrecht and Seynaeve, Gerdy},
  journal = {Pervasive and Mobile Computing},
  volume = {68},
  pages = {101263},
  year = {2020},
  doi = {10.1016/j.pmcj.2020.101263},
  url = {https://doi.org/10.1016/j.pmcj.2020.101263}
}

@article{salgado2021end_to_end,
  title = {An end-to-end statistical process with mobile network data for official statistics},
  author = {Salgado, David and Sanguiao, Luis and Oancea, Bogdan and Barragan, Sandra and Necula, Marian},
  journal = {EPJ Data Science},
  volume = {10},
  number = {20},
  year = {2021},
  doi = {10.1140/epjds/s13688-021-00275-w},
  url = {https://doi.org/10.1140/epjds/s13688-021-00275-w}
}

@inproceedings{isaacman2011important_places,
  title = {Identifying important places in people's lives from cellular network data},
  author = {Isaacman, Sibren and Becker, Richard and Caceres, Ramon and Kobourov, Stephen and Martonosi, Margaret and Rowland, James and Varshavsky, Alexander},
  booktitle = {Pervasive Computing},
  series = {Lecture Notes in Computer Science},
  volume = {6696},
  pages = {133--151},
  year = {2011},
  publisher = {Springer},
  doi = {10.1007/978-3-642-21726-5_9},
  url = {https://doi.org/10.1007/978-3-642-21726-5_9}
}

@article{li2021ghana_cdr,
  title = {Analysis of call detail records to inform the COVID-19 response in Ghana: Opportunities and challenges},
  author = {Li, Tong and Bowers, Cordelia and Seidu, Alhassan and Akoto-Bamfo, Gloria and Ofori-Boateng, Daniel and others},
  journal = {Data \& Policy},
  volume = {3},
  pages = {E11},
  year = {2021},
  doi = {10.1017/dap.2021.5},
  url = {https://doi.org/10.1017/dap.2021.5}
}

@misc{ess2019qaf,
  title = {Quality Assurance Framework of the European Statistical System, Version 2.0},
  author = {{European Statistical System}},
  year = {2019},
  url = {https://ec.europa.eu/eurostat/documents/64157/4392716/ESS-QAF-V1-2final.pdf/bbf5970c-1adf-46c8-afc3-58ce177a0646}
}

@inproceedings{ascari2024quality,
  title = {Quality aspects using Mobile Network Operators data for Official Statistics},
  author = {Ascari, G. and Cerasti, E. and Faricelli, C. and Mattera, P. and Piombo, S. and Radini, R. and Simeoni, G. and Tuoto, T.},
  booktitle = {2nd Workshop on Methodologies for Official Statistics: Proceedings},
  pages = {135--151},
  publisher = {Istituto Nazionale di Statistica},
  address = {Rome},
  year = {2024},
  url = {https://www.istat.it/wp-content/uploads/2024/11/2nd-Workshop-on-methodologies-for-official-statistics-Proceedings-1.pdf}
}

@misc{itu_academy_data_governance,
  title = {ITU Academy},
  author = {{International Telecommunication Union}},
  year = {n.d.},
  url = {https://academy.itu.int/}
}

@misc{flowgeek_data_governance,
  title = {Data Governance and Data Privacy for Mobile Phone Data},
  author = {{FlowGeek}},
  year = {n.d.},
  url = {https://flowgeek.org/}
}

@misc{gdpr_eu,
  title = {General Data Protection Regulation Compliance Overview},
  author = {{GDPR.eu}},
  year = {n.d.},
  url = {https://gdpr.eu/}
}

@article{jansen2021publictrust,
  title = {Guiding principles to maintain public trust in the use of mobile operator data for policy purposes},
  author = {Jansen, Ronald and Abels, Miglena and Papadakis, Savvas and Sakarovitch, Benjamin and others},
  journal = {Data \& Policy},
  volume = {3},
  pages = {E24},
  year = {2021},
  doi = {10.1017/dap.2021.21}
}

@misc{un2014fundamental_principles,
  title = {Fundamental Principles of Official Statistics},
  author = {{United Nations}},
  year = {2014},
  url = {https://unstats.un.org/unsd/dnss/gp/fundprinciples.aspx}
}

@misc{locus_charter,
  title = {The Locus Charter},
  author = {{Benchmark Initiative}},
  year = {2021},
  url = {https://ethicalgeo.org/locus-charter/}
}

@misc{african_union2018malabo,
  title = {African Union Convention on Cyber Security and Personal Data Protection},
  author = {{African Union}},
  year = {2018},
  url = {https://au.int/en/treaties/african-union-convention-cyber-security-and-personal-data-protection}
}

@article{rowe2022digitalfootprint,
  title = {Using digital footprint data to monitor human mobility and support rapid humanitarian responses},
  author = {Rowe, Francisco},
  journal = {Regional Studies, Regional Science},
  year = {2022},
  doi = {10.1080/21681376.2022.2135458},
  url = {https://doi.org/10.1080/21681376.2022.2135458}
}

@misc{rowe2024,
  title = {Digital Data and Population Studies},
  author = {Rowe, Francisco and {González-Leonardo}, Miguel},
  year = {2024},
  month = {10},
  date = {2024-10-15},
  url = {http://dx.doi.org/10.31219/osf.io/jb3e5}
}

@article{iradukunda_rowe_pietrostefani2025ukraine,
  title = {Estimating internal displacement in Ukraine from high-frequency GPS mobile phone data},
  author = {Iradukunda, Rodgers and Rowe, Francisco and Pietrostefani, Elisabetta},
  journal = {Humanities and Social Sciences Communications},
  year = {2025},
  doi = {10.1057/s41599-025-06137-4},
  url = {https://doi.org/10.1057/s41599-025-06137-4}
}

@misc{pietrostefani2025dynamic_displacement,
  title = {Dynamic Estimates of Displacement in Disaster Regions: A Policy-driven framework triangulating data},
  author = {Pietrostefani, Elisabetta and Mason, Matt and Iradukunda, Rodgers and Tran-Jones, Hong and Loktieva, Iryna and Rowe, Francisco},
  year = {2025},
  eprint = {2511.01955},
  archivePrefix = {arXiv},
  doi = {10.48550/arXiv.2511.01955},
  url = {https://arxiv.org/abs/2511.01955}
}

@misc{cabrera_rowe2025bias,
  title = {A systematic machine learning approach to measure and assess biases in mobile phone population data},
  author = {Cabrera, Carmen and Rowe, Francisco},
  year = {2025},
  eprint = {2509.02603},
  archivePrefix = {arXiv},
  doi = {10.48550/arXiv.2509.02603},
  url = {https://arxiv.org/abs/2509.02603}
}

@article{rowe2023urban_exodus,
  title = {Urban exodus? Understanding human mobility in Britain during the COVID-19 pandemic using Meta-Facebook data},
  author = {Rowe, Francisco and Calafiore, Alessia and Arribas-Bel, Daniel and Samardzhiev, Konstantin and Fleischmann, Martin},
  journal = {Population, Space and Place},
  year = {2023},
  doi = {10.1002/psp.2637},
  url = {https://doi.org/10.1002/psp.2637}
}

@misc{cabrera2025latin_america_mobility,
  title = {Sustained changes to urban mobility after COVID-19 amplified socio-economic inequalities in Latin America},
  author = {Cabrera, Carmen and others},
  year = {2025},
  eprint = {2504.15871},
  archivePrefix = {arXiv},
  doi = {10.48550/arXiv.2504.15871},
  url = {https://arxiv.org/abs/2504.15871}
}

@article{barreras2024,
  title = {The exciting potential and daunting challenge of using GPS human-mobility data for epidemic modeling},
  author = {Barreras, Francisco and Watts, Duncan J.},
  year = {2024},
  month = {06},
  date = {2024-06-19},
  journal = {Nature Computational Science},
  pages = {398--411},
  volume = {4},
  number = {6},
  doi = {10.1038/s43588-024-00637-0},
  url = {http://dx.doi.org/10.1038/s43588-024-00637-0},
  langid = {en}
}

@article{louail2014spatial_structure,
  title = {From mobile phone data to the spatial structure of cities},
  author = {Louail, Thomas and Lenormand, Maxime and Cantu Ros, Oliva G. and Picornell, Miguel and Herranz, Ricardo and Frias-Martinez, Enrique and Ramasco, Jose J. and Barthelemy, Marc},
  journal = {Scientific Reports},
  volume = {4},
  pages = {5276},
  year = {2014},
  doi = {10.1038/srep05276},
  url = {https://doi.org/10.1038/srep05276}
}

@misc{mpd_crossborder_flows_2025,
  title = {Mobile Phone Data for Cross-border Population \& Expenditure Flows: Ideas \& Challenges},
  year = {2025},
  date = {2025-05-14},
  type = {Presentation},
  howpublished = {Workshop: Measurement of the flows across the internal borders of the European Union},
  abstract = {This workshop talk discusses the use of mobile phone data to estimate cross-border population and expenditure flows across internal European Union borders, focusing on methodological opportunities and practical challenges for robust measurement.}
}
"""


QUARTO_YML = """project:
  type: book
  output-dir: _book

book:
  title: "Design and Implementation of Mobile Phone Data Initiatives"
  subtitle: "A Practical Manual"
  reader-mode: true
  author:
    - "Cathy Riley"
    - "Francisco Rowe"
    - "Esperanza Magpantay"
    - "Robert Eyre"
    - "Sophie Delaporte"
    - "James Harrison"
    - "Roland Hosner"
    - "Veronique Lefebvre"
    - "Thomas Smallwood"
    - "Luisa Chavez"
    - "Pablo Ruiz"
    - "Maria Henar Sales"
    - "Miguel Picornell"
    - "Egle Rüütli"
    - "Kaisa Vent"
    - "Siim Esko"
    - "Erki Saluveer"
    - "Ayumi Arai"
    - "Paul Blanchard"
    - "Sveta Milusheva"
    - "Trevor Monroe"
  date: "2026-05-26"
  publisher: "TBC"
  edition: "Version 1.4"
  license: "TBC"
  site-url: "https://un-cebd-mobile-data.github.io/mobile-phone-data-handbook/"
  repo-url: "https://github.com/un-cebd-mobile-data/mobile-phone-data-handbook"
  repo-branch: main
  repo-actions: [edit, issue]
  downloads: [pdf, epub]
  favicon: assets/un-cebd-logo.png
  page-footer:
    left: |
      UN-CEBD Mobile Phone Data Task Team | Publisher/imprint TBC | Licence TBC
    right: |
      Built with <a href="https://quarto.org/">Quarto</a>.
  chapters:
    - index.qmd
    - chapters/acknowledgements.qmd
    - chapters/glossary.qmd
    - chapters/01-planning.qmd
    - chapters/02-policy-applications.qmd
    - chapters/03-partnerships-data-access.qmd
    - chapters/04-data-processing-pipelines.qmd
    - chapters/05-data-quality-characteristics.qmd
    - chapters/06-data-governance-safeguards.qmd
    - chapters/07-communications.qmd
  appendices:
    - chapters/appendix-resources.qmd
    - chapters/references.qmd

bibliography: references.bib
link-citations: true
description: "A practical manual for designing and implementing mobile phone data initiatives."

format:
  html:
    theme:
      light:
        - cosmo
        - style/theme.scss
      dark:
        - darkly
        - style/dark.scss
    toc: true
    toc-depth: 3
    number-sections: true
    number-depth: 3
    code-copy: true
    include-in-header:
      text: |
        <script>
          document.addEventListener("DOMContentLoaded", function() {
            const sidebar = document.getElementById("quarto-sidebar");
            if (!sidebar || sidebar.querySelector(".un-cebd-sidebar-logo")) return;
            const anchor = document.createElement("a");
            anchor.className = "un-cebd-sidebar-logo";
            anchor.href = "https://unstats.un.org/bigdata/";
            anchor.setAttribute("aria-label", "UN Committee of Experts on Big Data and Data Science for Official Statistics");
            const image = document.createElement("img");
            const offset = document.querySelector('meta[name="quarto:offset"]')?.getAttribute("content") || "./";
            image.src = offset + "assets/un-cebd-logo.png";
            image.alt = "UN Committee of Experts on Big Data and Data Science for Official Statistics";
            anchor.appendChild(image);
            sidebar.prepend(anchor);
          });
        </script>
  pdf:
    documentclass: scrreprt
    papersize: a4
    pdf-engine: xelatex
    toc: true
    number-sections: true
    number-depth: 3
    colorlinks: true
    include-in-header: style/pdf-preamble.tex
    include-before-body: style/pdf-before-body.tex
  epub:
    toc: true
    number-sections: true
    number-depth: 3
    cover-image: assets/manual-cover.png

editor: visual
"""


THEME_SCSS = """/*-- scss:defaults --*/
$body-bg: #ffffff;
$body-color: #2C3E50;
$link-color: #0077a8;
$primary: #009edb;
$secondary: #3398dc;
$success: #18ba9b;
$info: #00bed6;
$warning: #e57d20;
$danger: #a10f2b;
$light: #f7f7f7;
$dark: #2C3E50;
$font-family-sans-serif: "Open Sans", "Source Sans Pro", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
$font-family-monospace: "Fira Code", "SFMono-Regular", Consolas, "Liberation Mono", monospace;
$headings-color: #1f3143;
$sidebar-bg: #f7f7f7;
$toc-color: #2C3E50;
$toc-active-border: #009edb;
$callout-color-note: #009edb;
$callout-color-tip: #18ba9b;
$callout-color-warning: #e57d20;
$callout-color-important: #a10f2b;
$callout-color-caution: #e57d20;

/*-- scss:rules --*/
.un-cebd-sidebar-logo {
  display: block;
  padding: 0.75rem 1rem 1rem;
  border-bottom: 1px solid rgba(44, 62, 80, 0.12);
  margin-bottom: 0.5rem;
}

.un-cebd-sidebar-logo img {
  display: block;
  max-width: 100%;
  height: auto;
}

.manual-cover-wrap {
  margin: 0 0 1.75rem;
}

.manual-cover {
  display: block;
  width: min(420px, 100%);
  height: auto;
  border: 1px solid rgba(44, 62, 80, 0.14);
  box-shadow: 0 18px 36px rgba(31, 49, 67, 0.18);
}

.navbar,
.quarto-title-banner {
  background: #009edb;
}

.sidebar-title {
  color: #2C3E50;
  font-weight: 700;
}

h1,
h2,
h3 {
  letter-spacing: 0;
}

h1.title {
  max-width: 18ch;
}

.subtitle {
  color: #585f69;
}

.callout {
  border-radius: 4px;
}

.callout.callout-style-default > .callout-header {
  background-color: rgba(0, 158, 219, 0.08);
}

table {
  font-size: 0.92rem;
}

caption,
figcaption {
  color: #585f69;
}

.chapter-number,
.header-section-number {
  color: #0077a8;
}

#quarto-sidebar .menu-text > .chapter-number {
  display: none;
}

#quarto-sidebar .menu-text > .chapter-number + .chapter-title {
  margin-left: -0.28em;
}

.quarto-title .chapter-number {
  display: none;
}

.quarto-title .chapter-number + .chapter-title {
  margin-left: -0.28em;
}

.quarto-appendix-heading {
  color: #2C3E50;
}
"""


DARK_SCSS = """/*-- scss:defaults --*/
$body-bg: #172433;
$body-color: #edf2f8;
$link-color: #6ecff6;
$primary: #00bed6;
$secondary: #3398dc;
$success: #18ba9b;
$info: #009edb;
$warning: #ffb45f;
$danger: #ff8f8f;
$light: #24384a;
$dark: #0f1b26;
$font-family-sans-serif: "Open Sans", "Source Sans Pro", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
$font-family-monospace: "Fira Code", "SFMono-Regular", Consolas, "Liberation Mono", monospace;
$headings-color: #ffffff;
$sidebar-bg: #0f1b26;
$toc-color: #edf2f8;
$toc-active-border: #00bed6;

/*-- scss:rules --*/
.un-cebd-sidebar-logo {
  display: block;
  padding: 0.75rem 1rem 1rem;
  border-bottom: 1px solid rgba(237, 242, 248, 0.16);
  margin-bottom: 0.5rem;
  background: #ffffff;
}

.un-cebd-sidebar-logo img {
  display: block;
  max-width: 100%;
  height: auto;
}

.manual-cover-wrap {
  margin: 0 0 1.75rem;
}

.manual-cover {
  display: block;
  width: min(420px, 100%);
  height: auto;
  border: 1px solid rgba(237, 242, 248, 0.18);
  box-shadow: 0 18px 36px rgba(0, 0, 0, 0.35);
}

.navbar,
.quarto-title-banner {
  background: #0f1b26;
}

.sidebar-title,
h1,
h2,
h3 {
  color: #ffffff;
  letter-spacing: 0;
}

.subtitle,
caption,
figcaption {
  color: #d6e2ee;
}

.chapter-number,
.header-section-number {
  color: #6ecff6;
}

#quarto-sidebar .menu-text > .chapter-number {
  display: none;
}

#quarto-sidebar .menu-text > .chapter-number + .chapter-title {
  margin-left: -0.28em;
}
"""


README = """# Design and Implementation of Mobile Phone Data Initiatives

This repository contains the Quarto website book for *Design and Implementation of Mobile Phone Data Initiatives: A Practical Manual* by Cathy Riley, Francisco Rowe, Esperanza Magpantay, Robert Eyre, Sophie Delaporte, James Harrison, Roland Hosner, Veronique Lefebvre, Thomas Smallwood, Luisa Chavez, Pablo Ruiz, Maria Henar Sales, Miguel Picornell, Egle Rüütli, Kaisa Vent, Siim Esko, Erki Saluveer, Ayumi Arai, Paul Blanchard, Sveta Milusheva, and Trevor Monroe.

Public site target: <https://un-cebd-mobile-data.github.io/mobile-phone-data-handbook/>

## Status

- Licence: TBC
- Publisher/imprint wording: TBC
- DOI: TBC
- Deployment: GitHub Pages
- Outputs: HTML website, PDF, EPUB

## Local preview

```bash
quarto preview
```

## Render all outputs

```bash
quarto render
```

To render individual formats:

```bash
quarto render --to html
quarto render --to pdf
quarto render --to epub
```

HTML output is written to `_book/`. PDF and EPUB outputs are generated by Quarto inside the rendered book output.

## Deployment

The GitHub Actions workflow in `.github/workflows/publish.yml` renders the book and deploys `_book/` to GitHub Pages.

In the GitHub repository settings, set **Pages** source to **GitHub Actions**.

## Logo assets

The site uses the official UN-CEBD logo downloaded from the UN Big Data website:

<https://unstats.un.org/bigdata/assets/img/logo/logo_2021_long.png>

Logo usage is assumed to be appropriate for this UN-CEBD task-team manual, but final branding approval should be confirmed.
"""


PUBLISH_YML = """name: Publish Quarto Book

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2

      - name: Set up TinyTeX
        uses: r-lib/actions/setup-tinytex@v2

      - name: Render book
        uses: quarto-dev/quarto-actions/render@v2

      - name: Upload GitHub Pages artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: _book

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
"""


GITIGNORE = """_book/
.quarto/
site_libs/

index.aux
index.html
index.log
index.out
index.pdf
index.tex
index.toc
*.log
*.docx
/Design-and-Implementation-of-Mobile-Phone-Data-Initiatives.pdf
/Design-and-Implementation-of-Mobile-Phone-Data-Initiatives.epub
chapters/*.html
assets/*-1280x640.png

.Rproj.user/
.Rhistory
.DS_Store

/.quarto/
**/*.quarto_ipynb
"""


def strip_heading_attrs(line: str) -> str:
    return re.sub(r"\s+\{#[^}]+\}\s*$", "", line)


def clean_heading_line(line: str) -> str:
    line = strip_heading_attrs(line.rstrip())
    line = re.sub(r"^(\d+\)\s+)?(#{1,6})\s+\*\*(.*?)\*\*\s*$", r"\2 \3", line)
    line = re.sub(r"^(#{1,6})\s+\*\*(.*?)\*\*\s*$", r"\1 \2", line)
    line = re.sub(r"^(#{2,6})\s+\d+(?:\.\d+)*\.?\s+", r"\1 ", line)
    return line


def convert_single_cell_boxes(lines: list[str]) -> list[str]:
    converted: list[str] = []
    i = 0
    while i < len(lines):
      line = lines[i]
      if line.startswith("| Box ") and i + 1 < len(lines) and re.match(r"^\|\s*:?-{3,}:?\s*\|\s*$", lines[i + 1]):
          text = line.strip().strip("|").strip()
          title, _, body = text.partition("  ")
          if not body:
              title, _, body = text.partition(": ")
              if body:
                  title = title + ":"
          converted.extend([
              f"::: {{.callout-note title=\"{title.strip()}\"}}",
              "",
              body.strip() or text.strip(),
              "",
              ":::",
          ])
          i += 2
          continue
      converted.append(line)
      i += 1
    return converted


PROTECTED_ABBREVIATION_PHRASES = {
    "__MPD_HANDBOOK_TITLE__": "Handbook on the Use of Mobile Phone Data for Official Statistics",
}


def protect_abbreviation_phrases(text: str) -> str:
    for placeholder, phrase in PROTECTED_ABBREVIATION_PHRASES.items():
        text = text.replace(phrase, placeholder)
    return text


def restore_abbreviation_phrases(text: str) -> str:
    for placeholder, phrase in PROTECTED_ABBREVIATION_PHRASES.items():
        text = text.replace(placeholder, phrase)
    return text


def abbreviate_mpd(text: str) -> str:
    text = protect_abbreviation_phrases(text)
    text = re.sub(r"\b[Mm]obile [Pp]hone [Dd]ata\s*\(MPD\)", "MPD", text)
    text = re.sub(r"\b[Mm]obile [Pp]hone [Dd]ata\b", "MPD", text)
    text = restore_abbreviation_phrases(text)
    return text


def abbreviate_cdr(text: str) -> str:
    text = re.sub(r"\b[Cc]all [Dd]etail [Rr]ecords\s*\(CDRs\)", "CDRs", text)
    text = re.sub(r"\b[Cc]all [Dd]etail [Rr]ecords\b", "CDRs", text)
    text = re.sub(r"\b[Cc]all [Dd]etail [Rr]ecord\b", "CDR", text)
    return text


def abbreviate_mno(text: str) -> str:
    text = re.sub(r"\b[Mm]obile [Nn]etwork [Oo]perators\s*\(MNOs\)", "MNOs", text)
    text = re.sub(r"\b[Mm]obile [Nn]etwork [Oo]perator\s*\(MNO\)", "MNO", text)
    text = re.sub(r"\b[Mm]obile [Nn]etwork [Oo]perators\b", "MNOs", text)
    text = re.sub(r"\b[Mm]obile [Nn]etwork [Oo]perator\b", "MNO", text)
    return text.replace("MNO Data", "MNO data")


def abbreviate_nso(text: str) -> str:
    text = re.sub(r"\b[Nn]ational [Ss]tatistical [Oo]ffices\s*\(NSOs\)", "NSOs", text)
    text = re.sub(r"\b[Nn]ational [Ss]tatistical [Oo]ffice\s*\(NSO\)", "NSO", text)
    text = re.sub(r"\b[Nn]ational [Ss]tatistical [Oo]ffices\b", "NSOs", text)
    text = re.sub(r"\b[Nn]ational [Ss]tatistical [Oo]ffice\b", "NSO", text)
    return text


def abbreviate_after_marker(text: str, marker: str, abbreviation_fn) -> str:
    position = text.find(marker)
    if position == -1:
        return abbreviation_fn(text)
    split_at = position + len(marker)
    return text[:split_at] + abbreviation_fn(text[split_at:])


def fix_abbreviation_grammar(text: str) -> str:
    replacements = {
        "The term MNO data or MNO data refers": "MNO data refers",
        "two main types of data MNO data": "two main types of MNO data",
        "MPD are held by private-sector MNOs, are legally sensitive, and are embedded": "MPD is held by private-sector MNOs, is legally sensitive, and is embedded",
        "MPD is held by private-sector MNOs, are legally sensitive, and are embedded": "MPD is held by private-sector MNOs, is legally sensitive, and is embedded",
        "* **National statistical offices:** The NSO normally": "* **National statistical offices (NSOs):** NSOs normally",
        "NSOs normally has": "NSOs normally have",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"\bA MPD\b", "An MPD", text)
    text = re.sub(r"\ba MPD\b", "an MPD", text)
    text = re.sub(r"\bA MNO\b", "An MNO", text)
    text = re.sub(r"\ba MNO\b", "an MNO", text)
    text = re.sub(r"\bA NSO\b", "An NSO", text)
    text = re.sub(r"\ba NSO\b", "an NSO", text)
    return text


def apply_abbreviation_policy(title: str, content: str) -> str:
    if title == "Preface":
        content = abbreviate_after_marker(content, "Mobile Phone Data (MPD)", abbreviate_mpd)
        content = abbreviate_after_marker(content, "Call Detail Records (CDRs)", abbreviate_cdr)
        return fix_abbreviation_grammar(content)

    if title == "Chapter 1: Planning a Mobile Phone Data Initiative":
        content = abbreviate_after_marker(content, "Mobile Phone Data (MPD)", abbreviate_mpd)
        content = abbreviate_after_marker(content, "Mobile Network Operator (MNO)", abbreviate_mno)
        content = abbreviate_cdr(content)
        content = fix_abbreviation_grammar(content)
        content = abbreviate_after_marker(content, "National statistical offices (NSOs)", abbreviate_nso)
        return fix_abbreviation_grammar(content)

    if title.startswith("Chapter "):
        content = abbreviate_mpd(content)
        content = abbreviate_cdr(content)
        content = abbreviate_mno(content)
        content = abbreviate_nso(content)
        return fix_abbreviation_grammar(content)

    return content


def clean_text(text: str) -> str:
    start = text.find("# Preface")
    if start == -1:
        raise RuntimeError("Could not find Preface heading")
    text = text[start:]
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\\-", "-")
    text = text.replace("\\.", ".")
    text = text.replace("\\(", "(")
    text = text.replace("\\)", ")")
    text = text.replace("\\_", "_")
    text = text.replace("objectives..", "objectives.")
    text = text.replace("CRD data", "CDR data")
    text = text.replace("passivelyand", "passively and")
    text = text.replace("as“home”", "as “home”")
    text = text.replace("not explicitly account for", "not explicitly accounted for")
    text = text.replace("multi-dimentional", "multi-dimensional")
    text = text.replace("2024/5", "2024/25")
    text = text.replace("roleplayers", "role players")
    text = text.replace("neighborhood", "neighbourhood")
    text = text.replace("behavior", "behaviour")
    text = text.replace("utilized", "used")
    text = text.replace("anonymized", "anonymised")
    text = text.replace("Anonymized", "Anonymised")
    text = text.replace("mroe", "more")
    text = text.replace("UNCEBD", "UN-CEBD")
    text = re.sub(r"(?m)^#{1,6}\s*$\n?", "", text)
    text = re.sub(r"(?m)^\[\^\d+\]:.*(?:\n[ \t].*)*", "", text)
    text = re.sub(r"\[([^\]]+)\]\(#[^)]+\)", r"\1", text)

    for note, replacement in FOOTNOTE_CITES.items():
        text = text.replace(f"[^{note}]", f" {replacement}")
    for note, replacement in INLINE_FOOTNOTES.items():
        text = text.replace(f"[^{note}]", replacement)

    # Add directly relevant academic sources where the manuscript makes methodological claims.
    text = text.replace(
        "Mobile phone data refers to digital traces generated through the operation and use of mobile communication devices. These traces are created as mobile phones interact either with mobile network infrastructure or with software applications installed on the device. Across all forms, mobile phone data has one defining characteristic: it can be used to approximate the geographic position of a device, and by extension its user, over time. This makes it particularly valuable for analysing patterns of human mobility and population dynamics.",
        "Mobile phone data refers to digital traces generated through the operation and use of mobile communication devices [@rowe2024]. These traces are created as mobile phones interact either with mobile network infrastructure or with software applications installed on the device. Across all forms, mobile phone data has one defining characteristic: it can be used to approximate the geographic position of a device, and by extension its user, over time. This makes it particularly valuable for analysing patterns of human mobility and population dynamics [@gonzalez2008human_mobility; @song2010predictability; @blondel2015survey].",
    )
    text = text.replace(
        "**GPS-derived mobile phone data** refers to location information captured directly by the **global positioning system (GPS) sensors** embedded in smartphones and other mobile devices, typically via apps that have permission to record and share location. Unlike the network-generated datasets described above, GPS data are collected from a device’s onboard navigation chipset and can provide **latitude/longitude coordinates, with high geographical precision** (**often within a few metres**) and **temporal frequency** (e.g., seconds to minutes). They can collect continuous data on devices anywhere in the globe, thus offering global data coverage. However, the geographical precision and temporal frequency of data may vary depending on how the app is configured, users engage with the app, user consent is managed, and the type of technology used to build the device collecting the data. ",
        "**GPS-derived mobile phone data** refers to location information captured directly by the **global positioning system (GPS) sensors** embedded in smartphones and other mobile devices, typically via apps that have permission to record and share location [@barreras2024]. Unlike the network-generated datasets described above, GPS data are collected from a device’s onboard navigation chipset and can provide **latitude/longitude coordinates, with high geographical precision** (**often within a few metres**) and **temporal frequency** (e.g., seconds to minutes). They can collect continuous data on devices anywhere in the globe, thus offering global data coverage. However, the geographical precision and temporal frequency of data may vary depending on how the app is configured, users engage with the app, user consent is managed, and the type of technology used to build the device collecting the data. ",
    )
    text = text.replace(
        "This training manual focuses exclusively on the former, and more specifically on Call Detail Records, because this is the data type most commonly available at national scale and most frequently used in official statistics and public policy applications.",
        "This training manual focuses exclusively on the former, and more specifically on Call Detail Records, because this is the data type most commonly available at national scale and most frequently used in official statistics and public policy applications [@unstats2019mpdhandbook; @ricciato2020present_population; @salgado2021end_to_end].",
    )
    text = text.replace(
        "The spatial resolution of CDR data is determined by the mobile network infrastructure rather than the device itself. Location is inferred from the cell site providing the service. This acts as a proxy for the user’s position, capturing the interaction between the mobile network infrastructure and geographic position of devices. In dense urban environments, cell towers may cover relatively small areas, resulting in finer spatial granularity. In rural or remote areas, a single tower may cover a larger area, leading to coarser location estimates. Planners must account for this variability when assessing whether CDRs are suitable for a particular analytical purpose and application.",
        "The spatial resolution of CDR data is determined by the mobile network infrastructure rather than the device itself. Location is inferred from the cell site providing the service. This acts as a proxy for the user’s position, capturing the interaction between the mobile network infrastructure and geographic position of devices. In dense urban environments, cell towers may cover relatively small areas, resulting in finer spatial granularity. In rural or remote areas, a single tower may cover a larger area, leading to coarser location estimates. Planners must account for this variability when assessing whether CDRs are suitable for a particular analytical purpose and application [@blondel2015survey; @ricciato2020present_population].",
    )
    text = text.replace(
        "The frequency events may affect the temporal resolution of CDR data. Data are generated based on the occurrence of events reflecting user behaviour, rather than being a continuous data stream per se (other forms of higher resolution data from mobile network operators include what may be called signalling or ping data). In CDRs, a user’s location can only be estimated when the user actively uses the network. As a result, the temporal density of CDRs can vary widely across individuals and contexts, influenced by factors such as phone ownership, usage patterns, socioeconomic status and network pricing. This intermittency introduces analytical challenges that must be addressed through appropriate statistical methods, data integration and careful interpretation. ",
        "The frequency of events may affect the temporal resolution of CDR data. Data are generated based on the occurrence of events reflecting user behaviour, rather than being a continuous data stream per se (other forms of higher resolution data from mobile network operators include what may be called signalling or ping data). In CDRs, a user’s location can only be estimated when the user actively uses the network. As a result, the temporal density of CDRs can vary widely across individuals and contexts, influenced by factors such as phone ownership, usage patterns, socioeconomic status and network pricing. This intermittency introduces analytical challenges that must be addressed through appropriate statistical methods, data integration and careful interpretation [@blondel2015survey; @wesolowski2013biases; @ricciato2020present_population]. ",
    )
    text = text.replace(
        "MPD is not designed to entirely replace conducting a census. Rather, it can be used to strengthen such data collection activities by, among other things: (a) Assisting in production of sample frames or enumeration areas; (b) Identifying populations that have been, or are at risk of being, undercounted; and (c) Providing interim updates between census rounds. When using MPD for such use cases, it is critical that planners explicitly address **bias risks**, given that mobile phone ownership is lower among children, the elderly, women in some contexts, and poorer households.",
        "MPD is not designed to entirely replace conducting a census. Rather, it can be used to strengthen such data collection activities by, among other things: (a) Assisting in production of sample frames or enumeration areas; (b) Identifying populations that have been, or are at risk of being, undercounted; and (c) Providing interim updates between census rounds. When using MPD for such use cases, it is critical that planners explicitly address **bias risks**, given that mobile phone ownership is lower among children, the elderly, women in some contexts, and poorer households [@wesolowski2013biases; @cabrera_rowe2025bias].",
    )
    text = text.replace(
        "As discussed in Chapter 1, MPD provides a continuous, passively collected record of population presence and mobility. Unlike traditional surveys or censuses, which are costly, infrequent, and static, MPD enables:",
        "As discussed in Chapter 1, MPD provides a continuous, passively collected record of population presence and mobility [@louail2014spatial_structure]. Unlike traditional surveys or censuses, which are costly, infrequent, and static, MPD enables:",
    )
    text = text.replace(
        "Traditional poverty data can often become quickly outdated, particularly in low- and middle-income countries and contexts with highly dynamic populations. In combination with traditional sources such as census and survey data, in periods between their data collection, and sometimes in combination with other forms of data such as geospatial datasets, MPD can be a useful tool for generating updated and spatially refined estimates of socio-economic variables such as wealth or poverty. ",
        "Traditional poverty data can often become quickly outdated, particularly in low- and middle-income countries and contexts with highly dynamic populations. In combination with traditional sources such as census and survey data, in periods between their data collection, and sometimes in combination with other forms of data such as geospatial datasets, MPD can be a useful tool for generating updated and spatially refined estimates of socio-economic variables such as wealth or poverty [@eagle2010network_diversity; @blumenstock2015poverty]. ",
    )
    text = text.replace(
        "The pipeline begins with data generation and collection at the mobile network operator, where individual phone activities create network events. These events are then prepared for analytical use through transformation and pseudonymisation. Subsequent processing stages add analytical value by correcting errors, inferring behaviour, and constructing meaningful indicators. Finally, aggregation and scaling convert processed data into population-level statistics suitable for publication and policy use.",
        "The pipeline begins with data generation and collection at the mobile network operator, where individual phone activities create network events. These events are then prepared for analytical use through transformation and pseudonymisation. Subsequent processing stages add analytical value by correcting errors, inferring behaviour, and constructing meaningful indicators. Finally, aggregation and scaling convert processed data into population-level statistics suitable for publication and policy use [@ricciato2020present_population; @salgado2021end_to_end].",
    )
    text = text.replace(
        "Another critical processing step is the detection of meaningful locations, such as home and work. By analysing spatial-temporal patterns such as where a subscriber spends most nights, analysts can infer habitual locations and define a person’s usual environment. Departures from this environment form the basis for identifying tourism trips and other forms of temporary mobility.",
        "Another critical processing step is the detection of meaningful locations, such as home and work. By analysing spatial-temporal patterns such as where a subscriber spends most nights, analysts can infer habitual locations and define a person’s usual environment. Departures from this environment form the basis for identifying tourism trips and other forms of temporary mobility [@isaacman2011important_places].",
    )
    text = text.replace(
        "Privacy by design is operationalised by distinguishing between three tiers of data sensitivity. Tier 1 data consists of raw, identifiable records and remains under the strict control of the mobile network operator. Tier 2 data is pseudonymised and used for processing under controlled conditions. Tier 3 data is fully aggregated and suitable for dissemination.",
        "Privacy by design is operationalised by distinguishing between three tiers of data sensitivity. Tier 1 data consists of raw, identifiable records and remains under the strict control of the mobile network operator. Tier 2 data is pseudonymised and used for processing under controlled conditions. Tier 3 data is fully aggregated and suitable for dissemination [@demontjoye2018privacy].",
    )
    text = text.replace(
        "Understanding these tiers helps organisations design appropriate technical and organisational safeguards at each stage of the pipeline. Access controls, encryption, auditing, and strict role-based permissions are essential for Tier 1 and Tier 2 data, where risks of re-identification or commercial sensitivity are highest. Even at Tier 3, where data are aggregated and prepared for release, disclosure control remains necessary to ensure that small cell sizes, rare combinations of attributes, or extreme values do not inadvertently reveal information about individuals or commercially sensitive patterns. Privacy by design therefore operates as a continuous principle across the entire pipeline, rather than a single compliance step.",
        "Understanding these tiers helps organisations design appropriate technical and organisational safeguards at each stage of the pipeline. Access controls, encryption, auditing, and strict role-based permissions are essential for Tier 1 and Tier 2 data, where risks of re-identification or commercial sensitivity are highest. Even at Tier 3, where data are aggregated and prepared for release, disclosure control remains necessary to ensure that small cell sizes, rare combinations of attributes, or extreme values do not inadvertently reveal information about individuals or commercially sensitive patterns. Privacy by design therefore operates as a continuous principle across the entire pipeline, rather than a single compliance step [@demontjoye2018privacy].",
    )
    text = text.replace(
        "In MPD initiatives, this distinction is particularly important because mobility data are inherently identifying. Even when explicit identifiers such as phone numbers or subscriber IDs are removed or replaced, individual movement patterns are often unique and highly regular. As a result, individual-level mobility data remain personal data, regardless of whether direct identifiers are present. Removing names or numbers alone does not anonymise such data.",
        "In MPD initiatives, this distinction is particularly important because mobility data are inherently identifying. Even when explicit identifiers such as phone numbers or subscriber IDs are removed or replaced, individual movement patterns are often unique and highly regular. As a result, individual-level mobility data remain personal data, regardless of whether direct identifiers are present. Removing names or numbers alone does not anonymise such data [@gonzalez2008human_mobility; @song2010predictability; @demontjoye2013unique].",
    )
    text = text.replace(
        "Non-personal data, by contrast, do not relate to any identifiable individual. In practice, most MPD initiatives rely on aggregated data products that summarise patterns across large groups of subscribers, rather than individual trajectories. However, whether data are genuinely non-personal depends on the level of aggregation, the availability of auxiliary information, and the evolving state of reidentification techniques. Governance frameworks must therefore adopt a cautious and context-aware approach to classification, recognising that what is considered anonymised today may not remain so in the future.",
        "Non-personal data, by contrast, do not relate to any identifiable individual. In practice, most MPD initiatives rely on aggregated data products that summarise patterns across large groups of subscribers, rather than individual trajectories. However, whether data are genuinely non-personal depends on the level of aggregation, the availability of auxiliary information, and the evolving state of reidentification techniques. Governance frameworks must therefore adopt a cautious and context-aware approach to classification, recognising that what is considered anonymised today may not remain so in the future [@demontjoye2013unique; @demontjoye2018privacy].",
    )
    text = text.replace(
        "MPD initiatives entail a range of interrelated risks that must be proactively identified and mitigated. Privacy risks include unauthorised access to sensitive data, reidentification of individuals, and the use of data for surveillance or profiling. Security risks encompass data breaches, whether through malicious attacks, inadequate access controls, or accidental disclosure. Ethical risks arise when data are misused, misinterpreted, or applied in ways that exacerbate bias, exclusion, or harm to vulnerable populations.",
        "MPD initiatives entail a range of interrelated risks that must be proactively identified and mitigated. Privacy risks include unauthorised access to sensitive data, reidentification of individuals, and the use of data for surveillance or profiling. Security risks encompass data breaches, whether through malicious attacks, inadequate access controls, or accidental disclosure. Ethical risks arise when data are misused, misinterpreted, or applied in ways that exacerbate bias, exclusion, or harm to vulnerable populations [@demontjoye2013unique; @demontjoye2018privacy].",
    )
    text = text.replace(
        "However, aggregation may not be sufficient to protect the individual privacy of all subscribers. Aggregation relies on there being a sufficient number of subscribers in each area in each time frame to prevent any individual being reidentified. Without any further checks, only aggregating CDR data risks producing outputs in which there is only a single or very few subscribers in a given location at a given time which may risk their reidentification. This is more likely to occur at high spatial and temporal resolution.",
        "However, aggregation may not be sufficient to protect the individual privacy of all subscribers. Aggregation relies on there being a sufficient number of subscribers in each area in each time frame to prevent any individual being reidentified. Without any further checks, only aggregating CDR data risks producing outputs in which there is only a single or very few subscribers in a given location at a given time which may risk their reidentification. This is more likely to occur at high spatial and temporal resolution [@demontjoye2013unique].",
    )
    text = text.replace(
        "While ensuring k-anonymity with a suitable threshold is currently sufficient to preserve the individual privacy of subscribers in a CDR dataset, anonymisation is a moving target as new methods for reidentification of subscribers and for data protection continue to be developed.",
        "While ensuring k-anonymity with a suitable threshold is currently sufficient to preserve the individual privacy of subscribers in a CDR dataset, anonymisation is a moving target as new methods for reidentification of subscribers and for data protection continue to be developed [@demontjoye2018privacy].",
    )
    text = text.replace(
        "Two broad categories of sensitive information commonly arise. The first is personal data, such as individual-level call detail record trajectories, which can reveal patterns of movement even when direct identifiers are removed. The second is commercially sensitive information, such as detailed network infrastructure data, which mobile network operators may need to protect for competitive or security reasons.",
        "Two broad categories of sensitive information commonly arise. The first is personal data, such as individual-level call detail record trajectories, which can reveal patterns of movement even when direct identifiers are removed. The second is commercially sensitive information, such as detailed network infrastructure data, which mobile network operators may need to protect for competitive or security reasons [@demontjoye2013unique; @demontjoye2018privacy].",
    )
    text = text.replace(
        "It is particularly important to explain data protection measures, such as pseudonymisation performed by operators and aggregation of results to population-level indicators. Explicitly stating that content of calls or messages is never accessed can help address common concerns and prevent misunderstanding.",
        "It is particularly important to explain data protection measures, such as pseudonymisation performed by operators and aggregation of results to population-level indicators. Explicitly stating that content of calls or messages is never accessed can help address common concerns and prevent misunderstanding [@demontjoye2018privacy].",
    )

    # Add a small number of directly relevant, verified Rowe references.
    text = text.replace(
        "Traditional statistics struggle to measure displacement and return dynamics. MPD can enable rapid estimation of:",
        "Traditional statistics struggle to measure displacement and return dynamics. MPD can enable rapid estimation of displacement, return, and recovery when digital trace data are carefully adjusted, validated, and triangulated with other sources [@uncebd_disaster_statistics; @lu2012haiti_displacement; @rowe2022digitalfootprint; @iradukunda_rowe_pietrostefani2025ukraine; @pietrostefani2025dynamic_displacement]. MPD can enable rapid estimation of:",
    )
    text = text.replace(
        "During the Ebola response in Sierra Leone and COVID-19 responses across multiple countries, CDR analysis showed measurable reductions in mobility following restrictions (and their reversal once measures were lifted), often within just a few days of implementation.",
        "During the Ebola response in Sierra Leone and COVID-19 responses across multiple countries, CDR and other digital trace analyses showed measurable reductions in mobility following restrictions (and their reversal once measures were lifted), often within just a few days of implementation [@rowe2023urban_exodus; @cabrera2025latin_america_mobility].",
    )
    text = text.replace(
        "This has been demonstrated across multiple disease contexts: CDR-derived mobility metrics outperformed conventional gravity models in predicting the spread of cholera in Haiti in 2010 and revealed the role of mass gatherings as a transmission driver during the 2005 Senegal epidemic.",
        "This has been demonstrated across multiple disease contexts: CDR-derived mobility metrics outperformed conventional gravity models in predicting the spread of cholera in Haiti in 2010 and revealed the role of mass gatherings as a transmission driver during the 2005 Senegal epidemic [@bengtsson2015cholera; @wesolowski2012malaria; @tizzoni2014epidemics].",
    )
    text = text.replace(
        "Ghana during COVID-19 (2020): Data from Vodafone Ghana was used to support government decision making by the Presidential Task Force around the effectiveness of COVID-19 lockdowns and what non-pharmaceutical interventions were working in the country, informing subsequent policies on movement restrictions.",
        "Ghana during COVID-19 (2020): Data from Vodafone Ghana was used to support government decision making by the Presidential Task Force around the effectiveness of COVID-19 lockdowns and what non-pharmaceutical interventions were working in the country, informing subsequent policies on movement restrictions [@li2021ghana_cdr].",
    )
    text = text.replace(
        "The UN Committee of Experts on Big Data and Data Science for Official Statistics has a Mobile Phone Data task team which has published guidance on using this data source for different specific use cases.",
        "The UN Committee of Experts on Big Data and Data Science for Official Statistics has a Mobile Phone Data task team which has published guidance on using this data source for different specific use cases [@uncebd_mobile_phone_task_team].",
    )
    text = text.replace(
        "Recognising these concerns is not a concession; it is a prerequisite for designing an engagement strategy that is realistic and credible.",
        "Recognising these concerns is not a concession; it is a prerequisite for designing an engagement strategy that is realistic and credible [@gsma2019bigdata].",
    )
    text = text.replace(
        "Because legal frameworks vary significantly across jurisdictions, expert legal advice is essential.",
        "Because legal frameworks vary significantly across jurisdictions, including regional frameworks such as the African Union Malabo Convention, expert legal advice is essential [@african_union2018malabo].",
    )
    text = text.replace(
        "In summary: Compared to GPS app data, CDRs and signalling data usually has lower spatial precision",
        "In summary: Compared to GPS app data, CDRs and signalling data usually have lower spatial precision",
    )

    lines = []
    for line in text.splitlines():
        if line.startswith("#"):
            line = clean_heading_line(line)
        lines.append(line.rstrip())
    lines = convert_single_cell_boxes(lines)
    output = "\n".join(lines).strip() + "\n"
    output = output.replace(
        '::: {.callout-note title="Box 4:"}\n\nBrief Case Studies of dynamic population data and internal migration ',
        '::: {.callout-note title="Box 4: Dynamic population data and internal migration"}\n\n',
    )
    output = re.sub(
        r'::: \{\.callout-note title="Box 7:[^"]+"\}\n\nand reduces the budget',
        '::: {.callout-note title="Box 7: MPD for tourism statistics"}\n\nIndonesia (2016, 2018, 2019): MPD was used for inbound tourism, domestic tourism, outbound tourism, and event-impact analysis. It reduced work burdens, increased granularity from province to city/municipality level, and reduced the budget',
        output,
    )
    output = output.replace(
        '::: {.callout-note title="Box 8:"}\n\nCase studies of MPD for Transport statistics ',
        '::: {.callout-note title="Box 8: MPD for transport statistics"}\n\n',
    )
    output = output.replace(
        " [@aiken2022machine_learning], [@worldbank2021novissi]",
        " [@aiken2022machine_learning; @worldbank2021novissi]",
    )
    output = re.sub(r"(?m)^\s*\d+\)\s+(####\s+)", r"\1", output)
    output = re.sub(r"(?m)^####\s+", "#### ", output)
    output = re.sub(r"(?m)([^\n])\n(####\s+)", r"\1\n\n\2", output)
    output = output.replace("{#call-detail-records-(cdrs)}", "{#call-detail-records-cdrs}")
    output = output.replace("and  routinely", "and routinely")
    output = output.replace(".  [@", ". [@")
    return output


def split_sections(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"(?m)^#\s+(.+?)\s*$", text))
    sections: dict[str, str] = {}
    for idx, match in enumerate(matches):
        title = match.group(1).strip()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        body = text[match.start():end].strip() + "\n"
        title = TITLE_REPLACEMENTS.get(title, title)
        body = body.replace(match.group(0), f"# {title}", 1)
        if title in SPLIT_FILES:
            sections[title] = body
    missing = [title for title in SPLIT_FILES if title not in sections]
    if missing:
        raise RuntimeError(f"Missing expected sections: {missing}")
    return sections


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content.rstrip() + "\n", encoding="utf-8")


def main() -> None:
    raw = SOURCE.read_text(encoding="utf-8")
    cleaned = clean_text(raw)
    sections = split_sections(cleaned)

    for title, path in SPLIT_FILES.items():
        content = apply_abbreviation_policy(title, sections[title])
        if title == "Preface":
            content = content.replace("# Preface", "# Preface {.unnumbered}" + PROJECT_STATUS_CALLOUT, 1)
        elif title in FRONT_MATTER_SECTIONS:
            content = content.replace(f"# {title}", f"# {title} {{.unnumbered}}", 1)
        if path == "index.qmd":
            content = INDEX_INTRO + content + AUTHORS_PREFACE + RECOMMENDED_CITATION
        write(path, content)

    write("chapters/references.qmd", REFERENCES_QMD)
    write("references.bib", BIBTEX)
    write("_quarto.yml", QUARTO_YML)
    write("style/theme.scss", THEME_SCSS)
    write("style/dark.scss", DARK_SCSS)
    write("README.md", README)
    write(".gitignore", GITIGNORE)
    write(".github/workflows/publish.yml", PUBLISH_YML)


if __name__ == "__main__":
    main()
