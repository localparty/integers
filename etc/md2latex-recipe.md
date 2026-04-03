# md2latex Recipe

## The Rule

**Write Unicode in markdown. The converter handles LaTeX.**

There is one recipe for all math, everywhere:

1. **Inline math** — fence with backticks: `` `Ω_DM/Ω_b ≈ 5` ``
2. **Equation blocks** — indent 4 spaces (markdown code block):
   ```
       P(↑_â, ↑_b̂) = ½ sin²(θ/2)
   ```
3. **The converter does the rest** — Unicode → LaTeX commands, backticks → `$...$`, equation blocks → `\begin{equation}...\end{equation}`

## What the converter handles automatically

- Greek letters: `α → \alpha`, `Ω → \Omega`, etc.
- Arrows: `↑ → \uparrow`, `↓ → \downarrow`
- Brackets: `⟨ → \langle`, `⟩ → \rangle`
- Operators: `∫ → \int`, `∂ → \partial`, `∇ → \nabla`, `√ → \sqrt`
- Relations: `≈ → \approx`, `≤ → \leq`, `≥ → \geq`, `∈ → \in`
- Subscripts/superscripts: `₀₁₂...` → `_{0}_{1}_{2}...`, `²³` → `^{2}^{3}`
- Hat/bar/dot/tilde: `â → \hat{a}`, `n̂ → \hat{n}` (combining diacritics)
- Trig functions: `sin → \sin`, `cos → \cos`, `exp → \exp`, `ln → \ln`
- Fractions: `½ → \tfrac{1}{2}`
- Subscript bracing: `↑_â → \uparrow_{\hat{a}}` (multi-token subscripts get `{}`)

## What you must do manually

- **Fence inline math with backticks.** Any expression with Greek, subscripts, superscripts, or operators needs backticks.
- **Use `\` for LaTeX-only commands** that have no Unicode equivalent: `\frac{a}{b}`, `\left(`, `\right)`, `\operatorname{sinc}`, `\text{...}`
- **Multi-char subscripts in equation blocks** use `_` with braces: `x_{total}`, `N_{eff}` (single char is fine without braces: `x_i`)

## What NOT to do

- Don't write LaTeX in inline text without backtick fencing — it'll be treated as plain text
- Don't use `$$...$$` for display math — use 4-space indentation
- Don't use double backticks ` `` ` — the converter only handles single backticks
- Don't worry about `\sin` vs `sin` in equation blocks — the converter adds the backslash
- Don't put Unicode inside `\text{...}` in equation blocks — the converter will try to convert it (e.g., `\text{ μm}` breaks; use plain `μm` instead)
- Don't use `\text{...}`, `\quad`, `\cdot` etc. in equation blocks — write plain Unicode and let the converter handle it
