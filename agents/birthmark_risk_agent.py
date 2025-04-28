from tools.image_reader import read_image
from tools.image_analyzer import analyze_image
from tools.risk_decider import decide_risk_level

class BirthmarkRiskAgent:
    def run(self, image_path):
        print("[Agent] Starting risk analysis...")
        image = read_image(image_path)
        if image is None:
            return "Failed to read image."

        analysis = analyze_image(image)
        risk = decide_risk_level(analysis)
        print("[Agent] Analysis completed.")
        return risk