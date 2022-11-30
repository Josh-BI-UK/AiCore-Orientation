# **How clone a only subdirectory from a Git repository?**
<br>

<font size=2> 
<b>Used help resources:</b>
<br>

1. GitLab Unfiltered - "Speed Run - Partial Clone, Sparse Checkout, and File Locking": https://www.youtube.com/watch?v=LMG_-uJVdsw
<br>

2. Stack overflow - "How do I clone a subdirectory only of a Git repository?": https://stackoverflow.com/questions/600079/how-do-i-clone-a-subdirectory-only-of-a-git-repository
</font>

----

**To create a directory for your spares repo.**

```console
mkdir <your_repo_name>
```

**_or you can use this command to pull all the metadata and folder from the gitHub repo._**
```console
git clone --filter=blob:none --sparse <url of your repo>
```

**Navigate to your repo**

```console
cd <your_repo_name>
```

**Initialise the git repository**
```console
git init
```

**Clone your sub-directory**
```console
git sparse-checkout set units/Essentials
```