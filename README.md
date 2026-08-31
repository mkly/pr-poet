# PR Poet

### A Github action to turn commits into poetry

**_Fix silly typo in readme_**:

> In README's pages where words reside,<br/>
> A silly typo found, no longer inside,<br/>
> With fixes applied, clarity shines new,<br/>
> Commit marked, code finds its view.<br/>

## Test it out

You can edit the `HELLO.md` file in this repo to open a new pull request to get a new poem.

## Example workflow usage

```
name: Poems
on:
  # This gives the workflow's GitHub token permission to comment on fork PRs.
  pull_request_target:
    types: [opened]

permissions:
  pull-requests: write

jobs:
  post-poem-on-pr-open:
    runs-on: ubuntu-latest
    steps:
      - name: PR Poet
        id: poet
        uses: mkly/pr-poet@main
        with:
          message: ${{ github.event.pull_request.title }}
      - name: Post comment to PR
        uses: actions/github-script@v6
        with:
          github-token: ${{ github.token }}
          script: |
            await github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: `${{steps.poet.outputs.poem}}`
            })
```

The workflow uses a custom fine-tuned 4bit quantized 0.6B model ([PR Poet Qwen3-0.6B Q4_K_M model](https://huggingface.co/mkly/pr-poet-Q4_K_M.gguf)) to be as small as possible while still creating a viable poem. See [mkly/pr-poet-training](https://github.com/mkly/pr-poet-training) for details on how the model was trained.
