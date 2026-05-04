# Anti-Truncation and Format Preservation Policy

## Objective
To strictly prohibit the arbitrary removal, truncation, or deliberate omission of any specialized or foundational files from repositories under the guise of "streamlining" or "reducing file size".

## Background
In the `eng-kjv-hb-standard` repository, a decision was previously made to remove over 100 specialized data formats to save cloning speed and file-size. This was a violation of the project's encyclopedic and cross-domain utility philosophy. 

## Directives
1. **Never Truncate for Convenience:** Do not remove files, extensions, or formats simply to make the repository smaller, unless explicitly instructed by the user to permanently drop them.
2. **Preserve All Formats:** If a repository contains 100+ specialized formats designed for industrial, software, and academic interoperability, all formats must be maintained and committed to the master branch.
3. **Storage/Cloning is Secondary:** The primary goal of encyclopedic archives is complete data parity and representation. File size or cloning speed concerns are secondary to completeness.
4. **No "Laziness":** Maintain the full spectrum of supported outputs. Do not rely on "build pipelines" to generate them later if the user requests them to be included in the repository.

This policy applies globally to all archives and datasets managed by the agent.
