from json import load


class Candidate:
    def __init__(self, path: str):
        self.path = path

    def load_candidates_from_json(self) -> list[dict]:
        with open(self.path, encoding='utf-8') as file:
            return load(file)

    def get_candidate_by_id(self, candidate_id: int) -> dict | None:
        for candidate in self.load_candidates_from_json():
            if candidate['id'] == candidate_id:
                return candidate

    def search_candidates_by_name(self, name_candidate: str) -> list[dict]:
        answer = []
        for candidate in self.load_candidates_from_json():
            if name_candidate.lower() in candidate['name'].lower():
                answer.append(candidate)
        return answer

    def search_candidates_by_skill(self, name_skill: str) -> list[dict]:
        answer = []
        for candidate in self.load_candidates_from_json():
            if name_skill.lower() in candidate['skills'].lower():
                answer.append(candidate)
        return answer
