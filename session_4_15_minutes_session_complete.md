# Session 4: 15-Minute Session Complete (The Agents Layer)

## 1. Workflow vs. Agent
*   **Workflow:** A human writes the exact steps the AI must follow (If/Then logic). It is deterministic, safe, and rigid. Ideal for high-risk operations (like moving money or issuing refunds).
*   **Agent:** The human provides a goal and a set of tools. The AI autonomously reasons, plans, and executes the steps required to achieve the goal, correcting its own errors along the way.
*   **Technical Example:** LangChain's `AgentExecutor`. You pass it an LLM and an array of `@tool` functions (like `search_database`). You prompt the Agent to "Find the cheapest competitor price." The Agent autonomously loops through a ReAct (Reasoning and Acting) cycle until it figures out the answer.
    *   *Read More:* [LangChain: Agents vs Chains (Workflows)](https://python.langchain.com/docs/modules/agents/)

## 2. Attention
*   **The Spotlight Mechanism:** Before 2017, AI read text left-to-right and forgot early words. The **Attention Mechanism** allows the AI to look at *every token simultaneously* and mathematically calculate how strongly each word relates to the others, giving it perfect context.
*   **Founder Takeaway:** Attention is the specific math equation that allows an AI to understand that the word "bank" means a river in one sentence, and a financial institution in another.
*   **Technical Example:** Self-attention uses Query, Key, and Value matrices. The AI computes a dot product between the Query of the current word and the Keys of all other words. A high dot product means high relevance, causing the AI to "attend" heavily to that specific word.
    *   *Read More:* [Google Research: Attention Is All You Need (Summary)](https://research.google/blog/transformer-a-novel-neural-network-architecture-for-language-understanding/)

## 3. The Transformer
*   **The Architecture:** The "T" in ChatGPT. It is the software architecture that houses the Attention mechanism. 
*   **Parallel Processing:** The breakthrough of the Transformer is that it processes all tokens in parallel rather than sequentially, allowing AI companies to train massive models using thousands of GPUs simultaneously.
*   **Technical Example:** Older Recurrent Neural Networks (RNNs) had to wait for token $t$ to process before they could process token $t+1$. Transformers process $t$, $t+1$, and $t+1000$ at the exact same millisecond across multiple GPU cores.
    *   *Read More:* [NVIDIA: What is a Transformer Model?](https://blogs.nvidia.com/blog/what-is-a-transformer-model/)

## 4. Self-Supervised Learning
*   **The Secret to Scale:** Instead of paying humans to label data, companies dump raw internet text into the Transformer. The AI hides a word from itself, guesses the word, and checks if it was right. It trains itself.
*   **Founder Takeaway:** This removes the human bottleneck, allowing models to be trained on trillions of words economically.
*   **Technical Example:** "Masked Language Modeling." In BERT, 15% of the input tokens are replaced with a `[MASK]` token. The model calculates the loss (error rate) of its prediction for that masked token and updates its parameter weights via backpropagation.
    *   *Read More:* [Meta AI: Self-Supervised Learning](https://ai.meta.com/research/no-supervision-required/)

## 5. Few-Shot Prompting
*   **The Needle vs The Sword:** Before spending money to Fine-Tune a model for a specific format, use Few-Shot Prompting. This means providing 3 to 5 perfect examples of the desired input/output directly inside the System Prompt.
*   **Technical Example:** Passing an array of examples in the API: `[{"role": "user", "content": "happy"}, {"role": "assistant", "content": "Positive"}, {"role": "user", "content": "terrible"}, {"role": "assistant", "content": "Negative"}]`. This mathematically biases the next-token prediction toward your exact desired format.
    *   *Read More:* [Anthropic: Few-Shot Prompting](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-examples)

## 6. Model Context Protocol (MCP)
*   **The Universal AI Plug:** An open-source standard created by Anthropic that acts like a USB-C cable for AI. It allows an AI to securely plug into external data sources (GitHub, Slack, local files) without founders having to write custom, brittle integration code for every app.
*   **Technical Example:** You run an MCP server locally for SQLite. The AI client sends a standardized JSON-RPC message over the MCP protocol to request the database schema. The server returns it, and the AI can now query the database without needing custom API endpoints written by you.
    *   *Read More:* [Anthropic: Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)

## 7. Context Engineering
*   **The Art of Curation:** You pay per token, and LLMs get confused by noise. Context Engineering is the process of aggressively filtering, prioritizing, and summarizing the data you inject into the Context Window to maximize accuracy and minimize cost.
*   **Founder Takeaway:** Just because a model has a 2-Million token context window doesn't mean you should use it. Cramming irrelevant data destroys your profit margins and confuses the AI.
*   **Technical Example:** Using a Python script to parse a 100-page PDF, run a regex to extract only the "Executive Summary" section, and passing only those 500 tokens to the OpenAI API instead of the full 100,000 token document.
    *   *Read More:* [Pinecone: Optimizing Context Windows](https://www.pinecone.io/learn/chunking-strategies/)
