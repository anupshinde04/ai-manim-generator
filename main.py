from src.backend import run_pipeline

if __name__ == "__main__":
    concept = input("Enter concept name: ")
    script, slides = run_pipeline(concept)
    print("\nGenerated Script:\n", script)
    print("\nGenerated Slides:\n", slides)
