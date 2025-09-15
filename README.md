# AI Manim Knowledge Graph Generator

## Description
This project demonstrates an AI-assisted system for generating educational content. Users can input a concept, and the system:

- Retrieves the definition from a **knowledge graph**.
- Generates an explanatory **script** using a pre-trained AI model.
- Produces **slide-like summaries**.
- Optionally creates **animations using Manim**.

> **Note:** Sadly, I didn't got much time to understand, learn and do the project on my own. I took assistance of chatgpt for it and don't want to take credits for coding. Will learn the concepts to make it on my own next time!
---

## Pseudocode

1. **Start**  
   Ask the user to enter a concept they want to learn about (e.g., “Stack”).

2. **Look it up**  
   Check the knowledge graph for the concept and get its definition.  
   - If the concept is not found, tell the user “Concept not found.”

3. **Generate script**  
   Use the AI model to create an easy-to-understand explanation of the concept.

4. **Generate slides**  
   Create a short slide-like summary including:  
   - Title  
   - Definition  
   - Key points

5. **Save outputs**  
   Store the script and slides in the `output` folder so they can be accessed later.

6. **Optional animation**  
   If needed, generate a visual animation using Manim to illustrate the concept.

```powershell
manim -pql src\manim_generator.py ConceptAnimation
```


7. **Done**  
   Show the generated script and slides to the user.

---

## How to Run

```powershell
# Activate virtual environment
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the pipeline
python main.py
# Enter a concept when prompted, e.g., "Stack"

# Optional: Generate animation
manim -pql src\manim_generator.py ConceptAnimation

##How to Run
.\venv\Scripts\activate
pip install -r requirements.txt
python main.py
Enter a concept when prompted, e.g., Stack
Optional: manim -pql src\manim_generator.py ConceptAnimation
