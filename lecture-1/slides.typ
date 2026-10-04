#import "../common/theme.typ": *

#show: lecture.with(number: 1, title: "Foundations of Generative AI")

#section("Learning from data")

#slide(title: [Rule-based and learned systems])[
  #fig(image("figures/shift.pdf", width: 84%))

  #key-point[
    Experts cannot state what they know. A radiologist sees a tumor in a second and cannot write down the rule.
  ]
]

#slide(title: [How to optimize])[
  #fig(
    image("figures/optimization.pdf", width: 72%),
    caption: [SGD: it starts at a random point and is iteratively improved until a local minimum is reached.],
  )

  $ x_(t+1) = x_t - eta dot f'(x_t) $
]

#slide(title: [Fitting a model to data])[
  #fig(image("figures/polynomial-fit.pdf", width: 100%))

  $ "model"(x) = #text(fill: emphasis)[$a_0$] + #text(fill: emphasis)[$a_1$] x + #text(fill: emphasis)[$a_2$] x^2 + #text(fill: emphasis)[$a_3$] x^3 #h(2em) min_(a_0, dots, a_3) thin sum_n (y_n - "model"(x_n))^2 $

  #aside[The coefficients $a_0, dots, a_3$ are the *parameters*, which are adjusted in each iteration of SGD to reduce the fitting error.]
]

#slide(title: [Neural networks])[
  #fig(image("figures/neural-network.pdf", width: 90%))
]

#slide(title: [Image classification], sources: [@cybenko1989])[
  #fig(image("figures/image-classifier.pdf", width: 94%))

  #key-point[
    With enough examples a neural network can *learn* essentially any relationship. Nobody programs the rule for "cat", it falls out of the data.
  ]
]

#slide(title: [Position within artificial intelligence])[
  #fig(image("figures/ai-landscape.pdf", width: 88%))
]

#slide(
  title: [Milestones, 2012–2026],
  sources: [@krizhevsky2012 @goodfellow2014 @sutskever2014 @vaswani2017 @brown2020 @deepseek2025],
)[
  #fig(
    image("figures/timeline.pdf", width: 100%),
    caption: [Everything on this line is the recipe from the previous slides, scaled up and pointed at new data.],
  )
]

#section("Language models")

#slide(title: [Tokenization], sources: [@sennrich2016])[
  A language model starts by dividing the text into subunits called *tokens*. Then, a neural network processes the sequence of tokens.

  #fig(image("figures/tokenization.pdf", width: 92%))

  #note[
    An LLM can read a maximum number of tokens within its *context window*. Modern models can read up to 1 million tokens.
  ]
]

#slide(title: [Autoregressive generation], sources: [@shannon1948])[
  #fig(image("figures/next-token.pdf", width: 84%))

  #note[
    The model outputs *$"Prob"("next token" thin | thin "context")$* for every possible next token, and one is sampled. In particular, the same prompt can give different continuations.
  ]
]

#slide(title: [Few-shot prompting], sources: [@radford2019 @brown2020])[
  With enough data, autoregressive training learns to repeat certain patterns:

  #fig(image("figures/few-shot.pdf", width: 78%))

  This was first observed in GPT 2 and used systematically in GPT 3.
]

#slide(title: [Emergent abilities], sources: [@brown2020 @wei2022emergent @schaeffer2023])[
  #cols(
    fig(
      image("figures/wei2022-emergence.pdf", width: 100%),
      caption: [Figure 2 of Wei et al. (2022). Whether the jumps are real or an artifact of grading is still argued.],
    ),
    [
      #note(title: "Three-digit addition")[
        `Q: 128 + 367 = 495` \
        `Q: 512 + 287 = 799` \
        `Q: 234 + 567 = `#text(fill: emerald)[`801`]
      ]
      #note(title: "Word unscramble")[
        `Q: elppa   = apple` \
        `Q: dloihya = `#text(fill: emerald)[`holiday`]
      ]
    ],
    weights: (1.9fr, 1fr),
  )
]

#slide(title: [Scaling laws], sources: [@vaswani2017 @sutton2019 @kaplan2020])[
  #fig(
    image("figures/kaplan2020-power-laws.pdf", width: 84%),
    caption: [Figure 1 of Kaplan et al. (2020): the error falls predictably with compute, data and size. That is what justified spending billions.],
  )

  #key-point(title: "The bitter lesson")[
    "General methods that leverage computation are ultimately the most effective". The architecture used today has not changed much from the original GPT, and the most notable advances are mainly due to the increase in scale.
  ]
]

