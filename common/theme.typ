#let deep = rgb("#00538A")
#let accent = rgb("#0072BC")
#let accent-soft = rgb("#D6EAF6")

#let emphasis = rgb("#B03A48")

#let ink = rgb("#1F2A3A")
#let ink-soft = rgb("#4D5E75")
#let ink-subtle = rgb("#7A8AA0")

#let bg = rgb("#FFFFFF")
#let surface = rgb("#EEF3F9")
#let border = rgb("#CFDBE8")

#let emerald = rgb("#0F766E")
#let emerald-soft = rgb("#D6F0EA")
#let gold = rgb("#A37430")
#let gold-bright = rgb("#E0A100")
#let gold-soft = rgb("#F6ECD8")
#let crimson = rgb("#B03A48")
#let crimson-soft = rgb("#FBE4E6")

#let author-name = "Fernando Fetis Riquelme"
#let institution = "Economic Commission for Latin America and the Caribbean"
#let term = "Spring 2026"

// Relative to this file, so a deck compiles whatever root it is given.
#let logo-lockup = "logos/eclac-un-lockup.svg"
#let logo-mark = "logos/eclac-mark.svg"

#let lecture-label = state("lecture-label", "")
#let section-counter = counter("section")
#let slide-counter = counter("slide")

#let rule = box(width: 100%, height: 2.4pt, grid(
  columns: (2.6cm, 1fr),
  align: horizon,
  std.rect(width: 100%, height: 2.4pt, fill: accent, stroke: none),
  std.rect(width: 100%, height: 0.6pt, fill: border, stroke: none),
))

#let footer = context {
  if slide-counter.get().first() == 0 { return }
  set text(size: 9pt, fill: ink-subtle)
  grid(
    columns: (1fr, auto, auto),
    align: (left + horizon, right + horizon, right + horizon),
    lecture-label.get(),
    box(inset: (right: 8pt), image(logo-mark, height: 0.38cm)),
    counter(page).display(),
  )
}

#let slide(title: none, top: false, sources: none, body) = {
  pagebreak(weak: true)
  slide-counter.step()
  context [#metadata(here().page())<slide-start>]
  if title != none {
    block(width: 100%, below: 14pt)[
      #text(size: 22pt, weight: 600, fill: deep, title)
      #v(9pt, weak: true)
      #rule
    ]
  }
  if top {
    body
  } else {
    v(0.5fr)
    body
    v(1fr)
  }
  if sources != none {
    place(bottom + left, dy: 0.05cm, block(width: 100%)[
      #set text(size: 10pt, fill: ink-subtle)
      #show cite: set text(size: 1em, fill: ink-subtle)
      #sources
    ])
  }
  context [#metadata(here().page())<slide-end>]
}

#let section(name) = {
  section-counter.step()
  page(header: none, footer: none, fill: deep, margin: (x: 2.9cm, y: 2.4cm))[
    #metadata(name)<section-name>
    #set text(fill: white)
    #set par(justify: false)
    #v(1fr)
    #block(below: 18pt, text(size: 76pt, weight: 700, fill: white.transparentize(72%))[
      #context section-counter.display("01")
    ])
    #block(below: 24pt, text(size: 38pt, weight: 600, name))
    #block(below: 20pt, std.rect(width: 3.4cm, height: 2.6pt, fill: gold-bright, stroke: none))
    #v(1fr)
    #place(bottom + right, image(logo-mark, height: 0.8cm))
  ]
}

#let panel(title: none, color: accent, background: accent-soft, body) = block(
  width: 100%,
  fill: background,
  inset: (x: 13pt, y: 11pt),
  radius: (right: 3pt),
  stroke: (left: 2.6pt + color),
  above: 10pt,
  below: 10pt,
)[
  #show raw: set text(size: 0.86em)
  #if title != none {
    block(below: 11pt, text(size: 0.8em, weight: 600, fill: color, tracking: 0.4pt, upper(title)))
  }
  #body
]

#let key-point(title: "Key idea", body) = panel(title: title, color: emerald, background: emerald-soft, body)
#let caution(title: "Watch out", body) = panel(title: title, color: crimson, background: crimson-soft, body)
#let note(title: none, body) = panel(title: title, color: ink-soft, background: surface, body)
#let practice(title: "In practice", body) = panel(title: title, color: gold, background: gold-soft, body)

#let aside(body) = block(width: 100%, above: 16pt, below: 0pt)[
  #set par(justify: false)
  #align(center, text(size: 0.82em, fill: ink-soft, body))
]

#let cols(..bodies, weights: none, gutter: 18pt, align-at: top) = {
  let items = bodies.pos()
  let widths = if weights == none { (1fr,) * items.len() } else { weights }
  grid(columns: widths, column-gutter: gutter, align: align-at, ..items)
}

#let fig(body, caption: none) = align(center)[
  #body
  #if caption != none {
    v(5pt, weak: true)
    block(width: 92%)[
      #set par(justify: false)
      #align(center, text(size: 11pt, fill: ink-soft, style: "italic", caption))
    ]
  }
]

