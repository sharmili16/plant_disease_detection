from imp import load_module
from flask import Flask,request,render_template
from forms import PredictionForm
from model import load_prediction_model
import os

from prediction import predict_image

app = Flask(__name__)
app.config["SECRET_KEY"] = "jhdbfj23432$@#kjm"
app.config["UPLOAD_PATH"] = "static/uploads"
model = load_prediction_model()

@app.route("/",methods=["GET"])
def home():
  form = PredictionForm()
  return render_template('home.html',form=form)

@app.route("/",methods=['POST'])
def upload_file():
  form = PredictionForm()
  print(request.files)
  uploaded_file = request.files['image']
  file_path =  os.path.join(app.config["UPLOAD_PATH"],uploaded_file.filename)
  uploaded_file.save(file_path)
  output = predict_image(file_path,model)
  return render_template('home.html',form=form,output=output,image=file_path)



if __name__ == '__main__':  
  app.run(debug=True)