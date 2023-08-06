# PR Poet

A Github action to turn commits and other comments into poetry

A PR title of **_Add initial readme with title for proxy_** would yield something similar to:

> A vision to view from afar,<br/>
> An image that glows with love,<br/>
> An emote's face, a smile to show,<br/>
> Online joy, a feeling so fine.

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
