"""
GPT vs GPM vs GPH - Educational Game
Flask application with improved game logic and comprehensive concept coverage
"""

from flask import Flask, render_template, jsonify, request
import random
import json

app = Flask(__name__)

class TextGenerator:
    """Generates text based on different model types"""
    
    def __init__(self):
        # Markov chain transitions
        self.markov_map = {
            'the': ['cat', 'dog', 'house', 'man', 'tree', 'bird'],
            'cat': ['ran', 'jumped', 'slept', 'meowed', 'sat'],
            'dog': ['barked', 'ran', 'ate', 'slept', 'played'],
            'on': ['the', 'a', 'top', 'fire', 'monday'],
            'sat': ['down', 'there', 'quietly', 'on', 'still'],
            'in': ['the', 'a', 'silence', 'winter', 'spring'],
            'was': ['a', 'the', 'not', 'very', 'quite'],
            'a': ['cat', 'dog', 'house', 'tree', 'bird', 'man'],
            'and': ['the', 'a', 'then', 'but', 'so'],
            'default': ['and', 'but', 'the', 'very', 'quite', 'then']
        }
    
    def generate_gpm(self, prompt):
        """GPM: Only remembers last 1-2 words, loses coherence quickly"""
        words = prompt.strip().split()
        result = prompt
        
        for i in range(random.randint(8, 12)):
            last_word = words[-1].lower().strip('.,!?')
            options = self.markov_map.get(last_word, self.markov_map['default'])
            next_word = random.choice(options)
            result += ' ' + next_word
            words.append(next_word)
        
        return result
    
    def generate_gpt(self, prompt):
        """GPT: Maintains context and coherence throughout"""
        prompt_lower = prompt.lower()
        
        # Context-aware completions
        templates = {
            'cat': [
                " mat and began grooming itself contentedly. The afternoon sunlight streamed through the window, creating a warm spot that the cat had claimed as its own.",
                " comfortable cushion, watching the world go by. It had perfected the art of relaxation, a skill that took years of dedicated practice.",
                " windowsill, observing the birds outside with great interest. Its tail swished rhythmically as it calculated the distance to its prey."
            ],
            'dog': [
                " park, wagging its tail excitedly as children played nearby. The happy dog loved these afternoon outings with its owner.",
                " grass and rolled over, seeking belly rubs from anyone who would oblige. Life was simple and good for this friendly canine.",
                " porch, keeping watch over the neighborhood. Every passing car and pedestrian was carefully noted and assessed."
            ],
            'scientist': [
                " laboratory bench, carefully examining the experimental results. The data suggested a breakthrough that could revolutionize the field.",
                " whiteboard, sketching out equations that represented months of theoretical work. Colleagues gathered around, discussing the implications."
            ],
            'once': [
                " upon a time, in a land far away, there lived a curious explorer who dreamed of discovering new worlds.",
                " the decision was made, there was no turning back. The team had committed to a path that would change everything."
            ],
            'default': [
                " beautiful morning when everything seemed possible. The world was full of opportunities waiting to be discovered.",
                " moment of clarity when all the pieces finally came together. Understanding dawned like sunrise breaking through clouds.",
                " journey that would test resolve and determination. But with careful planning and persistence, success was within reach."
            ]
        }
        
        # Find matching template
        for keyword, completions in templates.items():
            if keyword in prompt_lower:
                return prompt + random.choice(completions)
        
        return prompt + random.choice(templates['default'])
    
    def generate_gph(self, prompt):
        """GPH: Rich context, personal memories, metaphors, emotional depth"""
        prompt_lower = prompt.lower()
        
        # Human-like completions with personal experience and metaphor
        templates = {
            'cat': [
                " mat—a familiar throne from which she surveyed her kingdom. I remember my grandmother had a cat just like this, always choosing the sunniest spot with the wisdom of a creature who understood comfort on a profound level. There's something timeless about cats, isn't there?",
                " windowsill, and I was transported back to my childhood home. We had a tabby named Whiskers who would sit exactly like this, contemplating the mysteries of the universe—or perhaps just planning her next nap. Animals have this way of teaching us presence."
            ],
            'dog': [
                " beach, and watching him made me think about pure joy. Dogs have this incredible ability to live completely in the moment—something we humans spend years of meditation trying to achieve. That unbridled happiness, that's real wisdom.",
                " trail, and I couldn't help but reflect on loyalty and companionship. My father always said you could judge a person's character by how their dog behaved. There's a profound truth in that—dogs reflect back our own capacity for love."
            ],
            'scientist': [
                " crossroads between curiosity and discovery. You know, being a scientist isn't just about data and experiments—it's about maintaining childlike wonder while wielding adult rigor. My mentor once told me that every equation is a poem written in the language of the universe.",
                " edge of understanding, that thrilling and terrifying space where knowledge meets the unknown. Science is fundamentally human—driven by our deep need to make sense of our existence, to find patterns in chaos."
            ],
            'once': [
                " upon a time... those four words unlock something primal in us, don't they? We're storytelling creatures, building meaning through narrative. I think about how my children's eyes would light up when I'd start a story that way—that anticipation of possibility.",
                " the path seemed clear, but life has this way of revealing complexity where we expected simplicity. That's the human experience, isn't it? Navigating uncertainty with nothing but hope, memory, and the stories we tell ourselves."
            ],
            'default': [
                " journey of discovery, and thinking about it now, I'm reminded of what my teacher told me when I was young: 'Every ending is just another beginning dressed up.' Humans don't just predict the future—we create meaning from experience, weaving past and present into something new.",
                " threshold between what was and what could be. You know, there's this beautiful Japanese concept—'ma'—the space between things. It's in these pauses that we find meaning, where imagination lives and breathes."
            ]
        }
        
        for keyword, completions in templates.items():
            if keyword in prompt_lower:
                return prompt + random.choice(completions)
        
        return prompt + random.choice(templates['default'])

