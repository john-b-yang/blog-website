title: A Technical Dissection of the Libra Blockchain
date: 2019-06-20
description: So turns out, the Libra "Blockchain" isn't an actual blockchain? A discussion and benefits analysis of Libra's implementation
image: /static/pictures/Libra/head-image.png
readtime: 11 MINS
time: THURSDAY, JUNE 20, 2019
tags: [Paper]

Recently, Facebook has taken a dive into the field of cryptocurrency with the announcement of Libra, a financial service founded upon cryptographic principles and blockchain technology with a long term, grand vision of becoming a unified economic infrastructure on a multinational, global scale. Since its release several weeks ago, there has been plenty of reactions and feedback from news outlets and industry professionals debating the economic ramifications of the Libra organization. Regardless of the debate, Libra's coming out party marks an exciting milestone with regards to the formalization of blockchain technology as a potential solution for enforcing trust, integrity, and authentication in an increasingly digitalized world.

There's been plenty of comments and criticism targeting the monetary implications that come with Libra's growth. However, in this article, I'll be more focused on understanding the technical innovations powering the Libra platform, specifically the [Libra Blockchain](https://developers.libra.org/docs/the-libra-blockchain-paper). I'm primarily interested in how Libra attempts to address questions regarding how to support scalability and eliminate computational inefficiency (a.k.a. Proof of Work), challenges well publicized by the proliferation of Bitcoin and other cryptocurrency predecessors. Additionally, Libra adopts and mirrors smart contracts, an age old idea implemented in Ethereum, allowing client users to create their own protocols for a broad range of business. While the concept of smart contracts has indubitably made blockchain more useful, there have been no shortage of security issues associated with poorly written contracts. I'll also be examining Libra's companion DSL for programming smart contracts, called Move! It's an interesting redesign of Solidity that aims to make writing a contract a much safer, yet sufficiently expressive process.

This article's structure is the same as the Libra Blockchain PDF. Per section, I'll attempt to highlight and analysis Libra's advancements from the technical and industry perspective of established cryptocurrencies like Ethereum and Bitcoin. As usual, feedback and criticism are always welcome in the form of a comment below. Thanks for reading!

<br>
##### 1 Introduction

The start of this paper defines some terminology that will be use repeatedly throughout the article.

**Libra Coin** is the currency for the Libra blockchain. Libra is a fiat currency, meaning that is value is tied to a trove of real world monetary resources, specifically bank deposits and treasuries from banks. Because of this, Libra should be much less subject to the volatility of traditional cryptocurrencies like Bitcoin, where its value is a direct reflection of the market's assessment.

**Validators** are the entities responsible for processing transactions and maintaining the blockchain's state, similar to the role of a miner. As of Libra's inception, validator membership is limited to the Libra Association, but this will change as Libra changes from permissioned to a truly public blockchain. Why is Libra going through a permissioned phase instead of just starting off as public? This decision is likely borne from Libra's creators hoping to more easily perform course correction in response to user feedback and nurture Libra's initial growth into a more mature, refined, and tested platform. In addition, the select, known group of validators from the Libra Association means that the concern for an anonymous user with malicious intent is not an issue for now.

What's more is that instead of Proof of Work consensus, where the miner that gets to add the next transaction is determined randomly, validators switch off as the role of a *leader* which proposes transactions submitted by clients or other validators.  Just like in traditional cryptocurrencies, **clients** can submit transactions and query the database. The burden of authenticating this information, as usual, lies with the validators, not the clients. Clients can also verify that transactions were executed correctly by validators through a **replica** of the ledger database.

The description of the **Libra Blockchain** is where things get interesting. It's defined as a cryptographically authenticated database that serves as a ledger of programmable resources. However, unlike a traditional linked-list-esque structure, the "blockchain" is actually implemented with the [Merkle Tree](https://en.wikipedia.org/wiki/Merkle_tree) data structure, discussed much more in depth in section 4. The "why" and "how" of this will be discussed later on.

The authors also establish some of the objectives that serve as guiding design principles for Libra. One major theme is scalability, as the paper states "The Libra protocol must scale to support the transaction volume necessary... to grow into a global financial infrastructure".

##### 2 Logical Data Model

This section dives into the concepts and terminology surrounding the high level layout and entity relationships within the Libra ecosystem. First, the existing state of the database is stored and depicted with a **key-value** store, mapping an account's address (256 bit key) to its values, values meaning a collection of resources and modules. **Resources** are further defined as a record that assigns every value to an identifier.

##### 4 Authenticated Data Structures and Storage

The actual implementation of Libra
