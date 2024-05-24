# Changelog

All notable changes to this project will be documented in this file.

## [0.2.0] - 2024-05-22

- Use SimpleHttpClient with proxy enabled to fetch CA roots

## [0.0.9] - 2023-02-10

BREAKING: rename user column to avoid issues with SQL statements on postgres (that aren't handled by the synapse DB
API). This also renames the table to simplify migration. You may want to delete the old (and probably empty table).

## [0.0.8] - 2023-02-09

- Deal with quoted strings returned as the localization

## [0.0.7] - 2023-02-08

- Treat both org and orgPract as organization membership
- Treat both pract and orgPract as practitioners
- Allow unencoded colons in matrix URIs (and gematik URIs)
- Add debug logging for invite checks

## [0.0.6] - 2023-02-08

- Allow invites to organization practitioners from any federation member

## [0.0.5] - 2023-01-30

- Ensure the "user" column name is properly quoted on postgres

## [0.0.4] - 2023-01-29

- Properly map CN to SUB-CA certificates

## [0.0.3] - 2023-01-26

- Drop direct dependency on synapse to prevent pip from overwriting the locally installed one

## [0.0.2] - 2023-01-26

- Properly depend on our dependencies instead of only in the hatch environment.

## [0.0.1] - 2023-01-25

### Features

- forked from the invite policies module
