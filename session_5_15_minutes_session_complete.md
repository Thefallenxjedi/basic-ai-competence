# Session 5: 15-Minute Session Complete (The Models Layer)

## 1. Proprietary vs. Open Source Models
*   **Proprietary Models:** Owned by big tech (OpenAI, Anthropic, Google). You access them via an API. They are the absolute smartest models, requiring zero infrastructure setup. However, you face **Platform Risk** (pricing/rules can change anytime) and privacy concerns since data leaves your servers.
*   **Open Source (Open Weights) Models:** Created by companies like Meta (Llama 3) or Mistral, who release the actual mathematical parameter weights for free. You must host them on your own servers, meaning you pay the cloud compute costs but guarantee **100% data privacy** and infinite control over fine-tuning.
*   **Technical Example:** 
    *   *Proprietary:* You send a JSON payload to `api.openai.com/v1/chat/completions` and wait for the response. 
    *   *Open Source:* You download a 15GB `.safetensors` file from HuggingFace, spin up an AWS EC2 instance with an Nvidia A100 GPU, and run the model natively using an inference engine like vLLM.
    *   *Read More:* [IBM: Open Source vs Proprietary AI](https://www.ibm.com/think/insights/open-source-vs-proprietary-ai)

## 2. Reasoning Models (System 1 vs. System 2)
*   **Standard LLMs (System 1):** Fast, instinctive, automatic token prediction. Great for writing, summarizing, and standard tasks.
*   **Reasoning Models (System 2):** Slow, methodical, logical models (like OpenAI's **o1**). When prompted, they pause and generate a hidden **Chain of Thought** before answering. They test strategies, find their own flaws, and self-correct. 
*   **Founder Takeaway:** Reasoning Models are brilliant but cost roughly 10x more and take much longer to generate answers. Do not use them for simple tasks (like writing tweets or formatting text); reserve them for complex math, elite coding, or deep logic puzzles.
*   **Technical Example:** When you prompt the OpenAI `o1-preview` model, the API response includes a `completion_tokens_details` object showing `reasoning_tokens`. You pay for these hidden reasoning tokens, which is why the cost is exponentially higher than standard models.
    *   *Read More:* [OpenAI: Learning to Reason with LLMs (o1)](https://openai.com/index/learning-to-reason-with-llms/)

## 3. Small Models vs. Large Models (SLMs vs LLMs)
*   **Large Language Models (LLMs):** 70B+ parameters. Highly intelligent, capable of complex reasoning, but expensive and slower to run. (The "Senior Architect").
*   **Small Language Models (SLMs):** 1B to 8B parameters. Extremely fast, cheap, and small enough to run "on-device" (like directly on a smartphone) without an internet connection. (The "Intern").
*   **Model Routing:** The industry standard architectural practice of automatically sending simple tasks (like sentiment analysis or data extraction) to cheap SLMs, and sending complex logic tasks to expensive LLMs to optimize profit margins.
*   **Founder Takeaway:** To maximize margins, combine an SLM with **Few-Shot Prompting**. The examples in the prompt compensate for the model's smaller brain, allowing it to perform narrow tasks perfectly at a fraction of the cost.
*   **Technical Example:** Apple Intelligence runs a highly optimized ~3B parameter SLM locally on the iPhone's Neural Engine processor for fast text summarization. It only routes to a larger cloud model (like Private Cloud Compute or ChatGPT) if the user's prompt is too complex for the local parameters.
    *   *Read More:* [Microsoft: The Rise of Small Language Models](https://www.microsoft.com/en-us/research/blog/the-rise-of-small-language-models/)
