# 🧠 GPT vs GPM vs GPH - Educational Game

An interactive educational game that teaches the differences between three text generation approaches:
- **GPT** (Generative Pretrained Transformer) - Modern AI using attention mechanisms
- **GPM** (Generative Pretrained Markov Chain) - Simple probabilistic model  
- **GPH** (Generative Pretrained Human) - Human cognition and thinking

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-Educational-purple.svg)](LICENSE)

## 🎮 Live Demo

Try the game at: `http://127.0.0.1:5000` (after running locally)

## ✨ Features

### 🎯 Challenge Mode
- A random model generates text completion
- You guess which model created it
- Get detailed explanations of the clues
- Track your accuracy over time

### 📚 Learn Concepts
- Complete comparison table covering 9 key concepts:
  - Context Window, Tokenization, Parameters
  - Training Objective, Attention Mechanism
  - Embeddings/Representation, Generativity
  - Coherence, Knowledge Storage
- Visual analogies for each concept

### ❓ Concept Quiz
- Test your understanding with targeted questions
- Immediate feedback with explanations
- Reinforces key differences

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/gpt-vs-gpm-vs-gph-game.git
   cd gpt-vs-gpm-vs-gph-game
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python flask-game-app.py
   ```

4. **Open your browser**
   Navigate to `http://127.0.0.1:5000`

### Using Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python flask-game-app.py
```

## 🎲 How to Play

### Challenge Mode
1. Enter a prompt (or use the default "The cat sat on the")
2. Click "Generate Mystery Text"
3. Read the generated completion carefully
4. Look for clues:
   - **GPM**: Loses coherence, random word associations, considers only last word
   - **GPT**: Coherent narrative, maintains context, logical flow
   - **GPH**: Personal memories, metaphors, emotional depth, questions
5. Click your guess (GPT, GPM, or GPH)
6. Learn from the detailed explanation
7. Try another challenge!

### Learn Concepts
- Browse through all 9 key concepts
- See side-by-side comparisons
- Understand with helpful analogies

### Concept Quiz
- Answer multiple-choice questions
- Get instant feedback
- Deepen your understanding

## 🎓 Learning Objectives

Students will learn:

1. **Context Window**: How different models "remember" information
2. **Tokenization**: How models break down and process text
3. **Attention Mechanism**: Why GPT can link distant concepts
4. **Coherence**: Why Markov chains produce gibberish
5. **Human Cognition**: What makes human thinking unique (metaphors, memory, emotion)
6. **Practical Recognition**: Identify model outputs in real scenarios

## 🧠 Educational Value

This game teaches:
- Fundamental concepts in NLP and AI
- Differences between statistical and neural approaches
- Human cognitive capabilities vs AI limitations
- Critical thinking about AI-generated content
- Pattern recognition and analytical skills

## 🛠️ Project Structure

```
gpt-vs-gpm-vs-gph-game/
├── flask-game-app.py          # Main Flask application
├── requirements.txt           # Python dependencies
├── README.md                 # This file
├── .gitignore               # Git ignore rules
└── templates/
    └── index.html           # Web interface
```

## 🔧 Customization

### Adding More Prompts
Edit the templates in `flask-game-app.py` in the `generate_gpt()` and `generate_gph()` methods to add more context-aware completions.

### Adding Quiz Questions
Add more questions in the `quiz()` function in `flask-game-app.py`.

### Styling
Modify the CSS in `templates/index.html` to change colors, layouts, and appearance.

## 🐛 Troubleshooting

**Port already in use:**
```bash
# Change the port in flask-game-app.py
app.run(debug=True, port=5001)
```

**Flask not found:**
```bash
pip install --upgrade flask
```

**Template not found:**
Ensure `index.html` is in a folder named `templates` in the same directory as `flask-game-app.py`.

## 🚀 Future Enhancements

Potential additions:
- Leaderboard system
- Multiple difficulty levels
- More detailed statistical analysis
- Export learning progress
- Multiplayer mode
- Integration with real language models

## 📄 License

This educational game is provided for teaching purposes.

## 👨‍🏫 Credits

Based on the comparison table by Joaquin Carbonara (10/4/2025)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Have fun learning about AI and human cognition!** 🧠🤖👨‍🎓
