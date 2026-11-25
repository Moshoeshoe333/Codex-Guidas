# AI Engineering Learning and Application Map

**Status:** Proposed learning and reference map  
**Created:** 2026-11-25  
**Last source check:** 2026-11-25  
**Scope:** Learning resources supplied by the maintainer, grouped into a practical progression and mapped to portfolio engineering questions.

## Purpose

This map turns a broad list of AI courses, university materials and books into a usable learning route. It is intended to help the maintainer build enough conceptual and practical understanding to ask better questions, evaluate AI claims, design bounded experiments and recognise when a technique is inappropriate.

It is a **learning index**, not a new Codex-Guidas methodology, a certification framework, a project requirement or evidence that any listed method is effective in a particular product.

## Operating rules

1. **Learn for a real question.** Choose a resource because it addresses a current capability gap or a clearly stated future question—not because it is fashionable.
2. **Prefer primary providers.** Link to the university, course author, publisher or official platform where a reliable page is available. Class Central is useful for discovery and comparison, but it is not the course owner.
3. **Recheck access.** Syllabi, pricing, audit access, certificates, prerequisites and course availability change. Confirm these on the provider page before enrolling.
4. **Separate learning from proof.** Course completion demonstrates participation/completion under that provider's rules. It does not demonstrate independent competence, project suitability, model quality, safety or production readiness.
5. **Build a small reproducible exercise.** Record the question, data, baseline, method, evaluation, failures and limitations before proposing project adoption.
6. **Do not import complexity by default.** A neural network, LLM, agent, vector database or prediction model must solve a demonstrated problem better than a simpler baseline.
7. **Respect project authority.** This map does not authorize implementation, data collection, model training, access to personal data, or changes to any project's gate.

## Recommended learning route

This is a selective path, not a requirement to complete all 40 resources.

### Stage 0 — AI literacy and responsible use

