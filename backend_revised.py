from flask import Flask, render_template, request
import pickle
import re
import final_features


app = Flask(__name__)

log_regress = pickle.load(open("logistic_regression.pkl", 'rb'))
kneigh = pickle.load(open("kneighbour.pkl", 'rb'))


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        url = request.form['url']
        # print(url)
        featur=[
        final_features.extract_features(url),
        final_features.havingat(url),
        final_features.havingdash(url),
        final_features.emergencywords(url),
        final_features.depthhave(url),
        final_features.numbr(url),
        final_features.platformabuse(url),
        final_features.brandassubdirectory(url),
        final_features.typosquat(url),
        final_features.ipinurl(url),
        final_features.httpinurl(url)]
        #cleaned_url = re.sub(r'^https?://(www\.)?', '', url)
        # print(cleaned_url)
        
        predict = log_regress.predict([featur])[0]
        # print(predict)
        
        if predict == 50:
            predict = "this website scores 50 in phishing"
        elif predict < 50:
            predict = "this website scores less than 50"
        elif predict > 50:
            predict = "this website scores more than 50"
        else:
            predict = "Something went wrong !!"
        
        return render_template("index.html", predict=predict)
    
    else:
        return render_template("index.html")



if __name__=="__main__":
    app.run(debug=True)