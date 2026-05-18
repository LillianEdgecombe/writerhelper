import urllib.parse
import random
import re

class CharacterDeveloper:
    def __init__(self):
        self.character_data = {
            "Basic Information": {},
            "Physical Description": {},
            "Personality & Psychology": {},
            "Voice & Speech": {},
            "Backstory": "",
            "Portrait URL": ""
        }

    def ask_question(self, section, key, prompt, default=""):
        value = input(f"{prompt} [{default}]: ").strip()
        if not value:
            value = default
        self.character_data[section][key] = value

    def develop_basic_info(self):
        print("\n--- Basic Information ---")
        self.ask_question("Basic Information", "Name", "What is your character's name?")
        self.ask_question("Basic Information", "Gender", "What is their gender?")
        self.ask_question("Basic Information", "Genre", "What is the story genre?")
        self.ask_question("Basic Information", "Role", "What is their role in the story (e.g., Protagonist, Antagonist, Sidekick)?")

    def develop_physical_description(self):
        print("\n--- Physical Description ---")
        self.ask_question("Physical Description", "Age", "How old is the character?")
        self.ask_question("Physical Description", "Appearance", "Describe their physical appearance (height, hair, eyes, etc.)")
        self.ask_question("Physical Description", "Style", "What is their style of dress?")

    def develop_personality(self):
        print("\n--- Personality & Psychology ---")
        self.ask_question("Personality & Psychology", "Goal", "What is their primary goal?")
        self.ask_question("Personality & Psychology", "Fear", "What is their greatest fear?")
        self.ask_question("Personality & Psychology", "Flaw", "What is their biggest flaw?")

    def develop_voice(self):
        print("\n--- Voice & Speech ---")
        self.ask_question("Voice & Speech", "Tone", "Describe the tone of their voice (e.g., raspy, melodic, booming)")
        self.ask_question("Voice & Speech", "Cadence", "Describe their speech cadence (e.g., fast-talker, slow and deliberate)")
        self.ask_question("Voice & Speech", "Phrases", "Are there any unique phrases or catchphrases they use?")

    def develop_backstory(self):
        print("\n--- Backstory ---")
        backstory = input("Briefly summarize their backstory: ").strip()
        self.character_data["Backstory"] = backstory

    def generate_portrait(self):
        print("\n--- Generating Character Portrait ---")
        appearance = self.character_data["Physical Description"].get("Appearance", "")
        style = self.character_data["Physical Description"].get("Style", "")
        genre = self.character_data["Basic Information"].get("Genre", "")

        prompt = f"Character portrait of a {genre} character, {appearance}, wearing {style}. Cinematic lighting, detailed."
        encoded_prompt = urllib.parse.quote(prompt)
        seed = random.randint(0, 1000000)

        image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&seed={seed}&nologo=true"

        print(f"Portrait URL: {image_url}")
        self.character_data["Portrait URL"] = image_url
        print("Portrait generated successfully!")

    def export_profile(self):
        name = self.character_data["Basic Information"].get("Name", "Character")
        # Sanitize filename
        safe_name = re.sub(r'[^\w\s-]', '', name).strip().lower()
        safe_name = re.sub(r'[-\s]+', '_', safe_name)
        filename = f"{safe_name if safe_name else 'character'}_profile.md"

        print(f"\n--- Exporting Character Profile to {filename} ---")

        with open(filename, "w") as f:
            f.write(f"# Character Profile: {name}\n\n")
            f.write(f"![Character Portrait]({self.character_data['Portrait URL']})\n\n")

            for section, data in self.character_data.items():
                if isinstance(data, dict):
                    f.write(f"## {section}\n")
                    for key, value in data.items():
                        f.write(f"- **{key}:** {value}\n")
                    f.write("\n")
                elif section != "Portrait URL":
                    f.write(f"## {section}\n")
                    f.write(f"{data}\n\n")

        print(f"Profile exported successfully to {filename}")

    def run(self):
        print("Welcome to the Character Developer Tool!")
        self.develop_basic_info()
        self.develop_physical_description()
        self.develop_personality()
        self.develop_voice()
        self.develop_backstory()
        self.generate_portrait()
        self.export_profile()

        print("\nCharacter profile completed and exported!")

if __name__ == "__main__":
    dev = CharacterDeveloper()
    dev.run()
