---
marp: true
theme: ngi-theme.css
paginate: false
header: '_23.08.2023_'
footer: '![width:90 height:40](figures/logo/NGI/NGI_logo_transparent.gif)'



--- 
<!-- _class: title --> 
# Pydantic v2


## 

#### 
#### Technical hour
#### Sunniva Indrehus

---
 
<!-- _class: title --> 
# Keep model validation sexy


## 

#### 
#### Technical hour
#### Sunniva Indrehus


---

```
$ whoami
```


--- 

# Pydantic 

## What?

> Pydantic is the most widely used data validation library for Python...Fast and extensible, Pydantic plays nicely with your linters/IDE/brain. Define how data should be in pure, canonical Python 3.7+; validate it with Pydantic.
> 
*[From the official docs](https://docs.pydantic.dev/latest/#why-use-pydantic)*

:star: GitHub 15.4k (22.08.23)
:package: [Downloads per week](https://pypistats.org/packages/pydantic) $\approx$ 22M (22.08.23)

---

# Pydantic 

## Why? 

### Fact 
- Python is dynamically typed where we are allowed to change variables during run time 

### Consequence
- [PEP484 Type Hints](https://peps.python.org/pep-0484/)
- Not enforced during run time


--- 

# Pydantic 

## Stats

:star: GitHub 15.4k (22.08.23)
:package: [Downloads per week](https://pypistats.org/packages/pydantic) $\approx$ 22M (22.08.23)

---


# Pydantic v2

## Core rewritten in Rust

![bg right w:600 h:450](figures/illustrations/new-core.png) 

---

# Credit 

- Prashanth Rao, The Data Quarry, [Obtain a 5x speedup for free by upgrading to Pydantic v2](https://thedataquarry.com/posts/why-pydantic-v2-matters/)(accessed 22.08.2023)