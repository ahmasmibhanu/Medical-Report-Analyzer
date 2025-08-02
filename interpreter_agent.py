from typing import List

class HealthDataInterpreterAgent:
    def __init__(self):
        # Defined some simple normal ranges for common blood values
        self.reference_ranges = {
            "Hemoglobin": (13.5, 17.5),   # g/dL for males
            "WBC": (4.0, 11.0),           # x10^9/L
            "RBC": (4.5, 5.9),            # x10^12/L
            "Platelets": (150, 450),      # x10^9/L
        }

    def interpret(self, raw_text: str) -> List[str]:
        lines = raw_text.splitlines()
        results = []

        for line in lines:
            for marker in self.reference_ranges:
                if marker.lower() in line.lower():
                    # This tries to extract number from line
                    numbers = [float(word.replace(",", "").strip()) for word in line.split() if word.replace(",", "").replace(".", "").isdigit()]
                    if numbers:
                        value = numbers[0]
                        low, high = self.reference_ranges[marker]
                        if value < low:
                            status = "Low"
                        elif value > high:
                            status = "High"
                        else:
                            status = "Normal"
                        results.append(f"{marker}: {value} → {status} (Normal: {low}-{high})")
        return results


# === Quick Test ===
if __name__ == "__main__":
    sample_text = """
    Hemoglobin 11.2 g/dL
    WBC Count 14.5 x10^9/L
    Platelets 220 x10^9/L
    RBC 5.0 x10^12/L
    """
    agent = HealthDataInterpreterAgent()
    interpretation = agent.interpret(sample_text)

    print("\n📊 Interpretation:\n")
    for line in interpretation:
        print(line)