# Initialize generator
generator = TextGenerator()

# Game state storage (in production, use a database)
game_sessions = {}

@app.route('/')
def index():
    """Main game page"""
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate():
    """Generate text from a random model for the challenge"""
    data = request.json
    prompt = data.get('prompt', 'The cat sat on the')
    
    # Randomly select a model (this is hidden from the user)
    model = random.choice(['gpt', 'gpm', 'gph'])
    
    # Generate text
    if model == 'gpm':
        text = generator.generate_gpm(prompt)
    elif model == 'gpt':
        text = generator.generate_gpt(prompt)
    else:  # gph
        text = generator.generate_gph(prompt)
    
    # Create session
    session_id = str(random.randint(100000, 999999))
    game_sessions[session_id] = {
        'model': model,
        'prompt': prompt,
        'text': text
    }
    
    return jsonify({
        'session_id': session_id,
        'text': text
    })

@app.route('/api/guess', methods=['POST'])
def guess():
    """Check if the user's guess is correct"""
    data = request.json
    session_id = data.get('session_id')
    guessed_model = data.get('model')
    
    if session_id not in game_sessions:
        return jsonify({'error': 'Invalid session'}), 400
    
    session = game_sessions[session_id]
    correct = session['model'] == guessed_model
    
    # Get detailed explanation
    explanation = get_explanation(session['model'], session['text'])
    
    return jsonify({
        'correct': correct,
        'actual_model': session['model'],
        'explanation': explanation
    })

@app.route('/api/concepts')
def get_concepts():
    """Return all concepts from the comparison table"""
    concepts = {
        'Context Window': {
            'GPT': 'Thousands of tokens of prior text',
            'GPM': 'Last 1-3 words only',
            'GPH': 'Flexible memory span; can recall both short and long contexts',
            'analogy': 'GPT: remembering the whole conversation. GPM: remembering only the last word. GPH: recalling both the last sentence AND a story from childhood.'
        },
        'Tokenization': {
            'GPT': 'Splits into subword units',
            'GPM': 'Works only at word level',
            'GPH': 'Works with words, meanings, metaphors, and symbols',
            'analogy': 'GPT: "bio-" + "-logy." GPM: only exact "biology." GPH: understands "life study" as meaning "biology."'
        },
        'Parameters': {
            'GPT': 'Billions of learned weights encode patterns',
            'GPM': 'Transition counts only',
            'GPH': 'Billions of neurons and synapses adaptively encoding experiences',
            'analogy': 'GPT: vast associative memory. GPM: tally marks. GPH: lived experiences stored in neural networks.'
        },
        'Training Objective': {
            'GPT': 'Predict next token, minimize error',
            'GPM': 'Count and normalize co-occurrences',
            'GPH': 'Learn from environment, feedback, trial, error, reflection',
            'analogy': 'GPT: essay practice. GPM: memorizing a text. GPH: learning language from parents, teachers, and peers.'
        },
        'Attention Mechanism': {
            'GPT': 'Weighs relationships across whole context',
            'GPM': 'None; only local adjacency',
            'GPH': 'Flexible focus; can zoom in on details or zoom out to themes',
            'analogy': 'GPT: linking far-apart ideas. GPM: noticing last word only. GPH: following a complex story arc.'
        },
        'Embeddings / Representation': {
            'GPT': 'Vector space of meaning',
            'GPM': 'No embeddings: words are symbols',
            'GPH': 'Rich conceptual network including senses, emotions, and context',
            'analogy': 'GPT: "king" ~ "queen." GPM: "king" = "banana." GPH: "king" evokes power, history, crown, responsibility.'
        },
        'Generativity': {
            'GPT': 'Produces novel text',
            'GPM': 'Recombines fragments, often incoherently',
            'GPH': 'Produces novel ideas, metaphors, inventions',
            'analogy': 'GPT: new joke. GPM: shuffled punchlines. GPH: invents humor, irony, poetry.'
        },
        'Coherence Across Sentences': {
            'GPT': 'Maintains topic and logic across paragraphs',
            'GPM': 'Collapses quickly',
            'GPH': 'Maintains coherence across conversations, days, years',
            'analogy': 'GPT: consistent essay. GPM: nonsense after 2-3 lines. GPH: consistent worldview across decades.'
        },
        'Knowledge Storage': {
            'GPT': 'Stored in billions of weights',
            'GPM': 'None; just word transitions',
            'GPH': 'Stored in memory, language, culture, experience',
            'analogy': 'GPT: encoded in parameters. GPM: surface-level mimicry. GPH: lived and embodied knowledge.'
        }
    }
    return jsonify(concepts)

