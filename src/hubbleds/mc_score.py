from pydantic import Field
from typing import Dict

from .generic_question_model import GenericQuestion, GenericContainer

class MCScore(GenericQuestion):
    tag: str = ""
    score: int | None = None
    choice: int | None = None
    tries: int = 0
    wrong_attempts: int = 0
    stage: str | float = ''
    
    # not required but is useful for debugging/introspection
    def update(self, score: int, choice: int, tries: int, wrong_attempts: int):
        super().update(score = score, choice = choice, tries = tries, wrong_attempts = wrong_attempts)
    
    @property
    def completed(self):
        return (self.score is not None) and (self.score >  -1)
 
    
    
# Score Containers
class MCScoring(GenericContainer[MCScore]):
    scores: Dict[str, MCScore] = Field(default_factory = dict)
    _item_attribute_name: str = "scores"
    
    def add(self, tag: str) -> MCScore:
        return self.add_item(tag, MCScore)
    
    def get_or_create(self, tag: str) -> MCScore:
        return self.get_or_create_item(tag, MCScore)  
    
    def update_mc_score(self, tag: str, score: int, choice: int, tries: int, wrong_attempts: int):
        super().update_item(tag, score = score, choice = choice, tries = tries, wrong_attempts = wrong_attempts)
        
 