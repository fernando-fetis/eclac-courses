#import "../common/theme.typ": *

#show: lecture.with(number: 2, title: "Anatomy of a Language Model")

#section("Tokens, training and generation")

#slide(title: [Tokenization], sources: [@sennrich2016])[
  The text is transformed into a sequence of *tokens* belonging to a vocabulary:

  #fig(image("figures/tokenization.pdf", width: 100%))

  #note[
    The vocabulary is fixed before training and never changes. Everything the model will ever read or write is a sequence of *token IDs*.
  ]
]

#slide(title: [Building the vocabulary], sources: [@sennrich2016])[
  Initially, each character is an individual token. Then, all adjacent character pairs are counted, and the most frequent pair is combined into a new token.
  #fig(image("figures/byte-pair-encoding.pdf", width: 72%))
  This process is repeated until the desired vocabulary size is reached.
]

#slide(title: [The training objective], sources: [@radford2018])[
  #key-point[
    A *neural network* is trained to learn to predict the *next token*, given a sequence of tokens as *context*.
  ]

  #fig(image("figures/teacher-forcing.pdf", width: 70%))
]

#slide(title: [Training])[
  Therefore, the model *$p_theta ("next token" | "context")$* is trained so that the existing data, $cal(D) = {x_1, dots, x_N}$ has a high probability:

  $
    max_#text(fill: emphasis)[$theta$] thin 1 / (N dot T) sum_(n=1)^N sum_(t=1)^T log p_#text(fill: emphasis)[$theta$] (w_n^((t)) | w_n^((1, dots, t-1)))
  $
  #fig(image("figures/gradient-descent.pdf", width: 60%))
]

#slide(title: [Autoregressive generation])[
  To generate text, one begins with an initial text (*prompt*) and proceeds iteratively by predicting the next token using the trained model:
  #fig(image("figures/autoregressive.pdf", width: 100%))
]

#slide(title: [Decoding], sources: [@holtzman2020])[
  A simple rule is to choose the *most probable token*. One could also choose from the $K$ most probable tokens and adjust the *temperature* to control variability.

  #fig(image("figures/decoding.pdf", width: 100%))
]

#section("The Transformer")

#slide(title: [The Transformer], sources: [@vaswani2017])[
  #cols(
    fig(image("figures/transformer-overview.pdf", height: 13cm)),
    [
      The *Transformer* is a neural architecture published by Google in 2017. Today, its logic is present in most modern models, including LLMs.

      #key-point[
        The architecture consists of a *Transformer block* that is repeated several times. To increase the capacity of these models, one can increase the number of blocks.
      ]

      Here we will study the *GPT* architecture, which is a version of Transformer used to generate sequences.
    ],
    weights: (1fr, 1.8fr),
    align-at: horizon,
  )
]

#slide(title: [Embeddings])[
  Each token ID is mapped to an *embedding vector*. In this way, the neural network can work with vectors, on which mathematical operations can be performed.

  #fig(image("figures/embeddings.pdf", width: 100%))
]

#slide(title: [Positional encoding], sources: [@vaswani2017])[
  A *positional embedding* table is learned in a similar way, where each position within the sequence has an associated vector.
  #fig(image("figures/positional-encoding.pdf", width: 100%))

  #note[
    The first Transformer block of the neural network receives the sum of the token and position embedding vectors for each token within the input sequence.
  ]
]

#slide(title: [Self-attention], sources: [@vaswani2017])[
  #fig(image("figures/self-attention.pdf", width: 84%))

  #v(10pt, weak: true)
  #cols(
    [
      The output for token $i$ is a weighted sum of the tokens up to it:

      $ y^((i)) = sum_(j = 1)^i alpha_(i j) thin #text(fill: emerald)[$W_V x^((j))$] $
    ],
    [
      The weight $alpha_(i j)$ is assigned based on the similarity between tokens $i$ and $j$:

      $
        alpha_(i j) = "softmax"_j thin (1 / tau #text(fill: accent)[$W_Q x^((i))$] dot #text(fill: gold)[$W_K x^((j))$])
      $
    ],
  )
]

