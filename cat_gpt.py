import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, SimpleRNN

# Define the CatGPT model
def create_model():
    model = Sequential()
    model.add(SimpleRNN(32, input_shape=(10, 1)))
    model.add(Dense(3, activation="softmax"))
    model.compile(loss="categorical_crossentropy", optimizer="adam")
    return model

# Generate meows using the CatGPT model
def generate_meows(prompt):
    # Load the trained model
    model = create_model()
    
    # Simple dummy training to make the model learn "meow"
    x_train = np.random.rand(100, 10, 1)
    y_train = np.random.randint(0, 3, size=(100, 3))
    model.fit(x_train, y_train, epochs=5, verbose=0)

    # Generate meows
    meows = []
    for i in range(10):
        input_data = np.random.rand(1, 10, 1)
        output = model.predict(input_data)
        meow = np.argmax(output)
        meows.append(meow)

    # Convert meows to text
    meow_text = ""
    for meow in meows:
        if meow == 0:
            meow_text += "Meow. "
        elif meow == 1:
            meow_text += "Meeooow. "
        else:
            meow_text += "MEOW! "
    
    # Add some randomness to generate paragraphs or bullet points
    if len(prompt) > 10:
        meow_text = f"🐱 Here are your random meows:\n\n• {meow_text.replace('. ', '\n• ')}"
    
    return meow_text
