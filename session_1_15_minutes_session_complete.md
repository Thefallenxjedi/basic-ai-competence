# Session 1: 15-Minute Session Complete (Foundation Layer)

## 1. AI vs. Machine Learning vs. Deep Learning
*   **Artificial Intelligence (AI):** The broadest concept. Getting machines to mimic human intelligence (even using simple "if-then" rules).
*   **Machine Learning (ML):** A subset of AI. Instead of giving the machine rules, we give it data and it learns the patterns on its own.
*   **Deep Learning (DL):** A subset of ML. Uses massive, complex "Neural Networks" inspired by the human brain. Requires enormous data and compute power. Powers modern AI like ChatGPT.
*   **Founder Takeaway:** You don't always need Deep Learning. If you are predicting house prices based on just square footage and bedrooms, standard Machine Learning is the right tool for the job.

## 2. Neurons vs. Parameters
*   **Neurons (Nodes):** The *structure* of the network. Like lightbulbs holding a number.
*   **Parameters (Weights & Biases):** The *connections* between neurons. Think of them as the "dimmer switches" on a massive mixing board. 
*   **Founder Takeaway:** When models like GPT-4 or Llama 3 boast about their size (e.g., "70 Billion Parameters"), they are talking about the number of these tunable dials. **Parameters represent the actual learned "knowledge" of the model.** More parameters generally mean a smarter model, but it also means it is slower and more expensive to run (diminishing returns).

## 3. Training vs. Inference
*   **Training (Going to School):** The process of adjusting those billions of parameters. It requires thousands of GPUs, takes months, and costs millions of dollars. Usually done once upfront.
*   **Inference (Taking the Test):** What happens when a user actually asks the AI a question. The AI uses its finalized parameters to "infer" an answer. It takes seconds and costs fractions of a cent.
*   **Founder Takeaway:** If you use a pre-trained open-source model, you avoid the massive **CapEx (Capital Expenditure)** of Training. Your business only pays for **Inference compute**, which scales with user engagement.

## Vocabulary & Communication Upgrades
*   *Instead of:* "I would be using machine learning terms."
    *Say:* **"We would train a machine learning model on historical features."**
*   *Instead of:* "It would be much lower (slower)... and expensive."
    *Say:* **"A larger model yields higher quality reasoning, but the inference cost and latency will be much higher, potentially hitting a point of diminishing returns."**
*   *Instead of:* "You charge for the cost based on the form they are typing."
    *Say:* **"Our only unit cost is the cloud inference compute, which is based on user input."** (This directly links to "Tokens", our next topic!).
