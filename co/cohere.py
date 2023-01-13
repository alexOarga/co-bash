import cohere


def generate(prompt, key, model):
    co = cohere.Client(key)

    return co.generate(
      prompt=prompt,
      model=model,
      end_sequences=['\n']
    )