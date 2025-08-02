from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

class SummaryGeneratorAgent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_summary(self, interpreted_data: list) -> str:
        if not interpreted_data:
            return "No medical data to summarize."

        prompt = (
            "You're a friendly medical assistant. Explain the following results to a patient in plain language:\n\n"
            + "\n".join(interpreted_data)
            + "\n\nKeep it concise and easy to understand."
        )

        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )

        return response.choices[0].message.content.strip()


# === Quick Test ===
if __name__ == "__main__":
    test_data = [
        "Hemoglobin: 11.2 → Low (Normal: 13.5–17.5)",
        "WBC: 14.5 → High (Normal: 4.0–11.0)",
        "Platelets: 220.0 → Normal (Normal: 150–450)",
        "RBC: 5.0 → Normal (Normal: 4.5–5.9)"
    ]

    generator = SummaryGeneratorAgent()
    summary = generator.generate_summary(test_data)

    print("\n🗣️ Patient-Friendly Summary:\n")
    print(summary)