#slide(title: [Chain-of-thought reasoning], sources: [@kojima2022 @wei2022cot @rein2023 @deepseek2025])[
  #cols(
    [
      #caution(title: "Direct answer")[
        `A juggler has 16 balls. Half are` \
        `golf balls, and half of the golf` \
        `balls are blue. How many blue` \
        `golf balls are there?` \
        `A: 8` ✗
      ]
      #key-point(title: "Thinking first")[
        `A: 16 / 2 = 8 golf balls.` \
        `Half of them are blue, so` \
        `8 / 2 = 4. The answer is 4` ✓
      ]
    ],
    fig(
      image("figures/deepseek2025-aime.pdf", width: 92%),
      caption: [DeepSeek-R1: rewarded only on final answers, the model learns to think first, and competition-math accuracy climbs.],
    ),
    weights: (1.05fr, 1fr),
  )

  #note[
    Since 2024 models are trained to reason by default. On graduate-level science questions (GPQA) they now match PhD experts in the field.
  ]
]

#section("From model to assistant")

#slide(title: [The three training stages], sources: [@christiano2017 @radford2019 @brown2020 @ouyang2022])[
  #fig(image("figures/training-stages.pdf", width: 96%))
]

#slide(title: [Tool use], sources: [@schick2023])[
  #fig(image("figures/tool-calls.pdf", width: 96%))
]

#slide(title: [Agents], sources: [@yao2023 @mcp2024])[
  #fig(image("figures/agent-loop.pdf", width: 88%))
]

#section("Demonstrations")

#slide(title: [Demonstration 1: a chat assistant])[
  #cols(
    note(title: "The data")[
      *12 files* dragged into the chat.

      Excel and CSV mixed, 21 countries, 2000 to 2025.

      Nothing lines up.
    ],
    [
      *What we ask for*

      + Audit them: what would break a merge?
      + One clean table.
      + Poverty against inequality.
      + A dashboard to explore it.
      + Where does each number come from?
    ],
    weights: (1fr, 1.1fr),
  )
]

#slide(title: [Demonstration 2: an agent])[
  #note(title: "The same data")[
    Nothing is uploaded. The agent opens the folder itself.
  ]

  #v(10pt)
  *What we ask for*

  + The same audit, and a table that rebuilds itself.
  + A website: map, a page per country, comparison.
  + A chat over the data, driven by a language model.
  + The findings, and what *cannot* be concluded.
  + A short slide deck, compiled.
  + Test it before calling it done.
]

#section("Beyond text")

#slide(title: [Generative adversarial networks], sources: [@goodfellow2014 @karras2018])[
  #fig(image("figures/gan.pdf", width: 74%))

  #fig(
    image("figures/progan-faces-row.png", width: 40%),
    caption: [Faces synthesized by a GAN after training. None of these people exist.],
  )
]

#slide(title: [Diffusion models], sources: [@ho2020 @song2021 @rombach2022 @lipman2023])[
  #fig(image("figures/diffusion.pdf", width: 88%))

  #align(center)[
    Diffusion models constitute the *state of the art* for images, alongside flow matching and autoregressive generation.
  ]
]

#slide(title: [Image editing], sources: [@zhu2017 @rombach2022])[
  #cols(
    fig(
      image("figures/ldm-inpainting.png", width: 96%),
      caption: [Inpainting: regenerate only a masked region.],
    ),
    fig(
      image("figures/cyclegan-style-transfer.png", width: 96%),
      caption: [Style transfer: the same scene, re-rendered.],
    ),
  )

  #note[
    The same machinery allows for coloring photographs, increasing resolution, extending an image beyond its edges, and interpolating between two images.
  ]
]

#slide(title: [Audio generation], sources: [@oord2016])[
  To generate audio, a similar approach to autoregressive text generation can be used. Alternatively, the GAN or diffusion approach could be employed.

  #fig(image("figures/audio-generation.pdf", width: 100%))
]

#slide(title: [Video generation], sources: [@brooks2024 @polyak2024])[
  Diffusion models for images can be extended to videos, where the main difference is that a time variable must be added to the model.

  #fig(
    image("figures/moviegen-edit.png", width: 100%),
    caption: [Editing a video from a text instruction. Improving fast; still weak on physics and on text inside the frame.],
  )
]

#slide(title: [World models], sources: [@ha2018 @valevski2024])[
  The video generation approach can be extended to *world models* that respond, frame by frame, to actions performed by the user.

  #fig(
    image("figures/gamengen-doom.png", width: 80%),
    caption: [DOOM with no game engine: each frame is generated from the previous frames and the player's action.],
  )
]

#slide(title: [Robotics], sources: [@wang2024])[
  The planning mechanism and tool usage of LLM-based agents can be extended to robotics, where actions can be executed in a physical world.

  #fig(
    image("figures/llm-robot-plan.png", width: 80%),
    caption: [A language model turns "pour" into a step-by-step action plan the robot executes, then checks the result.],
  )
]