#let agenda(..rows) = {
  let cells = rows.pos()
  set text(size: 0.86em)
  set par(justify: false)
  table(
    columns: (0.9cm, 1fr, auto),
    inset: (x: 8pt, y: 8pt),
    align: (right + horizon, left + horizon, right + horizon),
    stroke: (x, y) => (top: if y == 0 { 0pt } else { 0.4pt + border }, bottom: 0pt),
    ..cells.enumerate().map(((i, cell)) => {
      let col = calc.rem(i, 3)
      if col == 0 { text(weight: 600, fill: accent, cell) }
      else if col == 1 { cell }
      else { text(fill: ink-subtle, cell) }
    }),
  )
}

#let contents(..names) = {
  set text(size: 0.95em)
  set par(justify: false)
  table(
    columns: (0.9cm, 1fr),
    inset: (x: 8pt, y: 10pt),
    align: (right + horizon, left + horizon),
    stroke: (x, y) => (top: if y == 0 { 0pt } else { 0.4pt + border }, bottom: 0pt),
    ..names.pos().enumerate().map(((i, name)) => (text(weight: 600, fill: accent, str(i + 1)), name)).flatten(),
  )
}

#let closing(title: "Thank you") = page(header: none, footer: none, fill: accent, margin: (x: 2.6cm, y: 2.2cm))[
  #set text(fill: white)
  #set par(justify: false)
  #set align(center + horizon)
  #block[
    #block(below: 26pt, text(size: 46pt, weight: 700, title))
    #block(below: 26pt, std.rect(width: 3.4cm, height: 2.6pt, fill: gold-bright, stroke: none))
    #block(below: 34pt, context text(size: 16pt, lecture-label.get()))
    #block(fill: white, radius: 5pt, inset: (x: 1.1cm, y: 0.9cm), image(logo-lockup, width: 2.6cm))
  ]
]

#let citation-style = "american-psychological-association"

// Takes the bibliography itself, not its path: Typst resolves a path where the call is written, so a path handed to this file would be looked for next to it.
#let references(source, title: "References") = {
  pagebreak(weak: true)
  slide-counter.step()
  block(width: 100%, below: 14pt)[
    #text(size: 22pt, weight: 600, fill: deep, title)
    #v(9pt, weak: true)
    #rule
  ]
  set text(size: 9pt)
  show cite: set text(size: 1em)
  columns(2, gutter: 18pt, source)
}

#let lecture(number: 1, title: "", body) = {
  let label = "Lecture " + str(number) + " · " + title
  set document(title: label, author: author-name)
  set page(
    paper: "presentation-16-9",
    margin: (left: 2.1cm, right: 2.1cm, top: 1.4cm, bottom: 1.05cm),
    fill: bg,
    footer: footer,
    footer-descent: 0.35cm,
  )
  set text(font: "Fira Sans", size: 19pt, fill: ink, lang: "en", hyphenate: false)
  set par(justify: false, leading: 0.72em, spacing: 1.05em, linebreaks: "optimized")
  set list(indent: 6pt, spacing: 0.95em, marker: (text(fill: accent, [•]), text(fill: accent, [–]), text(fill: accent, [·])))
  set enum(indent: 6pt, spacing: 0.95em, numbering: n => text(fill: accent, weight: 600, [#n.]))

  show math.equation: set text(font: "Fira Math", size: 0.96em)
  show math.equation.where(block: true): set text(size: 1.12em)
  show raw: set text(font: "JetBrains Mono", size: 0.82em)
  show link: set text(fill: emphasis)
  show cite: set text(size: 0.72em, fill: ink-subtle)

  // Emphasis by color alone: a heavier weight looks blunt at projection size.
  set strong(delta: 0)
  show strong: set text(fill: emphasis)

  lecture-label.update(label)

  page(header: none, footer: none, margin: 0pt)[
    #set par(justify: false)
    #grid(
      columns: (1fr, 10.2cm),
      rows: 100%,
      block(width: 100%, height: 100%, inset: (x: 1.2cm, y: 2.2cm))[
        #set align(center + horizon)
        #block[
          #block(below: 26pt, text(size: 10pt, weight: 600, fill: accent, tracking: 1.5pt, upper(institution)))
          #block(below: 30pt, par(leading: 0.42em, text(size: 36pt, weight: 700, fill: deep, title)))
          #block(below: 26pt, std.rect(width: 3.6cm, height: 2.6pt, fill: gold-bright, stroke: none))
          #block[
            #text(size: 17pt, weight: 600, fill: deep, author-name)
            #linebreak()
            #text(size: 14pt, fill: ink-soft, term)
          ]
        ]
      ],
      block(width: 100%, height: 100%, fill: accent, inset: 1.9cm)[
        #set align(center + horizon)
        #block(fill: white, radius: 6pt, inset: (x: 1.6cm, y: 1.4cm))[
          #image(logo-lockup, width: 4.6cm)
        ]
        #v(18pt, weak: true)
        #text(size: 12pt, fill: white.transparentize(15%), weight: 600, tracking: 1.6pt)[#upper("Lecture " + str(number))]
      ],
    )
  ]

  slide(title: [What this talk covers], top: true)[
    #context contents(..query(<section-name>).map(entry => entry.value))
  ]

  body
}
