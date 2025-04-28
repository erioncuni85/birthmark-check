from agents.birthmark_risk_agent import BirthmarkRiskAgent

def main():
    agent = BirthmarkRiskAgent()
    image_path = "sample_birthmark.jpg"  # make sure you have a sample image
    risk_level = agent.run(image_path)
    print(f"Result: {risk_level}")

if __name__ == "__main__":
    main()

# from agents.birthmark_openai_agent import BirthmarkOpenAIAgent
#
#
# def main():
#     agent = BirthmarkOpenAIAgent()
#     image_description = "A large irregularly shaped dark mole with uneven edges and multiple colors."
#     risk_assessment = agent.run(image_description)
#     print(f"Risk Assessment: {risk_assessment}")
#
#
# if __name__ == "__main__":
#     main()