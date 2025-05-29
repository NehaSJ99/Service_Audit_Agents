from crew import build_crew

def train():
    """
    Train the crew for one iteration and save the output to a file.
    """
    try:
        crew = build_crew()
        inputs = {
            "topic": "AI LLMs"  # Update as per your actual inputs
        }
        crew.train(n_iterations=1, filename='training.pkl', inputs=inputs)
        print("Training completed and saved to training.pkl.")
    except Exception as e:
        print(f"Training failed: {e}")

if __name__ == "__main__":
    train()