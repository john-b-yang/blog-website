title: A Technical Dissection of the Libra Blockchain
date: 2019-06-20
description: So turns out, the Libra "Blockchain" isn't an actual blockchain? A discussion and benefits analysis of Libra's implementation
image: /static/pictures/Libra/head-image.png
readtime: 11 MINS
time: THURSDAY, JUNE 20, 2019
tags: [Paper]

Recently, Facebook has taken a dive into the field of cryptocurrency with the announcement of Libra, a financial service founded upon cryptographic principles and blockchain technology with a long term, grand vision of becoming a unified economic infrastructure on a multinational, global scale. Since its release several weeks ago, there has been plenty of reactions and feedback from news outlets and industry professionals debating the economic ramifications of the Libra organization. Regardless of the debate, Libra's coming out party marks an exciting milestone with regards to the formalization of blockchain technology as a potential solution for enforcing trust, integrity, and authentication in an increasingly digitalized world.

There's been plenty of comments and criticism targeting the monetary implications that come with Libra's growth. However, in this article, I'll be more focused on summarizing the technical innovations powering the Libra platform, specifically the [Libra Blockchain](https://developers.libra.org/docs/the-libra-blockchain-paper). I'm primarily interested in how Libra attempts to address questions regarding how to support scalability and eliminate computational inefficiency (a.k.a. Proof of Work), challenges well publicized by the proliferation of Bitcoin and other cryptocurrency predecessors. Additionally, Libra adopts and mirrors smart contracts, an age old idea implemented in Ethereum, allowing client users to create their own protocols for a broad range of business. While the concept of smart contracts has indubitably made blockchain more useful, there have been no shortage of security issues associated with poorly written contracts. I'll also be examining Libra's companion DSL for programming smart contracts, called Move! It's an interesting redesign of Solidity that aims to make writing a contract a much safer, yet sufficiently expressive process.

This article's structure is the same as the Libra Blockchain PDF. Per section, I'll attempt to highlight and analysis Libra's advancements from the technical and industry perspective of established cryptocurrencies like Ethereum and Bitcoin. I'll try to avoid repeating the paper and keep things concise by focusing on the analysis instead of facts. As usual, feedback and criticism are always welcome in the form of a comment below. Thanks for reading!

<br>
##### 1 Introduction

The start of this paper defines some terminology that will be use repeatedly throughout the article.

**Libra Coin** is the currency for the Libra blockchain. Libra is a fiat currency, meaning that is value is tied to a trove of real world monetary resources. Because of this, Libra should be much less subject to the volatility of traditional cryptocurrencies like Bitcoin, where its value is a direct reflection of the market's assessment.

**Validators** are the entities responsible for processing transactions and maintaining the blockchain's state, similar to the role of a miner. As of Libra's inception, validator membership is limited to the Libra Association, but this will change as Libra changes from permissioned to a truly public blockchain.

Why is Libra going through a permissioned phase instead of just starting off as public? This decision is likely borne from Libra's creators hoping to more easily perform course correction in response to user feedback and nurture Libra's initial growth into a more mature, refined, and tested platform before fully ceding control to the public arena. In addition, because the validators from the Libra Association are known and more likely cooperative, the concern for an anonymous user with malicious intent would not be a tangible issue for now.

What's more is that instead of Proof of Work consensus, where the miner that gets to add the next transaction is chosen non-deterministically, validators switch off as a *leader* which proposes transactions submitted by clients or other validators. This setup foreshadows a interesting development towards creating a more computationally efficient consensus protocol, supplanting exhaustive tasks especially like Proof of Work.

The description of the **Libra Blockchain** is where things get interesting. It's officially defined as a "cryptographically authenticated database that serves as a ledger of programmable resources". However, under the hood, unlike a traditional linked-list-esque structure, the "blockchain" is actually implemented with the [Merkle Tree](https://en.wikipedia.org/wiki/Merkle_tree) data structure. The "why" and "how" of this will be discussed later on.

The authors also establish some of the objectives that serve as guiding design principles for Libra. One major theme is scalability, as the paper states "The Libra protocol must scale to support the transaction volume necessary...to grow into a global financial infrastructure". Through cryptographic principles and efficient structures, the authors believe Libra can enforce the same rigor of authentication and integrity without nearly as much computing power required.

<br>
##### 2 Logical Data Model

In this section, the authors discuss Libra's general organization and data model. They formalize the terminology regarding an individual ledger state and a transaction. Finally, how these two structures come together to form a historical ledger of states is explained.

From a high level, the Libra Blockchain can be visualized by the following diagram. For the most part, the general layout greatly resembles a traditional blockchain. One notable difference is that blockchains such as Bitcoin tend to group multiple transactions. However, a block (or in this case, "version") in Libra is distinguished by a *single* transaction. This model makes it much more straightforward for answering any queries regarding a ledger's state at any version. Incrementing a ledger's state per transactions also provides greater search granularity. Per usual, new transactions can only be added on top the most recent ledger state version.

<img src="/static/pictures/Libra/2-ledger-overview.png" alt="Ledger Overview" style="height:200px;display:block;margin-left:auto;margin-right:auto"/>

The next question that might naturally arise is, what goes into a ledger's state? It's really just a simple key-value store associating each account address with a set of resources (data values, i.e. how much Libra Coin does 0x123... have?) and modules (smart contracts, a.k.a. Move bytecode defining a new resource's type + associated procedures. i.e. transfer of Libra Coin between accounts). The below diagram is essentially appropriated from the paper, just with a couple additional illustrations for greater clarity and detail.

<img src="/static/pictures/Libra/2-ledger-state.png" alt="Ledger State" style="height:300px;display:block;margin-left:auto;margin-right:auto"/>

The schematics governing account addresses are nothing new. Each user has a verifying + signing key, and the public key, which would be the addresses in the above diagram, is just a cryptographic hash of the verifying key. Resources, broken down, simply associate a resource type (defined by modules) with a particular quantity or value.

*A Side Note*: The Libra paper states that "each account can store at most one resource of a given type", which was initially confusing to me. If I want to exchange Libra Coin, would I be barred from it because of the aforementioned limitation? After some thought, I realized that in such a situation, the *value* of the resource would be modified. Such a design has the benefit of eliminating both redundancy and the difficulties that come with fragmentation. In this context, by fragmentation, I mean a situation where there are multiple resources per type.

<img src="/static/pictures/Libra/2-ledger-resource.png" alt="Resource" style="height:150px;display:block;margin-left:auto;margin-right:auto"/>

Notice that a resource is uniquely identified by &lt;account address (creator)&gt; / &lt;module name&gt; / &lt;resource type&gt;. In other words, multiple modules and resources could have the same name, but are distinguished by their creators, making them distinct types. Therefore, in the above diagram, the two coins in account 0x27... have the same module name (Coin) and resource name (Coin.T), but ultimately, are different types (0x27.Coin.T vs. 0x45.Coin.T). I like this convention for identifying resource types because it prevents a first-come-first-serve issue for naming modules or resources (ala [domain squatting](https://en.wikipedia.org/wiki/Cybersquatting)). Similar to smart contracts, modules wholly define rules for mutating, deleting, and publishing a resource. As of this point, a published module is immutable, although methods for safe updates are being explored for release in the future.

<br>
##### 4 Authenticated Data Structures and Storage

The actual implementation of Libra

<br>
##### Questions & Thoughts
Can a single module declare multiple resource types?
If an account is deleted or removed, what happens to the modules it defines or the resources that it contains?
