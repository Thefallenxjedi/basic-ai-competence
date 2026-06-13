# Session 3: 15-Minute Session Complete (Modern AI Layer)

## 1. Embeddings & Vector Space
*   **Embeddings:** AI does not understand words; it understands math. An embedding is a process that converts a token into a mathematical coordinate in a high-dimensional **Vector Space**.
*   **The Magic of Meaning:** Words or concepts with similar meanings are placed physically close together in this vector space. This allows the AI to understand "context" and "similarity" rather than just relying on exact keyword matching.

## 2. Vector Databases
*   Traditional SQL databases cannot efficiently search these high-dimensional math coordinates. 
*   We use specialized **Vector Databases** (like Pinecone, Weaviate, or pgvector) to store our embeddings. These databases use **Cosine Similarity** to instantly find which coordinates are closest to each other.

## 3. RAG (Retrieval-Augmented Generation)
*   **The Hallucination Cure:** Because you cannot stop hallucinations using just prompts, RAG shifts the LLM from a *memorization engine* to a *reading comprehension engine*.
*   **The Pipeline:** 
    1. **Ingestion:** You break your Knowledge Base (PDFs, FAQs) into smaller text blocks called **chunks** and store their embeddings in a Vector DB.
    2. **Retrieval:** The user's prompt is embedded, and the Vector DB retrieves the Top-K most relevant chunks via Cosine Similarity.
    3. **Augmentation & Generation:** Those factual chunks are injected into the context window, and the LLM generates an answer strictly based on that retrieved data.
*   **Founder Takeaway:** RAG is incredibly cost-efficient because it prevents you from having to stuff a massive 200,000-token document into the context window for every single user query.

## 4. Fine-Tuning vs. RAG
*   **The Golden Rule:** Use **RAG** for adding changing Knowledge/Facts. Use **Fine-Tuning** for changing Behavior/Tone/Formatting.
*   **Procedural Fine-Tuning:** If you have a strict, multi-step logical or mathematical workflow, you can fine-tune the model on thousands of examples of that workflow. This builds "muscle memory." When the variable inputs change (like a new SI unit), the model flawlessly executes the steps because the *behavior* is locked into its parameters.

## 5. Function Calling (Tool Use) & Structured Outputs
*   **Giving the AI Hands:** An LLM cannot natively click buttons, search the web, or update databases. 
*   **How it works:** You provide the AI with a list of tools. When the AI detects the user's intent (e.g., "Update status to Closed Won"), it does *not* execute the action. Instead, it outputs a hidden, perfectly structured JSON command (e.g., `{"tool": "update_status", "company": "Acme Corp", "status": "Closed Won"}`).
*   **Founder Takeaway:** The LLM acts as the manager making the decision. Your traditional backend software catches the JSON and acts as the worker doing the actual API calls (like updating Salesforce).
