import subprocess
import settings

class OllamaClient:

    @staticmethod
    def chat(prompt):
        result = subprocess.run(
            ["ollama", "run", settings.MODEL_NAME, prompt],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            raise Exception(result.stderr.strip() or "Failed to get Ollama response")

        return result.stdout.strip()