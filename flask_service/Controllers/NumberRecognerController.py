from flask import Blueprint, request, jsonify
from datetime import datetime
from DataModels.CarNumber import CarNumber

webapi_number_recogner = Blueprint("number_recogner", __name__)
@webapi_number_recogner.route('/numberrecogner/recogn', methods=['POST'])
def Do_recogn():
    try:
        data = request.json
        _car_number_item = CarNumber(
            regno_recognize=data['regno_recognize'],
            afts_regno_ai=data['afts_regno_ai'],
            recognition_accuracy=data['recognition_accuracy'],
            afts_regno_ai_score=data['afts_regno_ai_score'],
            afts_regno_ai_char_scores=data['afts_regno_ai_char_scores'],
            afts_regno_ai_length_scores=data['afts_regno_ai_length_scores'],
            camera_type=data['camera_type'],
            camera_class=data['camera_class'],
            time_check=datetime.strptime(data['time_check'], "%Y-%m-%d %H:%M:%S"),
            direction=bool(data['direction'])
)


        result = CarNumber.get_car_number(_car_number_item)
        return jsonify(
                {
                    "Result":{
                        "max": result[0],
                        "min": result[1]
                        }
                }), 200
        

    except Exception as e:
        print(str(e))
        return jsonify({"error": f"Ошибка записи: {str(e)}"}), 400