from ocr_agent import OCRParserAgent
from interpreter_agent import HealthDataInterpreterAgent
from summary_agent import SummaryGeneratorAgent

def run_pipeline(image_path: str):
    print("\n🧠 Step 1: Extracting Text from Report Image...")
    ocr_agent = OCRParserAgent()
    raw_text = ocr_agent.extract_text_from_image(image_path)
    print(raw_text)

    print("\n🔍 Step 2: Interpreting Medical Values...")
    interpreter = HealthDataInterpreterAgent()
    interpretation = interpreter.interpret(raw_text)
    for item in interpretation:
        print(f"• {item}")

    print("\n🗣️ Step 3: Generating Summary for Patient...")
    summarizer = SummaryGeneratorAgent()
    summary = summarizer.generate_summary(interpretation)

    print("\n💬 Final Report Summary:\n")
    print(summary)


# === Run Pipeline ===
if __name__ == "__main__":
    image_path = "images/Sample_1.png"  # Change it if needed
    run_pipeline(image_path)