# Session 3: 15-Minute Session Complete (Modern AI Layer)

## 1. Embeddings & Vector Space
*   **Embeddings:** AI does not understand words; it understands math. An embedding is a process that converts a token into a mathematical coordinate in a high-dimensional **Vector Space**.
*   **The Magic of Meaning:** Words or concepts with similar meanings are placed physically close together in this vector space. This allows the AI to understand "context" and "similarity" rather than just relying on exact keyword matching.
*   **Technical Example:** OpenAI's `text-embedding-3-small` model takes a sentence and outputs an array of 1,536 floating-point numbers (e.g., `[0.0023, -0.0145, 0.884...]`). This array is the exact mathematical coordinate of that sentence's meaning.
    *   *Read More:* [OpenAI: What are Embeddings?](https://platform.openai.com/docs/guides/embeddings)

## 2. Vector Databases
*   Traditional SQL databases cannot efficiently search these high-dimensional math coordinates. 
*   We use specialized **Vector Databases** (like Pinecone, Weaviate, or pgvector) to store our embeddings. These databases use **Cosine Similarity** to instantly find which coordinates are closest to each other.
*   **Technical Example:** Instead of a SQL `SELECT * WHERE keyword = 'coat'`, you send a mathematical vector to a database like Pinecone. Pinecone runs a Cosine Similarity algorithm to find the nearest neighbor vectors in milliseconds, returning the document ID for "thermal jacket" because its vector is 99% similar to "warm coat".
    *   *Read More:* [Pinecone: What is a Vector Database?](https://www.pinecone.io/learn/vector-database/)

## 3. RAG (Retrieval-Augmented Generation)
*   **The Hallucination Cure:** Because you cannot stop hallucinations using just prompts, RAG shifts the LLM from a *memorization engine* to a *reading comprehension engine*.
*   **The Pipeline:** 
    1. **Ingestion:** You break your Knowledge Base (PDFs, FAQs) into smaller text blocks called **chunks** and store their embeddings in a Vector DB.
    2. **Retrieval:** The user's prompt is embedded, and the Vector DB retrieves the Top-K most relevant chunks via Cosine Similarity.
    3. **Augmentation & Generation:** Those factual chunks are injected into the context window, and the LLM generates an answer strictly based on that retrieved data.
*   **Founder Takeaway:** RAG is incredibly cost-efficient because it prevents you from having to stuff a massive 200,000-token document into the context window for every single user query.
*   **Technical Example:** Frameworks like LangChain or LlamaIndex automate this. During Ingestion, LangChain's `RecursiveCharacterTextSplitter` breaks your 50-page PDF into 1000-character chunks. During Retrieval, it pulls the top 3 chunks and builds a dynamic System Prompt: *"Answer the user using ONLY this context: [Chunk 1] [Chunk 2]"*.
    *   *Read More:* [LangChain: Q&A with RAG](https://python.langchain.com/docs/use_cases/question_answering/)

## 4. Fine-Tuning vs. RAG
*   **The Golden Rule:** Use **RAG** for adding changing Knowledge/Facts. Use **Fine-Tuning** for changing Behavior/Tone/Formatting.
*   **Procedural Fine-Tuning:** If you have a strict, multi-step logical or mathematical workflow, you can fine-tune the model on thousands of examples of that workflow. This builds "muscle memory." When the variable inputs change (like a new SI unit), the model flawlessly executes the steps because the *behavior* is locked into its parameters.
*   **Technical Example:** To fine-tune an OpenAI model, you don't use a PDF. You must prepare a strict `.jsonl` file with thousands of rows of conversation history mapping an exact User Prompt to an exact, perfectly formatted Assistant Response. The model runs training epochs over this file to adjust its internal parameter weights.
    *   *Read More:* [OpenAI: Fine-Tuning Guide](https://platform.openai.com/docs/guides/fine-tuning)

## 5. Function Calling (Tool Use) & Structured Outputs
*   **Giving the AI Hands:** An LLM cannot natively click buttons, search the web, or update databases. 
*   **How it works:** You provide the AI with a list of tools. When the AI detects the user's intent (e.g., "Update status to Closed Won"), it does *not* execute the action. Instead, it outputs a hidden, perfectly structured JSON command (e.g., `{"tool": "update_status", "company": "Acme Corp", "status": "Closed Won"}`).
*   **Founder Takeaway:** The LLM acts as the manager making the decision. Your traditional backend software catches the JSON and acts as the worker doing the actual API calls (like updating Salesforce).
*   **Technical Example:** In your API payload, you define a JSON Schema for a tool called `get_weather`. If the user asks for the weather, the API response won't contain conversational text. Instead, it returns `finish_reason: "tool_calls"`, containing the exact JSON arguments `{"location": "London"}`. Your Python/Node backend parses this JSON, runs an HTTP request to a weather API, and returns the result to the LLM.
    *   *Read More:* [Anthropic: Tool Use (Function Calling)](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)
