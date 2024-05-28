from typing import Any

from dataclasses_serialization.json import JSONSerializer
from examon_core.models.question_response import QuestionResponse


class Serializer:
    @staticmethod
    def serialize(question_response: QuestionResponse) -> Any:
        return JSONSerializer.serialize(question_response)
