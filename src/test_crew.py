from crew import build_crew

def test():
    """
    Test the crew for one iteration using the GPT-4o model.
    """
    try:
        crew = build_crew()
        inputs = {"data_file": "support_tickets_data.csv"}
        crew.test(n_iterations=1, inputs=inputs, eval_llm='gpt-4o')
        print("Testing completed.")
    except Exception as e:
        print(f"Testing failed: {e}")


if __name__ == "__main__":
    test()
