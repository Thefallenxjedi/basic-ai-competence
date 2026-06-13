# Session 2: 15-Minute Session Complete (LLM Layer)

## 1. Tokens and Context Windows
*   **Tokens:** AI reads text in chunks called tokens (usually 3-4 characters). This is the currency of AI—you pay per token for inference.
*   **Context Window:** The AI's "short-term memory." It is a hard limit on how many tokens it can hold in a single interaction (Prompt + Output combined). 
*   **Founder Takeaway:** If an AI is cutting off responses or forgetting the beginning of a document, your input tokens have likely saturated the context window. You must ensure there is enough **token overhead** (configured via the `max_tokens` API setting) for the model to generate its output.
*   **Technical Example:** If you type "apple" it is 1 token. If you type "hamburger", OpenAI's tokenizer breaks it into 3 tokens: `["ham", "bur", "ger"]`. On average, 1 token is about 0.75 English words. 
    *   *Read More:* [OpenAI Tokenizer Tool](https://platform.openai.com/tokenizer)

## 2. What is an LLM? (Next Token Prediction)
*   **The Core Engine:** Despite feeling like magic, an LLM (Large Language Model) is simply a massive prediction engine. It calculates the mathematical probability of what the next token should be, one by one.
*   **Founder Takeaway:** LLMs do not "think" in whole sentences and they are not databases looking up facts. They just guess the most statistically probable next piece of a word.
*   **Technical Example:** At the very end of a Transformer neural network, a mathematical function called "Softmax" converts raw scores into percentages. It looks at the dictionary of 100,000 possible tokens and assigns a probability to each. "blue" = 90%, "dark" = 9%. The model selects the highest percentage and appends it to your text.
    *   *Read More:* [Understanding LLMs and Next Token Prediction](https://ig.ft.com/generative-ai/)

## 3. Temperature
*   **The Randomness Dial:** A setting (usually 0.0 to 1.0) that controls how strictly the LLM follows its math.
*   **Temperature = 0.0:** Zero randomness. The AI always picks the #1 most probable token. Excellent for coding, data extraction, or legal documents. (Prevents infinite loops).
*   **Temperature = 0.7+:** Allows the AI to pick the 2nd or 3rd most probable token. Excellent for creative writing or brainstorming.
*   **Founder Takeaway:** Control the temperature based on your product's use case. Strict math vs. Creativity.
*   **Technical Example:** In API code, you set `"temperature": 0.0`. Mathematically, setting temperature closer to 0 makes the highest probability token approach 100% (eliminating all other choices). Setting it higher flattens the distribution, giving lower-probability tokens a fighting chance to be chosen.
    *   *Read More:* [OpenAI API: Temperature](https://platform.openai.com/docs/api-reference/chat/create#chat-create-temperature)

## 4. Hallucinations
*   **The Problem:** When an AI confidently states a completely false fact.
*   **The Truth:** Because LLMs are just next-token predictors optimizing for fluent language (not factual truth), you **cannot 100% prevent hallucinations** using just an LLM and a prompt alone. The AI literally does not know when it is lying.
*   **Technical Example:** In 2023, two lawyers used ChatGPT to prepare a legal brief. The LLM completely invented fake court cases (like "Mata v. Avianca"). Because the LLM saw the tokens "aviation" and "lawsuit", it mathematically predicted that "Avianca" was a highly probable next token, creating a flawless, plausible-sounding, but entirely fake legal citation.
    *   *Read More:* [Forbes: Lawyers Sanctioned for using Fake ChatGPT Cases](https://www.forbes.com/sites/mattnovak/2023/06/22/lawyers-fined-5000-for-using-fake-chatgpt-cases-in-court/)

## 5. System Prompts vs. User Prompts
*   **User Prompt:** What your customer types into the chat box.
*   **System Prompt:** The hidden "God Mode" instructions you send to the AI in the background before the user says hello. 
*   **Founder Takeaway:** The System Prompt is your control panel. It is where you define the AI's persona, its boundaries, and strict rules (like never mentioning a competitor or giving away the final answer).
*   **Technical Example:** In the actual JSON payload you send to an AI API, the System Prompt is literally an array object labeled `"role": "system"`, while the user's text is labeled `"role": "user"`. The model is mathematically trained to prioritize instructions coming from the "system" role over the "user" role.
    *   *Read More:* [Anthropic: System Prompts Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts)
