Circulation of a digital community currency | Scientific Reports
[Skip to main content](#content)
Thank you for visiting nature.com. You are using a browser version with limited support for CSS. To obtain
the best experience, we recommend you use a more up to date browser (or turn off compatibility mode in
Internet Explorer). In the meantime, to ensure continued support, we are displaying the site without styles
and JavaScript.
Advertisement
[![Advertisement](//pubads.g.doubleclick.net/gampad/ad?iu=/285/scientific_reports/article&sz=728x90&c=-218128824&t=pos%3Dtop%26type%3Darticle%26artid%3Ds41598-023-33184-1%26doi%3D10.1038/s41598-023-33184-1%26subjmeta%3D1042,2801,530,639,705,766%26kwrd%3DComplex+networks,Computational+science)](//pubads.g.doubleclick.net/gampad/jump?iu=/285/scientific_reports/article&sz=728x90&c=-218128824&t=pos%3Dtop%26type%3Darticle%26artid%3Ds41598-023-33184-1%26doi%3D10.1038/s41598-023-33184-1%26subjmeta%3D1042,2801,530,639,705,766%26kwrd%3DComplex+networks,Computational+science)
[![Scientific Reports]()](/srep)
* [View all journals]()
* [Search](#search-menu)
* [Log in]()
* [Explore
content](#explore)
* [About
the journal](#about-the-journal)
* [Publish
with us](#publish-with-us)
* [Sign up for alerts]()
* [RSS feed]()
1. [nature](/)
2. [scientific reports](/srep)
3. [articles](/srep/articles?type=article)
4. article
Circulation of a digital community currency
[Download PDF](/articles/s41598-023-33184-1.pdf)
[Download PDF](/articles/s41598-023-33184-1.pdf)
* Article
* [Open Access]()
* [Published:
11 April 2023](#article-info)
Circulation of a digital community currency
=============================================
* [Carolina E. S. Mattsson](#auth-Carolina_E__S_-Mattsson-Aff1)
[1](#Aff1)
,
* [Teodoro Criscione](#auth-Teodoro-Criscione-Aff2-Aff3)
[2](#Aff2)
,
[3](#Aff3)
&
* [Frank W. Takes](#auth-Frank_W_-Takes-Aff1)
[1](#Aff1)
[*Scientific Reports*](/srep)
**volume
13**
, Article number:
5864
(
2023
)
[Cite this article](#citeas)
* 1242
Accesses
* 12
Altmetric
* [Metrics
details](/articles/s41598-023-33184-1/metrics)
###
Subjects
* [Complex networks](/subjects/complex-networks)
* [Computational science](/subjects/computational-science)
Abstract
----------
Circulation is the characteristic feature of successful currency systems, from community currencies to cryptocurrencies to national currencies. In this paper, we propose a network analysis approach especially suited for studying circulation given a system's digital transaction records. Sarafu is a digital community currency that was active in Kenya over a period that saw considerable economic disruption due to the COVID-19 pandemic. We represent its circulation as a network of monetary flow among the 40,000 Sarafu users. Network flow analysis reveals that circulation was highly modular, geographically localized, and occurring among users with diverse livelihoods. Across localized sub-populations, network cycle analysis supports the intuitive notion that circulation requires cycles. Moreover, the sub-networks underlying circulation are consistently degree disassortative and we find evidence of preferential attachment. Community-based institutions often take on the role of local hubs, and network centrality measures confirm the importance of early adopters and of women's participation. This work demonstrates that networks of monetary flow enable the study of circulation within currency systems at a striking level of detail, and our findings can be used to inform the development of community currencies in marginalized areas.
Introduction
--------------
The circulation of money is generally studied in an abstract sense, for example as the extent to which monetary policy, productivity improvements, supply disruptions, or other shocks affect aggregate indicators of economic output
[1](#ref-CR1 "Nakamura, E. & Steinsson, J. Identification in macroeconomics. J. Econ. Persp. 32, 59-86.
(2018).")
,
[2](#ref-CR2 "McNerney, J., Savoie, C., Caravelli, F., Carvalho, V. M. & Farmer, J. D. How production networks amplify economic growth. Proc. Natl. Acad. Sci. 119, e2106031118.
(2022).")
,
[3](#ref-CR3 "Carvalho, V. M., Nirei, M., Saito, Y. & Tahbaz-Salehi, A. Supply Chain Disruptions: Evidence from the Great East Japan Earthquake. SSRN Scholarly ,, Social Science Research Network, Rochester, NY (2016).")
,
[4](/articles/s41598-023-33184-1#ref-CR4 "Acemoglu, D., Carvalho, V. M., Ozdaglar, A. & Tahbaz-Salehi, A. The network origins of aggregate fluctuations. Econometrica 80, .
(2012).")
. Detailed observation has long been impractical for lack of empirical data. However, modern payment infrastructure is increasingly digital
[5](/articles/s41598-023-33184-1#ref-CR5 "Adrian, T. & Mancini-Griffoli, T. The rise of digital money. No. no. 19/0018 in IMF FinTech notes (International Monetary Fund, Washington, D.C (2019).")
, and the circulation of money is leaving real-time records on the servers of financial institutions worldwide. These transaction records offer especially high granularity data in time and in space, and open up the possibility of fined-grained data-driven studies of currency systems
[6](#ref-CR6 "Frankova, E., Fousek, J., Kala, L. & Labohy, J. Transaction network analysis for studying Local Exchange Trading Systems (LETS): Research potentials and limitations. Ecol. Econ. 107, 266-275.
(2014).")
,
[7](#ref-CR7 "Alessandretti, L., ElBahrawy, A., Aiello, L. M. & Baronchelli, A. Anticipating cryptocurrency prices using machine learning. Complexity 2018 (2018).")
,
[8](#ref-CR8 "Aladangady, A. et al. From Transactions Data to Economic Statistics: Constructing Real-Time, High-Frequency, Geographic Measures of Consumer Spending. Big Data for 21st Century Economic Statistics (2019).")
,
[9](#ref-CR9 "Bouchaud, J.-P. Trades, Quotes and Prices: Financial Markets Under the Microscope 1st edn. (Cambridge University Press, 2018).")
,
[10](#ref-CR10 "Mattsson, C. E. S. & Takes, F. W. Trajectories through temporal networks. Appl. Netw. Sci. 6, 1-31.
(2021).")
,
[11](#ref-CR11 "Bardoscia, M. et al. The physics of financial networks. Nat. Rev. Phys. 3, 490-507.
(2021).")
,
[12](/articles/s41598-023-33184-1#ref-CR12 "Carvalho, V. M. et al. Tracking the COVID-19 crisis with high-resolution transaction data. R. Soc. Open Sci. 8, 210218.
(2021).")
. In this paper we consider the circulation of money as observed in transaction records, using
*networks of monetary flow*
to represent patterns of circulation over a period of time. Our findings show that techniques in network science -- flow-based community detection, measures of cyclic structure, network mixing patterns, and walk-based centrality metrics -- together capture key aspects of circulation within a real-world currency system when applied to such networks. We demonstrate that important practical and theoretical questions around the circulation of money can be studied using networks of monetary flow.
The main focus of this paper is on complementary currencies whose modern implementations produce comprehensive digital records, as these are cases where transaction records are available for an entire currency system. Complementary currencies circulate in parallel to national currencies in that tokens are
*not*
legal tender, nor necessarily exchangeable for legal tender
[13](#ref-CR13 "Stodder, J. Complementary credit networks and macroeconomic stability: Switzerland's Wirtschaftsring. J. Econ. Behav. Organ. 72, 79-95.
(2009).")
,
[14](#ref-CR14 "Lietaer, B. Complementary currencies in Japan today: History, originality and relevance. Int. J. Commun. Curr. Res. 8, 1-23.
(2004).")
,
[15](/articles/s41598-023-33184-1#ref-CR15 "Ussher, L., Ebert, L., Gomez, G. M. & Ruddick, W. O. Complementary currencies for humanitarian aid. J. Risk Financ. Manag. 14, 557.
(2021).")
; they are used under mutual agreements that come in many forms, from local community currencies
[6](/articles/s41598-023-33184-1#ref-CR6 "Frankova, E., Fousek, J., Kala, L. & Labohy, J. Transaction network analysis for studying Local Exchange Trading Systems (LETS): Research potentials and limitations. Ecol. Econ. 107, 266-275.
(2014).")
,
[16](/articles/s41598-023-33184-1#ref-CR16 "Muralt, V. The Woergl experiment with depreciating money. Ann. Public Cooper. Econ. 10, 48-57.
(1934).")
,
[17](/articles/s41598-023-33184-1#ref-CR17 "Kichiji, N. & Nishibe, M. Network analyses of the circulation flow of community currency. Evol. Inst. Econ. Rev. 4, 267-300.
(2008).")
to global cryptocurrencies
[18](#ref-CR18 "Nakamoto, S. Bitcoin: A Peer-to-Peer Electronic Cash System (Tech. Rep, Manubot, 2008).")
,
[19](#ref-CR19 "Kondor, D., Posfai, M., Csabai, I. & Vattay, G. Do the rich get richer? An empirical analysis of the bitcoin transaction network. PLoS ONE 9, e86197.
(2014).")
,
[20](/articles/s41598-023-33184-1#ref-CR20 "ElBahrawy, A., Alessandretti, L., Kandler, A., Pastor-Satorras, R. & Baronchelli, A. Evolutionary dynamics of the cryptocurrency market. R. Soc. Open Sci. 4, 170623 (2017).")
. Sardex, for example, is a digital complementary currency used among businesses in Sardinia. Digital records of transactions in Sardex have been studied to show that cycle motifs are related to performance and stability of the currency system
[21](/articles/s41598-023-33184-1#ref-CR21 "Iosifidis, G. et al. Cyclic motifs in the Sardex monetary network. Nat. Hum. Behav.
(2018).")
,
[22](/articles/s41598-023-33184-1#ref-CR22 "Fleischman, T. & Dini, P. Balancing the Payment System. (2020).
arXiv:2011.03517
[q-fin]")
. The full transaction histories of Bitcoin and other cryptocurrencies can be reconstructed from public ledgers
[23](#ref-CR23 "Ober, M., Katzenbeisser, S. & Hamacher, K. Structure and anonymity of the bitcoin transaction graph. Fut. Internet 5, 237-250.
(2013).")
,
[24](#ref-CR24 "Meiklejohn, S. et al. A fistful of Bitcoins: Characterizing payments among men with no names. Commun. ACM 59, 86-93.
(2016).")
,
[25](/articles/s41598-023-33184-1#ref-CR25 "Zhang, Y., Wang, J. & Luo, J. Heuristic-based address clustering in bitcoin. IEEE Access 8, 210582-210591.
(2020).")
. Bitcoin transactions reveal a currency system that supports substantial trade outside centralized marketplaces, but where inequality has been increasing over time
[19](/articles/s41598-023-33184-1#ref-CR19 "Kondor, D., Posfai, M., Csabai, I. & Vattay, G. Do the rich get richer? An empirical analysis of the bitcoin transaction network. PLoS ONE 9, e86197.
(2014).")
,
[26](/articles/s41598-023-33184-1#ref-CR26 "Nadini, M. Emergence and structure of decentralised trade networks around dark web marketplaces. Sci. Rep. 9, 1-9 (2022).")
. Sarafu, the currency considered in this work, is a "Community Inclusion Currency" (CIC) that incorporates elements of both community currencies and cryptocurrencies
[27](/articles/s41598-023-33184-1#ref-CR27 "Mattsson, C. E. S., Criscione, T. & Ruddick, W. O. Sarafu community inclusion currency, 2020-2021. Sci. Data
(2022).")
.
Community currencies are typically created with the aim to support local economic activity by facilitating local circulation
[16](/articles/s41598-023-33184-1#ref-CR16 "Muralt, V. The Woergl experiment with depreciating money. Ann. Public Cooper. Econ. 10, 48-57.
(1934).")
,
[17](/articles/s41598-023-33184-1#ref-CR17 "Kichiji, N. & Nishibe, M. Network analyses of the circulation flow of community currency. Evol. Inst. Econ. Rev. 4, 267-300.
(2008).")
,
[28](/articles/s41598-023-33184-1#ref-CR28 "Ruddick, W. O. Eco-Pesa: an evaluation of a complementary currency programme in Kenyaa informal settlements. Int. J. Commun. Curr. Res. 15, 12.
(2011).")
. Moreover, complementary currencies are counter-cyclical in that they tend to see higher circulation during periods of economic disruption
[29](/articles/s41598-023-33184-1#ref-CR29 "Stodder, J. & Lietaer, B. The macro-stability of Swiss WIR-Bank credits: Balance, velocity, and leverage. Comp. Econ. Stud. 58, 570-605.
(2016).")
,
[30](/articles/s41598-023-33184-1#ref-CR30 "Zeller, S. Economic advantages of community currencies. J. Risk Financ. Manag. 13, 271.
(2020).")
. We study Sarafu, a digital community currency with a presence in several local areas of Kenya, from January 2020 to June 2021, a period that saw considerable economic disruption due to the COVID-19 pandemic. Previously published data
[31](/articles/s41598-023-33184-1#ref-CR31 "Ruddick, W. O. Sarafu Community Inclusion Currency, 2020-2021, (2021).
")
and a data descriptor
[27](/articles/s41598-023-33184-1#ref-CR27 "Mattsson, C. E. S., Criscione, T. & Ruddick, W. O. Sarafu community inclusion currency, 2020-2021. Sci. Data
(2022).")
detail the transaction activity that occurred over Sarafu over this period. We detail transaction volumes in Sarafu over time and then study the circulation of Sarafu resulting from this activity as a network of monetary flow.
The Sarafu flow network encompasses 293.7 million Sarafu in transaction volume among around 40,000 users. This weighted, directed, time-aggregated network representation captures the patterns of circulation in intricate detail, allowing us to study what shapes the Sarafu currency system as a whole. We apply carefully selected network analysis techniques to the Sarafu flow network to answer three questions of particular relevance to research about community currencies:
*Among whom is Sarafu circulating?*
Anonymized information on account holders allows us to label each node with a geographic area, livelihood category, registration date, and reported gender. We investigate the composition of sub-populations within which Sarafu was circulating, as identified using a so-called community detection method developed especially for flow networks. Specifically, the map equation framework and the associated Infomap algorithm
[32](/articles/s41598-023-33184-1#ref-CR32 "Rosvall, M. & Bergstrom, C. T. Maps of random walks on complex networks reveal community structure. Proc. Natl. Acad. Sci. 105, .
(2008).")
,
[33](/articles/s41598-023-33184-1#ref-CR33 "Bohlin, L., Edler, D., Lancichinetti, A. & Rosvall, M. Community Detection and Visualization of Networks with the Map Equation Framework. In eDing, Y., eRousseau, R. & eWolfram, D. (eds.) Measuring Scholarly Impact, 3-34,
(Springer International Publishing, Cham, 2014).")
group nodes into sub-populations whose sub-networks capture as much of the transaction volume as possible.
*What network structures support the circulation of Sarafu?*
Degree disassortativity has been noted in a variety of economic networks
[19](/articles/s41598-023-33184-1#ref-CR19 "Kondor, D., Posfai, M., Csabai, I. & Vattay, G. Do the rich get richer? An empirical analysis of the bitcoin transaction network. PLoS ONE 9, e86197.
(2014).")
,
[34](#ref-CR34 "Fujiwara, Y. & Aoyama, H. Large-scale structure of a nation-wide production network. Eur. Phys. J. B 77, 565-580.
(2010).")
,
[35](#ref-CR35 "Mattsson, C. E. S. et al. Functional structure in production networks. Front. Big Data
(2021).")
,
[36](/articles/s41598-023-33184-1#ref-CR36 "Campajola, C., D'Errico, M. & Tessone, C. J. MicroVelocity: rethinking the Velocity of Money for digital currencies.
arXiv:2201.13416
[physics, q-fin] (2022).")
in that high-degree nodes generally transact with low-degree nodes. It has also been noted that network cycles may be key to the 'health' of currency systems and of individual accounts
[21](/articles/s41598-023-33184-1#ref-CR21 "Iosifidis, G. et al. Cyclic motifs in the Sardex monetary network. Nat. Hum. Behav.
(2018).")
. Indeed, detecting cycles and brokering 'missing' financial connections is seen by private actors as a promising credit clearing and risk management service
[22](/articles/s41598-023-33184-1#ref-CR22 "Fleischman, T. & Dini, P. Balancing the Payment System. (2020).
arXiv:2011.03517
[q-fin]")
,
[37](/articles/s41598-023-33184-1#ref-CR37 "Fleischman, T., Dini, P. & Littera, G. Liquidity-saving through obligation-clearing and mutual credit: An effective monetary innovation for SMEs in times of crisis. J. Risk Financ. Manag. 13, 295.
(2020).")
. In a similar vein, Ussher et al.
[15](/articles/s41598-023-33184-1#ref-CR15 "Ussher, L., Ebert, L., Gomez, G. M. & Ruddick, W. O. Complementary currencies for humanitarian aid. J. Risk Financ. Manag. 14, 557.
(2021).")
argue that community currencies compare favorably to cash assistance as an economic development intervention because they help establish economic connections that keep money local. We study the network structure underlying the circulation of Sarafu within the aforementioned sub-populations using network assortativity measures and relative cycle counts.
*What characterizes the most prominent Sarafu users?*
We would like to understand patterns in who holds Sarafu accounts that are especially prominent, or perhaps even systematically important. Prominent users are identified by means of a network centrality measure that is directly related to the circulation of Sarafu, as captured by a network of monetary flow. Specifically, weighted PageRank
[38](/articles/s41598-023-33184-1#ref-CR38 "Page, L., Brin, S., Motwani, R. & Winograd, T. The PageRank Citation Ranking: Bringing Order to the Web. Technical Report 1999-66, Stanford InfoLab (1999).")
computes a metric that corresponds to the share of funds a given account would control, at any given time, if the observed dynamics were to continue indefinitely. We calibrate this measure against empirical account balances and use it to investigate the account features most associated with prominent users.
The Sarafu user base grew substantially over the observation period and transaction volumes rose dramatically as the COVID-19 pandemic disrupted regular economic activities. However, our results indicate that circulation remained modular and geographically localized. Circulation occurred primarily within particular sub-populations consisting of co-located users with diverse livelihoods. This has concrete implications for humanitarian policy in marginalized areas, in that it implies that community currencies can help support specific areas during periods of economic stress and that such interventions are more likely to succeed in areas with a diverse mix of economic activities already present. Community currencies also support local economic development over longer periods of time
[13](/articles/s41598-023-33184-1#ref-CR13 "Stodder, J. Complementary credit networks and macroeconomic stability: Switzerland's Wirtschaftsring. J. Econ. Behav. Organ. 72, 79-95.
(2009).")
,
[15](/articles/s41598-023-33184-1#ref-CR15 "Ussher, L., Ebert, L., Gomez, G. M. & Ruddick, W. O. Complementary currencies for humanitarian aid. J. Risk Financ. Manag. 14, 557.
(2021).")
,
[21](/articles/s41598-023-33184-1#ref-CR21 "Iosifidis, G. et al. Cyclic motifs in the Sardex monetary network. Nat. Hum. Behav.
(2018).")
. For such initiatives, it is useful to know that community-based financial institutions, and, in a few cases, faith leaders, are especially prominent among Sarafu users. These "hubs" play a key structural role especially at a local level, in that the sub-networks underlying local circulation are consistently degree-disassortative. Moreover, an elevated presence of short cycles supports the intuitive notion that circulation requires cycles.
The findings and insights presented in this paper provide a fine-grained understanding of the circulation of Sarafu over a highly dynamic period that includes the arrival of the COVID-19 pandemic to Kenya. This investigation demonstrates that networks of monetary flow can capture key features of circulation within currency systems. Flow-, walk-, and cycle- based network measures and algorithms produce interpretable analyses that allow for characterising the system. Noteworthy is that the approach presented in this paper can be applied to study any currency system where digital transaction records are available. Indeed, there may be important regularities underlying the circulation of money in such systems, and these would be well worth exploring further.
The remainder of this paper is organized as follows. The "
[Data](/articles/s41598-023-33184-1#Sec2)
" section briefly describes the Sarafu system over this especially tumultuous period. The "
[Results](/articles/s41598-023-33184-1#Sec3)
" section presents our findings on patterns of circulation, prominent users, and the network structure underlying circulation. We synthesize these contributions and discuss the implications of our findings in the "
[Discussion](/articles/s41598-023-33184-1#Sec13)
" section. Finally, the "
[Methods](/articles/s41598-023-33184-1#Sec14)
" section details the data preparation, network analysis measures, and statistical methods used in this study and provides references to facilitate data, code, and software availability.
Data
------
Digital administrative records of the Sarafu CIC from January 2020 to June 2021 have been published by Grassroots Economics, a non-profit foundation based in Kenya that operates Sarafu and leads related economic development projects in marginalized and food-insecure areas of the country. The published dataset
[31](/articles/s41598-023-33184-1#ref-CR31 "Ruddick, W. O. Sarafu Community Inclusion Currency, 2020-2021, (2021).
")
has previously been described in raw form
[27](/articles/s41598-023-33184-1#ref-CR27 "Mattsson, C. E. S., Criscione, T. & Ruddick, W. O. Sarafu community inclusion currency, 2020-2021. Sci. Data
(2022).")
and used in a case study introducing CICs as a modality for humanitarian aid
[15](/articles/s41598-023-33184-1#ref-CR15 "Ussher, L., Ebert, L., Gomez, G. M. & Ruddick, W. O. Complementary currencies for humanitarian aid. J. Risk Financ. Manag. 14, 557.
(2021).")
. During the observation period, Sarafu was available throughout Kenya. Mimicking the well-developed mobile payment infrastructure of the national currency
[39](#ref-CR39 "Mbogo, M. The impact of mobile payments on the success and growth of micro-business: The case of M-Pesa in Kenya. J. Lang. Technol. Entrep. Africa 2, 182-203 (2010).")
,
[40](#ref-CR40 "Stuart, G. & Cohen, M. Cash In, Cash Out Kenya: The Role of M-PESA in the Lives of Low-Income People. The Financial Services Assesment project (Microfinance Opportunities, 2011).")
,
[41](#ref-CR41 "Mbiti, I. & Weil, D. N. Mobile banking: The impact of M-Pesa in Kenya (Tech. Rep, National Bureau of Economic Research, 2011).")
,
[42](#ref-CR42 "Suri, T. Mobile money. Annu. Rev. Econ. 9, 497-520.
(2017).")
,
[43](#ref-CR43 "International Finance Corporation & Mastercard Foundation. Digital Access: The Future of Financial Inclusion in Africa (Tech. Rep, Partnership for Financial Inclusion, 2018).")
,
[44](/articles/s41598-023-33184-1#ref-CR44 "Baah, B. et al. State of the Industry Report on Mobile Money 2021 (Industry Report, GSMA, 2021).")
, each Sarafu account was tied to a Kenyan mobile number and accessible over a mobile interface. An account could be created with an activation code sent to a particular mobile number, then used and managed via a series of simple menus. The resulting digital records became a dataset that includes hundreds of thousands of Sarafu transactions and anonymized account information for the tens of thousands of users.
January 2020 saw the consolidation of several precursor currencies onto a single platform: Sarafu. In prior years, several digital community currencies had been launched by Grassroots Economics in different areas
[27](/articles/s41598-023-33184-1#ref-CR27 "Mattsson, C. E. S., Criscione, T. & Ruddick, W. O. Sarafu community inclusion currency, 2020-2021. Sci. Data
(2022).")
,
[45](/articles/s41598-023-33184-1#ref-CR45 "Marion, C. Voucher Systems for Food Security: A Case Study on Kenya's Sarafu-Credit. Master's thesis, University of Copenhagen,
(2018).")
. These were designed to operate as separate systems over a decentralized infrastructure, interacting very little. Flow networks from earlier periods would have been composed of a dozen or so nearly-disconnected components, each corresponding to a different precursor currency serving a different local community. Shortly following the start of the observation period, the consolidated system expanded dramatically as the COVID-19 pandemic arrived in Kenya. Sarafu grew from 8,354 registered accounts in January 2020 to almost 55,000 in June 2021. Figure
[1](/articles/s41598-023-33184-1#Fig1)
shows the transaction volumes for each of the complete months over the observation period. Beginning in April 2020 and continuing through the second wave of COVID-19 in Kenya, Sarafu saw transaction volumes almost ten times higher than in February 2020. This dramatic expansion occurred primarily in particular regions, described below, and we see a return towards the baseline in these areas by the end of the observation period. The overall pattern is perhaps best explained by the counter-cyclical nature of complementary currencies, which are known to see spikes in usage levels during periods of economic disruption
[13](/articles/s41598-023-33184-1#ref-CR13 "Stodder, J. Complementary credit networks and macroeconomic stability: Switzerland's Wirtschaftsring. J. Econ. Behav. Organ. 72, 79-95.
(2009).")
,
[29](/articles/s41598-023-33184-1#ref-CR29 "Stodder, J. & Lietaer, B. The macro-stability of Swiss WIR-Bank credits: Balance, velocity, and leverage. Comp. Econ. Stud. 58, 570-605.
(2016).")
,
[30](/articles/s41598-023-33184-1#ref-CR30 "Zeller, S. Economic advantages of community currencies. J. Risk Financ. Manag. 13, 271.
(2020).")
.
**Figure 1**
[![figure 1](//media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-023-33184-1/MediaObjects/41598_2023_33184_Fig1_HTML.png)](/articles/s41598-023-33184-1/figures/1)
Monthly transaction volumes in total, and in each geographic area (shown at two different scales).
[Full size image](/articles/s41598-023-33184-1/figures/1)
The figures in this work employ a consistent color scheme for geographic area. Purple corresponds to
*Kinango Kwale*
, a rural area where GE has had a substantial presence in several local communities for many years; this area saw much growth during the COVID-19 pandemic due largely to word of mouth. Light green is
*Mukuru Nairobi*
, an urban area that was the site of a targeted introduction beginning in March 2020. For details we refer to the "
[Data preparation](/articles/s41598-023-33184-1#Sec15)
" section in "
[Methods](/articles/s41598-023-33184-1#Sec14)
". Accounts located elsewhere in
*Nairobi*
are shown in dark green. In light blue are accounts in
*Kisauni Mombasa*
, the site of a second introduction beginning in early 2021. Accounts located elsewhere in
*Mombasa*
are shown in dark blue.
*Kilifi*
, in dark grey, is the county where GE is headquartered. Users with an unknown location (the largest category within
*other*
), are in light grey. In Fig.
[1](/articles/s41598-023-33184-1#Fig1)
,
*other*
closely tracks the remote rural county of
*Turkana*
, in orange. Teal and red correspond to locations in
*Nyanza*
county or elsewhere in rural Kenya, respectively.
Results
---------
The Sarafu system supported over 400,000 transactions among more than 40,000 user accounts between January 2020 and June 2021. This resulted in the circulation of 293.7 million Sarafu, visualized in Fig.
[2](/articles/s41598-023-33184-1#Fig2)
as a network of monetary flow. The
*nodes*
are registered accounts, for which we know attributes such as the geographic area, livelihood category, and reported gender of the account holder. An
*edge*
from one account to another indicates that at least one transaction occurred across that link. The
*edge weight*
corresponds to the observed monetary flow along an edge, i.e., the total sum of transaction amounts across that link. The Sarafu flow network is a
*weighted, directed, time-aggregated network representation*
of the total circulation over the observation period, excluding system-run accounts. For details on the construction of the network, we refer to the "
[Data preparation](/articles/s41598-023-33184-1#Sec15)
" section of "
[Methods](/articles/s41598-023-33184-1#Sec14)
". The network visualization employs the same colors for geographic area as does Fig.
[1](/articles/s41598-023-33184-1#Fig1)
, revealing patterns suggestive of modular and geographically localized circulation.
**Figure 2**
[![figure 2](//media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-023-33184-1/MediaObjects/41598_2023_33184_Fig2_HTML.png)](/articles/s41598-023-33184-1/figures/2)
Visualization of the Sarafu flow network. Nodes are colored by the geographic area of the location reported for the account (see Fig.
[1](/articles/s41598-023-33184-1#Fig1)
for legend), and node size is proportional to the value of unweighted PageRank as computed for that node.
[Full size image](/articles/s41598-023-33184-1/figures/2)
In the remainder of this section, we share findings resulting from network analysis of the Sarafu flow network. The "
[Modular circulation](/articles/s41598-023-33184-1#Sec4)
" section considers sub-populations within which Sarafu was circulating, and their composition along lines of geographic area and livelihood category. In the "
[Underlying network structure](/articles/s41598-023-33184-1#Sec7)
" section, we consider the network structure that supports this circulation, including analyses of cyclic structure and network mixing patterns. The "
[Prominent Sarafu users](/articles/s41598-023-33184-1#Sec10)
" section compares relevant network centrality measures and describes the most prominent users of Sarafu.
###
Modular circulation
To more precisely understand the patterns of circulation present in the Sarafu flow network, we apply an especially suitable community detection method. The map equation
[32](/articles/s41598-023-33184-1#ref-CR32 "Rosvall, M. & Bergstrom, C. T. Maps of random walks on complex networks reveal community structure. Proc. Natl. Acad. Sci. 105, .
(2008).")
is defined in terms of flow networks and the associated Infomap algorithm
[33](/articles/s41598-023-33184-1#ref-CR33 "Bohlin, L., Edler, D., Lancichinetti, A. & Rosvall, M. Community Detection and Visualization of Networks with the Map Equation Framework. In eDing, Y., eRousseau, R. & eWolfram, D. (eds.) Measuring Scholarly Impact, 3-34,
(Springer International Publishing, Cham, 2014).")
groups nodes into hierarchical
*modules*
. Specifically, Infomap assigns nodes to modules (and sub-modules) within which a "random walker" on the network would stay for relatively long periods of time. In our case, the weights on the edges of the Sarafu flow network reflect real, observed flows of Sarafu and so the Infomap algorithm will seek to discover modules that contain especially much transaction volume. This identifies sub-populations within which Sarafu tended to
*circulate*
. For details, we refer to the "
[Circulation](/articles/s41598-023-33184-1#Sec16)
" section in "
[Methods](/articles/s41598-023-33184-1#Sec14)
".
The Infomap algorithm recovers a hierarchical, nested, modular structure to the Sarafu flow network. The hierarchical structure consists of top-level modules, sub-modules and sub-sub-modules at respectively the first, second and third level of the community hierarchy. Circulation of the Sarafu community currency was highly modular in that activity occurred almost exclusively within distinct sub-populations. At the first hierarchical level, 99.7% of the total transaction volume was contained within the five largest so-called
*top-level modules*
. Moreover, there are 37
*sub-modules*
composed of 100 or more accounts and these contained 96.5% of the total transaction volume. Only a small share of the overall circulation took place between the sub-populations defined at the second hierarchical level, and circulation within these sub-populations itself had a nested, modular structure. Indeed, the 455
*sub-sub-modules*
composed of 10 or more accounts capture 80% of the total transaction volume. Altogether, these findings suggest that the circulation of Sarafu was extremely modular over the observed period.
####
Geographic localization
We investigate the extent to which the distinct sub-populations discovered above localize in particular geographic areas. Figure
[3](/articles/s41598-023-33184-1#Fig3)
shows the geographic composition of the top-level modules--four of the five map directly onto one of the main areas labeled in the data:
*Kinango Kwale*
,
*Mukuru Nairobi*
,
*Kisauni Mombasa*
, or
*Turkana*
. Only one of the modules has substantial membership from several regions; its sub-modules are, however, also geographically delineated. This top-level module combines several less prominent localities, including in
*Kilifi*
, in
*Nyanza*
, and in two localities elsewhere in
*Nairobi*
. We conclude that the circulation of Sarafu was geographically localized over the observed period.
**Figure 3**
[![figure 3](//media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-023-33184-1/MediaObjects/41598_2023_33184_Fig3_HTML.png)](/articles/s41598-023-33184-1/figures/3)
Geographic composition of the five largest top-level modules and relevant numbered sub-modules.
[Full size image](/articles/s41598-023-33184-1/figures/3)
The top-level modules are amalgamations of circulation within sub-modules, which appear to correspond to geographic areas more granular than those labeled in the data. Indeed, raw reported locations were often quite precise and were converted to broader area labels in the anonymization that occurred prior to the publication of the data
[27](/articles/s41598-023-33184-1#ref-CR27 "Mattsson, C. E. S., Criscione, T. & Ruddick, W. O. Sarafu community inclusion currency, 2020-2021. Sci. Data
(2022).")
. Several of the sub-modules highlighted in Fig.
[3](/articles/s41598-023-33184-1#Fig3)
coincide with areas where early, physical community currencies were operating in the years before Sarafu became all-digital
[45](/articles/s41598-023-33184-1#ref-CR45 "Marion, C. Voucher Systems for Food Security: A Case Study on Kenya's Sarafu-Credit. Master's thesis, University of Copenhagen,
(2018).")
. Within
*Kinango Kwale*
, moreover, the sub-modules likely correspond to individual rural villages or clusters of villages
[15](/articles/s41598-023-33184-1#ref-CR15 "Ussher, L., Ebert, L., Gomez, G. M. & Ruddick, W. O. Complementary currencies for humanitarian aid. J. Risk Financ. Manag. 14, 557.
(2021).")
. Thus, circulation was geographically local, predominantly. We will further consider the sub-populations delineated by the Infomap sub-modules in subsequent analyses.
####
Diversity of economic activities
Now that we understand the modular structure and geographic localization of circulation, we consider the composition of the localized sub-populations with respect to economic activity. This is of particular interest to practitioners as it helps illustrate
*among whom*
Sarafu was circulating. There are 14 categories of economic activities into which user-reported livelihoods were grouped, the most common of which are
*labour*
in urban areas and
*farming*
in rural areas. Many other users (in both urban and rural areas) report selling
*food*
, running a
*shop*
, or providing
*transport*
.
Most notably, we see a mix of the different economic activities within the largest second-level sub-populations. Figure
[4](/articles/s41598-023-33184-1#Fig4)
illustrates the livelihood category given for each account in the 15 largest sub-modules identified by the Infomap algorithm. The largest sub-populations include several thousand accounts, and 13 of the 37 we consider have more than 1000 users. Notice that the livelihood mix is consistently diverse. To also give a sense of how this diversity is experienced from within sub-populations, we compute and report the view from the average user. The average user participates in a sub-module with around 2000 other users, and of these others, 66% report a category of work that is different from what they themselves report. Little diversity is lost as we consider even finer scales. The average user appears in a sub-sub-module with around 250 other users, 59% of whom do not share their same livelihood category. We conclude that the circulation of Sarafu involves a diversity of economic activities, even at the scale of a single village.
**Figure 4**
[![figure 4](//media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-023-33184-1/MediaObjects/41598_2023_33184_Fig4_HTML.png)](/articles/s41598-023-33184-1/figures/4)
Composition of discovered sub-modules (bars) in terms of user livelihoods (colors, as shown in legend).
[Full size image](/articles/s41598-023-33184-1/figures/4)
We also see that the composition of the sub-populations using Sarafu is substantively different in urban and rural areas. In Fig.
[4](/articles/s41598-023-33184-1#Fig4)
, the sub-modules where
*farming*
or
*fuel/energy*
are prominent are rural and composed of users reporting a location within
*Kinango Kwale*
, almost exclusively. Those where
*labour*
is prominent correspond to sub-populations localized primarily in urban or peri-urban areas including
*Mukuru Nairobi*
,
*Kisauni Mombasa*
, and
*Kilifi*
. The geographic aspect of circulation is further refined by means of the type of geographical area.
###
Underlying network structure
In this section, we consider the network structure underlying the circulation of Sarafu. Each of the sub-modules considered above in the "
[Modular circulation](/articles/s41598-023-33184-1#Sec4)
" section is associated with a sub-population of 100 or more accounts that defines a sub-network of 100 or more nodes. An (unweighted) edge from one account to another indicates that at least one transaction occurred across that edge. Node degree corresponds to an accounts' number of unique transaction partners, incoming and outgoing, in their same sub-population. In the "
[Cyclic structure](/articles/s41598-023-33184-1#Sec8)
" section we count the cycles present in the sub-networks, relating the presence of cycles to the notion of circulation and the sustainable operation of complementary currency systems. Next, the "
[Structural correlations](/articles/s41598-023-33184-1#Sec9)
" section quantifies network mixing patterns, relating degree disassortativity to the structural importance of local "hubs" in the sub-networks.
####
Cyclic structure
Network cycles may be key to understanding the conditions under which an area is, or overtime becomes, able to sustain local circulation
[15](/articles/s41598-023-33184-1#ref-CR15 "Ussher, L., Ebert, L., Gomez, G. M. & Ruddick, W. O. Complementary currencies for humanitarian aid. J. Risk Financ. Manag. 14, 557.
(2021).")
,
[21](/articles/s41598-023-33184-1#ref-CR21 "Iosifidis, G. et al. Cyclic motifs in the Sardex monetary network. Nat. Hum. Behav.
(2018).")
,
[22](/articles/s41598-023-33184-1#ref-CR22 "Fleischman, T. & Dini, P. Balancing the Payment System. (2020).
arXiv:2011.03517
[q-fin]")
. We explore the presence of cycles in the Sarafu sub-networks as compared to the expectation from a null model. We use two standard null models: Erdos-Renyi (ER) networks and random degree-preserving (RD) networks. ER networks have the same number of nodes and edges as the empirical network, but are wired randomly. Our RD networks preserve the indegree and outdegree sequences in expectation. For details we refer to the "
[Network cycles](/articles/s41598-023-33184-1#Sec17)
" section of "
[Methods](/articles/s41598-023-33184-1#Sec14)
".
Relative to the ER null model, nearly all of the sub-networks have many more cycles than expected at cycle lengths 2, 3, 4, and 5 (Fig.
[5](/articles/s41598-023-33184-1#Fig5)
, left). Extremely large magnitudes of the
*z*
-score may indicate that ER networks are not a suitable comparison. Indeed, short cycles are negligible in large Erdos-Renyi networks
[46](/articles/s41598-023-33184-1#ref-CR46 "Bianconi, G., Gulbahce, N. & Motter, A. E. Local structure of directed networks. Phys. Rev. Lett. 100, 118701.
(2008).")
. Figure
[5](/articles/s41598-023-33184-1#Fig5)
(right) shows the
*z*
-score of the cycle counts computed for each of the Sarafu sub-networks, relative to the RD null model. The values are positive and large for cycles of length 2 and 3 for most sub-networks, indicating cycle counts many standard deviations above expectation. Some sub-networks, especially in
*Mukuru Nairobi*
, also have unexpectedly many cycles of length 4 and 5. These findings are in line with prior findings for the Sardex currency in Sardinia, where a gradual increase in short cycles (relative to an RD null model) was observed over 2 years
[21](/articles/s41598-023-33184-1#ref-CR21 "Iosifidis, G. et al. Cyclic motifs in the Sardex monetary network. Nat. Hum. Behav.
(2018).")
. Notably, this is the case even though Kenya and Sardinia differ in their level of economic development, Sardex is aimed at businesses whereas Sarafu is aimed at individuals, and pandemic times are certainly different from regular times. Moreover, the currency management practices followed by the two providers are quite distinct
[21](/articles/s41598-023-33184-1#ref-CR21 "Iosifidis, G. et al. Cyclic motifs in the Sardex monetary network. Nat. Hum. Behav.
(2018).")
,
[27](/articles/s41598-023-33184-1#ref-CR27 "Mattsson, C. E. S., Criscione, T. & Ruddick, W. O. Sarafu community inclusion currency, 2020-2021. Sci. Data
(2022).")
. Short cycles are a prominent network connectivity pattern in the circulation of Sarafu, and perhaps of (community) currencies more generally.
**Figure 5**
[![figure 5](//media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-023-33184-1/MediaObjects/41598_2023_33184_Fig5_HTML.png)](/articles/s41598-023-33184-1/figures/5)
Relative cycle counts for each sub-network, at different cycle lengths. Points correspond to sub-modules, and are colored based on the dominant geographic area of users placed in the top-level module to which it belongs. Five observations are omitted from the ER plot, as the logarithmic scale cannot represent small negative
*z*
-scores. These are confined to two sub-modules, where one or no cycles occur at higher cycle lengths.
[Full size image](/articles/s41598-023-33184-1/figures/5)
####
Structural correlations
Degree disassortativity is an expected feature of currency networks
[19](/articles/s41598-023-33184-1#ref-CR19 "Kondor, D., Posfai, M., Csabai, I. & Vattay, G. Do the rich get richer? An empirical analysis of the bitcoin transaction network. PLoS ONE 9, e86197.
(2014).")
,
[36](/articles/s41598-023-33184-1#ref-CR36 "Campajola, C., D'Errico, M. & Tessone, C. J. MicroVelocity: rethinking the Velocity of Money for digital currencies.
arXiv:2201.13416
[physics, q-fin] (2022).")
and of economic networks, more broadly
[34](/articles/s41598-023-33184-1#ref-CR34 "Fujiwara, Y. & Aoyama, H. Large-scale structure of a nation-wide production network. Eur. Phys. J. B 77, 565-580.
(2010).")
,
[35](/articles/s41598-023-33184-1#ref-CR35 "Mattsson, C. E. S. et al. Functional structure in production networks. Front. Big Data
(2021).")
. In networks with this property, high-degree nodes generally interact with low-degree nodes, not other high-degree nodes. In avoiding one another, high-degree nodes tend to become "local hubs" that are prominent especially with respect to nearby nodes (i.e., their network neighborhood) that are predominantly of low-degree. Recall also that Sarafu sub-modules are diverse with respect to the livelihood reported by accounts ("
[Diversity of economic activities](/articles/s41598-023-33184-1#Sec6)
" section). Here we consider these and other structural correlations that help us better understand the circulation of Sarafu. Since the overall influence of account attributes on the Sarafu flow network is limited by the constraints of geography, and may be heterogeneous across sub-populations, we consider degree and attribute assortativities across the Sarafu sub-networks. For details we refer to the "
[Network mixing patterns](/articles/s41598-023-33184-1#Sec18)
" section of "
[Methods](/articles/s41598-023-33184-1#Sec14)
".
Table
[1](/articles/s41598-023-33184-1#Tab1)
reports the average, the median, and the range for each property as computed on the undirected version of each sub-network. We find substantial disassortativity in degree across nearly all sub-networks. As expected, we also find that attribute assortativity is consistently low along the dimension of livelihood category. The consistency of these observations across sub-populations suggests that there may be important regularities in the structural correlations of networks that support the local circulation of community currencies such as Sarafu.
**Table 1 Network statistics and feature assortativity across the 37 sub-modules with 100 or more nodes.**
[Full size table](/articles/s41598-023-33184-1/tables/1)
Correlations with respect to
*gender*
and
*registration date*
in the structure of the sub-networks can also be substantial, although these effects are not consistent across sub-populations. Again from Table
[1](/articles/s41598-023-33184-1#Tab1)
, attribute assortativity on gender is present in about half of the 37 sub-populations and is substantial in several. This may be related to the activity of community-based savings and investment groups, where women's participation is high
[47](/articles/s41598-023-33184-1#ref-CR47 "Avanzo, S. E. A relational analysis of sarafu network: Emergence of a monetary ecosystem for the prosperity of the communities. Master's thesis, University of Torino, Torino (2019).")
,
[48](/articles/s41598-023-33184-1#ref-CR48 "Rasulova, S., Storchi, S., Karim, M., Moratti, M. & Johnson, S. Impact evaluation of FSD Kenya's savings groups project (Tech. Rep, FSD Kenya, 2017).")
. Within Sarafu, such groups provide opportunities to transact assortatively on gender. Gender assortativity in payment networks may also reflect, for instance, gendered economic roles in ways that deserve further study. Strong correlations in registration date also appear in several sub-networks, indicating a cohort effect. For example, during targeted introductions as described in the "
[Data preparation](/articles/s41598-023-33184-1#Sec15)
" section, groups of users who share latent economic ties would together adopt Sarafu over a relatively short period of time. Correlations by cohort are likely to appear in any digital payment system where use is voluntary and adoption can be coordinated.
###
Prominent Sarafu users
Local hubs play a key structural role in the circulation of Sarafu, and it is important to understand who takes on such prominent positions. We ask what features are especially consistent among accounts with high network centrality, now across the entire Sarafu flow network. In the "
[Identifying prominent users](/articles/s41598-023-33184-1#Sec11)
" section we consider an account's number of unique transaction partners, transaction volumes, and especially relevant network centrality measures. Next, the "
[Characterizing prominent users](/articles/s41598-023-33184-1#Sec12)
" section asks what features of Sarafu accounts are strongly and consistently associated with high network centrality.
####
Identifying prominent users
As a first step towards understanding prominent Sarafu users, we consider distributions of relevant account statistics. Figure
[6](/articles/s41598-023-33184-1#Fig6)
(left) shows the empirical distributions of node degree, binned on a logarithmic scale. Node degree corresponds to an account's number of unique transaction partners. We note that values are highly heterogeneous across accounts; the distribution is right-skewed and there is a "heavy" or "thick" tail indicating that a small share of accounts has orders of magnitude more unique transaction partners than do most accounts. Indeed, the in- and out- high-degree tails both fit a Pareto distribution with power-law exponent of 2.9. For details we refer to the "
[High-degree tail estimation](/articles/s41598-023-33184-1#Sec21)
" section of "
[Methods](/articles/s41598-023-33184-1#Sec14)
".
**Figure 6**
[![figure 6](//media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-023-33184-1/MediaObjects/41598_2023_33184_Fig6_HTML.png)](/articles/s41598-023-33184-1/figures/6)
Distribution of degree (left) and weighted degree (right) for the Sarafu flow network. Probability densities are scaled such that nodes with a value of zero shrink the distribution total, as zero cannot be plotted on a logarithmic scale.
[Full size image](/articles/s41598-023-33184-1/figures/6)
The Sarafu flow network has hubs, in that a small share of nodes are especially prominent. Moreover, the power-law tail indicates the likely presence of so-called "preferential attachment" as the Sarafu network grew
[49](#ref-CR49 "Barabasi, A.-L. & Albert, R. Emergence of scaling in random networks. Science 286, 509-512.
(1999).")
,
[50](#ref-CR50 "Barabasi, A.-L. Network Science 1st edn. (Cambridge University Press, 2016).")
,
[51](/articles/s41598-023-33184-1#ref-CR51 "Lynn, C. W., Holmes, C. M. & Palmer, S. E. Emergent scale-free networks,
(2022).")
. Under such dynamics, accounts with many unique transaction partners are proportionately more likely to attract or create additional connections. Because degree is disassortative (see the "
[Structural correlations](/articles/s41598-023-33184-1#Sec9)
" section), we also know that high-degree nodes are dispersed across the network and likely to be what we call "local hubs" prominent among predominantly low-degree neighbors.
We also see that a relatively small number of account holders spend orders of magnitude more Sarafu than do the bulk of the users. Figure
[6](/articles/s41598-023-33184-1#Fig6)
(right) shows binned empirical distributions of weighted degree, which corresponds to total transaction volumes into and out of accounts. These values are spread over a wide range and also exhibit a heavy tail. Reflecting the underlying accounting consistency present in networks of monetary flow, weighted in- and out- degree are exceptionally highly correlated (Fig.
[7](/articles/s41598-023-33184-1#Fig7)
). Accounts must receive large amounts of Sarafu in order to spend large amounts of Sarafu.
**Figure 7**
[![figure 7](//media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-023-33184-1/MediaObjects/41598_2023_33184_Fig7_HTML.png)](/articles/s41598-023-33184-1/figures/7)
Pearson correlation between values for degree, weighted degree, and centrality metrics.
[Full size image](/articles/s41598-023-33184-1/figures/7)
More generally, degree and weighted degree are not interchangeable, capturing different notions of prominence in the system. Figure
[7](/articles/s41598-023-33184-1#Fig7)
shows the Pearson correlation between node degree, weighted degree, and two especially relevant centrality metrics. The unweighted PageRank algorithm produces a non-zero value for each node that is correlated with both the in- and out- degree; this makes it a practical measure for downstream tasks involving the unweighted network. Unweighted PageRank is closely related to the indegree
[52](/articles/s41598-023-33184-1#ref-CR52 "Litvak, N., Scheinhardt, W. R. W. & Volkovich, Y. In-Degree and PageRank: Why Do They Follow Similar Power Laws?. Internet Mathematics 4, 175-198.
(2007).")
,
[53](/articles/s41598-023-33184-1#ref-CR53 "Fortunato, S., Bogun a, M., Flammini, A. & Menczer, F. Approximating PageRank from In-Degree. In eAiello, W., eBroder, A., eJanssen, J. & eMilios, E. (eds.) Algorithms and Models for the Web-Graph, Lecture Notes in Computer Science, 59-71,
(Springer, Berlin, Heidelberg, 2008).")
. More interesting is the weighted PageRank, which captures something distinct from the in- or out- degree, the weighted in- or out- degree, and unweighted PageRank. Noteworthy is that values of weighted PageRank are interpretable as the share of system funds that an account would eventually control, if the observed dynamics were to continue. Further details, including an empirical calibration to account balances, are presented in the "
[Network centrality](/articles/s41598-023-33184-1#Sec19)
" section in "
[Methods](/articles/s41598-023-33184-1#Sec14)
".
####
Characterizing prominent users
To characterize prominent users of the Sarafu system, we ask what features are especially consistent among accounts with high network centrality. Figure
[8](/articles/s41598-023-33184-1#Fig8)
illustrates the regression coefficients on account properties when PageRank and weighted, inflow-adjusted PageRank are used as outcome variables. Ordinary least squares (OLS) provides an estimated statistical contribution for each account feature, while Elastic Net (EN) incorporates regularization to highlight only those features most consistently associated with centrality. For details, we refer to the "
[Linear regression](/articles/s41598-023-33184-1#Sec22)
" section in "
[Methods](/articles/s41598-023-33184-1#Sec14)
".
**Figure 8**
[![figure 8](//media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-023-33184-1/MediaObjects/41598_2023_33184_Fig8_HTML.png)](/articles/s41598-023-33184-1/figures/8)
Regression coefficients for linear models fitting account features to centrality measures, using Ordinary least squares (OLS) and Elastic Net (EN). For the three categorical predictors, the reference categories are accounts that report a location in
*Kinango Kwale*
, report selling
*food*
, and do not report a gender.
[Full size image](/articles/s41598-023-33184-1/figures/8)
PageRank and weighted inflow-adjusted PageRank capture distinct aspects of node importance, but are positively and negatively associated with many of the same account features. Most strongly and consistently associated with high network centrality are accounts held by
*savings*
groups. Indeed, community-based savings and investment groups are a key feature of local economies in Kenya and of the Sarafu system (as noted in the "
[Data preparation](/articles/s41598-023-33184-1#Sec15)
" section in "
[Methods](/articles/s41598-023-33184-1#Sec14)
"). The size of this category is quite small, however, containing only 264 accounts. The number of
*faith*
leaders is even smaller, and some appear to play an especially prominent role in the local circulation supported by this community currency.
The other regression coefficients in Fig.
[8](/articles/s41598-023-33184-1#Fig8)
reveal additional nuances among some of the largest categories of users. Accounts that were created
*prior*
to the consolidation of Sarafu, which occurred as the data collection period began, are consistently associated with high network centrality; early adopters show a higher tendency to be prominent users. This is consistent with the presence of preferential attachment in this system, as noted in the previous section. We also find that account holders reporting their gender as
*female*
are associated with higher centrality in the Sarafu flow network--this prominence of women is remarkable. In fact, it conforms to qualitative accounts from field studies in Kinango, Kwale that report strong participation of women, and women's leadership, within community-based savings and investment groups that use Sarafu
[47](/articles/s41598-023-33184-1#ref-CR47 "Avanzo, S. E. A relational analysis of sarafu network: Emergence of a monetary ecosystem for the prosperity of the communities. Master's thesis, University of Torino, Torino (2019).")
. This has also been noted about savings groups in Kenya, more generally
[48](/articles/s41598-023-33184-1#ref-CR48 "Rasulova, S., Storchi, S., Karim, M., Moratti, M. & Johnson, S. Impact evaluation of FSD Kenya's savings groups project (Tech. Rep, FSD Kenya, 2017).")
. With respect to geography, recall that
*Mukuru Nairobi*
and
*Kisauni Mombasa*
refer to the site of targeted introductions in spring 2020 and early 2021, respectively. Timing appears to have made a substantial difference: the second intervention did not spur large transaction volumes, while those reporting a location within
*Mukuru Nairobi*
have higher network centrality (on average) than users in
*Kinango Kwale*
(the reference category). Perhaps most interestingly,
*farming*
is associated with lower centrality than other reported economic activities. Non-farming activities (e.g. selling
*food*
, running a
*shop*
, or providing
*labour*
) appear to be "central" to local economies even in areas of rural Kenya, such as
*Kinango Kwale*
, that rely heavily on subsistence agriculture.
Discussion
------------
Our study of the Sarafu system complements and corroborates a growing body of work informing policy on alternative interventions in marginalized areas
[15](/articles/s41598-023-33184-1#ref-CR15 "Ussher, L., Ebert, L., Gomez, G. M. & Ruddick, W. O. Complementary currencies for humanitarian aid. J. Risk Financ. Manag. 14, 557.
(2021).")
,
[54](#ref-CR54 "Ruddick, W. O., Richards, M. A. & Bendell, J. Complementary currencies for sustainable development in Kenya: The case of the bangla-pesa. Int. J. Commun. Curr. Res. 19, 13.
(2015).")
,
[55](#ref-CR55 "Mauldin, R. L. Local currency for community development: Policy barriers and support. J. Commun. Pract. 23, 462-476.
(2015).")
,
[56](#ref-CR56 "Fuders, F. Smarter Money for Smarter Cities: How Regional Currencies Can Help to Promote a Decentralised and Sustainable Regional Development. In eDick, E., eGaesing, K., eInkoom, D. & eKausel, T. (eds.) Decentralisation and Regional Development: Experiences and Lessons from Four Continents over Three Decades, Springer Geography, 155-185,
(Springer International Publishing, 2016).")
,
[57](/articles/s41598-023-33184-1#ref-CR57 "eGomez, G. M. (ed.) Monetary Plurality in Local, Regional and Global Economies (Routledge, 2018).")
. In particular, our findings shed new light on the conditions under which community currencies might form part of successful humanitarian or development interventions. The circulation of Sarafu remained modular and local even as the system saw dramatic growth in its user base and accommodated large spikes in transaction volumes. In areas where local economic activities are already diverse, the rapid deployment (or scaling up) of community currency operations may be able to support the aims of a broader humanitarian response. Over longer periods of time, and in more peripheral areas, community currencies support economic development to the extent that they encourage diverse productive activities and strengthen short, local supply chains that keep money within a community
[15](/articles/s41598-023-33184-1#ref-CR15 "Ussher, L., Ebert, L., Gomez, G. M. & Ruddick, W. O. Complementary currencies for humanitarian aid. J. Risk Financ. Manag. 14, 557.
(2021).")
. Here it is useful to note that community-based financial institutions, and, in some cases, faith leaders, played a key role in the Sarafu system. Future initiatives would likely benefit from finding ways to better assist in the discovery or creation of short cycles in local economies. Practically speaking, it may be possible to identify "missing links" in local economic or financial networks such that policymakers and organizers might intervene to close cycles by brokering among local businesses
[22](/articles/s41598-023-33184-1#ref-CR22 "Fleischman, T. & Dini, P. Balancing the Payment System. (2020).
arXiv:2011.03517
[q-fin]")
,
[37](/articles/s41598-023-33184-1#ref-CR37 "Fleischman, T., Dini, P. & Littera, G. Liquidity-saving through obligation-clearing and mutual credit: An effective monetary innovation for SMEs in times of crisis. J. Risk Financ. Manag. 13, 295.
(2020).")
.
More broadly, this work has demonstrated that a network approach can unveil meaningful patterns and extract relevant insights about the circulation of money from digital transaction records. Our contextually relevant findings demonstrate the explanatory power of representing circulation as a network of monetary flow. When applied to such networks, walk- and flow- based network analysis methods (e.g., PageRank and Infomap) produce outputs that are readily interpretable in terms of circulation and account balances. Notably, these methods rely on scalable algorithms meaning that our approach can be applied to study sizeable currency systems where transaction data is recorded in digital form. This includes other community currencies
[6](/articles/s41598-023-33184-1#ref-CR6 "Frankova, E., Fousek, J., Kala, L. & Labohy, J. Transaction network analysis for studying Local Exchange Trading Systems (LETS): Research potentials and limitations. Ecol. Econ. 107, 266-275.
(2014).")
,
[16](/articles/s41598-023-33184-1#ref-CR16 "Muralt, V. The Woergl experiment with depreciating money. Ann. Public Cooper. Econ. 10, 48-57.
(1934).")
,
[17](/articles/s41598-023-33184-1#ref-CR17 "Kichiji, N. & Nishibe, M. Network analyses of the circulation flow of community currency. Evol. Inst. Econ. Rev. 4, 267-300.
(2008).")
,
[21](/articles/s41598-023-33184-1#ref-CR21 "Iosifidis, G. et al. Cyclic motifs in the Sardex monetary network. Nat. Hum. Behav.
(2018).")
as well as major global cryptocurrencies
[19](/articles/s41598-023-33184-1#ref-CR19 "Kondor, D., Posfai, M., Csabai, I. & Vattay, G. Do the rich get richer? An empirical analysis of the bitcoin transaction network. PLoS ONE 9, e86197.
(2014).")
,
[20](/articles/s41598-023-33184-1#ref-CR20 "ElBahrawy, A., Alessandretti, L., Kandler, A., Pastor-Satorras, R. & Baronchelli, A. Evolutionary dynamics of the cryptocurrency market. R. Soc. Open Sci. 4, 170623 (2017).")
,
[26](/articles/s41598-023-33184-1#ref-CR26 "Nadini, M. Emergence and structure of decentralised trade networks around dark web marketplaces. Sci. Rep. 9, 1-9 (2022).")
,
[36](/articles/s41598-023-33184-1#ref-CR36 "Campajola, C., D'Errico, M. & Tessone, C. J. MicroVelocity: rethinking the Velocity of Money for digital currencies.
arXiv:2201.13416
[physics, q-fin] (2022).")
. Recent methodological advances
[10](/articles/s41598-023-33184-1#ref-CR10 "Mattsson, C. E. S. & Takes, F. W. Trajectories through temporal networks. Appl. Netw. Sci. 6, 1-31.
(2021).")
,
[58](/articles/s41598-023-33184-1#ref-CR58 "Kawamoto, T. Single-trajectory map equation.
arXiv:2203.04044
[physics] (2022).")
promise to extend applicability also to payment systems that are not themselves full currency systems, such as mobile money systems
[10](/articles/s41598-023-33184-1#ref-CR10 "Mattsson, C. E. S. & Takes, F. W. Trajectories through temporal networks. Appl. Netw. Sci. 6, 1-31.
(2021).")
,
[59](/articles/s41598-023-33184-1#ref-CR59 "Blumenstock, J. E., Eagle, N. & Fafchamps, M. Airtime transfers and mobile communications: Evidence in the aftermath of natural disasters. J. Dev. Econ. 120, 157-181.
(2016).")
,
[60](/articles/s41598-023-33184-1#ref-CR60 "Economides, N. & Jeziorski, P. Mobile Money in Tanzania. Mark. Sci. 36, 815-837.
(2017).")
, large value payment systems
[61](#ref-CR61 "SoramAki, K., Bech, M. L., Arnold, J., Glass, R. J. & Beyeler, W. E. The topology of interbank payment flows. Physica A Stat. Mech. Appl. 379, 317-333.
(2007).")
,
[62](#ref-CR62 "Iori, G., De Masi, G., Precup, O. V., Gabbi, G. & Caldarelli, G. A network analysis of the Italian overnight money market. J. Econ. Dyn. Control 32, 259-278.
(2008).")
,
[63](#ref-CR63 "Kyriakopoulos, F., Thurner, S., Puhr, C. & Schmitz, S. W. Network and eigenvalue analysis of financial transaction networks. Eur. Phys. J. B 71, 523.
(2009).")
,
[64](#ref-CR64 "Bech, M. L. & Garratt, R. J. Illiquidity in the interbank payment system following wide-scale disruptions. J. Money Credit Bank. 44, 903-929.
(2012).")
,
[65](#ref-CR65 "Barucca, P. & Lillo, F. The organization of the interbank network and how ECB unconventional measures affected the e-MID overnight market. CMS 15, 33-53.
(2018).")
,
[66](#ref-CR66 "Rubio, J., Barucca, P., Gage, G., Arroyo, J. & Morales-Resendiz, R. Classifying payment patterns with artificial neural networks: An autoencoder approach. Latin Am. J. Central Bank. 1, 100013.
(2020).")
,
[67](/articles/s41598-023-33184-1#ref-CR67 "Bianchi, F., Bartolucci, F., Peluso, S. & Mira, A. Longitudinal networks of dyadic relationships using latent trajectories: Evidence from the European interbank market. J. R. Stat. Soc.: Ser. C (Appl. Stat.) 69, 711-739.
(2020).")
, major banks
[12](/articles/s41598-023-33184-1#ref-CR12 "Carvalho, V. M. et al. Tracking the COVID-19 crisis with high-resolution transaction data. R. Soc. Open Sci. 8, 210218.
(2021).")
,
[68](#ref-CR68 "Zanin, M., Papo, D., Romance, M., Criado, R. & Moral, S. The topology of card transaction money flows. Physica A 462, 134-140.
(2016).")
,
[69](#ref-CR69 "Rendon de la Torre, S., Kalda, J., Kitt, R. & Engelbrecht, J. On the topologic structure of economic complex networks: Empirical evidence from large scale payment network of Estonia. Chaos, Solitons & Fractals 90, 18-27,
(2016).")
,
[70](/articles/s41598-023-33184-1#ref-CR70 "Ialongo, L. N. et al. Reconstructing firm-level interactions: the Dutch input-output network.
arXiv:2111.15248
[physics, q-fin] (2021).")
, and, in an exciting development, centralized national payment infrastructures
[71](#ref-CR71 "Triepels, R., Daniels, H. & Heijmans, R. Detection and Explanation of Anomalous Payment Behavior in Real-Time Gross Settlement Systems. In eHammoudi, S.,emialek, M., eCamp, O. & eFilipe, J. (eds.) Enterprise Information Systems, Lecture Notes in Business Information Processing, 145-161,
(Springer International Publishing, 2018).")
,
[72](#ref-CR72 "Sabetti, L. & Heijmans, R. Shallow or deep? Training an autoencoder to detect anomalous flows in a retail payment system. Latin Am. J. Central Bank. 2, 100031.
(2021).")
,
[73](/articles/s41598-023-33184-1#ref-CR73 "Arevalo, F. et al. Identifying clusters of anomalous payments in the salvadorian payment system. Latin Am. J. Central Bank. 3, 100050.
(2022).")
or central bank digital currencies
[74](/articles/s41598-023-33184-1#ref-CR74 "Bank of Canada et al. Central bank digital currencies: executive summary. Tech. Rep., Bank for International Settlements (2021).")
.
This study considers the aggregated circulation of Sarafu over the full observation period, and applies especially suitable network analysis techniques using openly available tools. While this already presents interesting findings, networks of monetary flow are static representations and potentially interesting temporal or sequential information is lost
[10](/articles/s41598-023-33184-1#ref-CR10 "Mattsson, C. E. S. & Takes, F. W. Trajectories through temporal networks. Appl. Netw. Sci. 6, 1-31.
(2021).")
,
[36](/articles/s41598-023-33184-1#ref-CR36 "Campajola, C., D'Errico, M. & Tessone, C. J. MicroVelocity: rethinking the Velocity of Money for digital currencies.
arXiv:2201.13416
[physics, q-fin] (2022).")
,
[75](#ref-CR75 "Saramaki, J. & Holme, P. Exploring temporal networks with greedy walks. Eur. Phys. J. B 88, 334.
(2015).")
,
[76](#ref-CR76 "LaRock, T., Scholtes, I. & Eliassi-Rad, T. Sequential motifs in observed walks. J. Complex Netw. 10, cnac036.
(2022).")
,
[77](/articles/s41598-023-33184-1#ref-CR77 "Mattsson, C. E. S., Luedtke, A. & Takes, F. W. Measuring the Velocity of Money,
(2022).")
. Several changes to the system occurred within this period and could be studied in future work
[27](/articles/s41598-023-33184-1#ref-CR27 "Mattsson, C. E. S., Criscione, T. & Ruddick, W. O. Sarafu community inclusion currency, 2020-2021. Sci. Data
(2022).")
. Transaction processes are compelling examples of real-world walk processes
[10](/articles/s41598-023-33184-1#ref-CR10 "Mattsson, C. E. S. & Takes, F. W. Trajectories through temporal networks. Appl. Netw. Sci. 6, 1-31.
(2021).")
, and we hope that the interpretability of walk-based network analysis methods as applied to our static representation of Sarafu can help motivate the development of equally interpretable methods for dynamic representations. It may be possible, for instance, to produce measures of the fidelity between the temporal network that fully describes a transaction process and its static representation, as has been done for interaction networks in the context of spreading processes
[78](/articles/s41598-023-33184-1#ref-CR78 "Lentz, H. H. K., Selhorst, T. & Sokolov, I. M. Unfolding accessibility provides a macroscopic approach to temporal networks. Phys. Rev. Lett. 110, 118701.
(2013).")
. Indeed, reproducing observed trajectories (from, for example, a real-world walk process) using a static network representation is already the logic underlying multi-order models of complex systems
[10](/articles/s41598-023-33184-1#ref-CR10 "Mattsson, C. E. S. & Takes, F. W. Trajectories through temporal networks. Appl. Netw. Sci. 6, 1-31.
(2021).")
,
[79](/articles/s41598-023-33184-1#ref-CR79 "Xu, J., Wickramarathne, T. L. & Chawla, N. V. Representing higher-order dependencies in networks. Sci. Adv. 2, e1600028.
(2016).")
,
[80](/articles/s41598-023-33184-1#ref-CR80 "Lambiotte, R., Rosvall, M. & Scholtes, I. From networks to optimal higher-order models of complex systems. Nat. Phys.
(2019).")
. Future methodological advances would also be welcome in the analysis of network cycles and of log-normal distributions with Pareto tails.
Studies on additional systems and further methodological development could bring us towards a future where entire economies might be studied as (interconnected, dynamic) networks of monetary flow. Notably, degree disassortativity has been found across many economic networks
[19](/articles/s41598-023-33184-1#ref-CR19 "Kondor, D., Posfai, M., Csabai, I. & Vattay, G. Do the rich get richer? An empirical analysis of the bitcoin transaction network. PLoS ONE 9, e86197.
(2014).")
,
[34](#ref-CR34 "Fujiwara, Y. & Aoyama, H. Large-scale structure of a nation-wide production network. Eur. Phys. J. B 77, 565-580.
(2010).")
,
[35](#ref-CR35 "Mattsson, C. E. S. et al. Functional structure in production networks. Front. Big Data
(2021).")
,
[36](/articles/s41598-023-33184-1#ref-CR36 "Campajola, C., D'Errico, M. & Tessone, C. J. MicroVelocity: rethinking the Velocity of Money for digital currencies.
arXiv:2201.13416
[physics, q-fin] (2022).")
and short cycles are over-represented also in at least one other complementary currency system
[21](/articles/s41598-023-33184-1#ref-CR21 "Iosifidis, G. et al. Cyclic motifs in the Sardex monetary network. Nat. Hum. Behav.
(2018).")
despite considerable contextual differences. This is some indication that there may be important network-structural regularities underlying the circulation of money, which deserve to be further explored across currency systems large and small.
Methods
---------
The "
[Data preparation](/articles/s41598-023-33184-1#Sec15)
" section provides a detailed description of the portion of the raw Sarafu data used in constructing our timeseries and our network of monetary flow, plus three peculiarities of the Sarafu currency system that are of relevance to the implementation or interpretation of our analyses. Network analysis methods are used to quantitatively analyze the Sarafu flow network. The "
[Circulation](/articles/s41598-023-33184-1#Sec16)
" section articulates how the map equation framework captures and quantifies the circulation of money given a network of monetary flow. The "
[Network centrality](/articles/s41598-023-33184-1#Sec19)
" section describes walk-based measures of network centrality for characterizing prominent users. The "
[Network cycles](/articles/s41598-023-33184-1#Sec17)
" and "
[Network mixing patterns](/articles/s41598-023-33184-1#Sec18)
" sections introduce relative cycle counts and assortativity as tools to analyse the structure of the underlying, unweighted network.
###
Data preparation
The Sarafu CIC data
[31](/articles/s41598-023-33184-1#ref-CR31 "Ruddick, W. O. Sarafu Community Inclusion Currency, 2020-2021, (2021).
")
includes a transaction dataset and an account dataset collected from January 25th, 2020 to June 15th 2021. The raw form of this data has previously been described in detail
[27](/articles/s41598-023-33184-1#ref-CR27 "Mattsson, C. E. S., Criscione, T. & Ruddick, W. O. Sarafu community inclusion currency, 2020-2021. Sci. Data
(2022).")
. The transaction records are labeled with a transaction type, and we consider the
standard
transactions. Figure
[1](/articles/s41598-023-33184-1#Fig1)
shows the total volume of such transactions for each complete month. Note that the value of one Sarafu was understood by users to be about that of a Kenyan Shilling, though actual exchange was facilitated only in very limited instances. The Sarafu flow network is constructed from the
standard
transactions that occurred within the Sarafu system over the observation period. Basic network statistics are shown in Table
[2](/articles/s41598-023-33184-1#Tab2)
. As noted in the main text, the
*nodes*
are registered accounts, for which the account dataset includes relevant account features (detailed below). An
*edge*
from one account to another indicates that at least one
standard
transaction occurred across that link. The
*edge weight*
corresponds to the total sum of all
standard
transaction amounts across that link. Then, system-run accounts are filtered out from the Sarafu flow network. Regular accounts who neither sent nor received even a single
standard
transaction from another regular account are isolates, which we also exclude from the network. Note that the giant connected component (GCC) encompasses nearly all the nodes, meaning that the majority of users are indirectly connected through their transactions.
**Table 2 Basic statistics for the network of aggregated
standard
transactions, the Sarafu flow network, and its giant connected component (GCC).**
[Full size table](/articles/s41598-023-33184-1/tables/2)
####
Account features
The account dataset includes the registration date and reported gender of the account holder as well as categorical labels derived from reported information on home location and livelihood. Mattsson, Criscione, & Ruddick
[27](/articles/s41598-023-33184-1#ref-CR27 "Mattsson, C. E. S., Criscione, T. & Ruddick, W. O. Sarafu community inclusion currency, 2020-2021. Sci. Data
(2022).")
provide a descriptive overview of each account feature. Notably, each geographic area is a combination of user-reported localities that could be quite precise. Ussher et al.
[15](/articles/s41598-023-33184-1#ref-CR15 "Ussher, L., Ebert, L., Gomez, G. M. & Ruddick, W. O. Complementary currencies for humanitarian aid. J. Risk Financ. Manag. 14, 557.
(2021).")
present an overview of the user-reported work activities that make up the livelihood categories. System-run accounts are those labeled with
*system*
in place of the node attribute indicating the user's livelihood, or assigned a formal role as an
admin
or
vendor
account.
####
Savings and investment groups
Community-based savings and investment groups are common in Kenya
[81](/articles/s41598-023-33184-1#ref-CR81 "Biggart, N. W. Banking on each other: The situational logic of rotating savings and credit associations. Adv. Qual. Organ. Res. 3, 129-153 (2001).")
,
[82](/articles/s41598-023-33184-1#ref-CR82 "Central Bank of Kenya, Kenya National Bureau of Statistics & FSD Kenya. Inclusive Finance? Headline findings from FinAccess 2019. Tech. Rep., FSD Kenya (2019).")
and a feature of many communities that use Sarafu, specifically
[15](/articles/s41598-023-33184-1#ref-CR15 "Ussher, L., Ebert, L., Gomez, G. M. & Ruddick, W. O. Complementary currencies for humanitarian aid. J. Risk Financ. Manag. 14, 557.
(2021).")
,
[45](/articles/s41598-023-33184-1#ref-CR45 "Marion, C. Voucher Systems for Food Security: A Case Study on Kenya's Sarafu-Credit. Master's thesis, University of Copenhagen,
(2018).")
. Several hundreds of so-called "chamas" are present in the data, many with the label
*savings*
in place of the node attribute indicating the user's livelihood. For a time, Sarafu operator Grassroots Economics also had a program whereby field staff would verify the operation of community-based groups and provide additional support to verified "chamas"
[27](/articles/s41598-023-33184-1#ref-CR27 "Mattsson, C. E. S., Criscione, T. & Ruddick, W. O. Sarafu community inclusion currency, 2020-2021. Sci. Data
(2022).")
. Verified groups were conduits for development initiatives and humanitarian aid on several occasions, some of which involved payments made to system-run accounts, in Sarafu, in exchange for donated food, items, or Kenyan Shillings.
####
Targeted introductions
There were two so-called targeted introductions during the observation period, conducted by the Kenyan Red Cross in collaboration with Grassroots Economics
[27](/articles/s41598-023-33184-1#ref-CR27 "Mattsson, C. E. S., Criscione, T. & Ruddick, W. O. Sarafu community inclusion currency, 2020-2021. Sci. Data
(2022).")
. These consisted of outreach efforts and training programs in specific areas. The Mukuru kwa Njenga slum in Nairobi was the site of the first; educational and outreach programs began in April 2020. Soon thereafter, this intervention was scaled up in response to the COVID-19 pandemic and related economic disruptions. Again, community currencies tend to gain in popularity during times of economic and financial crisis
[13](/articles/s41598-023-33184-1#ref-CR13 "Stodder, J. Complementary credit networks and macroeconomic stability: Switzerland's Wirtschaftsring. J. Econ. Behav. Organ. 72, 79-95.
(2009).")
,
[29](/articles/s41598-023-33184-1#ref-CR29 "Stodder, J. & Lietaer, B. The macro-stability of Swiss WIR-Bank credits: Balance, velocity, and leverage. Comp. Econ. Stud. 58, 570-605.
(2016).")
,
[30](/articles/s41598-023-33184-1#ref-CR30 "Zeller, S. Economic advantages of community currencies. J. Risk Financ. Manag. 13, 271.
(2020).")
. A second Red Cross intervention began in in Kisauni, Mombasa in early 2021. This resulted in a wave of account creations
[27](/articles/s41598-023-33184-1#ref-CR27 "Mattsson, C. E. S., Criscione, T. & Ruddick, W. O. Sarafu community inclusion currency, 2020-2021. Sci. Data
(2022).")
and rising activity by accounts with location
*Kisauni Mombasa*
[15](/articles/s41598-023-33184-1#ref-CR15 "Ussher, L., Ebert, L., Gomez, G. M. & Ruddick, W. O. Complementary currencies for humanitarian aid. J. Risk Financ. Manag. 14, 557.
(2021).")
. However, as we can see in Fig.
[1](/articles/s41598-023-33184-1#Fig1)
, overall transaction volumes did not rise as dramatically during this targeted introduction as they did during the first.
####
Currency creation
The digital payment system, as a whole, saw inflows when new units of Sarafu were created. For instance, newly-created accounts would receive an initial disbursement of 400 Sarafu, later reduced to 50 Sarafu. New users could receive an additional sum if and when they verified their account information with staff at Grassroots Economics. Existing users could also receive newly created funds, such as in reward for transaction activity and as bonus for referring others. These and other non-
standard
inflows are summarized as an aggregated value in the account dataset. We refer to prior work for a full account of currency management and system administration over the data collection period
[27](/articles/s41598-023-33184-1#ref-CR27 "Mattsson, C. E. S., Criscione, T. & Ruddick, W. O. Sarafu community inclusion currency, 2020-2021. Sci. Data
(2022).")
.
###
Circulation
To study circulation we turn to the map equation framework
[32](/articles/s41598-023-33184-1#ref-CR32 "Rosvall, M. & Bergstrom, C. T. Maps of random walks on complex networks reveal community structure. Proc. Natl. Acad. Sci. 105, .
(2008).")
and the associated Infomap algorithm
[33](/articles/s41598-023-33184-1#ref-CR33 "Bohlin, L., Edler, D., Lancichinetti, A. & Rosvall, M. Community Detection and Visualization of Networks with the Map Equation Framework. In eDing, Y., eRousseau, R. & eWolfram, D. (eds.) Measuring Scholarly Impact, 3-34,
(Springer International Publishing, Cham, 2014).")
. This is an approach based on computations involving a walk process over a given network, which is relevant in that financial transactions describe a real-world walk process
[10](/articles/s41598-023-33184-1#ref-CR10 "Mattsson, C. E. S. & Takes, F. W. Trajectories through temporal networks. Appl. Netw. Sci. 6, 1-31.
(2021).")
. The edge weights of the Sarafu flow network already reflect flows and so simulating a walk process is not necessary. Infomap takes the weighted, directed flow network as input and outputs a hierarchical mapping of nodes grouped into discovered
*modules*
. This grouping is done via computational optimization. Specifically, the map equation defines a notion of entropy whose value is higher the more of the observed flow over the given network occurs between rather than within modules. The Infomap algorithm exploits meso-scale network structure to minimize that value, grouping together nodes with much observed flow among themselves (and little outside). We refer to top-level modules, sub-modules and sub-sub-modules at respectively the first, second and third level of the discovered hierarchy. The composition of these sub-populations can then be understood by means of an approach where we quantify their heterogeneity along dimensions of geography, livelihood, and gender, i.e., the node attributes. Implementation details for running Infomap and analyzing the resulting module mapping are included in Supplementary File
[2](/articles/s41598-023-33184-1#MOESM2)
.
###
Network cycles
To describe the network connectivity patterns underlying the circulation of Sarafu, we consider cycles. A
*cycle*
is a simple path starting and ending at the same node. In the context of complementary currencies, cycles ensure the flow of liquidity throughout the system. For cycles to occur, users must be willing to both spend and earn in the complementary currency. Following this observation, we analyze cyclic structures in the Sarafu network using the
*z*
-score of the empirical cycle count as compared to a null model. We consider two common null models: Erdos-Renyi (ER) networks and random degree-preserving (RD) networks. ER networks have the same number of nodes and edges as the empirical network, but are wired randomly. Our RD networks preserve the indegree and outdegree sequences of the empirical network in expectation, but are otherwise random. Specifically, we sample from a binary, directed Exponential Random Graph Model
[83](/articles/s41598-023-33184-1#ref-CR83 "Vallarano, N. et al. Fast and scalable likelihood maximization for Exponential Random Graph Models with local constraints. Sci. Rep. 11, 15227.
(2021).")
. The
*z*
-score is defined in relation to the mean and standard deviation of the number of cycles of length
*k*
detected in 100 realizations of the relevant null model.
The cycle
*z*
-score is computed separately for each Infomap sub-module composed of 100 or more accounts (see: "
[Circulation](/articles/s41598-023-33184-1#Sec16)
" section). Directed cycles are detected and counted using an existing approach
[84](/articles/s41598-023-33184-1#ref-CR84 "Butts, C. T. Cycle Census Statistics for Exponential Random Graph Models*. Tech. Rep., UC Irvine: Institute for Mathematical Behavioral Sciences (2006).")
. This is done for each empirical sub-network, and for the ER and RD graphs generated from the empirical sub-network. An implementation is provided in Supplementary Files
[4](/articles/s41598-023-33184-1#MOESM4)
and
[5](/articles/s41598-023-33184-1#MOESM5)
.
###
Network mixing patterns
To characterize the mixing patterns underlying the network structure of the Sarafu community currency, we consider degree and attribute assortativity
[85](/articles/s41598-023-33184-1#ref-CR85 "Newman, M. E. J. Mixing patterns in networks. Phys. Rev. E 67, 026126.
(2003).")
,
[86](/articles/s41598-023-33184-1#ref-CR86 "Foster, J. G., Foster, D. V., Grassberger, P. & Paczuski, M. Edge direction and the structure of networks. Proc. Natl. Acad. Sci. 107, 10815-10820.
(2010).")
. Values are computed separately for each sub-network delineated by the Infomap sub-modules composed of 100 or more accounts (see: "
[Circulation](/articles/s41598-023-33184-1#Sec16)
" section). The categorical attribute assorativity is calculated along dimensions of livelihood category and reported gender, using the undirected version of the networks. These measures compare the number of links between accounts with the same livelihood or gender to that which would be expected at random, and can range from -1 to 1. A value of 0 corresponds to random expectation; a value of 1 corresponds to a network where transactions only occurred between accounts with the same attribute value. When there is no variation within a sub-population, the sub-network is given an assortativity value of 1. Similarly, we calculate the numerical attribute assorativity to quantify mixing patterns with respect to registration date, in-degree, and out-degree. Implementation details are reported in Supplementary File
[2](/articles/s41598-023-33184-1#MOESM2)
.
###
Network centrality
To characterize prominent users of Sarafu, we employ network centrality measures on the Sarafu flow network. Purely structural node-based metrics such as degree and weighted degree correspond to straightforward statistics about accounts. We also use walk-based methods for node centrality as these are especially interpretable with respect to monetary flow; the well-known PageRank algorithm is flexible and computationally tractable. These centrality measures are computed for our network, and then interpreted in the context of node attributes of the account-holders using linear regression. This lets us characterize prominent users without highlighting individual account holders, which is neither our goal nor desirable for privacy reasons. Below, we briefly discuss each employed measure.
*Indegree and outdegree*
in the Sarafu flow network correspond to an account's number of unique incoming and outgoing transaction partners, respectively, over the observation period. It is possible for nodes to have zero indegree
*or*
outdegree, but accounts with neither incoming nor outgoing transaction partners would be isolates and these are filtered out.
*Weighted indegree and weighted outdegree*
in the Sarafu flow network correspond to total transaction volumes into and out of accounts over the observation period. Note that these are mechanistically related in that money must be obtained before it can be spent according to the accounting consistency enforced within payment systems.
*PageRank*
is an algorithm that produces a walk-based metric for node centrality given a directed network
[6](/articles/s41598-023-33184-1#ref-CR6 "Frankova, E., Fousek, J., Kala, L. & Labohy, J. Transaction network analysis for studying Local Exchange Trading Systems (LETS): Research potentials and limitations. Ecol. Econ. 107, 266-275.
(2014).")
,
[38](/articles/s41598-023-33184-1#ref-CR38 "Page, L., Brin, S., Motwani, R. & Winograd, T. The PageRank Citation Ranking: Bringing Order to the Web. Technical Report 1999-66, Stanford InfoLab (1999).")
. The obtained centrality values approximate the probability of finding a random walker at a given node at any given moment. More specifically, PageRank computes the stationary probability of a random walk process with restarts on a given network. A single parameter
\(\alpha\)
is used to control the propensity for the simulated walkers to restart. An
\(\alpha\)
value of 0.85 is the long-established default, meaning that
\(15\%\)
of times a random walker will restart rather than follow an out-link from the node where it currently resides. By default, restarts are uniformly random across the nodes. However, it is also possible to specify the probability of restarting at any particular node using a so-called personalization vector.
*Weighted PageRank*
is an analogous centrality metric for weighted, directed networks. Over a weighted network, the random walkers choose among available out-links in proportion to their edge weights. Weighted edges are flows of money, in our case, and so the stationary probability of a random walker would then corresponds to the share of the total balance held by each account at equilibrium. This makes the Weighted PageRank algorithm especially applicable in the context of a currency system, since it means that the values are interpretable as the share of system funds that an account would eventually control if observed dynamics continued. Within this intuition,
*Weighted Inflow-adjusted PageRank*
employs a personalization vector to better capture idiosyncratic patterns of currency creation; real-world currency systems may be poorly represented by the default assumption of uniformly random restarts. Recall from the "
[Data preparation](/articles/s41598-023-33184-1#Sec15)
" section that Sarafu users could receive disbursements and rewards in addition to inflows from regular transactions. We use the aggregated values of non-
standard
inflows, available in the account dataset, to set the PageRank personalization vector. The simulated random walk process is then constrained to reproduce the observed pattern of currency creation, on average.
####
Empirical calibration
Running the Weighted PageRank algorithm requires specifying the aforementioned parameter
\(\alpha\)
. We would like to understand whether this parameter affects the suitability of these values as a centrality measure for networks of monetary flow. Since Weighted PageRank extrapolates the observed patterns of circulation towards a future where an equilibrium is reached, the output values can be understood as a prediction for hypothetical future account balances (as a fraction of the total balance). While we cannot expect such strong modeling assumptions to produce especially accurate estimates, it is nonetheless instructive to compare to empirical account balances. We can determine whether this centrality metric is sensitive to
\(\alpha\)
and whether modeling non-random currency creation, via the PageRank personalization vector, matters for this particular real-world system.
**Figure 9**
[![figure 9](//media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-023-33184-1/MediaObjects/41598_2023_33184_Fig9_HTML.png)](/articles/s41598-023-33184-1/figures/9)
Pearson correlation of Weighted and Weighted Inflow-adjusted PageRank with final account balances.
[Full size image](/articles/s41598-023-33184-1/figures/9)
We consider the correlation between our centrality metrics computed on the Sarafu flow network with Sarafu balances observed at the time of data collection on June 15th, 2021. Figure
[9](/articles/s41598-023-33184-1#Fig9)
plots the correlation between these final balances and the values given by the Weighted PageRank algorithm, with and without adjusting the simulated walk process to account for currency creation. The resulting correlations are at most
\(R = 0.57\)
and
\(R = 0.56\)
, respectively. Taking the perspective that Weighted PageRank estimates hypothetical future account balances, it is encouraging to note that these values correlate more closely with final balances than do the in- or out- degree (
\(R = 0.28\)
,
\(R = 0.21\)
), and the weighted in- or out- degree (
\(R = 0.52\)
,
\(R = 0.47\)
). Moreover, both versions of Weighted PageRank produce values that are consistently correlated with final balances over a wide range of parameter values that includes the long-established default (
\(\alpha = 0.85\)
); our centrality metrics are not overly sensitive to the propensity for restarts. We conclude that Weighted PageRank, especially Weighted Inflow-adjusted PageRank, is a highly suitable centrality metric for downstream analyses of networks of monetary flow.
###
High-degree tail estimation
To estimate the high-degree tail exponent of the degree distributions, we apply a recent approach based in extreme value theory
[87](/articles/s41598-023-33184-1#ref-CR87 "Voitalov, I., van der Hoorn, P., van der Hofstad, R. & Krioukov, D. Scale-free networks well done. Phys. Rev. Res. 1, 033034.
(2019).")
. This approach posits that heavy-tailed degree distributions might be usefully described as so-called "regularly varying" distributions, following a power-law at high degrees even if they take on an
*arbitrary functional form*
at lower degrees. Specifically, regularly varying distributions have a probability density function (PDF) of the form
\(P(k)=\ell (k) k^\gamma\)
, where
\(\ell (k)\)
is a slowly varying function. The PDF tail exponent
\(\gamma\)
, the complementary cumulative distribution function (CCDF) tail exponent
\(\alpha =\gamma -1\)
, and the so-called tail index
\(\xi = \frac{1}{\alpha }\)
can be estimated using established techniques. Regularly varying distributions have a tail index greater than zero, that is,
\(\frac{1}{\gamma -1}=\frac{1}{\alpha }=\xi >0\)
.
**Figure 10**
[![figure 10](//media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-023-33184-1/MediaObjects/41598_2023_33184_Fig10_HTML.png)](/articles/s41598-023-33184-1/figures/10)
Complementary cumulative distribution functions (CCDF) and fitted tail exponents for the indegree, outdegree, and weighted indegree of the Sarafu flow network. Weighted outdegree is not shown.
[Full size image](/articles/s41598-023-33184-1/figures/10)
The high-degree tail exponent can be estimated for our indegree and outdegree sequences, using the automated and openly available fitting procedure
[88](/articles/s41598-023-33184-1#ref-CR88 "Voitalov, I. Tail Index Estimation for Degree Sequences of Complex Networks (2022).")
provided alongside Voitalov et. al. (2019)
[87](/articles/s41598-023-33184-1#ref-CR87 "Voitalov, I., van der Hoorn, P., van der Hofstad, R. & Krioukov, D. Scale-free networks well done. Phys. Rev. Res. 1, 033034.
(2019).")
. Figure
[10](/articles/s41598-023-33184-1#Fig10)
reproduces the output of the fitting procedure, wherein the empirical CCDF is plotted against tail fits by the three available estimators. The Moments estimator appears well-behaved for both indegree (left) and outdegree (center); the full diagnostic plots are included in Supplementary File
[6](/articles/s41598-023-33184-1#MOESM6)
. Notably, the other estimators also show local minima with respect to the fitting criteria at or near the tail-cutoff selected by the Moments estimator. We conclude that the best estimate of
\(\gamma\)
is around 2.9 for the in- and out- high-degree tails. Lowering the tail cutoff to include the bulk of the outdegree distribution produces a lower estimate for
\(\gamma\)
, at around 2.2.
The high-degree tail exponents for the weighted degree distributions, however, cannot be estimated in this straightforward way. Figure
[10](/articles/s41598-023-33184-1#Fig10)
(right) shows the empirical CCDF of the weighted indegree and the fitted high-degree tail of the CCDF as estimated by the three available estimators. Recall that weighted in- and out- degree are closely correlated due to the underlying accounting consistency of the system (see the "
[Identifying prominent users](/articles/s41598-023-33184-1#Sec11)
" section). In both cases, the fitted exponent varies smoothly with the fraction of nodes included in the high-degree tail. This may be due to the inherent difficulty of empirically distinguishing Pareto from log-normal distributions
[89](/articles/s41598-023-33184-1#ref-CR89 "Mitzenmacher, M. A brief history of generative models for power law and lognormal distributions. Internet Math. 1, 226-251.
(2004).")
,
[90](/articles/s41598-023-33184-1#ref-CR90 "Broido, A. D. & Clauset, A. Scale-free networks are rare. Nat. Commun. 10, 1017.
(2019).")
. Indeed, the weighted in-degree of the Sarafu flow network corresponds to some notion of "income" within this system and, at the national scale, such distributions are often described as log-normal with a Pareto tail
[91](#ref-CR91 "Souma, W. Universal structure of the personal income distribution. Fractals 09, 463-470.
(2001).")
,
[92](#ref-CR92 "Reed, W. J. & Jorgensen, M. The double pareto-lognormal distribution-a new parametric model for size distributions. Commun. Stat. Theory Methods 33, .
(2004).")
,
[93](#ref-CR93 "Clementi, F. & Gallegati, M. Pareto's Law of Income Distribution: Evidence for Germany, the United Kingdom, and the United States. In eChatterjee, A., eYarlagadda, S. & eChakrabarti, B. K. (eds.) Econophysics of Wealth Distributions: Econophys-Kolkata I, New Economic Windows, 3-14,
(Springer, 2005).")
,
[94](/articles/s41598-023-33184-1#ref-CR94 "Battistin, E., Blundell, R. & Lewbel, A. Why is consumption more log normal than income? Gibrat's law revisited. J. Polit. Econ. 117, .
(2009).")
. Additional approaches, such as finite size scaling analysis
[95](/articles/s41598-023-33184-1#ref-CR95 "Serafino, M. et al. True scale-free networks hidden by finite size effects. Proc. Natl. Acad. Sci. 118, e2013825118.
(2021).")
, would be needed to determine the functional form and estimate the high-degree tail exponents for the weighted degree distributions.
###
Linear regression
To assess what recorded features of the account holders associate with higher prominence, as measured by network centrality, we use linear regression. Ordinary least squares (OLS) is used to fit a linear model to an outcome, in our case a network centrality measure, providing an estimated contribution for each input feature
[96](/articles/s41598-023-33184-1#ref-CR96 "Montgomery, D. C., Peck, E. A. & Vining, G. G. Introduction to Linear Regression Analysis 5th edn. (Wiley, 2012).")
. Regularization is a fitting technique that introduces a penalty term to the optimization limiting the number of regressors and/or their magnitudes
[97](/articles/s41598-023-33184-1#ref-CR97 "Friedman, J., Hastie, T. & Tibshirani, R. Regularization paths for generalized linear models via coordinate descent. J. Stat. Softw. 33, 1-22 (2010).")
. So-called Elastic Net (EN) regularization, as we use it, penalizes the number of regressors and their magnitude equally. The penalty weight is selected using five-fold cross validation, just before the point where additional features begin entering the model without qualitatively improving the statistical fit. Further implementation details are noted in Supplementary File
[3](/articles/s41598-023-33184-1#MOESM3)
, alongside the code that replicates the analysis.
Data availibility
-------------------
The dataset analyzed in this study
[31](/articles/s41598-023-33184-1#ref-CR31 "Ruddick, W. O. Sarafu Community Inclusion Currency, 2020-2021, (2021).
")
is available via the UK Data Service (UKDS) under their End User License, which stipulates suitable data-privacy protections. The dataset is available for download from the UKDS ReShare repository (
<
) to users registered with the UKDS (
<
). Further usage notes and an extensive description of the dataset are available in a complementary publication
[27](/articles/s41598-023-33184-1#ref-CR27 "Mattsson, C. E. S., Criscione, T. & Ruddick, W. O. Sarafu community inclusion currency, 2020-2021. Sci. Data
(2022).")
.
Code availability
-------------------
The code required to construct the network and reproduce each analysis is included the Supplementary Information. Supplementary File
[1](/articles/s41598-023-33184-1#MOESM1)
contains code to construct the network from the raw data. Supplementary File
[2](/articles/s41598-023-33184-1#MOESM2)
contains code to reproduce the analysis in the "
[Modular circulation](/articles/s41598-023-33184-1#Sec4)
" section and "
[Structural correlations](/articles/s41598-023-33184-1#Sec9)
" sections. Supplementary File
[3](/articles/s41598-023-33184-1#MOESM3)
contains code to reproduce the analysis in the "
[Prominent Sarafu users](/articles/s41598-023-33184-1#Sec10)
" section. Supplementary File
[4](/articles/s41598-023-33184-1#MOESM4)
contains code to reproduce the analysis in the "
[Cyclic structure](/articles/s41598-023-33184-1#Sec8)
" section. Supplementary File
[5](/articles/s41598-023-33184-1#MOESM5)
contains code to reproduce the figures in the "
[Cyclic structure](/articles/s41598-023-33184-1#Sec8)
" section. Supplementary File
[6](/articles/s41598-023-33184-1#MOESM6)
contains the full diagnostic plots referred to in the "
[High-degree tail estimation](/articles/s41598-023-33184-1#Sec21)
" section and a high-resolution version of Fig.
[2](/articles/s41598-023-33184-1#Fig2)
.
Software availability
-----------------------
All software used in this study are available under an open-source licence:
infomap v1.6.0
[98](/articles/s41598-023-33184-1#ref-CR98 "Edler, D., Eriksson, A. & Rosvall, M. The MapEquation software package (2021).")
;
networkx v2.6.3
[99](/articles/s41598-023-33184-1#ref-CR99 "Hagberg, A. A., Schult, D. A. & Swart, P. J. Exploring Network Structure, Dynamics, and Function using NetworkX. In Proceedings of the 7th Python in Science Conference, 5 (Pasadena, CA, 2008).")
;
netdiffuseR v1.22.3
[100](/articles/s41598-023-33184-1#ref-CR100 "Vega Yon, G., Dyal, S., Hayes, T. & Valente, T. netdiffuseR: Analysis of Diffusion and Contagion Processes on Networks (2021).")
;
sna v2.6
[101](/articles/s41598-023-33184-1#ref-CR101 "Butts, C. T. SNA: Tools for Social Network Analysis (2020).")
;
statsmodels v0.13.2
[102](/articles/s41598-023-33184-1#ref-CR102 "Seabold, S. & Perktold, J. Statsmodels: Econometric and Statistical Modeling with Python. In Proceedings of the 9th Python in Science Conference, 92-96,
(Austin, 2010).")
;
seaborn v0.11.2
[103](/articles/s41598-023-33184-1#ref-CR103 "Waskom, M. Seaborn: Statistical data visualization. J. Open Source Softw. 6, 3021.
(2021).")
;
matplotlib v3.5.2
[104](/articles/s41598-023-33184-1#ref-CR104 "Hunter, J. D. Matplotlib: A 2D graphics environment. Comput. Sci. Eng. 9, 90-95.
(2007).")
;
pandas v1.4.2
[105](/articles/s41598-023-33184-1#ref-CR105 "Reback, J. et al. pandas-dev/pandas,
(2022).")
;
NEMtropy v2.1.1
[106](/articles/s41598-023-33184-1#ref-CR106 "Vallarano, N., Marchese, E. & Bruno, M. NEMtropy: Network Entropy Maximization, a Toolbox Running On PYthon 736 (2022).")
.
References
------------
1. Nakamura, E. & Steinsson, J. Identification in macroeconomics.
*J. Econ. Persp.*
**32**
, 59-86.
<
(2018).
[Article]()
[MATH]()
[Google Scholar]()
2. McNerney, J., Savoie, C., Caravelli, F., Carvalho, V. M. & Farmer, J. D. How production networks amplify economic growth.
*Proc. Natl. Acad. Sci.*
**119**
, e2106031118.
<
(2022).
[Article]()
[CAS](/articles/cas-redirect/1:CAS:528:DC%2BB38XhvV2nt7k%3D)
[PubMed]()
[Google Scholar]()
3. Carvalho, V. M., Nirei, M., Saito, Y. & Tahbaz-Salehi, A. Supply Chain Disruptions: Evidence from the Great East Japan Earthquake. SSRN Scholarly ,, Social Science Research Network, Rochester, NY (2016).
4. Acemoglu, D., Carvalho, V. M., Ozdaglar, A. & Tahbaz-Salehi, A. The network origins of aggregate fluctuations.
*Econometrica*
**80**
, .
<
(2012).
[Article]()
[MathSciNet]()
[MATH]()
[Google Scholar]()
5. Adrian, T. & Mancini-Griffoli, T. The rise of digital money. No. no. 19/0018 in IMF FinTech notes (International Monetary Fund, Washington, D.C (2019).
6. Frankova, E., Fousek, J., Kala, L. & Labohy, J. Transaction network analysis for studying Local Exchange Trading Systems (LETS): Research potentials and limitations.
*Ecol. Econ.*
**107**
, 266-275.
<
(2014).
[Article]()
[Google Scholar]()
7. Alessandretti, L., ElBahrawy, A., Aiello, L. M. & Baronchelli, A. Anticipating cryptocurrency prices using machine learning. Complexity
**2018**
(2018).
8. Aladangady, A. et al. From Transactions Data to Economic Statistics: Constructing Real-Time, High-Frequency, Geographic Measures of Consumer Spending. Big Data for 21st Century Economic Statistics (2019).
9. Bouchaud, J.-P.
*Trades, Quotes and Prices: Financial Markets Under the Microscope*
1st edn. (Cambridge University Press, 2018).
10. Mattsson, C. E. S. & Takes, F. W. Trajectories through temporal networks.
*Appl. Netw. Sci.*
**6**
, 1-31.
<
(2021).
[Article]()
[Google Scholar]()
11. Bardoscia, M.
*et al.*
The physics of financial networks.
*Nat. Rev. Phys.*
**3**
, 490-507.
<
(2021).
[Article]()
[Google Scholar]()
12. Carvalho, V. M.
*et al.*
Tracking the COVID-19 crisis with high-resolution transaction data.
*R. Soc. Open Sci.*
**8**
, 210218.
<
(2021).
[Article]()
[ADS]()
[PubMed]()
[PubMed Central]()
[Google Scholar]()
13. Stodder, J. Complementary credit networks and macroeconomic stability: Switzerland's Wirtschaftsring.
*J. Econ. Behav. Organ.*
**72**
, 79-95.
<
(2009).
[Article]()
[Google Scholar]()
14. Lietaer, B. Complementary currencies in Japan today: History, originality and relevance.
*Int. J. Commun. Curr. Res.*
**8**
, 1-23.
<
(2004).
[Article]()
[Google Scholar]()
15. Ussher, L., Ebert, L., Gomez, G. M. & Ruddick, W. O. Complementary currencies for humanitarian aid.
*J. Risk Financ. Manag.*
**14**
, 557.
<
(2021).
[Article]()
[Google Scholar]()
16. Muralt, V. The Woergl experiment with depreciating money.
*Ann. Public Cooper. Econ.*
**10**
, 48-57.
<
(1934).
[Article]()
[Google Scholar]()
17. Kichiji, N. & Nishibe, M. Network analyses of the circulation flow of community currency.
*Evol. Inst. Econ. Rev.*
**4**
, 267-300.
<
(2008).
[Article]()
[Google Scholar]()
18. Nakamoto, S. Bitcoin: A Peer-to-Peer Electronic Cash System (Tech. Rep, Manubot, 2008).
19. Kondor, D., Posfai, M., Csabai, I. & Vattay, G. Do the rich get richer? An empirical analysis of the bitcoin transaction network.
*PLoS ONE*
**9**
, e86197.
<
(2014).
[Article]()
[ADS]()
[CAS](/articles/cas-redirect/1:CAS:528:DC%2BC2cXhsVGrsLjJ)
[PubMed]()
[PubMed Central]()
[Google Scholar]()
20. ElBahrawy, A., Alessandretti, L., Kandler, A., Pastor-Satorras, R. & Baronchelli, A. Evolutionary dynamics of the cryptocurrency market.
*R. Soc. Open Sci.*
**4**
, 170623 (2017).
[Article]()
[MathSciNet]()
[PubMed]()
[PubMed Central]()
[Google Scholar]()
21. Iosifidis, G.
*et al.*
Cyclic motifs in the Sardex monetary network.
*Nat. Hum. Behav.*
<
(2018).
[Article]()
[PubMed]()
[Google Scholar]()
22. Fleischman, T. & Dini, P. Balancing the Payment System. (2020).
[arXiv:2011.03517]()
[q-fin]
23. Ober, M., Katzenbeisser, S. & Hamacher, K. Structure and anonymity of the bitcoin transaction graph.
*Fut. Internet*
**5**
, 237-250.
<
(2013).
[Article]()
[Google Scholar]()
24. Meiklejohn, S.
*et al.*
A fistful of Bitcoins: Characterizing payments among men with no names.
*Commun. ACM*
**59**
, 86-93.
<
(2016).
[Article]()
[Google Scholar]()
25. Zhang, Y., Wang, J. & Luo, J. Heuristic-based address clustering in bitcoin.
*IEEE Access*
**8**
, 210582-210591.
<
(2020).
[Article]()
[Google Scholar]()
26. Nadini, M. Emergence and structure of decentralised trade networks around dark web marketplaces.
*Sci. Rep.*
**9**
, 1-9 (2022).
[Google Scholar]()
27. Mattsson, C. E. S., Criscione, T. & Ruddick, W. O. Sarafu community inclusion currency, 2020-2021.
*Sci. Data*
<
(2022).
[Article]()
[PubMed]()
[PubMed Central]()
[Google Scholar]()
28. Ruddick, W. O. Eco-Pesa: an evaluation of a complementary currency programme in Kenyaa informal settlements.
*Int. J. Commun. Curr. Res.*
**15**
, 12.
<
(2011).
[Article]()
[Google Scholar]()
29. Stodder, J. & Lietaer, B. The macro-stability of Swiss WIR-Bank credits: Balance, velocity, and leverage.
*Comp. Econ. Stud.*
**58**
, 570-605.
<
(2016).
[Article]()
[Google Scholar]()
30. Zeller, S. Economic advantages of community currencies.
*J. Risk Financ. Manag.*
**13**
, 271.
<
(2020).
[Article]()
[Google Scholar]()
31. Ruddick, W. O. Sarafu Community Inclusion Currency, 2020-2021, (2021).
<
32. Rosvall, M. & Bergstrom, C. T. Maps of random walks on complex networks reveal community structure.
*Proc. Natl. Acad. Sci.*
**105**
, .
<
(2008).
[Article]()
[ADS]()
[PubMed]()
[PubMed Central]()
[Google Scholar]()
33. Bohlin, L., Edler, D., Lancichinetti, A. & Rosvall, M. Community Detection and Visualization of Networks with the Map Equation Framework. In eDing, Y., eRousseau, R. & eWolfram, D. (eds.) Measuring Scholarly Impact, 3-34,
<
(Springer International Publishing, Cham, 2014).
34. Fujiwara, Y. & Aoyama, H. Large-scale structure of a nation-wide production network.
*Eur. Phys. J. B*
**77**
, 565-580.
<
(2010).
[Article]()
[ADS]()
[CAS](/articles/cas-redirect/1:CAS:528:DC%2BC3cXhtl2rtr3F)
[Google Scholar]()
35. Mattsson, C. E. S.
*et al.*
Functional structure in production networks.
*Front. Big Data*
<
(2021).
[Article]()
[PubMed]()
[PubMed Central]()
[Google Scholar]()
36. Campajola, C., D'Errico, M. & Tessone, C. J. MicroVelocity: rethinking the Velocity of Money for digital currencies.
[arXiv:2201.13416]()
[physics, q-fin] (2022).
37. Fleischman, T., Dini, P. & Littera, G. Liquidity-saving through obligation-clearing and mutual credit: An effective monetary innovation for SMEs in times of crisis.
*J. Risk Financ. Manag.*
**13**
, 295.
<
(2020).
[Article]()
[Google Scholar]()
38. Page, L., Brin, S., Motwani, R. & Winograd, T. The PageRank Citation Ranking: Bringing Order to the Web. Technical Report 1999-66, Stanford InfoLab (1999).
39. Mbogo, M. The impact of mobile payments on the success and growth of micro-business: The case of M-Pesa in Kenya.
*J. Lang. Technol. Entrep. Africa*
**2**
, 182-203 (2010).
[Article]()
[Google Scholar]()
40. Stuart, G. & Cohen, M. Cash In, Cash Out Kenya: The Role of M-PESA in the Lives of Low-Income People. The Financial Services Assesment project (Microfinance Opportunities, 2011).
41. Mbiti, I. & Weil, D. N. Mobile banking: The impact of M-Pesa in Kenya (Tech. Rep, National Bureau of Economic Research, 2011).
42. Suri, T. Mobile money.
*Annu. Rev. Econ.*
**9**
, 497-520.
<
(2017).
[Article]()
[Google Scholar]()
43. International Finance Corporation & Mastercard Foundation. Digital Access: The Future of Financial Inclusion in Africa (Tech. Rep, Partnership for Financial Inclusion, 2018).
44. Baah, B.
*et al.*
State of the Industry Report on Mobile Money 2021 (Industry Report, GSMA, 2021).
45. Marion, C. Voucher Systems for Food Security: A Case Study on Kenya's Sarafu-Credit. Master's thesis, University of Copenhagen,
<
(2018).
46. Bianconi, G., Gulbahce, N. & Motter, A. E. Local structure of directed networks.
*Phys. Rev. Lett.*
**100**
, 118701.
<
(2008).
[Article]()
[ADS]()
[CAS](/articles/cas-redirect/1:CAS:528:DC%2BD1cXjs1Kis70%3D)
[PubMed]()
[Google Scholar]()
47. Avanzo, S. E. A relational analysis of sarafu network: Emergence of a monetary ecosystem for the prosperity of the communities. Master's thesis, University of Torino, Torino (2019).
48. Rasulova, S., Storchi, S., Karim, M., Moratti, M. & Johnson, S. Impact evaluation of FSD Kenya's savings groups project (Tech. Rep, FSD Kenya, 2017).
49. Barabasi, A.-L. & Albert, R. Emergence of scaling in random networks.
*Science*
**286**
, 509-512.
<
(1999).
[Article]()
[ADS]()
[MathSciNet]()
[PubMed]()
[MATH]()
[Google Scholar]()
50. Barabasi, A.-L.
*Network Science*
1st edn. (Cambridge University Press, 2016).
51. Lynn, C. W., Holmes, C. M. & Palmer, S. E. Emergent scale-free networks,
<
(2022).
52. Litvak, N., Scheinhardt, W. R. W. & Volkovich, Y. In-Degree and PageRank: Why Do They Follow Similar Power Laws?.
*Internet Mathematics*
**4**
, 175-198.
<
(2007).
[Article]()
[MathSciNet]()
[MATH]()
[Google Scholar]()
53. Fortunato, S., Bogun a, M., Flammini, A. & Menczer, F. Approximating PageRank from In-Degree. In eAiello, W., eBroder, A., eJanssen, J. & eMilios, E. (eds.) Algorithms and Models for the Web-Graph, Lecture Notes in Computer Science, 59-71,
<
(Springer, Berlin, Heidelberg, 2008).
54. Ruddick, W. O., Richards, M. A. & Bendell, J. Complementary currencies for sustainable development in Kenya: The case of the bangla-pesa.
*Int. J. Commun. Curr. Res.*
**19**
, 13.
<
(2015).
[Article]()
[Google Scholar]()
55. Mauldin, R. L. Local currency for community development: Policy barriers and support.
*J. Commun. Pract.*
**23**
, 462-476.
<
(2015).
[Article]()
[Google Scholar]()
56. Fuders, F. Smarter Money for Smarter Cities: How Regional Currencies Can Help to Promote a Decentralised and Sustainable Regional Development. In eDick, E., eGaesing, K., eInkoom, D. & eKausel, T. (eds.) Decentralisation and Regional Development: Experiences and Lessons from Four Continents over Three Decades, Springer Geography, 155-185,
<
(Springer International Publishing, 2016).
57. eGomez, G. M. (ed.)
*Monetary Plurality in Local, Regional and Global Economies*
(Routledge, 2018).
58. Kawamoto, T. Single-trajectory map equation.
[arXiv:2203.04044]()
[physics] (2022).
59. Blumenstock, J. E., Eagle, N. & Fafchamps, M. Airtime transfers and mobile communications: Evidence in the aftermath of natural disasters.
*J. Dev. Econ.*
**120**
, 157-181.
<
(2016).
[Article]()
[Google Scholar]()
60. Economides, N. & Jeziorski, P. Mobile Money in Tanzania.
*Mark. Sci.*
**36**
, 815-837.
<
(2017).
[Article]()
[Google Scholar]()
61. SoramAki, K., Bech, M. L., Arnold, J., Glass, R. J. & Beyeler, W. E. The topology of interbank payment flows.
*Physica A Stat. Mech. Appl.*
**379**
, 317-333.
<
(2007).
[Article]()
[ADS]()
[Google Scholar]()
62. Iori, G., De Masi, G., Precup, O. V., Gabbi, G. & Caldarelli, G. A network analysis of the Italian overnight money market.
*J. Econ. Dyn. Control*
**32**
, 259-278.
<
(2008).
[Article]()
[MATH]()
[Google Scholar]()
63. Kyriakopoulos, F., Thurner, S., Puhr, C. & Schmitz, S. W. Network and eigenvalue analysis of financial transaction networks.
*Eur. Phys. J. B*
**71**
, 523.
<
(2009).
[Article]()
[ADS]()
[CAS](/articles/cas-redirect/1:CAS:528:DC%2BD1MXhsVSms7vI)
[MATH]()
[Google Scholar]()
64. Bech, M. L. & Garratt, R. J. Illiquidity in the interbank payment system following wide-scale disruptions.
*J. Money Credit Bank.*
**44**
, 903-929.
<
(2012).
[Article]()
[Google Scholar]()
65. Barucca, P. & Lillo, F. The organization of the interbank network and how ECB unconventional measures affected the e-MID overnight market.
*CMS*
**15**
, 33-53.
<
(2018).
[Article]()
[MathSciNet]()
[Google Scholar]()
66. Rubio, J., Barucca, P., Gage, G., Arroyo, J. & Morales-Resendiz, R. Classifying payment patterns with artificial neural networks: An autoencoder approach.
*Latin Am. J. Central Bank.*
**1**
, 100013.
<
(2020).
[Article]()
[Google Scholar]()
67. Bianchi, F., Bartolucci, F., Peluso, S. & Mira, A. Longitudinal networks of dyadic relationships using latent trajectories: Evidence from the European interbank market.
*J. R. Stat. Soc.: Ser. C (Appl. Stat.)*
**69**
, 711-739.
<
(2020).
[Article]()
[MathSciNet]()
[Google Scholar]()
68. Zanin, M., Papo, D., Romance, M., Criado, R. & Moral, S. The topology of card transaction money flows.
*Physica A*
**462**
, 134-140.
<
(2016).
[Article]()
[ADS]()
[Google Scholar]()
69. Rendon de la Torre, S., Kalda, J., Kitt, R. & Engelbrecht, J. On the topologic structure of economic complex networks: Empirical evidence from large scale payment network of Estonia. Chaos, Solitons & Fractals
**90**
, 18-27,
<
(2016).
70. Ialongo, L. N. et al. Reconstructing firm-level interactions: the Dutch input-output network.
[arXiv:2111.15248]()
[physics, q-fin] (2021).
71. Triepels, R., Daniels, H. & Heijmans, R. Detection and Explanation of Anomalous Payment Behavior in Real-Time Gross Settlement Systems. In eHammoudi, S.,emialek, M., eCamp, O. & eFilipe, J. (eds.) Enterprise Information Systems, Lecture Notes in Business Information Processing, 145-161,
<
(Springer International Publishing, 2018).
72. Sabetti, L. & Heijmans, R. Shallow or deep? Training an autoencoder to detect anomalous flows in a retail payment system.
*Latin Am. J. Central Bank.*
**2**
, 100031.
<
(2021).
[Article]()
[Google Scholar]()
73. Arevalo, F.
*et al.*
Identifying clusters of anomalous payments in the salvadorian payment system.
*Latin Am. J. Central Bank.*
**3**
, 100050.
<
(2022).
[Article]()
[Google Scholar]()
74. Bank of Canada et al. Central bank digital currencies: executive summary. Tech. Rep., Bank for International Settlements (2021).
75. Saramaki, J. & Holme, P. Exploring temporal networks with greedy walks.
*Eur. Phys. J. B*
**88**
, 334.
<
(2015).
[Article]()
[ADS]()
[CAS](/articles/cas-redirect/1:CAS:528:DC%2BC2MXitVWqsb3O)
[Google Scholar]()
76. LaRock, T., Scholtes, I. & Eliassi-Rad, T. Sequential motifs in observed walks.
*J. Complex Netw.*
**10**
, cnac036.
<
(2022).
[Article]()
[MATH]()
[Google Scholar]()
77. Mattsson, C. E. S., Luedtke, A. & Takes, F. W. Measuring the Velocity of Money,
<
(2022).
78. Lentz, H. H. K., Selhorst, T. & Sokolov, I. M. Unfolding accessibility provides a macroscopic approach to temporal networks.
*Phys. Rev. Lett.*
**110**
, 118701.
<
(2013).
[Article]()
[ADS]()
[CAS](/articles/cas-redirect/1:CAS:528:DC%2BC3sXlslGktLg%3D)
[PubMed]()
[Google Scholar]()
79. Xu, J., Wickramarathne, T. L. & Chawla, N. V. Representing higher-order dependencies in networks.
*Sci. Adv.*
**2**
, e1600028.
<
(2016).
[Article]()
[ADS]()
[PubMed]()
[PubMed Central]()
[Google Scholar]()
80. Lambiotte, R., Rosvall, M. & Scholtes, I. From networks to optimal higher-order models of complex systems.
*Nat. Phys.*
<
(2019).
[Article]()
[PubMed]()
[PubMed Central]()
[Google Scholar]()
81. Biggart, N. W. Banking on each other: The situational logic of rotating savings and credit associations.
*Adv. Qual. Organ. Res.*
**3**
, 129-153 (2001).
[Google Scholar]()
82. Central Bank of Kenya, Kenya National Bureau of Statistics & FSD Kenya. Inclusive Finance? Headline findings from FinAccess 2019. Tech. Rep., FSD Kenya (2019).
83. Vallarano, N.
*et al.*
Fast and scalable likelihood maximization for Exponential Random Graph Models with local constraints.
*Sci. Rep.*
**11**
, 15227.
<
(2021).
[Article]()
[CAS](/articles/cas-redirect/1:CAS:528:DC%2BB3MXhslKhurbK)
[PubMed]()
[PubMed Central]()
[Google Scholar]()
84. Butts, C. T. Cycle Census Statistics for Exponential Random Graph Models\*. Tech. Rep., UC Irvine: Institute for Mathematical Behavioral Sciences (2006).
85. Newman, M. E. J. Mixing patterns in networks.
*Phys. Rev. E*
**67**
, 026126.
<
(2003).
[Article]()
[ADS]()
[MathSciNet]()
[CAS](/articles/cas-redirect/1:CAS:528:DC%2BD3sXitV2ktb0%3D)
[Google Scholar]()
86. Foster, J. G., Foster, D. V., Grassberger, P. & Paczuski, M. Edge direction and the structure of networks.
*Proc. Natl. Acad. Sci.*
**107**
, 10815-10820.
<
(2010).
[Article]()
[ADS]()
[CAS](/articles/cas-redirect/1:CAS:528:DC%2BC3cXmsFKksL8%3D)
[PubMed]()
[PubMed Central]()
[Google Scholar]()
87. Voitalov, I., van der Hoorn, P., van der Hofstad, R. & Krioukov, D. Scale-free networks well done.
*Phys. Rev. Res.*
**1**
, 033034.
<
(2019).
[Article]()
[CAS](/articles/cas-redirect/1:CAS:528:DC%2BB3cXhvVOhtbfM)
[Google Scholar]()
88. Voitalov, I. Tail Index Estimation for Degree Sequences of Complex Networks (2022).
89. Mitzenmacher, M. A brief history of generative models for power law and lognormal distributions.
*Internet Math.*
**1**
, 226-251.
<
(2004).
[Article]()
[MathSciNet]()
[MATH]()
[Google Scholar]()
90. Broido, A. D. & Clauset, A. Scale-free networks are rare.
*Nat. Commun.*
**10**
, 1017.
<
(2019).
[Article]()
[ADS]()
[CAS](/articles/cas-redirect/1:CAS:528:DC%2BC1MXnvFygsLo%3D)
[PubMed]()
[PubMed Central]()
[Google Scholar]()
91. Souma, W. Universal structure of the personal income distribution.
*Fractals*
**09**
, 463-470.
<
(2001).
[Article]()
[Google Scholar]()
92. Reed, W. J. & Jorgensen, M. The double pareto-lognormal distribution-a new parametric model for size distributions.
*Commun. Stat. Theory Methods*
**33**
, .
<
(2004).
[Article]()
[MathSciNet]()
[MATH]()
[Google Scholar]()
93. Clementi, F. & Gallegati, M. Pareto's Law of Income Distribution: Evidence for Germany, the United Kingdom, and the United States. In eChatterjee, A., eYarlagadda, S. & eChakrabarti, B. K. (eds.) Econophysics of Wealth Distributions: Econophys-Kolkata I, New Economic Windows, 3-14,
<
(Springer, 2005).
94. Battistin, E., Blundell, R. & Lewbel, A. Why is consumption more log normal than income? Gibrat's law revisited.
*J. Polit. Econ.*
**117**
, .
<
(2009).
[Article]()
[Google Scholar]()
95. Serafino, M.
*et al.*
True scale-free networks hidden by finite size effects.
*Proc. Natl. Acad. Sci.*
**118**
, e2013825118.
<
(2021).
[Article]()
[MathSciNet]()
[CAS](/articles/cas-redirect/1:CAS:528:DC%2BB3MXhsVCit7c%3D)
[PubMed]()
[MATH]()
[Google Scholar]()
96. Montgomery, D. C., Peck, E. A. & Vining, G. G.
*Introduction to Linear Regression Analysis*
5th edn. (Wiley, 2012).
97. Friedman, J., Hastie, T. & Tibshirani, R. Regularization paths for generalized linear models via coordinate descent.
*J. Stat. Softw.*
**33**
, 1-22 (2010).
[Article]()
[PubMed]()
[PubMed Central]()
[Google Scholar]()
98. Edler, D., Eriksson, A. & Rosvall, M. The MapEquation software package (2021).
99. Hagberg, A. A., Schult, D. A. & Swart, P. J. Exploring Network Structure, Dynamics, and Function using NetworkX. In Proceedings of the 7th Python in Science Conference, 5 (Pasadena, CA, 2008).
100. Vega Yon, G., Dyal, S., Hayes, T. & Valente, T. netdiffuseR: Analysis of Diffusion and Contagion Processes on Networks (2021).
101. Butts, C. T. SNA: Tools for Social Network Analysis (2020).
102. Seabold, S. & Perktold, J. Statsmodels: Econometric and Statistical Modeling with Python. In Proceedings of the 9th Python in Science Conference, 92-96,
<
(Austin, 2010).
103. Waskom, M. Seaborn: Statistical data visualization.
*J. Open Source Softw.*
**6**
, 3021.
<
(2021).
[Article]()
[ADS]()
[Google Scholar]()
104. Hunter, J. D. Matplotlib: A 2D graphics environment.
*Comput. Sci. Eng.*
**9**
, 90-95.
<
(2007).
[Article]()
[Google Scholar]()
105. Reback, J. et al. pandas-dev/pandas,
<
(2022).
106. Vallarano, N., Marchese, E. & Bruno, M. NEMtropy: Network Entropy Maximization, a Toolbox Running On PYthon 736 (2022).
[Download references]()
Acknowledgements
------------------
The authors thank Janos Kertesz, Tiago P. Peixoto, Pim van der Hoorn, and William O. Ruddick for valuable feedback.
Author information
--------------------
###
Authors and Affiliations
1. Leiden Institute of Advanced Computer Science, Leiden University, 2333 CA, Leiden, The Netherlands
Carolina E. S. Mattsson & Frank W. Takes
2. Department of Network and Data Science, Central European University, 1100, Wien, Austria
Teodoro Criscione
3. Freiburg Institute for Basic Income Studies, University of Freiburg, 79098, Freiburg, Germany
Teodoro Criscione
Authors
1. Carolina E. S. Mattsson
[View author publications](/search?author=Carolina%20E.%20S.%20Mattsson)
You can also search for this author in
[PubMed]()
[Google Scholar]()
2. Teodoro Criscione
[View author publications](/search?author=Teodoro%20Criscione)
You can also search for this author in
[PubMed]()
[Google Scholar]()
3. Frank W. Takes
[View author publications](/search?author=Frank%20W.%20Takes)
You can also search for this author in
[PubMed]()
[Google Scholar]()
###
Contributions
C.M. and F.W.T. developed the methods. C.M. conducted the research and drafted the initial manuscript. T.C. performed the cycle analysis and drafted the corresponding sections. All authors contributed to the final manuscript.
###
Corresponding author
Correspondence to
[Carolina E. S. Mattsson](mailto:)
.
Ethics declarations
---------------------
###
Competing interests
The authors declare no competing interests.
Additional information
------------------------
###
Publisher's note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
Supplementary Information
---------------------------
###
[Supplementary Information 1.]()
###
[Supplementary Information 2.]()
###
[Supplementary Information 3.]()
###
[Supplementary Information 4.]()
###
[Supplementary Information 5.]()
###
[Supplementary Information 6.]()
Rights and permissions
------------------------
**Open Access**
This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit
<
.
[Reprints and Permissions]()
About this article
--------------------
[![Check for updates. Verify currency and authenticity via CrossMark](data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjgxIiB3aWR0aD0iNTciIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIj48cGF0aCBkPSJtMTcuMzUgMzUuNDUgMjEuMy0xNC4ydi0xNy4wM2gtMjEuMyIgZmlsbD0iIzk4OTg5OCIvPjxwYXRoIGQ9Im0zOC42NSAzNS40NS0yMS4zLTE0LjJ2LTE3LjAzaDIxLjMiIGZpbGw9IiM3NDc0NzQiLz48cGF0aCBkPSJtMjggLjVjLTEyLjk4IDAtMjMuNSAxMC41Mi0yMy41IDIzLjVzMTAuNTIgMjMuNSAyMy41IDIzLjUgMjMuNS0xMC41MiAyMy41LTIzLjVjMC02LjIzLTIuNDgtMTIuMjEtNi44OC0xNi42Mi00LjQxLTQuNC0xMC4zOS02Ljg4LTE2LjYyLTYuODh6bTAgNDEuMjVjLTkuOCAwLTE3Ljc1LTcuOTUtMTcuNzUtMTcuNzVzNy45NS0xNy43NSAxNy43NS0xNy43NSAxNy43NSA3Ljk1IDE3Ljc1IDE3Ljc1YzAgNC43MS0xLjg3IDkuMjItNS4yIDEyLjU1cy03Ljg0IDUuMi0xMi41NSA1LjJ6IiBmaWxsPSIjNTM1MzUzIi8+PHBhdGggZD0ibTQxIDM2Yy01LjgxIDYuMjMtMTUuMjMgNy40NS0yMi40MyAyLjktNy4yMS00LjU1LTEwLjE2LTEzLjU3LTcuMDMtMjEuNWwtNC45Mi0zLjExYy00Ljk1IDEwLjctMS4xOSAyMy40MiA4Ljc4IDI5LjcxIDkuOTcgNi4zIDIzLjA3IDQuMjIgMzAuNi00Ljg2eiIgZmlsbD0iIzljOWM5YyIvPjxwYXRoIGQ9Im0uMiA1OC40NWMwLS43NS4xMS0xLjQyLjMzLTIuMDFzLjUyLTEuMDkuOTEtMS41Yy4zOC0uNDEuODMtLjczIDEuMzQtLjk0LjUxLS4yMiAxLjA2LS4zMiAxLjY1LS4zMi41NiAwIDEuMDYuMTEgMS41MS4zNS40NC4yMy44MS41IDEuMS44MWwtLjkxIDEuMDFjLS4yNC0uMjQtLjQ5LS40Mi0uNzUtLjU2LS4yNy0uMTMtLjU4LS4yLS45My0uMi0uMzkgMC0uNzMuMDgtMS4wNS4yMy0uMzEuMTYtLjU4LjM3LS44MS42Ni0uMjMuMjgtLjQxLjYzLS41MyAxLjA0LS4xMy40MS0uMTkuODgtLjE5IDEuMzkgMCAxLjA0LjIzIDEuODYuNjggMi40Ni40NS41OSAxLjA2Ljg4IDEuODQuODguNDEgMCAuNzctLjA3IDEuMDctLjIzcy41OS0uMzkuODUtLjY4bC45MSAxYy0uMzguNDMtLjguNzYtMS4yOC45OS0uNDcuMjItMSAuMzQtMS41OC4zNC0uNTkgMC0xLjEzLS4xLTEuNjQtLjMxLS41LS4yLS45NC0uNTEtMS4zMS0uOTEtLjM4LS40LS42Ny0uOS0uODgtMS40OC0uMjItLjU5LS4zMy0xLjI2LS4zMy0yLjAyem04LjQtNS4zM2gxLjYxdjIuNTRsLS4wNSAxLjMzYy4yOS0uMjcuNjEtLjUxLjk2LS43MnMuNzYtLjMxIDEuMjQtLjMxYy43MyAwIDEuMjcuMjMgMS42MS43MS4zMy40Ny41IDEuMTQuNSAyLjAydjQuMzFoLTEuNjF2LTQuMWMwLS41Ny0uMDgtLjk3LS4yNS0xLjIxLS4xNy0uMjMtLjQ1LS4zNS0uODMtLjM1LS4zIDAtLjU2LjA4LS43OS4yMi0uMjMuMTUtLjQ5LjM2LS43OC42NHY0LjhoLTEuNjF6bTcuMzcgNi40NWMwLS41Ni4wOS0xLjA2LjI2LTEuNTEuMTgtLjQ1LjQyLS44My43MS0xLjE0LjI5LS4zLjYzLS41NCAxLjAxLS43MS4zOS0uMTcuNzgtLjI1IDEuMTgtLjI1LjQ3IDAgLjg4LjA4IDEuMjMuMjQuMzYuMTYuNjUuMzguODkuNjdzLjQyLjYzLjU0IDEuMDNjLjEyLjQxLjE4Ljg0LjE4IDEuMzIgMCAuMzItLjAyLjU3LS4wNy43NmgtNC4zNmMuMDcuNjIuMjkgMS4xLjY1IDEuNDQuMzYuMzMuODIuNSAxLjM4LjUuMjkgMCAuNTctLjA0LjgzLS4xM3MuNTEtLjIxLjc2LS4zN2wuNTUgMS4wMWMtLjMzLjIxLS42OS4zOS0xLjA5LjUzLS40MS4xNC0uODMuMjEtMS4yNi4yMS0uNDggMC0uOTItLjA4LTEuMzQtLjI1LS40MS0uMTYtLjc2LS40LTEuMDctLjctLjMxLS4zMS0uNTUtLjY5LS43Mi0xLjEzLS4xOC0uNDQtLjI2LS45NS0uMjYtMS41MnptNC42LS42MmMwLS41NS0uMTEtLjk4LS4zNC0xLjI4LS4yMy0uMzEtLjU4LS40Ny0xLjA2LS40Ny0uNDEgMC0uNzcuMTUtMS4wNy40NS0uMzEuMjktLjUuNzMtLjU4IDEuM3ptMi41LjYyYzAtLjU3LjA5LTEuMDguMjgtMS41My4xOC0uNDQuNDMtLjgyLjc1LTEuMTNzLjY5LS41NCAxLjEtLjcxYy40Mi0uMTYuODUtLjI0IDEuMzEtLjI0LjQ1IDAgLjg0LjA4IDEuMTcuMjNzLjYxLjM0Ljg1LjU3bC0uNzcgMS4wMmMtLjE5LS4xNi0uMzgtLjI4LS41Ni0uMzctLjE5LS4wOS0uMzktLjE0LS42MS0uMTQtLjU2IDAtMS4wMS4yMS0xLjM1LjYzLS4zNS40MS0uNTIuOTctLjUyIDEuNjcgMCAuNjkuMTcgMS4yNC41MSAxLjY2LjM0LjQxLjc4LjYyIDEuMzIuNjIuMjggMCAuNTQtLjA2Ljc4LS4xNy4yNC0uMTIuNDUtLjI2LjY0LS40MmwuNjcgMS4wM2MtLjMzLjI5LS42OS41MS0xLjA4LjY1LS4zOS4xNS0uNzguMjMtMS4xOC4yMy0uNDYgMC0uOS0uMDgtMS4zMS0uMjQtLjQtLjE2LS43NS0uMzktMS4wNS0uN3MtLjUzLS42OS0uNy0xLjEzYy0uMTctLjQ1LS4yNS0uOTYtLjI1LTEuNTN6bTYuOTEtNi40NWgxLjU4djYuMTdoLjA1bDIuNTQtMy4xNmgxLjc3bC0yLjM1IDIuOCAyLjU5IDQuMDdoLTEuNzVsLTEuNzctMi45OC0xLjA4IDEuMjN2MS43NWgtMS41OHptMTMuNjkgMS4yN2MtLjI1LS4xMS0uNS0uMTctLjc1LS4xNy0uNTggMC0uODcuMzktLjg3IDEuMTZ2Ljc1aDEuMzR2MS4yN2gtMS4zNHY1LjZoLTEuNjF2LTUuNmgtLjkydi0xLjJsLjkyLS4wN3YtLjcyYzAtLjM1LjA0LS42OC4xMy0uOTguMDgtLjMxLjIxLS41Ny40LS43OXMuNDItLjM5LjcxLS41MWMuMjgtLjEyLjYzLS4xOCAxLjA0LS4xOC4yNCAwIC40OC4wMi42OS4wNy4yMi4wNS40MS4xLjU3LjE3em0uNDggNS4xOGMwLS41Ny4wOS0xLjA4LjI3LTEuNTMuMTctLjQ0LjQxLS44Mi43Mi0xLjEzLjMtLjMxLjY1LS41NCAxLjA0LS43MS4zOS0uMTYuOC0uMjQgMS4yMy0uMjRzLjg0LjA4IDEuMjQuMjRjLjQuMTcuNzQuNCAxLjA0Ljcxcy41NC42OS43MiAxLjEzYy4xOS40NS4yOC45Ni4yOCAxLjUzcy0uMDkgMS4wOC0uMjggMS41M2MtLjE4LjQ0LS40Mi44Mi0uNzIgMS4xM3MtLjY0LjU0LTEuMDQuNy0uODEuMjQtMS4yNC4yNC0uODQtLjA4LTEuMjMtLjI0LS43NC0uMzktMS4wNC0uN2MtLjMxLS4zMS0uNTUtLjY5LS43Mi0xLjEzLS4xOC0uNDUtLjI3LS45Ni0uMjctMS41M3ptMS42NSAwYzAgLjY5LjE0IDEuMjQuNDMgMS42Ni4yOC40MS42OC42MiAxLjE4LjYyLjUxIDAgLjktLjIxIDEuMTktLjYyLjI5LS40Mi40NC0uOTcuNDQtMS42NiAwLS43LS4xNS0xLjI2LS40NC0xLjY3LS4yOS0uNDItLjY4LS42My0xLjE5LS42My0uNSAwLS45LjIxLTEuMTguNjMtLjI5LjQxLS40My45Ny0uNDMgMS42N3ptNi40OC0zLjQ0aDEuMzNsLjEyIDEuMjFoLjA1Yy4yNC0uNDQuNTQtLjc5Ljg4LTEuMDIuMzUtLjI0LjctLjM2IDEuMDctLjM2LjMyIDAgLjU5LjA1Ljc4LjE0bC0uMjggMS40LS4zMy0uMDljLS4xMS0uMDEtLjIzLS4wMi0uMzgtLjAyLS4yNyAwLS41Ni4xLS44Ni4zMXMtLjU1LjU4LS43NyAxLjF2NC4yaC0xLjYxem0tNDcuODcgMTVoMS42MXY0LjFjMCAuNTcuMDguOTcuMjUgMS4yLjE3LjI0LjQ0LjM1LjgxLjM1LjMgMCAuNTctLjA3LjgtLjIyLjIyLS4xNS40Ny0uMzkuNzMtLjczdi00LjdoMS42MXY2Ljg3aC0xLjMybC0uMTItMS4wMWgtLjA0Yy0uMy4zNi0uNjMuNjQtLjk4Ljg2LS4zNS4yMS0uNzYuMzItMS4yNC4zMi0uNzMgMC0xLjI3LS4yNC0xLjYxLS43MS0uMzMtLjQ3LS41LTEuMTQtLjUtMi4wMnptOS40NiA3LjQzdjIuMTZoLTEuNjF2LTkuNTloMS4zM2wuMTIuNzJoLjA1Yy4yOS0uMjQuNjEtLjQ1Ljk3LS42My4zNS0uMTcuNzItLjI2IDEuMS0uMjYuNDMgMCAuODEuMDggMS4xNS4yNC4zMy4xNy42MS40Ljg0LjcxLjI0LjMxLjQxLjY4LjUzIDEuMTEuMTMuNDIuMTkuOTEuMTkgMS40NCAwIC41OS0uMDkgMS4xMS0uMjUgMS41Ny0uMTYuNDctLjM4Ljg1LS42NSAxLjE2LS4yNy4zMi0uNTguNTYtLjk0LjczLS4zNS4xNi0uNzIuMjUtMS4xLjI1LS4zIDAtLjYtLjA3LS45LS4ycy0uNTktLjMxLS44Ny0uNTZ6bTAtMi4zYy4yNi4yMi41LjM3LjczLjQ1LjI0LjA5LjQ2LjEzLjY2LjEzLjQ2IDAgLjg0LS4yIDEuMTUtLjYuMzEtLjM5LjQ2LS45OC40Ni0xLjc3IDAtLjY5LS4xMi0xLjIyLS4zNS0xLjYxLS4yMy0uMzgtLjYxLS41Ny0xLjEzLS41Ny0uNDkgMC0uOTkuMjYtMS41Mi43N3ptNS44Ny0xLjY5YzAtLjU2LjA4LTEuMDYuMjUtMS41MS4xNi0uNDUuMzctLjgzLjY1LTEuMTQuMjctLjMuNTgtLjU0LjkzLS43MXMuNzEtLjI1IDEuMDgtLjI1Yy4zOSAwIC43My4wNyAxIC4yLjI3LjE0LjU0LjMyLjgxLjU1bC0uMDYtMS4xdi0yLjQ5aDEuNjF2OS44OGgtMS4zM2wtLjExLS43NGgtLjA2Yy0uMjUuMjUtLjU0LjQ2LS44OC42NC0uMzMuMTgtLjY5LjI3LTEuMDYuMjctLjg3IDAtMS41Ni0uMzItMi4wNy0uOTVzLS43Ni0xLjUxLS43Ni0yLjY1em0xLjY3LS4wMWMwIC43NC4xMyAxLjMxLjQgMS43LjI2LjM4LjY1LjU4IDEuMTUuNTguNTEgMCAuOTktLjI2IDEuNDQtLjc3di0zLjIxYy0uMjQtLjIxLS40OC0uMzYtLjctLjQ1LS4yMy0uMDgtLjQ2LS4xMi0uNy0uMTItLjQ1IDAtLjgyLjE5LTEuMTMuNTktLjMxLjM5LS40Ni45NS0uNDYgMS42OHptNi4zNSAxLjU5YzAtLjczLjMyLTEuMy45Ny0xLjcxLjY0LS40IDEuNjctLjY4IDMuMDgtLjg0IDAtLjE3LS4wMi0uMzQtLjA3LS41MS0uMDUtLjE2LS4xMi0uMy0uMjItLjQzcy0uMjItLjIyLS4zOC0uM2MtLjE1LS4wNi0uMzQtLjEtLjU4LS4xLS4zNCAwLS42OC4wNy0xIC4ycy0uNjMuMjktLjkzLjQ3bC0uNTktMS4wOGMuMzktLjI0LjgxLS40NSAxLjI4LS42My40Ny0uMTcuOTktLjI2IDEuNTQtLjI2Ljg2IDAgMS41MS4yNSAxLjkzLjc2cy42MyAxLjI1LjYzIDIuMjF2NC4wN2gtMS4zMmwtLjEyLS43NmgtLjA1Yy0uMy4yNy0uNjMuNDgtLjk4LjY2cy0uNzMuMjctMS4xNC4yN2MtLjYxIDAtMS4xLS4xOS0xLjQ4LS41Ni0uMzgtLjM2LS41Ny0uODUtLjU3LTEuNDZ6bTEuNTctLjEyYzAgLjMuMDkuNTMuMjcuNjcuMTkuMTQuNDIuMjEuNzEuMjEuMjggMCAuNTQtLjA3Ljc3LS4ycy40OC0uMzEuNzMtLjU2di0xLjU0Yy0uNDcuMDYtLjg2LjEzLTEuMTguMjMtLjMxLjA5LS41Ny4xOS0uNzYuMzFzLS4zMy4yNS0uNDEuNGMtLjA5LjE1LS4xMy4zMS0uMTMuNDh6bTYuMjktMy42M2gtLjk4di0xLjJsMS4wNi0uMDcuMi0xLjg4aDEuMzR2MS44OGgxLjc1djEuMjdoLTEuNzV2My4yOGMwIC44LjMyIDEuMi45NyAxLjIuMTIgMCAuMjQtLjAxLjM3LS4wNC4xMi0uMDMuMjQtLjA3LjM0LS4xMWwuMjggMS4xOWMtLjE5LjA2LS40LjEyLS42NC4xNy0uMjMuMDUtLjQ5LjA4LS43Ni4wOC0uNCAwLS43NC0uMDYtMS4wMi0uMTgtLjI3LS4xMy0uNDktLjMtLjY3LS41Mi0uMTctLjIxLS4zLS40OC0uMzctLjc4LS4wOC0uMy0uMTItLjY0LS4xMi0xLjAxem00LjM2IDIuMTdjMC0uNTYuMDktMS4wNi4yNy0xLjUxcy40MS0uODMuNzEtMS4xNGMuMjktLjMuNjMtLjU0IDEuMDEtLjcxLjM5LS4xNy43OC0uMjUgMS4xOC0uMjUuNDcgMCAuODguMDggMS4yMy4yNC4zNi4xNi42NS4zOC44OS42N3MuNDIuNjMuNTQgMS4wM2MuMTIuNDEuMTguODQuMTggMS4zMiAwIC4zMi0uMDIuNTctLjA3Ljc2aC00LjM3Yy4wOC42Mi4yOSAxLjEuNjUgMS40NC4zNi4zMy44Mi41IDEuMzguNS4zIDAgLjU4LS4wNC44NC0uMTMuMjUtLjA5LjUxLS4yMS43Ni0uMzdsLjU0IDEuMDFjLS4zMi4yMS0uNjkuMzktMS4wOS41M3MtLjgyLjIxLTEuMjYuMjFjLS40NyAwLS45Mi0uMDgtMS4zMy0uMjUtLjQxLS4xNi0uNzctLjQtMS4wOC0uNy0uMy0uMzEtLjU0LS42OS0uNzItMS4xMy0uMTctLjQ0LS4yNi0uOTUtLjI2LTEuNTJ6bTQuNjEtLjYyYzAtLjU1LS4xMS0uOTgtLjM0LTEuMjgtLjIzLS4zMS0uNTgtLjQ3LTEuMDYtLjQ3LS40MSAwLS43Ny4xNS0xLjA4LjQ1LS4zMS4yOS0uNS43My0uNTcgMS4zem0zLjAxIDIuMjNjLjMxLjI0LjYxLjQzLjkyLjU3LjMuMTMuNjMuMi45OC4yLjM4IDAgLjY1LS4wOC44My0uMjNzLjI3LS4zNS4yNy0uNmMwLS4xNC0uMDUtLjI2LS4xMy0uMzctLjA4LS4xLS4yLS4yLS4zNC0uMjgtLjE0LS4wOS0uMjktLjE2LS40Ny0uMjNsLS41My0uMjJjLS4yMy0uMDktLjQ2LS4xOC0uNjktLjMtLjIzLS4xMS0uNDQtLjI0LS42Mi0uNHMtLjMzLS4zNS0uNDUtLjU1Yy0uMTItLjIxLS4xOC0uNDYtLjE4LS43NSAwLS42MS4yMy0xLjEuNjgtMS40OS40NC0uMzggMS4wNi0uNTcgMS44My0uNTcuNDggMCAuOTEuMDggMS4yOS4yNXMuNzEuMzYuOTkuNTdsLS43NC45OGMtLjI0LS4xNy0uNDktLjMyLS43My0uNDItLjI1LS4xMS0uNTEtLjE2LS43OC0uMTYtLjM1IDAtLjYuMDctLjc2LjIxLS4xNy4xNS0uMjUuMzMtLjI1LjU0IDAgLjE0LjA0LjI2LjEyLjM2cy4xOC4xOC4zMS4yNmMuMTQuMDcuMjkuMTQuNDYuMjFsLjU0LjE5Yy4yMy4wOS40Ny4xOC43LjI5cy40NC4yNC42NC40Yy4xOS4xNi4zNC4zNS40Ni41OC4xMS4yMy4xNy41LjE3LjgyIDAgLjMtLjA2LjU4LS4xNy44My0uMTIuMjYtLjI5LjQ4LS41MS42OC0uMjMuMTktLjUxLjM0LS44NC40NS0uMzQuMTEtLjcyLjE3LTEuMTUuMTctLjQ4IDAtLjk1LS4wOS0xLjQxLS4yNy0uNDYtLjE5LS44Ni0uNDEtMS4yLS42OHoiIGZpbGw9IiM1MzUzNTMiLz48L2c+PC9zdmc+)]()
###
Cite this article
Mattsson, C.E.S., Criscione, T. & Takes, F.W. Circulation of a digital community currency.
*Sci Rep*
**13**
, 5864 (2023).
[Download citation]()
* Received
:
08 March 2023
* Accepted
:
08 April 2023
* Published
:
11 April 2023
* DOI
:
###
Share this article
Anyone you share the following link with will be able to read this content:
Get shareable link
Sorry, a shareable link is not currently available for this article.
Copy to clipboard
Provided by the Springer Nature SharedIt content-sharing initiative
Comments
----------
By submitting a comment you agree to abide by our
[Terms](/info/tandc.html)
and
[Community Guidelines](/info/community-guidelines.html)
. If you find something abusive or that does not comply with our terms or guidelines please flag it as inappropriate.
[Download PDF](/articles/s41598-023-33184-1.pdf)
Advertisement
[![Advertisement](//pubads.g.doubleclick.net/gampad/ad?iu=/285/scientific_reports/article&sz=300x250&c=-&t=pos%3Dright%26type%3Darticle%26artid%3Ds41598-023-33184-1%26doi%3D10.1038/s41598-023-33184-1%26subjmeta%3D1042,2801,530,639,705,766%26kwrd%3DComplex+networks,Computational+science)](//pubads.g.doubleclick.net/gampad/jump?iu=/285/scientific_reports/article&sz=300x250&c=-&t=pos%3Dright%26type%3Darticle%26artid%3Ds41598-023-33184-1%26doi%3D10.1038/s41598-023-33184-1%26subjmeta%3D1042,2801,530,639,705,766%26kwrd%3DComplex+networks,Computational+science)
Explore content
-----------------
* [Research articles](/srep/research-articles)
* [News & Comment](/srep/news-and-comment)
* [Collections](/srep/collections)
* [Subjects](/srep/browse-subjects)
* [Follow us on Facebook]()
* [Follow us on Twitter]()
* [Sign up for alerts]()
* [RSS feed]()
About the journal
-------------------
* [About Scientific Reports](/srep/about)
* [Open Access](/srep/open-access)
* [Journal policies](/srep/journal-policies)
* [Guide to referees](/srep/guide-to-referees)
* [Calls for Papers](/srep/calls-for-papers)
* [Contact](/srep/contact)
* [Editor's Choice](/srep/editorschoice)
* [Journal highlights](/srep/highlights)
Publish with us
-----------------
* [For authors](/srep/author-instructions)
* [Language editing services]()
* [Submit manuscript]()
Search
--------
Search articles by subject, keyword or author
Show results from
All journals
This journal
Search
[Advanced search](/search/advanced)
###
Quick links
* [Explore articles by subject](/subjects)
* [Find a job](/naturecareers)
* [Guide to authors](/authors/index.html)
* [Editorial policies](/authors/editorial_policies/)
Scientific Reports (
*Sci Rep*
)
ISSN
2045-2322
(online)
nature.com sitemap
--------------------
###
About Nature Portfolio
* [About us]()
* [Press releases]()
* [Press office]()
* [Contact us]()
###
Discover content
* [Journals A-Z]()
* [Articles by subject]()
* [Nano]()
* [Protocol Exchange]()
* [Nature Index]()
###
Publishing policies
* [Nature portfolio policies]()
* [Open access]()
###
Author & Researcher services
* [Reprints & permissions]()
* [Research data]()
* [Language editing]()
* [Scientific editing]()
* [Nature Masterclasses]()
* [Live Expert Trainer-led workshops]()
* [Research Solutions]()
###
Libraries & institutions
* [Librarian service & tools]()
* [Librarian portal]()
* [Open research]()
* [Recommend to library]()
###
Advertising & partnerships
* [Advertising]()
* [Partnerships & Services]()
* [Media kits]()
* [Branded
content]()
###
Career development
* [Nature Careers]()
* [Nature
Conferences]()
* [Nature
events]()
###
Regional websites
* [Nature Africa]()
* [Nature China]()
* [Nature India]()
* [Nature Italy]()
* [Nature Japan]()
* [Nature Korea]()
* [Nature Middle East]()
* [Privacy
Policy]()
* [Use
of cookies]()
* Your privacy choices/Manage cookies
* [Legal
notice]()
* [Accessibility
statement]()
* [Terms & Conditions]()
* [Your US state privacy rights]()
[![Springer Nature](/static/images/logos/sn-logo-white-ea63208b81.svg)]()
©️ 2023 Springer Nature Limited
xml version="1.0" encoding="UTF-8"?
Close banner
Close
![Nature Briefing](/static/images/logos/nature-briefing-logo-n150-white-d81c9da3ec.svg)
Sign up for the
*Nature Briefing*
newsletter -- what matters in science, free to your inbox daily.
Email address
Sign up
I agree my information will be processed in accordance with the
*Nature*
and Springer Nature Limited
[Privacy Policy]()
.
Close banner
Close
Get the most important science stories of the day, free in your inbox.
[Sign up for Nature Briefing](/briefing/signup/)
![]()
![](/q8bcz7xr/article/s41598-023-33184-1)