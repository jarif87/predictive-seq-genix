from django.shortcuts import render
from tensorflow.keras.models import load_model
import numpy as np
import os
import re

def handler(request):
    result = None
    form_errors = None
    if request.method == 'POST' and 'pred_button' in request.POST:
        sequence = request.POST.get('Name')  # Safe access
        if sequence:
            try:
                data = preprocessing(sequence)
                result = predicting(data)
                result = round(float(result), 2)  # Round to 2 decimal places
            except ValueError as e:
                form_errors = f"Invalid input: {str(e)}. Use [10,20,30,40,50,60,70,80,90,100]."
            except FileNotFoundError as e:
                form_errors = f"Model file not found: {str(e)}. Please contact the administrator."
            except Exception as e:
                form_errors = f"Error: {str(e)}"
        else:
            form_errors = "Please enter a sequence."
    return render(request, "index.html", {'result': result, 'form_errors': form_errors})

def predicting(data):
    # Adjust the path to your model file
    model_path = os.path.join("myapp", "model.keras")  # Update to NumberSequence.h5 if needed
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")
    model = load_model(model_path)
    result = model.predict(data, verbose=0)
    return result[0][0]  # Extract scalar

def preprocessing(s):
    # Validate input format matches the pattern
    pattern = r'^\[\s*(\d+\s*,\s*){9}\d+\s*\]$'
    if not re.match(pattern, s):
        raise ValueError("Please match the requested format. Enter exactly 10 numbers in brackets, e.g., [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]")
    
    # Remove brackets and split on commas
    s = s.strip('[]')
    s_ = [x.strip() for x in s.split(',')]
    # Convert to integers, skip empty strings
    try:
        s_ = [int(x) for x in s_ if x]
    except ValueError:
        raise ValueError("All elements must be valid integers.")
    if len(s_) != 10:
        raise ValueError("Sequence must contain exactly 10 numbers.")
    # Use all 10 numbers for model
    s_new = np.array(s_).reshape((1, 10, 1))  # Shape (1, 10, 1) like [[[10],[20],...]]
    return s_new