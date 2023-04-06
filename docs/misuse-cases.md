# Misuse Cases

This document describes the misuse cases for the _not-reddit_. These misuse cases will be used
to derive the non-functional *security* requirements for the application.

## Misuse Case 1: SQL Injection

SQL injection attacks that could allow an attacker to execute arbitrary SQL commands against the
application’s database, potentially allowing them to steal sensitive data or modify data in the
database.

## Misuse Case 2: Denial-of-Service (DoS)

Denial-of-service (DoS) attacks that could overwhelm the application’s servers with traffic,
making it unavailable to legitimate users.

## Misuse Case 3: Spamming

A malicious user creates multiple accounts and posts irrelevant or unsolicited content in multiple
subreddits to manipulate or disrupt the platform. This can cause inconvenience to users and impact
the overall user experience.

## Misuse Case 4: Malware and Phishing

A user shares links or downloads files that contain malware or phishing scams to infect other users'
devices or steal their personal information.
