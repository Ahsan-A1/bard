class PromptBuilder:
    def build_turn_prompt(self, story_id: str, action: str) -> str:
        raise NotImplementedError

    def build_bootstrap_prompt(self, base_prompt: str) -> str:
        raise NotImplementedError
