title: A Technical Dissection of the Libra Blockchain
date: 2019-06-20
description: So turns out, the Libra "Blockchain" isn't an actual blockchain? A discussion and benefits analysis of Libra's implementation
image: /static/pictures/Libra/head-image.png
readtime: 11 MINS
time: THURSDAY, JUNE 20, 2019
tags: [Paper]

Recently, Facebook has taken a dive into the field of cryptocurrency with the announcement of Libra, a financial service founded upon cryptographic principles and blockchain technology with a long term, grand vision of becoming a unified economic infrastructure on a multinational, global scale. Since its release several weeks ago, there has been plenty of reactions and feedback from news outlets and industry professionals debating the economic ramifications of the Libra organization. Regardless of the debate, Libra's coming out party marks an exciting milestone with regards to the formalization of blockchain technology as a potential solution for enforcing trust, integrity, and authentication in an increasingly digitalized world.

There's been plenty of comments and criticism targeting the monetary implications that come with Libra's growth. However, in this article, I'll be more focused on understanding the technical innovations powering the Libra platform, specifically the [Libra Blockchain](https://developers.libra.org/docs/the-libra-blockchain-paper). I'm primarily interested in how Libra attempts to address questions regarding how to support scalability and eliminate computational inefficiency (a.k.a. Proof of Work), challenges well publicized by the proliferation of Bitcoin and other cryptocurrency predecessors. Additionally, Libra adopts and mirrors smart contracts, an age old idea implemented in Ethereum, allowing client users to create their own protocols for a broad range of business. While the concept of smart contracts has indubitably made blockchain more useful, there have been no shortage of security issues associated with poorly written contracts. I'll also be examining Libra's companion DSL for programming smart contracts, called Move!r It's an interesting redesign of Solidity that aims to make writing a contract a much safer, yet sufficiently expressive process.

This article's structure is the same as the Libra Blockchain PDF. Per section, I'll attempt to highlight and analysis Libra's advancements from the technical and industry perspective of established cryptocurrencies like Ethereum and Bitcoin. As usual, feedback and criticism are always welcome in the form of a comment below. Thanks for reading!
