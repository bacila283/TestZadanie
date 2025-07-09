import datetime


class CarNumber:
    def __init__(self, regno_recognize: str, afts_regno_ai: str, recognition_accuracy: float,
                 afts_regno_ai_score: float, afts_regno_ai_char_scores: str,
                 afts_regno_ai_length_scores: str, camera_type: str,
                 camera_class: str, time_check: datetime, direction: bool):
        self.regno_recognize = regno_recognize
        self.afts_regno_ai = afts_regno_ai
        self.recognition_accuracy = recognition_accuracy
        self.afts_regno_ai_score = afts_regno_ai_score
        self.afts_regno_ai_char_scores = afts_regno_ai_char_scores
        self.afts_regno_ai_length_scores = afts_regno_ai_length_scores
        self.camera_type = camera_type
        self.camera_class = camera_class
        self.time_check = time_check
        self.direction = direction
    
    def get_car_number(self):
        from AIServices.pick_regno import pick_regno
        return pick_regno(self.regno_recognize, 
                   self.afts_regno_ai, 
                   self.recognition_accuracy, 
                   self.afts_regno_ai_score,
                   self.afts_regno_ai_char_scores,
                   self.afts_regno_ai_length_scores,
                   self.camera_type,
                   self.camera_class,
                   self.time_check,
                   self.direction)


