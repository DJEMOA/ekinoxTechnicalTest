from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
# We redirect to the offer page
def home():
    return redirect('/landing')

# compute offers
def getOffers(text):
    result = 0
    if len(text) > 0 :
        listText = text.split('\n')
        newListBooks = []
        countDifferentBooks = 0
        resultOutOfSaga = 0
        finalPrice = 0

        # Apply offers
        for book in listText:
            if "Back to the Future" in book:
                result = result + 15
                if book not in newListBooks:
                    newListBooks.append(book)
                    countDifferentBooks += 1

            else:
                # Offers for non saga articles
                resultOutOfSaga = resultOutOfSaga + 20
        # apply offers for saga
        if countDifferentBooks == 2:
            result = result - 0.1*result
        elif countDifferentBooks > 2:
            result = result - 0.2*result

        return round(result + resultOutOfSaga)

    else:
        return "Error : Empty value inserted"

# getting value from front and doing coputation of offers
@app.route('/landing', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        message = request.form["message"]
        result = getOffers(message)
        return redirect(url_for("getResult", result=result))
    else:
        return render_template("landing.html")
    
# To send the result of the total price with discount
@app.route("/<result>")
def getResult(result):
    return f"""<h1>{result}</h1> 
    <form action="/redirect">
      <input type="submit" value="Nouvel achat?">
    </form>"""

# to go back to the landing page
@app.route('/redirect')
def redirect_page():
    return redirect('/landing')


if __name__ == "__main__":
    app.run(debug=True)