#slide(title: [Scientific applications], sources: [@lam2023])[
  The same approaches can be used to predict weather or other geospatial phenomena.

  #fig(
    image("figures/graphcast-rollout.png", width: 60%),
    caption: [GraphCast produces a 10-day global forecast in under a minute, more accurately than the leading conventional system (Science, 2023).],
  )

  #note[
    Related models now prove theorems, solve partial differential equations, and flag anomalies in astronomical surveys.
  ]
]

#slide(title: [Molecules and materials], sources: [@jumper2021 @alakhdar2024])[
  Generative models can also be applied to the generation of molecules, where a model can learn to generate new drugs or materials with certain properties.
  #fig(
    image("figures/molecule-diffusion.png", width: 100%),
    caption: [The diffusion recipe from images, applied to molecules: from noise to a candidate drug.],
  )

  #key-point[
    Protein misfolding underlies many diseases, and determining one structure experimentally can take months of laboratory work. *AlphaFold* predicts one in minutes (2024 Nobel Prize in Chemistry).
  ]
]

#section("Current limitations")

#slide(title: [Attention over long contexts], sources: [@liu2023lost])[
  #cols(
    fig(
      image("figures/liu2023-lost-in-the-middle.pdf", width: 88%),
      caption: [Figure 1 of Liu et al. (2023).],
    ),
    [
      LLMs have trouble finding information in intermediate sections of the context. Mitigating problems of this kind is an active area of research.

      #practice[
        Place specific and important instructions at the beginning or end of the prompt. This tip may become obsolete in the near future.
      ]
    ],
    weights: (1.05fr, 1fr),
  )
]

#slide(
  title: [Hallucination, bias and sycophancy],
  sources: [@david2023 @sharma2023 @gallegos2024 @robertson2024 @kalai2025],
)[
  #cols(
    fig(
      image("figures/bias-midjourney-robbery.jpg", height: 6.4cm),
      caption: [Midjourney, 2023: asked for a white man robbing a store.],
    ),
    fig(
      image("figures/bias-gemini-soldiers.jpg", height: 6.4cm),
      caption: [Gemini, 2024: asked for a 1943 German soldier.],
    ),
    [
      #set text(size: 0.9em)
      *Hallucination.* Plausible and reliable content, but incorrect.

      *Bias.* Gender, race, religion, age, disability, politics.

      *Sycophancy.* Models tend to say what the user wants to hear, and to agree with them even if they are wrong.
    ],
    weights: (1fr, 1fr, 1fr),
  )
]

#slide(title: [Prompt injection], sources: [@greshake2023 @nasr2023 @jiang2024])[
  #cols(
    [
      It is possible to construct malicious prompts to encourage the LLM to do things that are outside of their guidelines.
      #caution(title: "Caution")[
        A model that reads a page or a document also reads instructions hidden inside it. White text in a PDF can be enough.
      ]

    ],

    fig(
      image("figures/artprompt2024-attack.pdf", width: 100%),
      caption: [A masked word drawn in ASCII art slips past safety training.],
    ),
    weights: (1.2fr, 1fr),
  )
  Attacks of this type can cause an LLM to reveal their *system prompt* or provide information about their training.
]

#section("Closing")

#slide(title: [Five takeaways])[
  #agenda(
    [1],
    [A model is *fitted, not programmed*: training only reduces an error score on examples.],
    [section 1],
    [2],
    [Guessing the next token, at *scale*, is enough to produce language, reasoning and abilities nobody wrote down.],
    [section 2],
    [3],
    [The assistant is a *thin layer* on top: alignment makes it useful, tools and a loop make it act.],
    [section 3],
    [4],
    [The same recipe now generates *images, audio, video, forecasts and molecules*.],
    [section 5],
    [5],
    [Fluency is not accuracy: *hallucination, bias and prompt injection* make the human check part of the work.],
    [section 6],
  )
]

#slide(title: [Recommended reading])[
  #grid(
    columns: (1fr,) * 5,
    column-gutter: 14pt,
    align: center + horizon,
    ..(
      ("figures/cover-llm.jpg", "https://www.manning.com/books/build-a-large-language-model-from-scratch"),
      ("figures/cover-reasoning.jpg", "https://www.manning.com/books/build-a-reasoning-model-from-scratch"),
      ("figures/cover-handson.jpg", "https://www.oreilly.com/library/view/hands-on-generative-ai/9781098149239/"),
      ("figures/cover-vlm.jpg", "https://www.oreilly.com/library/view/vision-language-models/9798341624030/"),
      ("figures/cover-murphy.jpg", "https://probml.github.io/pml-book/book2.html"),
    ).map(((path, url)) => link(url, image(path, height: 4.9cm))),
  )

  #v(40pt, weak: true)
  - Generative AI blog: #link("https://fernandofetis.ai/blog")[fernandofetis.ai/blog]

  - Contact: #link("mailto:fernando.fetis@uchile.cl")[fernando.fetis\@uchile.cl]
]

#closing(title: "Thank you")

#references(bibliography("bib.yml", style: citation-style, title: none))
