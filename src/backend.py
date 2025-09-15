from src.knowledge_graph import load_graph, query_concept
from src.ai_module import generate_script, generate_slides
from src.formatter import format_script, format_slides

def run_pipeline(concept):
    G = load_graph()
    content = query_concept(G, concept)
    
    script = generate_script(concept, content)
    slides = generate_slides(concept, content)
    
    formatted_script = format_script(script)
    formatted_slides = format_slides(slides)
    
    # Windows-safe UTF-8 writing
    with open(f"output/scripts/{concept}.txt", "w", encoding="utf-8") as f:
        f.write(formatted_script)
    with open(f"output/slides/{concept}.md", "w", encoding="utf-8") as f:
        f.write(formatted_slides)
    
    print("✅ Script and slides generated.")
    return formatted_script, formatted_slides
