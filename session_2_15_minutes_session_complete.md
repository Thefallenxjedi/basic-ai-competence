# Session 2: 15-Minute Session Complete (LLM Layer)

## 1. Tokens and Context Windows
*   **Tokens:** AI reads text in chunks called tokens (usually 3-4 characters). This is the currency of AI—you pay per token for inference.
*   **Context Window:** The AI's "short-term memory." It is a hard limit on how many tokens it can hold in a single interaction (Prompt + Output combined). 
*   **Founder Takeaway:** If an AI is cutting off responses or forgetting the beginning of a document, your input tokens have likely saturated the context window. You must ensure there is enough **token overhead** (configured via the `max_tokens` API setting) for the model to generate its output.

## 2. What is an LLM? (Next Token Prediction)
*   **The Core Engine:** Despite feeling like magic, an LLM (Large Language Model) is simply a massive prediction engine. It calculates the mathematical probability of what the next token should be, one by one.
*   **Founder Takeaway:** LLMs do not "think" in whole sentences and they are not databases looking up facts. They just guess the most statistically probable next piece of a word.

## 3. Temperature
*   **The Randomness Dial:** A setting (usually 0.0 to 1.0) that controls how strictly the LLM follows its math.
*   **Temperature = 0.0:** Zero randomness. The AI always picks the #1 most probable token. Excellent for coding, data extraction, or legal documents. (Prevents infinite loops).
*   **Temperature = 0.7+:** Allows the AI to pick the 2nd or 3rd most probable token. Excellent for creative writing or brainstorming.
*   **Founder Takeaway:** Control the temperature based on your product's use case. Strict math vs. Creativity.

## 4. Hallucinations
*   **The Problem:** When an AI confidently states a completely false fact.
*   **The Truth:** Because LLMs are just next-token predictors optimizing for fluent language (not factual truth), you **cannot 100% prevent hallucinations** using just an LLM and a prompt alone. The AI literally does not know when it is lying.

## 5. System Prompts vs. User Prompts
*   **User Prompt:** What your customer types into the chat box.
*   **System Prompt:** The hidden "God Mode" instructions you send to the AI in the background before the user says hello. 
*   **Founder Takeaway:** The System Prompt is your control panel. It is where you define the AI's persona, its boundaries, and strict rules (like never mentioning a competitor or giving away the final answer).
