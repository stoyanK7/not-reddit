# Accelerating API response times for high-traffic social media platforms with caching

By Kostadinov, Stoyan S.L.

## Introduction

### Context

The goal of this research paper is to gain insight into different caching techniques and decide on
the most suitable one for the _not-reddit_ project [[1]](#references).

> _not-reddit_ is a social news aggregation platform with sub-communities, messaging, and awards
> that allows users to post and share content, vote on submissions, and comment on posts.

Majority of the content on _not-reddit_ is text-based and media-based (videos and images). Adding
the fact that _"Reddit received 30 billion average monthly views in 2020"_ [[2]](#references), it is
clear that the platform is a high-traffic one. This means that the API response times are important
and should be as low as possible.

Reddit's developers say they battle this problem by using a caching layer in front of their
database - _"Lots of caching. Queries are pre-calculated and cached into Cassandra."_
[[3]](#references).

### Research questions and objectives

The purpose of this research paper is to answer one main research question and several
sub-questions:

> _**How can caching be used to accelerate API response times for a high-traffic social media
platform?**_

To get to the answer to this central question, several more-specific sub-questions have to be
answered:

- > What does an API request currently look like in not-reddit?
- > What caching techniques support storing both text and media?
- > How can caching be implemented in a microservice architecture in the context of not-reddit?
- > How can the impact of caching on API response times be measured and evaluated?


### Methodology


  
### Table of contents

### Glossary

## Literature review

## References

    [1] [not-reddit](https://github.com/stoyanK7/not-reddit/)

    [2] [Reddit Revenue and Usage Statistics](https://www.businessofapps.com/data/reddit-statistics/)

    [3] [Comment from a reddit developer on caching](https://www.reddit.com/r/programming/comments/z9sm8/comment/c62uf7c/?utm_source=share&utm_medium=web2x&context=3)
