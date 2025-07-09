from catboost import CatBoostClassifier

model = None  # глобальная переменная

def get_model(model_path: str | None = None):
    global model
    if model is None:
        model = CatBoostClassifier()
        try:
            if(model_path is None):
                raise Exception("Model path is NONE")
            model.load_model(model_path)
            print("Model loaded")
            return model
        except Exception as e:
            print(f"CANT LOAD MODEL: {e}")
            return None
    return model
    