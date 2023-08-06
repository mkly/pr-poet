from ctransformers import AutoModelForCausalLM, AutoConfig, Config
import re
import os

config = AutoConfig(
  model_type='llama',
  config=Config(
    max_new_tokens=77,
  )
)
llm = AutoModelForCausalLM.from_pretrained('/action/orca-mini-3b.ggmlv3.q4_0.bin', config=config)

commit_message = os.getenv('INPUT_COMMIT_MESSAGE')

prompt = f"""
COMMIT: Allow RSS feed to be cached if user is logged in.
POEM:
LINE_ONE: In feeds that dance on screens so bright,
LINE_TWO: A user logged, enjoys the sight,
LINE_THREE: Caching RSS, a seamless flow,
LINE_FOUR: Connection's embrace, a glow to show.

COMMIT: Bring back try/catch for 5.1
POEM:
LINE_ONE: In 5.1, a plea to mend,
LINE_TWO: Bring back try/catch, an old friend,
LINE_THREE: Errors caught, a graceful dance,
LINE_FOUR: Code's embrace in a second chance.

COMMIT: {commit_message}
POEM:
"""

result = str(llm(prompt))
lines = result.split("\n")
poem = re.sub("LINE_ONE: |LINE_TWO: |LINE_THREE: |LINE_FOUR: ", "", "\n".join(lines[:4]))

with open(os.getenv('GITHUB_OUTPUT', 'none.txt'), "w") as file:
    file.write(f'poem="{poem}"')