def get_explanation(model, text):
    """Generate explanation based on the model characteristics"""
    explanations = {
        'gpt': {
            'clues': [
                'Maintains coherent narrative throughout',
                'References earlier context in the prompt',
                'Logical flow and thematic consistency',
                'Uses attention to link ideas across the text',
                'Novel but predictable continuation'
            ],
            'description': 'GPT maintains context across thousands of tokens, using its attention mechanism to weigh relationships throughout the entire prompt. The completion is coherent, stays on topic, and demonstrates understanding of the full context.'
        },
        'gpm': {
            'clues': [
                'Loses coherence after a few words',
                'Only considers the last 1-2 words',
                'Random-seeming word associations',
                'No awareness of earlier context',
                'Degrades into word salad quickly'
            ],
            'description': 'GPM (Markov Chain) only remembers the last word or two. It has no attention mechanism and cannot maintain context. Each word is chosen based solely on what came immediately before, leading to rapid degradation of meaning.'
        },
        'gph': {
            'clues': [
                'Includes personal memories or experiences',
                'Uses metaphors and rich imagery',
                'Reflects emotional depth',
                'Questions and philosophical musings',
                'References culture, history, or relationships',
                'Self-awareness and metacognition'
            ],
            'description': 'GPH (Human) draws from lived experience, creating meaning through personal memory, cultural knowledge, and emotional understanding. Humans don\'t just predict—they create metaphors, question, reflect, and weave past experiences into present expression.'
        }
    }
    return explanations.get(model, {})

@app.route('/api/quiz')
def quiz():
    """Get a concept quiz question"""
    concepts = [
        {
            'question': 'Which model can remember a conversation from last week?',
            'options': ['GPT', 'GPM', 'GPH'],
            'correct': 'GPH',
            'explanation': 'Humans (GPH) have flexible long-term memory spanning years. GPT has a context window of thousands of tokens (current conversation only). GPM only remembers 1-3 words.'
        },
        {
            'question': 'Which model understands "H₂O" means water at multiple levels (chemical, cultural, experiential)?',
            'options': ['GPT', 'GPM', 'GPH'],
            'correct': 'GPH',
            'explanation': 'Humans have rich conceptual networks including senses, emotions, and context. GPT has vector embeddings. GPM treats words as mere symbols.'
        },
        {
            'question': 'Which model would generate "the cat sat on the fire and but very then"?',
            'options': ['GPT', 'GPM', 'GPH'],
            'correct': 'GPM',
            'explanation': 'Markov chains (GPM) only look at the last word, leading to incoherent word salad. They collapse into nonsense within 2-3 words.'
        },
        {
            'question': 'Which model uses an attention mechanism to weigh relationships across the entire input?',
            'options': ['GPT', 'GPM', 'GPH'],
            'correct': 'GPT',
            'explanation': 'GPT\'s transformer architecture uses attention to link ideas across the whole context. GPM has no attention (only local adjacency). GPH has flexible focus but different mechanisms.'
        },
        {
            'question': 'Which model learns through trial, error, feedback, and reflection?',
            'options': ['GPT', 'GPM', 'GPH'],
            'correct': 'GPH',
            'explanation': 'Humans learn from lived experience through complex processes including feedback and reflection. GPT learns by predicting next tokens. GPM just counts co-occurrences.'
        },
        {
            'question': 'Which model stores knowledge in billions of trained weights?',
            'options': ['GPT', 'GPM', 'GPH'],
            'correct': 'GPT',
            'explanation': 'GPT stores patterns in billions of learned parameters. GPM has no knowledge storage (just transition counts). GPH stores knowledge in memory, language, and culture.'
        },
        {
            'question': 'If shown "king" which model would think of power, history, crown, and responsibility?',
            'options': ['GPT', 'GPM', 'GPH'],
            'correct': 'GPH',
            'explanation': 'Humans have rich conceptual networks with sensory, emotional, and cultural associations. GPT has semantic embeddings ("king" ~ "queen"). GPM treats "king" as just another symbol.'
        },
        {
            'question': 'Which model can split "biology" into "bio-" and "-logy"?',
            'options': ['GPT', 'GPM', 'GPH'],
            'correct': 'GPT',
            'explanation': 'GPT uses subword tokenization to handle word pieces. GPM works only at word level. GPH understands meanings and can decompose concepts flexibly.'
        }
    ]
    
    return jsonify(random.choice(concepts))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5010)