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

The next question that might naturally arise is, what goes into a **ledger's state**? It's really just a simple key-value store associating each account address with a set of resources (data values, i.e. how much Libra Coin does 0x123... have?) and modules (smart contracts, a.k.a. Move bytecode defining a new resource's type + associated procedures. i.e. transfer of Libra Coin between accounts). The below diagram is essentially appropriated from the paper, just with a couple additional illustrations for greater clarity and detail.

<img src="/static/pictures/Libra/2-ledger-state.png" alt="Ledger State" style="height:300px;display:block;margin-left:auto;margin-right:auto"/>

The schematics governing account addresses are nothing new. Each user has a verifying + signing key, and the public key, which would be the addresses in the above diagram, is just a cryptographic hash of the verifying key. Resources, broken down, simply associate a resource type (defined by modules) with a particular quantity or value.

*A Side Note*: The Libra paper states that "each account can store at most one resource of a given type", which was initially confusing to me. If I want to exchange Libra Coin, would I be barred from it because of the aforementioned limitation? After some thought, I realized that in such a situation, the *value* of the resource would be modified. Such a design has the benefit of eliminating both redundancy and the difficulties that come with fragmentation. In this context, by fragmentation, I mean a situation where there are multiple resources per type.

<img src="/static/pictures/Libra/2-ledger-resource.png" alt="Resource" style="height:150px;display:block;margin-left:auto;margin-right:auto"/>

Notice that a resource is uniquely identified by &lt;account address (creator)&gt; / &lt;module name&gt; / &lt;resource type&gt;. In other words, multiple modules and resources could have the same name, but are distinguished by their creators, making them distinct types. Therefore, in the above diagram, the two coins in account 0x27... have the same module name (Coin) and resource name (Coin.T), but ultimately, are different types (0x27.Coin.T vs. 0x45.Coin.T). I like this convention for identifying resource types because it prevents a first-come-first-serve issue for naming modules or resources (ala [domain squatting](https://en.wikipedia.org/wiki/Cybersquatting)). Similar to smart contracts, modules wholly define rules for mutating, deleting, and publishing a resource. As of this point, a module published to Libra is immutable, although methods for safe updates are being explored for release in the future.

Ok, now that we've defined state, what about **transactions**, the medium for going from one state to another? A transaction consists of a transaction script (Move bytecode) + arguments. Section 3 will go into the flow of executing and committing a transaction.

One noteworthy distinction is between an *output* and an *event*. An *output* details information consistently associated with every executed transaction, specifically the new resulting ledger state, gas usage, and execution status code. *Events* are much more open-ended and defined by the transaction code. This difference highlights an interesting distinction. In Libra, a transaction that is processed and recorded in the ledger history does not imply successful execution. This is where an *event* helps indicate whether the transaction actually took effect.

Initially, this design was a bit confusing to me. Why record transactions that, if they presumably failed due to an error or running out of gas, don't actually change the ledger state? Upon some additional thought, such a record would be necessary because regardless of the transaction's ultimate output, the validator that attempted to process the transaction still receives Libra Coin for its effort; thus, such a exchange should be recorded. This necessitates *events* in addition to a fixed set of *output* fields.

The big picture...

<img src="/static/pictures/Libra/2-ledger-cumulative.png" alt="Big Picture" style="height:600px;display:block;margin-left:auto;margin-right:auto"/>

<br>
##### 3 Executing Transactions

Now that we've got the data model down, this section explores, to greater depths, the logical and technical flow of transitioning from one ledger state to the next via an executed transaction. Section 3.1 is largely derivative of existing blockchain systems' execution requirements, namely deterministic transaction outputs and metered execution (a.k.a. Ethereum's gas model). Determinism ensures consensus among multiple validators can be achieved. Metered execution, broken down into gas price (Libra / unit of gas client will pay) and gas cost (gas needed to execute Xact entirely), is a technique for preventing Libra from being overwhelmed with too many transactions.

The anatomy of a transaction and its execution by the Move Virtual Machine are detailed below. This diagram is essentially a summary of sections 3.2 and 3.3.

<img src="/static/pictures/Libra/3-Xact-Flow.gif" alt="Xact Flow" style="height:400px;display:block;margin-left:auto;margin-right:auto"/>

Although the Prologue and Epilogue steps involve running Move bytecode, the client is not charged gas costs for their execution since its is required no matter what transaction is executed. The code is also distinct from the client's transaction's bytecode. Perhaps the most interesting development is Step 3, where the transaction's script and modules are verified. Designing a smart contract involves many safety issues, and in recent years, vulnerabilities such as [reentrancy attacks](https://medium.com/@gus_tavo_guim/reentrancy-attack-on-smart-contracts-how-to-identify-the-exploitable-and-an-example-of-an-attack-4470a2d8dfe4) have cost many contract authors and clients a great deal of money. There is much ongoing research in industry and academia designing tools for catching exploitable bugs within smart contracts before they are committed to the blockchain and become immutable. Libra's script + module verification step represents a notable first time where contract checking is being directly integrated in the transaction deployment process. Unfortunately, how exactly contract checking is implemented in Libra is not discussed in greater detail anywhere else in the paper.

The remainder of this section previews the technical foundations and design motivations of the Move DSL for writing modules and scripts in Libra. The Move programming language can be broken down into three different representations. As of this article, the source language is not available to the general public, so preliminary script and module development can only be written in the intermediate representation, which the authors claim is still human readable.

<img src="/static/pictures/Libra/3-move-basics.png" alt="Move Basics" style="height:150px;display:block;margin-left:auto;margin-right:auto"/>

There are two notable facets of Move that I think are worth pointing out with regards to security. First, the safety checks and guarantees that the Move Virtual Machine performs before processing a transaction (recall Step 3 from above) are enacted on Move bytecode (a.k.a. *bytecode verification*). This is wise design; performing safety checks at the IR or Source Code level presents an opportunity for malicious clients to evade these checks by simply just writing the code at a lower level. Again, however, how comprehensive these checks are have yet to be elaborated upon by the Libra team.

Another trend is that the more low-level the representation, the more constrained the code base becomes. While the Source Language and IR support more complex paradigms such as conditionals and loops, the bytecode representing these patterns, when compiled, is based on a much smaller instruction set. In fact, the Move VM ultimately supports just six different types and values. I think the authors put a subjectively positive spin on their decision; limiting the instruction set should reduce the scope of potential vulnerabilities, but it comes at the cost of expressivity.

Given that the IR and Source Code language are still very much in development, it will be interesting to see how limitations on the bytecode instruction set affects how expressive the higher level representations can really be. As Libra matures over time, I'd venture that the codebase for all three representations would grow to accommodate more use cases. The Move code available to the public right now is likely limited on purpose, as Libra's maintainers would rather support a safer DSL that is more secure than it is expressive to build trust in the platform.

<br>
##### 4 Authenticated Data Structures and Storage

In this section, the authors dive into the data structures behind the data models described in section 2. The Libra Blockchain's technical implementation is dominated by [Merkle Trees](https://en.wikipedia.org/wiki/Merkle_tree), and the use of this structure is perhaps its greatest distinction from existing blockchain systems.

Before diving into how the ledger history, event list, ledger state, etc are stored within Merkle Trees, it's helpful to have a bit of background on authenticated data structures (ADS). For me, this [paper](https://www.cs.umd.edu/~mwh/papers/gpads.pdf) was particularly useful for achieving basic comprehension of the motivations, terminology, and technicalities surrounding ADS's in general. I'd recommend reading section 2, which mentions Merkle Trees as a canonical example of an ADS. In one sentence, ADS's are useful because they allow untrusted *provers* (i.e. validators) to perform operations on and modify the state of the data structure; such changes can be checked for authenticity by *verifiers* (i.e. clients). In a certain sense, today's most popular blockchain systems can be thought of as a decentralized, distributed ADS. The illustration below depicts a simplified workflow of how provers modify and verifiers check the state of an ADS. The label's letters correspond to the notation used in Section 4.1 of the paper.

<img src="/static/pictures/Libra/4-ads-flow.png" alt="ADS Flow" style="height:250px;display:block;margin-left:auto;margin-right:auto"/>

What is the significance of a prover being *untrusted*? After all, as of today, the only validators are verified members of the Libra Association; these validators are, in a sense, trusted. However, as Libra expands later on, the plan is that entities from the general public can become validators. At that point, trust in validators is no longer a guarantee, which is why authentication with *untrusted* provers modifying the ADS must be tolerable.

So what does a result (R), proof of the computation (π), and authentication look like in the context of a Merkle Tree data structure?

So why not just use a normal linked-list style blockchain? What's all the hurrah over using a Merkle Tree? This change originates out of the drive for scalability and a more efficient authentication process for a client.

<br>
##### Questions & Thoughts
Can a single module declare multiple resource types?
If an account is deleted or removed, what happens to the modules it defines or the resources that it contains?
