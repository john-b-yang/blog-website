title: An Opinionated Intro to Git
date: 2019-04-19
description: The Git tutorial I'd like to think I wish I had
image: /static/pictures/FlaskBlog/head-image.png
readtime: 11 MINS
time: FRIDAY, APRIL 19, 2019
tags: [Git, Tutorial]

Berkeley's CS 61B Data Structures Course is the first time that many students and developers are introduced to version control in the form of Git! In somewhat normalized Berkeley fashion, version control is introduced in a single one hour discussion and not covered too in depth, yet students are expected to have a working understanding of the commitment workflow without necessarily understanding what Git is capable of beyond just a Google Drive for code. A couple months ago, I gave a shot at writing the kind of Git tutorial that I wish I had back then. At the time, version control felt like a very foreign concept relative to my existing domain knowledge in computer science, so I thought that analogies and comparisons to more real life contexts might make some of the ideas more palpable. Feel free to give it a read, and if you have any feedback please let me know in the comments below!!

Towards the end of this article, I include an aggregate list of some of the more niche Github problems I've run into, along with my solutions. Check it out if Stack Overflow doesn't quite have what you're looking for! ;)

<br>
##### Basics
Created in 2005, Git is one of the most widely used Version Control Systems to date. To understand version control, imagine you are working on an intensive Java game when all of a sudden, your program crashes. All progress over the past two weeks is lost and you have to start over from the beginning. What a nuisance!

Introducing Git, a Unix based program that serves many powerful purposes, two of which will be heavily explored in CS 61B:
1. Keep track of file revisions and the history of a project.
2. Distribute work on files among multiple people.
Git is popular among computer scientists across all levels as a source code management tool. With Git, you can save working copies of coding projects, revert broken code to the latest working version, create different branches of the same code for developing features independently, and collaborate in the form of forks and branches. Don't worry if some of these don't make sense. Once you get the hang of it, learning Git becomes a very organic process.

To understand the true power of Git, another way to define its utility is outside the context of programming. In fact, you can use Git to save changes for anything, from PDFs to JPGs to GIFs. Although this thinking is a bit reductive, for now, you can think of Git as an elaborate, well-documented 'save' function. A Git file is capable of recording any changes for any computer file across any period of time.

**Github vs. Git**<br>
Github is a service that does web based hosting of your code and allows you to save your git history to a remote server. In contrast, git by itself performs the above operations on a 'local' level, which just means that everything you do happens and stays on your computer. Github is also know as the company that manages the whole process of saving your local git changes to a remote server. Their website serves as an online platform that allows you to view revisions and monitor collaborations. In addition, in case anything happens to your computer, your code will be recoverable and safe as long as you've committed it to Github. It's a fantastic resource.

**Resources**<br>
1. Git Cheat Sheet: https://www.git-tower.com/blog/git-cheat-sheet/<br>
2. Git Tutorial (In Depth): https://www.tutorialspoint.com/git/<br>
3. Official Git Documentation: https://git-scm.com/documentation<br>
4. Student Developer Pack: https://education.github.com/pack<br>

<br>
##### Commands
Here, we're going to review some of the basic commands in git, especially the options associated with adding, removing, and monitoring changes in your files. Don't be worried if by the end of this section, you're still not sure how each command is related or come together. We'll go over that in the next section titled  "Workflow". One term we're going to be using multiple times is "option". An option can be thought of as a parameter for a unix command, and they usually come in the form of -(character) or --(word). There are a multitude of options with varying utility, but for now, we'll review the staples. If you're interested in learning about more options out there, you can always type in just the git command itself (i.e. 'git add') and you'll be given a list describing the syntax, parameters, and utility of each option.

**An Anecdote**<br>
Perhaps the greatest initial barrier to learning Git is understanding what each command is actually doing. Here's a somewhat silly anecdote that, I hope, will serve as a roadmap for comprehending Git going forwards. Imagine an apple farmer. As a farmer, the first thing you'd probably do is pick every apple off of your tree. Then, you'd inspect your harvest, throwing out the bad apples that have mold, insects, etc., while keeping the good ones. Finally, you'd pack the good apples and send them off to the store and turn it into profit.

Git works in a similar fashion. You're the apple farmer. An apple is the equivalent to modifying your project. In other words, every changed file is recorded with a unique signature aka the apple. When you 'git add', you're telling the computer which modifications, or which apples, you want to keep. Finally, with 'git commit', you've packed up the modifications and officially saved a new version of your directory.

**Adding / Staging Changes**<br>
<pre class="inline-block prettyprint lang-bsh" style="border-radius: 10px;padding: 15px;">
git add -A
git add (name of change here)
</pre>
'git add' is the Git command responsible for selecting modifications. When a file is modified, your computer has no idea which modifications are or aren't important. 'git add' is essentially your way of picking out the modifications that you're telling your computer you'd like to keep. A file that has been added is considered 'staged'. To select a change individually, just 'git add (name of modification here)'. Out of the options, you will most likely be using 'git add -A' the most.

<img src="/static/pictures/GitCS61B/add-options.png" alt="Add Options" style="width:400px;display:block;margin-left:0;"/>

**Committing Staged Changes**<br>
<pre class="inline-block prettyprint lang-bsh" style="border-radius: 10px;padding: 15px;">
git commit -m 'Commit Message Here'
</pre>
It's time to ship the apples. 'git commit'  finalizes the staged changes you want to keep and revises the .git file to store a new latest version of the directory. With git commit, you can view previous versions of the directory, compare different commits, and revert back to a previous commit in case something happens to your project.

<img src="/static/pictures/GitCS61B/commit-options.png" alt="Commit Options" style="width:400px;display:block;margin-left:0;"/>

**Removing or Postponing Changes**<br>
<pre class="inline-block prettyprint lang-bsh" style="border-radius: 10px;padding: 15px;">
git checkout -- (filename)
git rm (filename)
git rm --cached (filename)
git stash save --keep-index
git stash drop
</pre>
You've encountered a change that you don't want. Time for cleanup. There are two ways to deal with changes that you want. Either delete those changes, or store these changes to be introduced later. Keep in mind, the process of removing files is different for files that *have* been committed versus those that *have not* been committed yet. If your file has *not* been committed, the 'git checkout -- <filename>' command

One way to go about deleting a file is 'git rm'. This command removes a file from a working directory. Unlike a regular unix 'rm', 'git rm' not only removes the file, but also stages that deletion. If you only want to delete the file from your .git file, but would like to keep a copy in your local directory, use the '--cached' option. Keep in mind, 'git rm' removes *files*, not *changes*.

On the other hand, if you're not sure you want to keep the changes you've made, use the 'git stash' command. 'git stash save' allows you to remember the modifications you've made while returning you to the latest commit of your working directory.

**Remote Repository Interaction**<br>
<pre class="inline-block prettyprint lang-bsh" style="border-radius: 10px;padding: 15px;">
git remote add origin <remote repo url>
git remote prune
</pre>
So far, the above commands have been enacting change on a local level. With 'git remote', we are able to manage Github repositories stored in remote servers. Most remote commands will revolve around getting/setting repository URLs or renaming branches. A sizable set of remote commands also deal with branch management, so we will touch on them in this table, but if you're unclear as to what those are, refer to the collaboration section.

**Miscellaneous Commands**<br><br>
<img src="/static/pictures/GitCS61B/misc-commands.png" alt="Commit Options" style="width:500px;display:block;margin-left:0;"/>