#slide(title: [Multi-head attention], sources: [@vaswani2017])[
  #key-point[
    The aforementioned mechanism is called an *attention head*. An attention head typically learns specific subtasks.
  ]
  It is common to use several heads in parallel and concatenate their outputs:

  #fig(image("figures/multi-head.pdf", width: 76%))
]

#slide(title: [The feedforward network])[
  The attention sub-block allows the sequence tokens to interact. The *feed-forward* sub-block transforms the resulting vector at each position.

  #fig(image("figures/neural-network.pdf", width: 92%))
]

#slide(title: [The Transformer block], sources: [@vaswani2017])[
  #cols(
    fig(image("figures/transformer-block.pdf", height: 10.8cm)),
    [
      Consequently, a *Transformer block* serves as a backbone that transforms the vector representations of each token.

      First, each position interacts with the other positions, and then each position is transformed individually.

      Both sub-blocks operate by adding their contribution to the backbone.
    ],
    weights: (1fr, 1.05fr),
    align-at: horizon,
  )
]

#slide(title: [The GPT architecture], sources: [@radford2018 @radford2019])[
  The GPT architecture stacks multiple Transformer blocks and then transforms the final representation of the *last token* to predict the *probability of the next token*:
  #cols(
    fig(image("figures/gpt-architecture.pdf", height: 9.4cm)),
    fig(image("figures/language-head.pdf", width: 100%)),
    weights: (1fr, 1.6fr),
    align-at: horizon,
  )
]

#section("Pre-training and post-training")

#slide(title: [Training phases], sources: [@ouyang2022])[
  #fig(image("figures/training-pipeline.pdf", width: 100%))
]

#slide(title: [Instruction tuning], sources: [@wei2022finetuned @ouyang2022])[
  Pre-training yields a *base model*, which is then *fine-tuned* to learn how to respond in a helpful style. Data following the desired format is used for this purpose.

  #fig(image("figures/chat-template.pdf", width: 68%))

  #caution[
    The model is trained to strictly adhere to its *system prompt*.
  ]
]

#slide(
  title: [Preference learning],
  sources: [@christiano2017 @ouyang2022 @rafailov2023],
)[
  The next stage is the one associated with *alignment*, where the model is fine-tuned to generate preferred responses.
  #fig(image("figures/preference-learning.pdf", width: 100%))
]

#section("Scale, reasoning and evaluation")

#slide(title: [Scaling laws], sources: [@kaplan2020 @hoffmann2022 @dubey2024])[
  The error falls predictably as the model, the data and the compute grow, which is why the number of parameters kept climbing. Between GPT 1 and the models used today the general backbone barely changed.

  #fig(image("figures/model-sizes.pdf", width: 72%))
]

#slide(title: [Reasoning], sources: [@wei2022cot @deepseek2025])[
  While *Chain of Thought* began as a prompting technique, the model is now trained using this type of data to encourage it to reason through complex problems.

  #fig(image("figures/reasoning-effort.pdf", width: 66%))

  #note[
    *Test-time compute* became a second scaling axis, where a harder question is answered by thinking longer, not by a larger model.
  ]
]

#slide(title: [Evaluating a model], sources: [@sainz2023 @zheng2023])[
  #fig(image("figures/evaluation.pdf", width: 100%))
]

#section("Closing")

#slide(title: [Takeaways])[
  #agenda(
    [1],
    [A model does not look anything up: it *predicts the next token*. Whatever it states as fact still has to be checked against a source.],
    [section 1],
    [2],
    [Different models bill or measure usage based on tokens, so extensive contexts or reasoning processes result in *higher costs*.],
    [section 1],
    [3],
    [All the model reads is just a long sequence of tokens. *Special tokens* are used to separate them into roles or subsections.],
    [section 3],
    [4],
    [Public scores do not transfer. Keep a *small set of your own cases* and run it again whenever the model or the prompt changes.],
    [section 4],
  )
]

#slide(title: [Next session])[
  #agenda(
    [1],
    [Other families: encoders, embeddings, diffusion, multimodal],
    [],
    [2],
    [RAG],
    [],
    [3],
    [From model to agents],
    [],
    [4],
    [Integration protocols: MCP and A2A],
    [],
    [5],
    [Use of Claude Code],
    [],
  )
]

#closing(title: "Thank you")

#references(bibliography("bib.yml", style: citation-style, title: none))
