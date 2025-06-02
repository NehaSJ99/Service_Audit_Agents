# Support Data Insights Analysis

This repository contains a modular multi-agent system for analyzing customer support ticket data using [CrewAI](https://crewai.com/). It leverages role-specific agents to generate actionable insights, performance reports, and visual charts for business intelligence and decision-making.

---

## Key Features

- **Modular CrewAI architecture** using YAML for agent and task configuration.
- **Agents** for:
  - Suggestion generation from historical tickets.
  - Performance and satisfaction reporting.
  - Chart creation and visualizations.
- **Custom Tooling** for intelligent CSV data querying using `pandas`.
- **Training and Testing** support using `crew.train()` and `crew.test()` methods.
- **Visual Outputs** saved automatically into the `outputs/` directory.

---

## Architecture

![System Architecture](image.png)

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/NehaSJ99/Service_Audit_Agents.git
   ```

2. **Create and activate a virtual environment**
   ```bash
   conda create -p venv python==3.10 -y
   conda activate venv
   ```

3. **Install dependencies**
   ```bash
   pip install -e .
   ```

4. **Add your OpenAI API key**
  Create a `.env` file in the root directory:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

---

## Running the Project

1. **To generate the report using the Crew**
   ```bash
   python src/main.py
   ```

2. **To test the Crew setup**
   ```bash
   python src/test_crew.py
   ```
3. **To train the Crew setup**
   ```bash
   python src/train_crew.py
   ```

---

## Output

- The agent-generated visual charts will be saved in the `outputs/` directory. Make sure doker is installed to execute code and save output images into output directory.
- The final report is composed dynamically from CSV data, insights, and images.

---

## Notes

- This system is designed to be easily extendable. You can modify agents, tasks, and tools by editing the YAML files and `crew.py`.
- Uses CrewAI v0.28.8+ and follows its best practices for memory, task dependencies, and modular testing.

---

## License

MIT License
