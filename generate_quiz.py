import re
import json

def parse_markdown():
    with open('/Users/sourabhk/Rag_basics/Basic_ai_competence/100_mcq_review_exam.md', 'r') as f:
        content = f.read()

    # Split into questions and answer key
    parts = content.split('## Answer Key')
    if len(parts) != 2:
        print("Could not find Answer Key section")
        return

    questions_text = parts[0]
    answers_text = parts[1]

    # Parse answers
    answer_key = {}
    for line in answers_text.split('\n'):
        match = re.match(r'^(\d+)\.\s*([A-D])', line.strip())
        if match:
            q_num = int(match.group(1))
            ans = match.group(2)
            answer_key[q_num] = ans

    # Parse questions
    questions = []
    
    # Regex to find questions: e.g. **1. What is...**
    q_pattern = r'\*\*(\d+)\.\s*(.*?)\*\*\n(.*?(?=\n\n\*\*|\Z))'
    
    matches = re.finditer(q_pattern, questions_text, re.DOTALL)
    
    for match in matches:
        q_num = int(match.group(1))
        q_text = match.group(2).strip()
        options_text = match.group(3).strip()
        
        options = []
        for opt_line in options_text.split('\n'):
            opt_line = opt_line.strip()
            if opt_line and re.match(r'^[A-D]\)', opt_line):
                letter = opt_line[0]
                text = opt_line[2:].strip()
                options.append({"id": letter, "text": text})
                
        questions.append({
            "id": q_num,
            "question": q_text,
            "options": options,
            "answer": answer_key.get(q_num, "")
        })

    return questions

def generate_html(questions):
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Founder Interactive Exam</title>
    <style>
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #0f172a;
            color: #f8fafc;
            line-height: 1.6;
            padding: 2rem;
            max-width: 800px;
            margin: 0 auto;
        }
        h1 {
            text-align: center;
            color: #38bdf8;
            margin-bottom: 2rem;
        }
        .progress-container {
            position: sticky;
            top: 0;
            background: #0f172a;
            padding: 1rem 0;
            border-bottom: 1px solid #334155;
            margin-bottom: 2rem;
            z-index: 100;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .progress-text {
            font-weight: bold;
            color: #94a3b8;
        }
        .score {
            font-weight: bold;
            color: #10b981;
        }
        .question-card {
            background: #1e293b;
            border-radius: 12px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }
        .question-text {
            font-size: 1.25rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
            color: #f1f5f9;
        }
        .options {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }
        .option {
            background: #334155;
            border: 2px solid transparent;
            border-radius: 8px;
            padding: 1rem;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
        }
        .option:hover:not(.disabled) {
            background: #475569;
            transform: translateY(-2px);
        }
        .option.disabled {
            cursor: default;
            opacity: 0.8;
        }
        .option.correct {
            background: #064e3b;
            border-color: #10b981;
            color: #fff;
        }
        .option.incorrect {
            background: #7f1d1d;
            border-color: #ef4444;
            color: #fff;
        }
        .option-letter {
            font-weight: bold;
            margin-right: 1rem;
            background: #1e293b;
            color: #38bdf8;
            width: 30px;
            height: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            flex-shrink: 0;
        }
        .option.correct .option-letter, .option.incorrect .option-letter {
            background: transparent;
            color: #fff;
        }
        .feedback {
            margin-top: 1rem;
            font-weight: bold;
            min-height: 24px;
        }
        .feedback.correct { color: #10b981; }
        .feedback.incorrect { color: #ef4444; }
    </style>
</head>
<body>

    <h1>The Ultimate AI Founder Exam</h1>
    
    <div class="progress-container">
        <div class="progress-text">Completed: <span id="completed-count">0</span> / 100</div>
        <div class="score">Score: <span id="score-count">0</span></div>
    </div>

    <div id="quiz-container"></div>

    <script>
        const questions = """ + json.dumps(questions) + """;
        
        let completed = 0;
        let score = 0;

        const container = document.getElementById('quiz-container');
        const completedEl = document.getElementById('completed-count');
        const scoreEl = document.getElementById('score-count');

        questions.forEach((q, index) => {
            const card = document.createElement('div');
            card.className = 'question-card';
            card.id = `q-${q.id}`;
            
            let optionsHtml = '';
            q.options.forEach(opt => {
                optionsHtml += `
                    <div class="option" onclick="selectAnswer(${index}, '${opt.id}', this)">
                        <div class="option-letter">${opt.id}</div>
                        <div class="option-text">${opt.text}</div>
                    </div>
                `;
            });

            card.innerHTML = `
                <div class="question-text">${q.id}. ${q.question}</div>
                <div class="options" id="options-${index}">
                    ${optionsHtml}
                </div>
                <div class="feedback" id="feedback-${index}"></div>
            `;
            container.appendChild(card);
        });

        function selectAnswer(qIndex, selectedId, clickedElement) {
            const q = questions[qIndex];
            const optionsContainer = document.getElementById(`options-${qIndex}`);
            const feedbackEl = document.getElementById(`feedback-${qIndex}`);
            
            // Check if already answered
            if (optionsContainer.classList.contains('answered')) return;
            
            optionsContainer.classList.add('answered');
            completed++;
            
            const isCorrect = selectedId === q.answer;
            if (isCorrect) score++;

            // Update stats
            completedEl.innerText = completed;
            scoreEl.innerText = score;

            // Highlight answers
            const options = optionsContainer.getElementsByClassName('option');
            for (let opt of options) {
                opt.classList.add('disabled');
                const optId = opt.querySelector('.option-letter').innerText;
                
                if (optId === q.answer) {
                    opt.classList.add('correct');
                } else if (optId === selectedId && !isCorrect) {
                    opt.classList.add('incorrect');
                }
            }

            // Show feedback
            if (isCorrect) {
                feedbackEl.innerText = "✅ Correct!";
                feedbackEl.className = "feedback correct";
            } else {
                feedbackEl.innerText = `❌ Incorrect. The right answer was ${q.answer}.`;
                feedbackEl.className = "feedback incorrect";
            }
        }
    </script>
</body>
</html>"""
    
    with open('/Users/sourabhk/Rag_basics/Basic_ai_competence/index.html', 'w') as f:
        f.write(html_template)
    print("Successfully generated index.html")

if __name__ == "__main__":
    qs = parse_markdown()
    if qs:
        generate_html(qs)
