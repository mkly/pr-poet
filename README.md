# PR Poet

A Github action to turn commits and other comments into poetry

A PR title of **_Fix null handling, covered by integration tests_** would yield something similar to:

> In code that handles null,<br/>
> A test covers it all,<br/>
> Null handled, no need to fret,</br>
> Integration tested, a solid stand.</br>

## Example workflow usage

```
name: Poems
on:
  pull_request:
    types: [opened]

permissions:
  pull-requests: write

jobs:
  post-poem-on-pr-open:
    runs-on: ubuntu-latest
    steps:
      - name: PR Poet
        id: poet
        uses: mkly/pr-poet@v1.0.9
        with:
          message: ${{ github.event.pull_request.title }}
      - name: Post comment to PR
        uses: actions/github-script@v6
        with:
          script: |
            await github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: `${{steps.poet.outputs.poem}}`
            })
```
