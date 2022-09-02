''' 
Created on Aug 16, 2022

@author: manjo
'''
import flask
import Walmart
import Sprouts 
import Albertsons
import CostCo  
app = flask.Flask(__name__)
#Deployment 
#Renders landing page for site
@app.route('/', methods=['POST', 'GET'])
def index():
        return flask.render_template('Home.html')
#Renders result page for product searched from landing page, and provides elements for further searching
@app.route('/search', methods=['POST', 'GET'])
def catch():
    item=flask.request.form['searchable']
    #In order to save API request I will be testing/debugging without certain calls
    #The function calls within the parameter of the render hold product data from several stores
    return flask.render_template('Search.html', table_data=Walmart.DataCapture(item), Albert_data=Albertsons.AlbertsonCapture(item), CostCo_data=CostCo.CostCoCapture(item),Sprouts_data=Sprouts.SproutsCapture(item))
#404 Error handler in case a bad request is made to a element that does not exist
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return flask.render_template('404Error.html'), 404
#500 Error handler in case internal occurs
@app.errorhandler(500)
def internal_error(e):
    # note that we set the 500 status explicitly
    return flask.render_template('500Error.html'), 500
#Renders about page
@app.route('/about', methods=['POST', 'GET'])
def about():
    return flask.render_template('About.html')
if __name__ == '__main__':
    app.run()
    
