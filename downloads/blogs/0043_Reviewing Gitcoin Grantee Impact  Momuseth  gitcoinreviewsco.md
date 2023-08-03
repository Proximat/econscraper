Reviewing Gitcoin Grantee Impact - Momus.eth & gitcoinreviews.co - 🧙 🧙‍♀️ Ideas and Open Discussion - Gitcoin Governance
[Gitcoin Governance](/)
[Reviewing Gitcoin Grantee Impact - Momus.eth & gitcoinreviews.co](/t/reviewing-gitcoin-grantee-impact-momus-eth-gitcoinreviews-co/15215)
==========================================================================================================================================
[🧙 🧙‍♀️ Ideas and Open Discussion]()
[contributors]()
,
[Grants2]()
,
[community]()
[jon-spark-eco]()
May 31, 2023, 6:42pm
#1
**tl;dr**
==========
As a long-time supporter of the Gitcoin climate grant round, Momus.eth has made it a mission to support the emerging regenerative finance movement. They have contributed generously to the Climate grant round matching fund and individual grantees. After making significant contributions, the question is whether these grantees have made an impact with the funding received. Out of this need, Momus built a new tool called DeReSy (DEcentralized REview SYstem), with the first use case being reviewing climate round grantees' impact and use of funds. The first set of reviews was conducted and found that seven out of the top ten most funded climate projects in GR14 had made a positive impact with their work and should receive additional funding (reviews can be found here:
[gitcoinreviews.co]()
).
**Who is Momus**
=================
momus.eth, aka the Momus Collective, is an anonymous group that we do not know much about. They did well in the early days of crypto and curated a fantastic collection of early NFTs from 2018-2020. They were betting on artists in a bear market at a time when most people didn't understand or see the value of NFTs. They saw the possibilities at the intersection of the physical and digital world and used their precious ETH to encourage artists to push the space forward. They own many early and historically significant CryptoArt pieces.
In the same spirit of funding and supporting the next generation of innovation on the blockchain, they began funding regens and climate-focused projects. In their words, "This regenerative movement is especially critical now, at a point in history when we need to be re-aligning human incentives to enable a sustainable way of life for the planet and future generations." They have begun selling some of their NFT art collection to fund this critical work and, in their words, "to signal that your (climate/ReFi projects) contribution to the space is valuable and that you can persevere through the doubts of the bear...Regens Unite!" In late 2021, the Momus Collective began funding projects via Gitcoin and has contributed 1.5 Million DAI to the Gitcoin grant climate round matching fund and over 444k DAI in direct donations to grants.
You can read their most recent public statement here:
<
**What is DeReSy?**
====================
Momus built a contract-based review system deployed on Arbitrum: DeReSy (DEcentralized REview SYstem). This review system was initially designed to enable the evaluation of Gitcoin funding in a transparent, scalable, self-service, credibly neutral way. However, DeReSy is application-agnostic: it could review a list of movies, products, protocols, or VC funds. The hope is that others use DeReSy to increase the efficiency of their work through contracted reviews.
The general idea is that a sponsor writes a ReviewForm to evaluate a set of Targets. The sponsor then selects a group of Reviewers who will be compensated - in ETH - to fill in the ReviewForm for each Target. This is done by creating a ReviewRequest and depositing enough ETH to guarantee reviewers will be paid for their work. DeReSy is built on Arbitrum and can be forked by anyone to begin using it. Arbitrum is used to automate the execution of the payment logic, and IPFS is used to store data. DeReSy does not rely on any centralized component and is unstoppable as long as Arbitrum and IPFS exist. Momus is excited to see how others use this tool.
Fully-Decentralized DeReSy application, on arbitrum and ipfs:
<
DeReSy smart contract code and IPFS Single Page Application:
![]()
[GitHub]()
![]()
###
[GitHub - chimi-co/deresy]()
Contribute to chimi-co/deresy development by creating an account on GitHub.
DeReSy V1 deployment:
[DeresyRequests | Address 0x50e9a780bde93ccfa592ce9e981d5dbaf9cfc107 | Arbiscan]()
**What is
[GitcoinReviews.co]()
?**
===============================================================
One of the challenges the Momus Collective has faced is determining what Gitcoin grants to fund and, perhaps more importantly, whether these projects are making an impact with the funding. There was a need for a tool to review grants, so Momus funded building one.
[Gitcoinreviews.co]()
is the first use case for DeReSy.
As an initial test of
[gitcoinreview.co]()
and the underlying DeReSy protocol, Momus used the site to review the top 10 most funded projects from the GR14 climate round. They worked with two reviewers (as seen on-chain, I was one of the reviewers) to independently review these grants/projects. All reviews are on-chain, and as previously noted, Arbitrum was used for the execution and payments, and IPFS stores all the data. A third party, like Momus, can fund these reviews by issuing bounties for reviewers to perform due diligence on projects.
During the test run, the two reviewers sometimes disagreed with each other. Still, there are clear trends on the positive impact projects generated and how much they would benefit from additional funding. The compiled review data is below.
[![Screenshot 2023-05-31 at 2.38.26 PM]()
Screenshot 2023-05-31 at 2.38.26 PM
823x467 61.4 KB]( "Screenshot 2023-05-31 at 2.38.26 PM")
While DeReSy has the advantage of being an unstoppable, immutable, self-service protocol, the user experience from serving content from IPFS and looking up key review data from Arbitrum is slow and not ideal for end users. For this reason,
[gitcoinreviews.co]()
serves as a fast-cache to both IPFS and Arbitrum, and interacts with the underlying DeReSy platform to serve content and provide a UI for the reviewers to complete their reviews efficiently.
[GitcoinReviews.co]()
UI code:
<
[GitcoinReviews.co]()
API code:
<
**Why?**
=========
The use of funds and progress projects are making is important to funders. Contributors will contribute more if they can assess the project's progress and see the impact they are funding. There is no easy way for matching fund contributors and individual contributors to evaluate a project's impact and progress.
[Gitcoinreviews.co]()
provides a way to assess project progress and impact.
To conduct due diligence, you can review a project's Twitter, webpage, Discord, and other online presence to assess what they are working on and shipping. You can investigate on-chain activity to see where funds have gone and what % have been off-ramped to FIAT. The problem is with hundreds of projects in grant rounds; this is time-consuming and inefficient.
Momus built
[Gitcoinreviews.co]()
to outsource this due diligence work. The tool provides a 3rd party audit of the project that should present a non-biased view of the project. Momus funded the initial alpha test reviews and plans to fund further reviews of the climate grant round. We hope to see other matching pool contributors do this for additional grant rounds.
**The Future**
===============
[Gitcoinreviews.co]()
pulled in data from the old c-Grants platform. We are beginning work on v2 of the site, including integration with the Allo Protocol and the Grants Stack. Some feature improvements include editing and updating reviews and tracking version history all on-chain. There will be improvements to the UI/UX for both reviewers and the public view of the site. For the projects being reviewed, we also want to incorporate an on-chain feedback form for self-reporting work accomplished and project impacts.
We are also working with other projects, including
[Hypercerts]()
, to explore using these reviews as on-chain attestations of verified impact. We may explore integrating the project's Hypercerts into the project reviews. Another possibility is for the site to connect to various api's to pull more data and metrics about the projects into the review site.
If you are interested in working with us or spinning up another use case for DeReSy please contact us at
[](mailto:)
.
12 Likes
[Governance update: May 2023]()
[Governance update: June 2023]()
[Gitcoin Digest #8 2023]()
[Governance update: June 2023]()
[carlosjmelgar]()
May 31, 2023, 9:10pm
#2
I love this. Devansh and I just had a call discussing something like this. We discussed creating a group of reviewers from varied backgrounds to review grantees across various platforms.
I would like to know if there is a process for opting in. This could be very helpful to smaller grantees who are confident about their impact and lack visibility.
3 Likes
[thedevanshmehta]()
June 1, 2023, 11:48am
#3
I went through the
[gitcoinreviews.co]()
site in detail and really love how its presented, especially for a first version. I can imagine it evolving as a Twitter community notes equivalent for gitcoin, showing up for projects against their listing in a round. Separating the signal from the noise is key to improving donor experience!
I have a background as an investigative reporter and then 5 years in the social space. As i discussed with Carlos earlier, I feel I could do evaluations fairly well so count me in for any bounties on reviewing more gitcoin projects.
1 Like
[jon-spark-eco]()
June 1, 2023, 1:18pm
#4
Thanks,
[@carlosjmelgar](/u/carlosjmelgar)
! For the first test, Momus chose to fund a small subset of reviews based on the top ten funded grants in the round. We plan to do a larger set of reviews of the alpha/beta rounds. At this time, the bounty funder who spins up a request for reviews chooses what projects to review and chooses the reviewers. I think in future versions, there may be a way for projects to opt-in.
One thing I didn't write as much about is that we also sent a form to projects to fill out and "self-review" their own impact. The reviewers then used this as a starting place for the review. This was an off-chain process; we hope to bring it on-chain in v2. I think these self-reviews will be a place for smaller projects to dig in and show their work with proof. During our first set of reviews, projects that provided detailed information about the work they accomplished, uses of funds with backup, and a clear roadmap for future use of funds got higher reviews unless the reviewer found issues with these self-reviews.
Hey,
[@thedevanshmehta](/u/thedevanshmehta)
, I will reach out to chat. It sounds like you would be a good candidate for being a reviewer. We would like to get to a point where we are providing a score based on the reviews, and ideally, this would be integrated into the grants stack at some point.
3 Likes
[shawn16400]()
June 1, 2023, 1:24pm
#5
Wow. This capability is exciting and I love the decentralized nature of evaluating impact - which I think web3 needs to do better at across the board.
![]()
jon-spark-eco:
>
>
> The first set of reviews was conducted and found that seven out of the top ten most funded climate projects in GR14 had made a positive impact with their work and should receive additional funding (reviews can be found here:
> [gitcoinreviews.co]()
> ).
>
>
>
>
Time is short, but I would encourage you to consider applying for a retroactive public goods funding via the Gitcoin Citizens Round. Nominations / applications close on Sunday.
<
3 Likes
[shawn16400]()
June 1, 2023, 1:28pm
#6
![]()
jon-spark-eco:
>
>
> DeReSy
>
>
>
>
And... really interested to see if / how we might use this capability for later Gitcoin Citizens Rounds -= both for pre and post assessment... DM sent.
2 Likes
[knome7337]()
June 2, 2023, 2:30am
#7
Great to see community engagement on this. Jon and myself spent a lot of time working through available data and reviews are a crucial element to track projects.
We welcome community inputs on datapoints to be covered in future reviews and a huge shoutout to Momus for their support.
2 Likes
[jengajojo]()
June 2, 2023, 8:45am
#8
Thank you Momus.eth for shipping this! Great to hear about the future hypercerts integration
I like the fact that this decentralizes the review system, I wonder if the reviewers are incentivised to collude with each other to pick up the bounty? Maybe the reviwers themselves should be asked to stake some GTC with slashing conditions. I understand that this may demotivate newbies from participating, but may incentivize professional groups to apply as reviewers.
2 Likes
[thedevanshmehta]()
June 2, 2023, 11:00am
#9
I love the quant based approach to evaluations! We could go the way of yelp/airbnb/amazon where every reviewer gives their own score, or one that's standardized across certain parameters (1 = team is not responsive/not continuing the project , 2 = ...). Whichever route we go, we shouldn't neglect the qualitative, which can be helpful to the projects as an outside assessment of their work.
I have been playing around with GPT4 scoring impact certificates. Not much to report on that front except the importance of giving it prompts to anchor ratings, otherwise everything gets between a 3 and 4
![🤣]( "🤣")
Edit for an unsolicited suggestion: Deresys sounds better than Deresy
2 Likes
[jon-spark-eco]()
June 2, 2023, 1:10pm
#10
gm,
[@jengajojo](/u/jengajojo)
I appreciate the feedback. I don't think there is an incentive for reviewers to collude. The way the initial test worked was Momus chose two allow-listed reviewers (
[@knome7337](/u/knome7337)
and Myself). They funded two reviews per project with equal payouts. This way, we were incentivized to conduct the reviews but not to collude. By allow-listing reviewers, the party funding the reviews can choose trusted individuals to conduct a thorough review. We are still exploring how the incentives would work if these were open bounties for anyone to claim. By allow-listing reviewers the review funder is essentially hiring them to do the reviews but the work and payments are decentralized. In the case of an anon like Momus this is ideal as they can fund the contract and then the reviewers do the reviews without them having to do any further work.
2 Likes
[MathildaDV]()
June 2, 2023, 7:34pm
#11
This is great
[@jon-spark-eco](/u/jon-spark-eco)
! This ties in so well with how we're exploring further ways of improving the relationship and transparency between grantees and funders, and how we might support those initiatives. Very excited for V2 and a possible implementation of Hypercerts! There's a lot to do here and I'm eager to explore more
2 Likes
[thedevanshmehta]()
June 4, 2023, 1:52pm
#12
Hi Jon,
I was going through the
[Arbitrum DAO governance forum]()
and had the thought that we could submit a proposal to them for using Deresy to pay reviewers evaluating Gitcoin grantees. It's the right time as they recently got decentralized and are looking for avenues to deploy $4 billion+ in treasury funds to grow the ecosystem.
It could be a compelling pitch for them as it positions Arbitrum as the leading blockchain for grant evaluators. The outcome from their grant would be creating a pool of evaluators interacting with the Deresy smart contract on Arbitrum to receive payouts and post their reviews. Eventually, we would aim for this to be sustainable by giving donors the option of allocating 7-10% of their donation to the evaluator pool (the standard in the traditional nonprofit world).
Let me know your thoughts, happy to work on putting a proposal together!
2 Likes
[ZER8]()
June 9, 2023, 7:32pm
#13
Thanks for writing this Jon. I personally find it amazing that someone took time and put effort into solving an issue that has been around for so much time- namely creating a decentralized review system.
I don't think we ever chatted, but I would be very interested in reviewing grants with Deresy. Sending an e-mail now
![:slight_smile:]( ":slight_smile:")
As time passes I'm sure we can reach a even better "review" formula. Good times
2 Likes
* [Home](/)
* [Categories](/categories)
* [FAQ/Guidelines](/guidelines)
* [Terms of Service](/tos)
* [Privacy Policy](/privacy)
Powered by
[Discourse]()
, best viewed with JavaScript enabled