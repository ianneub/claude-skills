---
name: commit-message
description: Generate concise commit messages for staged git changes. Analyzes the diff and writes a clear message for the user to copy. Use when you have staged files and want a commit message suggestion.
---

# Generate Commit Message

Generate a concise commit message for currently staged git changes.

**IMPORTANT: Do NOT actually run git commit. Only provide the message for the user to use.**

## Process

1. **Check for staged changes**
   Run `git diff --cached --stat` to verify there are staged changes. If nothing is staged, inform the user and stop.

2. **Analyze the changes**
   Run `git diff --cached` to see the actual code changes. Understand what was modified, added, or removed.

3. **Generate commit message**
   Write a concise commit message following these rules:
   - Start with imperative verb (Add, Fix, Update, Remove, Refactor, Improve)
   - Keep subject line under 72 characters
   - Focus on *what* changed and *why*, not *how*
   - No period at the end of subject line
   - Be specific but concise

4. **Present to user**
   Display the proposed commit message. Do NOT run git commit.

## Message Examples

Good:
- `Add user authentication with JWT tokens`
- `Fix null pointer exception in payment processing`
- `Update dependencies to address security vulnerabilities`
- `Remove deprecated API endpoints`
- `Refactor database queries for better performance`

Bad:
- `Updated stuff` (too vague)
- `Fixed the bug.` (no period, be specific)
- `Add new feature to allow users to do things` (too wordy)
- `WIP` (not descriptive)
