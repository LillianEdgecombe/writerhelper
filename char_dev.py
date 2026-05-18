import urllib.parse
import random
import re

class Character:
    def __init__(self, data=None):
        self.data = data or {
            "Basic Information": {},
            "Physical Description": {},
            "Personality & Psychology": {},
            "Voice & Speech": {},
            "Backstory": "",
            "Portrait URL": ""
        }

    def generate_portrait_url(self):
        appearance = self.data["Physical Description"].get("Appearance", "")
        style = self.data["Physical Description"].get("Style", "")
        genre = self.data["Basic Information"].get("Genre", "")

        prompt = f"Character portrait of a {genre} character, {appearance}, wearing {style}. Cinematic lighting, detailed."
        encoded_prompt = urllib.parse.quote(prompt)
        seed = random.randint(0, 1000000)

        image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&seed={seed}&nologo=true"
        self.data["Portrait URL"] = image_url
        return image_url

    def get_safe_filename(self):
        name = self.data["Basic Information"].get("Name", "Character")
        safe_name = re.sub(r'[^\w\s-]', '', name).strip().lower()
        safe_name = re.sub(r'[-\s]+', '_', safe_name)
        return f"{safe_name if safe_name else 'character'}_profile.md"

    def to_markdown(self):
        name = self.data["Basic Information"].get("Name", "Character")
        md = f"# Character Profile: {name}\n\n"
        if self.data.get("Portrait URL"):
            md += f"![Character Portrait]({self.data['Portrait URL']})\n\n"

        for section, content in self.data.items():
            if isinstance(content, dict):
                md += f"## {section}\n"
                for key, value in content.items():
                    md += f"- **{key}:** {value}\n"
                md += "\n"
            elif section != "Portrait URL":
                md += f"## {section}\n"
                md += f"{content}\n\n"
        return md

class CharacterDeveloperCLI:
    def __init__(self):
        self.character = Character()

    def ask_question(self, section, key, prompt, default=""):
        value = input(f"{prompt} [{default}]: ").strip()
        if not value:
            value = default
        self.character.data[section][key] = value

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
        self.character.data["Backstory"] = backstory

    def run(self):
        print("Welcome to the Character Developer Tool!")
        self.develop_basic_info()
        self.develop_physical_description()
        self.develop_personality()
        self.develop_voice()
        self.develop_backstory()

        print("\n--- Generating Character Portrait ---")
        url = self.character.generate_portrait_url()
        print(f"Portrait URL: {url}")

        filename = self.character.get_safe_filename()
        print(f"\n--- Exporting Character Profile to {filename} ---")
        with open(filename, "w") as f:
            f.write(self.character.to_markdown())

        print(f"Profile exported successfully to {filename}")
        print("\nCharacter profile completed and exported!")

if __name__ == "__main__":
    dev = CharacterDeveloperCLI()
    dev.run()
