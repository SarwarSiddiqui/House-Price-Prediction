#Import Libraries
from flask import Flask, request, render_template

import model # load model.py

app = Flask(__name__)

# render htmp page
@app.route('/')
def home():
    return render_template('index.html')

# get user input and the predict the output and return to user
@app.route('/predict',methods=['POST'])
def predict():
    
    #take data from form and store in each feature    
    input_features = [x for x in request.form.values()]
    bath = input_features[0]
    balcony = input_features[1]
    bhk = input_features[2]
    location = input_features[3]
    total_sqft_int = input_features[4]
    price_per_sqft = input_features[5]
    area_type = input_features[6]
    availability = input_features[7]
    print("Bathroom : ",bath," Balcony : ", balcony," BHK : ",bhk," Location : ",location)
    print("Total Area : ",total_sqft_int," Price Per/sqft : ", price_per_sqft," Area Type : ",area_type," Availability : ",availability)

    # predict the price of house by calling model.py
    predicted_price = model.predict_house_price(bath,balcony,total_sqft_int,bhk,price_per_sqft,area_type,availability,location)       


    print(predicted_price)
    def formatINR(number):
        s, *d = str(number).partition(".")
        r = ",".join([s[x-2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
        return "".join([r] + d)
    
    predicted_price = formatINR(predicted_price)
    
    # render the html page and show the output
    return render_template('index.html', prediction_text='Predicted Price of House : ₹{}'.format(predicted_price))

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port="8080")
    
if __name__ == "__main__":
    app.run()



    
