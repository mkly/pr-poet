# PR Poet

A Github action to turn commits and other comments into poetry

A PR title of **_Fix null handling, covered by integration tests_** would yield something similar to:

> In code that handles null,<br/>
> A test covers it all,<br/>
> Null handled, no need to fret,</br>
> Integration tested, a solid stand.</br>

## Test it out

You can edit the `HELLO.md` file in this repo to open a new pull request and get a new poem.

## Example workflow usage

```
name: Poems
on:
  # Use `pull_request_target` to view secrets
  pull_request_target:
    types: [opened]

permissions:
  pull-requests: write

jobs:
  post-poem-on-pr-open:
    runs-on: ubuntu-latest
    # Set to the environment with your personal access token
    environment: pr-poet-token-env
    steps:
      - name: PR Poet
        id: poet
        uses: mkly/pr-poet@v1.0.9
        with:
          message: ${{ github.event.pull_request.title }}
      - name: Post comment to PR
        uses: actions/github-script@v6
        with:
          # Add your personal access token to the PR comment request
          github-token: ${{ secretes.PAT_TOKEN }}
          script: |
            await github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: `${{steps.poet.outputs.poem}}`
            })
```