Start with one broad introduction:
- [Elements of AI — University of Helsinki / MinnaLearn](https://www.elementsofai.com/)
- [AI for Everyone — DeepLearning.AI / Andrew Ng](https://www.coursera.org/learn/ai-for-everyone)

Then use current practical guidance:
- [OpenAI Academy](https://academy.openai.com/)
- [Anthropic Academy](https://academy.claude.com/)

**Exit evidence:** Explain the difference between AI, machine learning, deep learning and generative AI; identify at least three limitations or failure modes; distinguish an AI-assisted workflow from an autonomous decision.

### Stage 1 — Classical AI, Python and machine-learning foundations

Choose based on current skill:
- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/)
- [Kaggle: Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning)
- [Kaggle: Intermediate Machine Learning](https://www.kaggle.com/learn/intermediate-machine-learning/)
- [Harvard CS50: Introduction to AI with Python](https://cs50.harvard.edu/ai/)
- [MIT 6.034: Artificial Intelligence](https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/)

**Exit evidence:** Build and evaluate a simple baseline; explain train/validation/test separation, leakage, overfitting, class imbalance and why accuracy alone may mislead.

### Stage 2 — Neural networks and deep learning

Choose one practical and one conceptual resource:
- [Neural Networks: Zero to Hero — Andrej Karpathy](https://github.com/karpathy/nn-zero-to-hero)
- [Practical Deep Learning for Coders — fast.ai](https://course.fast.ai/)
- [MIT 6.S191 — Introduction to Deep Learning](https://introtodeeplearning.com/)
- [Dive into Deep Learning](https://d2l.ai/)
- [Understanding Deep Learning — Simon J. D. Prince](https://udlbook.github.io/udlbook/)
- [Deep Learning — Goodfellow, Bengio and Courville](https://www.deeplearningbook.org/)

Use [Mathematics for Machine Learning](https://mml-book.github.io/) when linear algebra, calculus, probability or optimisation is the actual blocker.

**Exit evidence:** Explain a model's inputs, outputs, training objective, evaluation design and failure cases; reproduce a small exercise and compare it to a simple baseline.

### Stage 3 — LLMs, application engineering and agents

Suggested order:
1. [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1)
2. [ChatGPT Prompt Engineering for Developers — DeepLearning.AI](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)
3. [LangChain for LLM Application Development — DeepLearning.AI](https://www.deeplearning.ai/courses/langchain/)
4. [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/en/unit0/introduction)
5. [Full Stack Deep Learning](https://fullstackdeeplearning.com/course/)

Use provider documentation alongside the courses. Framework APIs and agent patterns change quickly; course completion is not a substitute for current documentation, security review or evaluation.

**Exit evidence:** Build a bounded prototype with explicit inputs, outputs, tool permissions, error handling, evaluation cases, human review and a clear stop condition. Demonstrate what happens when the model is wrong or a tool fails.

### Stage 4 — Specialist study when a project question justifies it

- **Computer vision:** [Stanford CS231n](https://cs231n.stanford.edu/), [Udacity Introduction to Computer Vision](https://www.udacity.com/course/introduction-to-computer-vision--cd0360), [DeepLearning.AI Convolutional Neural Networks](https://www.coursera.org/learn/convolutional-neural-networks)
- **Natural language processing:** [Stanford CS224N](https://web.stanford.edu/class/cs224n/), [NLP with Classification and Vector Spaces](https://www.coursera.org/learn/classification-vector-spaces-in-nlp)
- **Machine learning theory:** [Stanford CS229](https://see.stanford.edu/Course/CS229)
- **Language-model internals:** [Stanford CS336 — Language Modeling from Scratch](https://cs336.stanford.edu/)
- **Reinforcement learning:** [UC Berkeley CS285](https://rail.eecs.berkeley.edu/deeprlcourse/)
- **Autonomous driving:** [Introduction to Self-Driving Cars](https://www.coursera.org/learn/intro-self-driving-cars) and [Self-Driving Cars Specialization](https://www.coursera.org/specializations/self-driving-cars)

Do not study every specialist area in parallel. Select one only when a concrete project question needs it.

## Portfolio application map

These are **candidate learning-to-project connections**, not approved features or claims that AI is required.

| Project | Potential learning connection | Evidence required before adoption |
|---|---|---|
| **Codex-Guidas** | Search relevance, embeddings, retrieval-augmented generation, evaluation of AI-assisted knowledge retrieval | Compare against existing keyword search; create a labelled query set; measure recall/precision or task success; inspect false matches; retain source citations and human review |
| **ScoutSA** | Video/image analysis, computer vision, uncertainty, bias and human-in-the-loop decision support | Lawful data basis and consent; safeguarding review; representative labelled data; independent validation; error analysis across relevant groups; no automated player ranking, selection or exposure decisions |
| **SoulSyncMobile** | Classification, anomaly detection, adversarial robustness, multilingual text and constrained/on-device inference | Compare against deterministic rules; test false positives and false negatives; evaluate adversarial and language variation; measure latency/resource use; preserve privacy and fail-safe behaviour |
| **SoulSync 3** | AI-assisted engineering workflows, structured extraction and evidence retrieval | Exact provenance; deterministic checks remain authoritative; independent evaluation; no model-generated ratification, closure or verification |
| **NAVIGRE / Mall-Navigre** | Ranking, recommendation, route/context inference and uncertainty-aware search | Measure relevance and freshness; evaluate location uncertainty and edge cases; minimise location data; provide fallback and user correction; do not imply certainty unsupported by signals |

### Codex-Guidas-specific recommendation

Do **not** jump directly from this course list to vector search or an AI agent inside Codex-Guidas.

The correct sequence is:

1. Define a small set of real knowledge-retrieval questions.
2. Establish a labelled baseline using the existing keyword/tag search.
3. Record relevant and irrelevant results, missed records and user effort.
4. Identify whether the shortfall is lexical matching, metadata quality, missing tags, duplicated concepts or genuinely semantic similarity.
5. Test the simplest intervention first: better tags, synonyms, query expansion or metadata.
6. Only if those are insufficient, compare a small embedding-based retrieval experiment against the baseline.
7. Keep retrieval results as leads; the source Markdown record and its evidence remain authoritative.

An LLM may help draft summaries or suggest related records, but it must not silently change lesson status, severity, evidence class, defect state or project authority.

## Learning-to-knowledge capture protocol

A course or experiment should enter the knowledge base only when it produces something reusable.

For a meaningful learning exercise, capture:

- **Question:** What engineering question did the study address?
- **Resource:** Exact course/book/module, provider, URL and access date.
- **Concept learned:** A concise explanation in the maintainer's own words.
- **Exercise:** What was built, measured or reproduced?
- **Baseline:** What simpler method was compared?
- **Evidence:** Code, notebook, dataset description, tests, results or source references.
- **Limitations:** What was not tested, what failed, and where the result may not transfer.
- **Project relevance:** Which project could benefit, and why?
- **Decision:** Keep as personal study, create/update a Proposed lesson, run a bounded experiment, or take no action.
- **Authority:** Name the owning project gate or approval required before implementation.

Do not create a new CG lesson merely because a course was completed. Update an existing lesson when the principle is already represented. Keep personal study notes outside the verified lesson ledger until a reusable, evidence-backed engineering principle exists.

## Evidence and maturity ladder for AI learning

| Level | Meaning | What it does not mean |
|---|---|---|
| **Resource identified** | A course or reference has been found | The resource has been studied |
| **Studied** | The learner completed or reviewed material | Independent competence |
| **Concept explained** | The learner can explain the concept and its limitations | The concept works in the target project |
| **Exercise reproduced** | A bounded exercise was repeated with recorded inputs and outputs | Production readiness |
| **Experiment evaluated** | A project-relevant hypothesis was tested against a baseline | General validity or cross-project transfer |
| **Project adopted** | The owning project approved implementation and its controls | Permanent correctness; continued monitoring is required |

This is a descriptive learning record, not a replacement for the repository's existing evidence classes or lesson status vocabulary.

## Full resource catalogue (40 supplied items)

The entries below preserve the maintainer's supplied list. Official provider links are used where identified. Where the supplied Class Central URL was truncated or a canonical provider page was not confirmed during this review, the entry is marked **verify link/access** rather than inventing a destination. Availability, pricing and syllabus currency must be checked at enrolment.

| # | Resource | Provider / area | Reference |
|---:|---|---|---|
| 01 | Elements of AI | University of Helsinki / MinnaLearn | [Official course](https://www.elementsofai.com/) |
| 02 | Harvard CS50's Introduction to AI with Python | Harvard | [Official course](https://cs50.harvard.edu/ai/) |
| 03 | MIT 6.034 Artificial Intelligence | MIT OpenCourseWare | [Official course](https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/) |
| 04 | Neural Networks: Zero to Hero | Andrej Karpathy | [Course and notebooks](https://github.com/karpathy/nn-zero-to-hero) |
| 05 | Building AI | University of Helsinki / MinnaLearn | [Course provider](https://www.elementsofai.com/) — verify current course entry |
| 06 | AI for Everyone | DeepLearning.AI / Andrew Ng | [Official course](https://www.coursera.org/learn/ai-for-everyone) |
| 07 | Introduction to Artificial Intelligence | Udacity | Verify link/access |
| 08 | Convolutional Neural Networks | DeepLearning.AI | [Official course](https://www.coursera.org/learn/convolutional-neural-networks) |
| 09 | Deep Learning Specialization | DeepLearning.AI | [Specialization](https://www.coursera.org/specializations/deep-learning) |
| 10 | Applied Machine Learning in Python | University of Michigan / Coursera | [Course page](https://www.coursera.org/learn/python-machine-learning) — verify current title/access |
| 11 | Introduction to Computer Vision | Udacity | [Official course](https://www.udacity.com/course/introduction-to-computer-vision--cd0360) |
| 12 | NLP with Classification and Vector Spaces | DeepLearning.AI | [Official course](https://www.coursera.org/learn/classification-vector-spaces-in-nlp) |
| 13 | Structuring Machine Learning Projects | DeepLearning.AI | Verify link/access |
| 14 | Introduction to Self-Driving Cars | University of Toronto / Coursera | [Course](https://www.coursera.org/learn/intro-self-driving-cars) |
| 15 | Self-Driving Cars Specialization | University of Toronto / Coursera | [Specialization](https://www.coursera.org/specializations/self-driving-cars) |
| 16 | Prompt Engineering for Everyone | CodeSignal / provider as listed by Class Central | Verify link/access |
| 17 | Google AI Essentials | Google | [Google AI learning](https://grow.google/ai-essentials/) — verify current enrolment/access |
| 18 | ChatGPT Prompt Engineering for Developers | DeepLearning.AI / OpenAI | [Short course](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) |
| 19 | LangChain for LLM Application Development | DeepLearning.AI / LangChain | [Course](https://www.deeplearning.ai/courses/langchain/) |
| 20 | AI for Beginners | Microsoft | [Official curriculum](https://microsoft.github.io/AI-For-Beginners/) |
| 21 | Introduction to Generative AI | Google | [Google Cloud Skills Boost](https://www.cloudskillsboost.google/) — locate current course |
| 22 | Machine Learning Crash Course | Google | [Official course](https://developers.google.com/machine-learning/crash-course/) |
| 23 | Practical Deep Learning for Coders | fast.ai | [Official course](https://course.fast.ai/) |
| 24 | Hugging Face LLM Course | Hugging Face | [Official course](https://huggingface.co/learn/llm-course/chapter1/1) |
| 25 | Hugging Face Agents Course | Hugging Face | [Official course](https://huggingface.co/learn/agents-course/en/unit0/introduction) |
| 26 | OpenAI Academy | OpenAI | [Official academy](https://academy.openai.com/) |
| 27 | Anthropic Academy | Anthropic | [Official academy](https://academy.claude.com/) |
| 28 | Kaggle Intro to Machine Learning | Kaggle | [Official course](https://www.kaggle.com/learn/intro-to-machine-learning) |
| 29 | Kaggle Intermediate Machine Learning | Kaggle | [Official course](https://www.kaggle.com/learn/intermediate-machine-learning/) |
| 30 | Stanford CS229 Machine Learning | Stanford | [Stanford Engineering Everywhere](https://see.stanford.edu/Course/CS229) |
| 31 | MIT 6.S191 Introduction to Deep Learning | MIT | [Course site](https://introtodeeplearning.com/) |
| 32 | Stanford CS231n | Stanford | [Official course](https://cs231n.stanford.edu/) |
| 33 | Stanford CS224n | Stanford | [Official course](https://web.stanford.edu/class/cs224n/) |
| 34 | Stanford CS336 | Stanford | [Official course](https://cs336.stanford.edu/) |
| 35 | Berkeley CS285 Deep Reinforcement Learning | UC Berkeley | [Official course](https://rail.eecs.berkeley.edu/deeprlcourse/) |
| 36 | Full Stack Deep Learning | Full Stack Deep Learning | [Official course](https://fullstackdeeplearning.com/course/) |
| 37 | Dive into Deep Learning | Open textbook | [Official book](https://d2l.ai/) |
| 38 | Deep Learning | Goodfellow, Bengio and Courville | [Official book](https://www.deeplearningbook.org/) |
| 39 | Mathematics for Machine Learning | Deisenroth, Faisal and Ong | [Official book](https://mml-book.github.io/) |
| 40 | Understanding Deep Learning | Simon J. D. Prince | [Official book](https://udlbook.github.io/udlbook/) |

## Review and maintenance

- Review this map every six months or when a linked provider materially changes its course.
- Prefer replacing stale links with official current links; preserve the original resource title and note the change.
- Do not add completion badges or course certificates to the CG lesson ledger as proof of engineering controls.
- A resource may be removed or deprioritised if it is outdated, inaccessible, redundant or no longer relevant.
- New AI resources should be added only when they fill a learning gap not already served by the current catalogue.

## Source notes

Official provider pages checked on 2026-11-25 include Elements of AI, Harvard CS50 AI, MIT 6.034, Google ML Crash Course, fast.ai, OpenAI Academy, Hugging Face LLM and Agents courses, Stanford CS229/CS231n/CS224N/CS336, Berkeley CS285, Full Stack Deep Learning, Kaggle Learn, and the linked deep-learning textbooks. The original Class Central links supplied for several entries were shortened/truncated in the message; those entries are explicitly marked for link/access verification.

**Status discipline:** This map is Proposed. It has not been ratified as a mandatory curriculum, and no listed resource is endorsed as a universal prerequisite.
