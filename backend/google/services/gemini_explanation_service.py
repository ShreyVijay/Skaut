from google.providers.google_providers import GoogleGeminiProvider
from google.schemas.provider_dtos import ExplanationDTO

class GeminiExplanationService:
    def __init__(self):
        self.provider = GoogleGeminiProvider()

    def get_recommendation_explanation(
        self,
        recommendation: dict,
        reasoning: dict,
        audit: dict,
    ) -> ExplanationDTO:
        return self.provider.generate_explanation(
            recommendation,
            reasoning,
        audit,
    )

    def get_travel_narrative(
        self,
        route_data: dict,
        recommendation: dict,
    ) -> ExplanationDTO:
        return self.provider.generate_travel_narrative(
            route_data,
            recommendation,
        )

    def generate(self, prompt: str) -> str:
        if hasattr(self.provider, "generate_text"):
            return self.provider.generate_text(prompt)

        if hasattr(self.provider, "chat"):
            return self.provider.chat(prompt)

        if hasattr(self.provider, "generate"):
            return self.provider.generate(prompt)

        raise AttributeError(
            "GoogleGeminiProvider does not expose generate_text, chat, or generate"
        )